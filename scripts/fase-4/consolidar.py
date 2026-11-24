#!/usr/bin/env python3
"""Refaz, a partir dos dados brutos, todos os resultados publicados da Fase 4.

1. Valida os dados brutos (quantidade de execuções, erros, versões, evidências existentes).
2. Executa, na ordem, os scripts de cada característica:
     scripts/fase-4/eficiencia/resumo.sh        bruto -> eficiencia/resumo.csv
     scripts/fase-4/eficiencia/pontuar.py       resumo.csv -> eficiencia/pontuacao.csv
     scripts/fase-4/flexibilidade/pontuar.py    bruto -> flexibilidade/pontuacao.csv
     scripts/fase-4/melhoria/diagnostico.py     bruto -> melhoria/diagnostico.csv e imagens-pagina.csv
3. Reúne os resultados em data/fase-4/consolidado/:
     medidas.csv      uma linha por recorte das 19 métricas, com o caminho do dado bruto
     classificacao.csv   pontos por métrica, questão e característica, e a classificação

Não acessa o portal. Métrica sem dado válido aparece como NC (não classificável), nunca como
zero (docs/fase-2/niveis-pontuacao.md, seção 1, regra 5).

Uso, na raiz do repositório:
  scripts/fase-4/consolidar.py              recalcula e grava os arquivos
  scripts/fase-4/consolidar.py --verificar  recalcula em uma pasta temporária, sem alterar o
                                            repositório, e compara com os arquivos versionados

Termina com código 1 se um dado bruto for inválido ou se um arquivo divergir.
Requisitos: Python 3 (biblioteca padrão), bash e jq.
"""

import csv
import importlib.util
import io
import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from statistics import mean, median

RAIZ = Path(__file__).resolve().parents[2]
SCRIPTS = RAIZ / "scripts/fase-4"
DADOS = Path("data/fase-4")
DERIVADOS = [
    "eficiencia/resumo.csv",
    "eficiencia/pontuacao.csv",
    "flexibilidade/pontuacao.csv",
    "melhoria/diagnostico.csv",
    "melhoria/imagens-pagina.csv",
    "consolidado/medidas.csv",
    "consolidado/classificacao.csv",
]
QUESTOES = {
    "Q1.1": ["M1.1.1", "M1.1.2"], "Q1.2": ["M1.2.1"], "Q1.3": ["M1.3.1"],
    "Q1.4": ["M1.4.1", "M1.4.2"], "Q1.5": ["M1.5.1", "M1.5.2"], "Q1.6": ["M1.6.1", "M1.6.2"],
    "Q2.1": ["M2.1.1"], "Q2.2": ["M2.2.1", "M2.2.2"], "Q2.3": ["M2.3.1"],
    "Q3.1": ["M3.1.1", "M3.1.2"], "Q3.2": ["M3.2.1"], "Q3.3": ["M3.3.1"], "Q3.4": ["M3.4.1"],
}
QUESTAO_DE = {m: q for q, ms in QUESTOES.items() for m in ms}
CARACTERISTICAS = {
    "G1": "Capacidade de interação",
    "G2": "Flexibilidade",
    "G3": "Eficiência de desempenho",
}
COLUNAS_MEDIDAS = [
    "caracteristica", "questao", "metrica", "recorte", "valor", "unidade", "minimo", "maximo",
    "execucoes", "pontos", "nivel", "pontos_no_minimo", "pontos_no_maximo", "situacao", "dado_bruto",
]
COLUNAS_CLASSIFICACAO = ["tipo", "item", "pontos", "classificacao_media", "limitador", "classificacao_final", "situacao"]


def modulo(caminho, nome):
    """Carrega um pontuar.py para reaproveitar faixas e recortes, sem duplicar limites."""
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sys.dont_write_bytecode = True
G3 = modulo(SCRIPTS / "eficiencia/pontuar.py", "pontuar_g3")
G2 = modulo(SCRIPTS / "flexibilidade/pontuar.py", "pontuar_g2")


def ler(arquivo):
    with open(arquivo, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def ler_bloco_csv(arquivo, cabecalho):
    linhas = arquivo.read_text(encoding="utf-8").splitlines()
    inicio = next((i for i, linha in enumerate(linhas) if linha == cabecalho), None)
    if inicio is None:
        raise ValueError(f"{arquivo}: cabeçalho não encontrado: {cabecalho}")
    fim = next((i for i in range(inicio + 1, len(linhas)) if not linhas[i].strip()), len(linhas))
    return list(csv.DictReader(io.StringIO("\n".join(linhas[inicio:fim]))))


def participantes_g1(dados):
    return ler_bloco_csv(
        dados / "capacidade-de-interacao/coleta_G1_rodada01.csv",
        "codigo,publico_representado,familiaridade_digital,primeiro_acesso,consentimento_confirmado,rodada,observacoes",
    )


def quantidade_participantes_g1(dados):
    return len({linha["codigo"] for linha in participantes_g1(dados)})


def gravar(arquivo, colunas, linhas):
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    with open(arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=colunas, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


def validar(dados):
    """Devolve (erros, lacunas). Erro impede o cálculo; lacuna indica cobertura insuficiente."""
    erros, lacunas = [], []

    versoes = set()
    for pagina in G3.PAGINAS:
        arquivos = sorted((dados / "eficiencia/lighthouse").glob(f"{pagina}-*.json"))
        if len(arquivos) != G3.EXECUCOES:
            lacunas.append(f"lighthouse/{pagina}: {len(arquivos)} execuções (esperado {G3.EXECUCOES})")
        for arquivo in arquivos:
            r = json.loads(arquivo.read_text(encoding="utf-8"))
            versoes.add(r["lighthouseVersion"])
            if r.get("runtimeError"):
                erros.append(f"{arquivo.name}: runtimeError {r['runtimeError'].get('code')}")
            for auditoria in ("first-contentful-paint", "largest-contentful-paint", "mainthread-work-breakdown"):
                if r["audits"][auditoria].get("numericValue") is None:
                    erros.append(f"{arquivo.name}: sem valor de {auditoria}")
    if len(versoes) > 1:
        erros.append(f"mais de uma versão do Lighthouse na coleta: {sorted(versoes)}")

    amostra_g1 = quantidade_participantes_g1(dados)
    if amostra_g1 != 5:
        lacunas.append(f"G1: {amostra_g1}/5 participantes previstos (#71)")

    tarefas = json.loads((dados / "eficiencia/tarefas.json").read_text(encoding="utf-8"))
    for tarefa, nome in (("T1", "T1"), ("T2", "T2"), (None, "downloads")):
        linhas = [t for t in tarefas if t["tarefa"] == tarefa]
        if len(linhas) != G3.EXECUCOES:
            lacunas.append(f"tarefas.json, {nome}: {len(linhas)} execuções (esperado {G3.EXECUCOES})")
        campos = ["heap_carga_mb"] + (["tempo_s", "heap_tarefa_mb"] if tarefa else [])
        erros += [f"tarefas.json, {nome}: sem {c}" for t in linhas for c in campos if t.get(c) is None]

    flex = dados / "flexibilidade"
    rolagem, funcoes = ler(flex / "rolagem.csv"), ler(flex / "funcoes.csv")
    for nome, linhas, chaves, esperado in (
        ("rolagem.csv", rolagem, ("execucao", "pagina", "largura"), 30),
        ("funcoes.csv", funcoes, ("execucao", "funcao", "largura"), 100),
    ):
        unicas = {tuple(l[c] for c in chaves) for l in linhas}
        if len(linhas) != len(unicas):
            erros.append(f"{nome}: {len(linhas) - len(unicas)} linhas repetidas")
        if len(unicas) != esperado:
            erros.append(f"{nome}: {len(unicas)} linhas distintas (esperado {esperado})")
    erros += [f"rolagem.csv: captura ausente {l['captura']}" for l in rolagem
              if not (flex / "capturas" / l["captura"]).exists()]
    for falha in ler(flex / "falhas.csv"):
        for evidencia in filter(None, (e.strip() for e in falha["evidencia"].split(";"))):
            if not (flex / evidencia).exists():
                erros.append(f"falhas.csv, {falha['id']}: evidência ausente {evidencia}")

    # melhoria/resumo.csv é gravado por medir.js, que acessa o portal; aqui só se confere o cálculo.
    medicao = json.loads((dados / "melhoria/medicao.json").read_text(encoding="utf-8"))
    campo = {"LCP (s)": "lcp_s", "Peso da página (kB)": "peso_pagina_kb"}
    for l in ler(dados / "melhoria/resumo.csv"):
        valores = [m[campo[l["medida"]]] for m in medicao if m["condicao"] == l["condicao"]]
        calculado = (median(valores), min(valores), max(valores), len(valores))
        publicado = tuple(float(l[c]) for c in ("mediana", "minimo", "maximo", "execucoes"))
        if not all(math.isclose(a, b, abs_tol=1e-6) for a, b in zip(calculado, publicado)):
            erros.append(f"melhoria/resumo.csv, {l['condicao']} {l['medida']}: {publicado} != {calculado}")
    return erros, lacunas


def calcular(base):
    """Executa os scripts de cada característica, com base como pasta de trabalho."""
    for comando in (
        ["bash", str(SCRIPTS / "eficiencia/resumo.sh")],
        [sys.executable, str(SCRIPTS / "eficiencia/pontuar.py")],
        [sys.executable, str(SCRIPTS / "flexibilidade/pontuar.py")],
        [sys.executable, str(SCRIPTS / "melhoria/diagnostico.py")],
    ):
        r = subprocess.run(comando, cwd=base, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"falha em {comando[-1]}:\n{r.stderr or r.stdout}")


def linha_medida(metrica, recorte, **campos):
    l = dict.fromkeys(COLUNAS_MEDIDAS, "")
    l.update(caracteristica="G" + metrica[1], questao=QUESTAO_DE[metrica], metrica=metrica,
             recorte=recorte, pontos="NC", nivel="NC", situacao="NC")
    l.update(campos)
    return l


def pontos_g1(metrica, valor, recorte, inspecoes, numerador=None):
    if metrica == "M1.1.1":
        quantidade = int(numerador)
        return 0 if quantidade <= 5 else 1 if quantidade == 6 else 2 if quantidade <= 8 else 3
    if metrica in ("M1.1.2", "M1.2.1", "M1.4.1", "M1.4.2"):
        return 0 if valor < 0.6 else 1 if valor < 0.8 else 2 if valor < 1 else 3
    if metrica == "M1.3.1":
        return 0 if valor < 0.5 else 1 if valor < 0.7 else 2 if valor < 0.9 else 3
    if metrica == "M1.5.1":
        return 0 if valor < 51 else 1 if valor < 71 else 2 if valor < 85 else 3
    if metrica == "M1.5.2":
        return 0 if valor < 3 else 1 if valor < 3.5 else 2 if valor < 4.5 else 3
    if metrica == "M1.6.1":
        return 0 if valor < 0.8 else 1 if valor < 0.9 else 2 if valor < 1 else 3
    if metrica == "M1.6.2":
        pagina = inspecoes[recorte]
        criticos, serios = int(pagina["criticos_distintos"]), int(pagina["serios_distintos"])
        return 0 if criticos or serios >= 6 else 1 if serios >= 3 else 2 if serios else 3
    raise ValueError(f"Métrica G1 sem regra de pontuação: {metrica}")


def medidas_g1(dados):
    pasta = dados / "capacidade-de-interacao"
    coleta = pasta / "coleta_G1_rodada01.csv"
    tentativas = ler_bloco_csv(
        coleta,
        "rodada,codigo,tarefa,tentativa,inicio_fuso,duracao_s,primeira_acao,primeiro_destino,acerto_primeiro_destino,status,evidencia_resultado,ajuda_ou_incidente,sequencia_passos,passos_avaliador_1,passos_avaliador_2,passos_consenso,passos_minimos,razao,evidencia_gravacao",
    )
    consolidados = ler_bloco_csv(
        coleta,
        "rodada,metrica,recorte,numerador,denominador,observacoes_validas,valor,unidade,nivel,evidencia,observacoes",
    )
    inspecoes = {
        linha["pagina"]: linha
        for linha in ler_bloco_csv(
            pasta / "inspecoes_G1_rodada01.csv",
            "rodada,pagina,url,data_hora_fuso,axe_versao,json,passes,violations,incomplete,inapplicable,proporcao_aprovada,criticos_distintos,serios_distintos,total_afetado,ocorrencias",
        )
    }

    por_metrica = {}
    for linha in consolidados:
        metrica, recorte = linha["metrica"], linha["recorte"]
        if recorte == "média T1–T3":
            continue
        por_metrica.setdefault(metrica, {})[recorte] = linha

    def iniciou_em_inicio(tentativa):
        acao = tentativa["primeira_acao"].casefold()
        return "início" in acao or "inicio" in acao

    for metrica in ("M1.1.2", "M1.2.1", "M1.3.1"):
        for tarefa in ("T2", "T3"):
            linhas_validas = [t for t in tentativas if t["tarefa"] == tarefa and iniciou_em_inicio(t)]
            original = por_metrica.get(metrica, {}).get(tarefa)
            if metrica == "M1.1.2" and linhas_validas:
                acertos = sum(t["acerto_primeiro_destino"] == "1" for t in linhas_validas)
                por_metrica[metrica][tarefa] = {
                    "metrica": metrica, "recorte": tarefa, "valor": str(acertos / len(linhas_validas)),
                    "unidade": "proporção", "observacoes_validas": str(len(linhas_validas)),
                    "situacao": "classificada com observações iniciadas em Início",
                    "evidencia": "tentativas deste arquivo",
                }
            elif metrica == "M1.2.1" and linhas_validas:
                concluidas = sum(t["status"] == "sucesso" for t in linhas_validas)
                por_metrica[metrica][tarefa] = {
                    "metrica": metrica, "recorte": tarefa, "valor": str(concluidas / len(linhas_validas)),
                    "unidade": "proporção", "observacoes_validas": str(len(linhas_validas)),
                    "situacao": "classificada com observações iniciadas em Início",
                    "evidencia": "tentativas deste arquivo",
                }
            elif metrica == "M1.3.1":
                concluidas = [t for t in linhas_validas if t["status"] == "sucesso" and t["razao"] not in ("", "NC")]
                if concluidas:
                    valor = mean(float(t["razao"]) for t in concluidas)
                    por_metrica[metrica][tarefa] = {
                        "metrica": metrica, "recorte": tarefa, "valor": str(valor),
                        "unidade": "razão", "observacoes_validas": str(len(concluidas)),
                        "situacao": "classificada com tarefas concluídas iniciadas em Início",
                        "evidencia": "tentativas deste arquivo",
                    }
                else:
                    por_metrica[metrica][tarefa] = {
                        "metrica": metrica, "recorte": tarefa, "valor": "",
                        "unidade": "razão", "observacoes_validas": "0",
                        "situacao": "NC: sem tarefa concluída iniciada em Início",
                        "evidencia": "tentativas deste arquivo",
                    }
            else:
                por_metrica.setdefault(metrica, {})[tarefa] = {
                    "metrica": metrica, "recorte": tarefa, "valor": "",
                    "unidade": (original or {}).get("unidade", ""),
                    "observacoes_validas": "0",
                    "situacao": "NC: tarefa não iniciada em Início",
                    "evidencia": "tentativas deste arquivo",
                }

    linhas = []
    for questao, metricas in QUESTOES.items():
        if not questao.startswith("Q1"):
            continue
        for metrica in metricas:
            recortes = por_metrica.get(metrica, {})
            for recorte, bruto in recortes.items():
                valor = bruto.get("valor", "")
                unidade = bruto.get("unidade", "")
                arquivo_bruto = (
                    f"{DADOS}/capacidade-de-interacao/inspecoes_G1_rodada01.csv"
                    if metrica in ("M1.1.1", "M1.4.1", "M1.4.2", "M1.6.1", "M1.6.2")
                    else f"{DADOS}/capacidade-de-interacao/coleta_G1_rodada01.csv"
                )
                if not valor or valor == "NC":
                    linhas.append(linha_medida(
                        metrica, recorte, unidade=unidade, execucoes=bruto.get("observacoes_validas", ""),
                        situacao=bruto.get("situacao", "NC: sem resultado válido"), dado_bruto=arquivo_bruto,
                    ))
                    continue
                pontos = pontos_g1(metrica, float(valor), recorte, inspecoes, bruto.get("numerador"))
                linhas.append(linha_medida(
                    metrica, recorte, valor=valor, unidade=unidade, execucoes=bruto.get("observacoes_validas", ""),
                    pontos=pontos, nivel=pontos, situacao=bruto.get("situacao", "classificada"),
                    dado_bruto=arquivo_bruto,
                ))
    return linhas


def medidas_g2(dados):
    obtidas = {(l["item"], l["recorte"]): l for l in ler(dados / "flexibilidade/pontuacao.csv")}
    ambientes = list(G2.AMBIENTES.values())
    sem_referencia = [n for a, n in G2.AMBIENTES.items() if a != G2.REFERENCIA]
    plano = [
        ("M2.1.1", ambientes, "tarefas concluídas", "execucoes.csv", "NC: matriz de ambientes não executada (#72)"),
        ("M2.2.1", ["3 páginas × 5 larguras"], "combinações sem rolagem", "rolagem.csv", "NC: sem dados"),
        ("M2.2.2", list(G2.PAGINAS.values()), "funções preservadas", "funcoes.csv", "NC: sem dados"),
        ("M2.3.1", sem_referencia, "falhas bloqueantes/graves/cosméticas", "falhas.csv",
         "NC: depende da matriz de ambientes (#72)"),
    ]
    linhas = []
    for metrica, recortes, unidade, arquivo, motivo in plano:
        bruto = f"{DADOS}/flexibilidade/{arquivo}"
        for recorte in recortes:
            l = obtidas.get((metrica, recorte))
            if l is None:
                linhas.append(linha_medida(metrica, recorte, unidade=unidade, situacao=motivo, dado_bruto=bruto))
                continue
            linhas.append(linha_medida(
                metrica, recorte, valor=l["valor"], unidade=unidade, pontos=l["pontos"], nivel=l["nivel"],
                execucoes=2 if metrica.startswith("M2.2") else "", situacao="classificada", dado_bruto=bruto))
    return linhas


def medidas_g3(dados):
    resumo = {(l["objeto"], l["metrica"]): l for l in ler(dados / "eficiencia/resumo.csv")}
    pontuacao = {(l["metrica"], l["recorte"]): l for l in ler(dados / "eficiencia/pontuacao.csv")}
    lighthouse = [(m, o, G3.METRICAS[m][0], n, f"{DADOS}/eficiencia/lighthouse/{o}-<1 a 5>.json")
                  for m in ("M3.1.1", "M3.1.2", "M3.3.1") for o, n in G3.PAGINAS.items()]
    tarefas = f"{DADOS}/eficiencia/tarefas.json"
    script = [("M3.2.1", t, G3.METRICAS["M3.2.1"][0], t, tarefas) for t in ("T1", "T2")]
    script += [("M3.4.1", o, rotulo, desc, tarefas) for o, rotulo, desc in G3.RECORTES_MEMORIA]
    linhas = []
    for metrica, objeto, rotulo, recorte, bruto in sorted(lighthouse + script, key=lambda x: x[0]):
        r, p = resumo.get((objeto, rotulo)), pontuacao[(metrica, recorte)]
        classificada = p["pontos"] != "NC"
        campos = dict(unidade=rotulo.rsplit("(", 1)[1].rstrip(")"), dado_bruto=bruto, pontos=p["pontos"],
                      nivel=p["nivel"], situacao="classificada" if classificada else "NC: menos de 5 execuções válidas")
        if r:
            limites = G3.METRICAS[metrica][1]
            campos.update(valor=r["mediana"], minimo=r["minimo"], maximo=r["maximo"], execucoes=r["execucoes"])
            if classificada:
                campos.update(pontos_no_minimo=G3.nivel(float(r["minimo"]), limites),
                              pontos_no_maximo=G3.nivel(float(r["maximo"]), limites))
        linhas.append(linha_medida(metrica, recorte, **campos))
    return linhas


def limitador(g, medidas, dados):
    """Limitadores de docs/fase-2/niveis-pontuacao.md, seção 5.2: (descrição, classificação máxima)."""
    if g == "G1":
        acessibilidade = ler_bloco_csv(
            dados / "capacidade-de-interacao/inspecoes_G1_rodada01.csv",
            "rodada,pagina,url,data_hora_fuso,axe_versao,json,passes,violations,incomplete,inapplicable,proporcao_aprovada,criticos_distintos,serios_distintos,total_afetado,ocorrencias",
        )
        criticas = [l["pagina"] for l in acessibilidade if int(l["criticos_distintos"]) > 0]
        if criticas:
            return "violação crítica de acessibilidade em " + ", ".join(criticas), "Insatisfatório"
        tarefas_baixas = [
            f"M1.2.1 {l['recorte']}" for l in medidas
            if l["metrica"] == "M1.2.1" and l["valor"] != "" and float(l["valor"]) < 0.6
        ]
        if tarefas_baixas:
            return "; ".join(tarefas_baixas), "Aceitável"
    if g == "G3":
        lentos = [f"{l['metrica']} {l['recorte']}" for l in medidas if l["valor"] != "" and (
            (l["metrica"] == "M3.1.2" and float(l["valor"]) > 4.0)
            or (l["metrica"] == "M3.2.1" and float(l["valor"]) > 10.0))]
        if lentos:
            return "; ".join(lentos), "Aceitável"
    if g == "G2":
        bloqueantes = sorted({f["id"] for f in ler(dados / "flexibilidade/falhas.csv")
                              if f["gravidade"] == "bloqueante" and f["reproduzida"] == "sim"
                              and f["tambem_na_referencia"] != "sim"})
        if bloqueantes:
            return "; ".join(bloqueantes), "Insatisfatório"
    return "", None


def classificar(medidas, dados):
    ordem = list(G3.NIVEIS.values())
    linhas, pontos = [], {}

    def registrar(tipo, item, partes, **extra):
        valor = mean(partes) if partes and all(p is not None for p in partes) else None
        pontos[item] = valor
        l = dict.fromkeys(COLUNAS_CLASSIFICACAO, "")
        l.update(tipo=tipo, item=item, pontos="NC" if valor is None else f"{valor:.4f}",
                 situacao="pendente" if valor is None else "concluída", **extra)
        linhas.append(l)
        return l

    for g in CARACTERISTICAS:
        questoes = {q: ms for q, ms in QUESTOES.items() if q[1] == g[1]}
        for metrica in (m for ms in questoes.values() for m in ms):
            registrar("métrica", metrica, [None if l["pontos"] == "NC" else int(l["pontos"])
                                           for l in medidas if l["metrica"] == metrica])
        for q, ms in questoes.items():
            registrar("questão", q, [pontos[m] for m in ms])
        l = registrar("característica", g, [pontos[q] for q in questoes])
        descricao, maximo = limitador(g, medidas, dados)
        l["limitador"] = descricao
        if pontos[g] is None:
            l["classificacao_final"] = "pendente"
            continue
        l["classificacao_media"] = l["classificacao_final"] = G3.classificacao(pontos[g])
        if g == "G1" and quantidade_participantes_g1(dados) != 5:
            l["classificacao_final"] = "pendente"
            l["situacao"] = "pendente: amostra inferior aos 5 participantes previstos"
            continue
        if maximo and ordem.index(l["classificacao_final"]) > ordem.index(maximo):
            l["classificacao_final"] = maximo
    return linhas


def iguais(a, b):
    """Compara dois CSV célula a célula; números com tolerância de arredondamento."""
    def celulas(arquivo):
        with open(arquivo, encoding="utf-8", newline="") as f:
            return list(csv.reader(f))

    def igual(x, y):
        if x == y:
            return True
        try:
            return math.isclose(float(x), float(y), rel_tol=1e-9)
        except ValueError:
            return False

    ca, cb = celulas(a), celulas(b)
    return len(ca) == len(cb) and all(
        len(x) == len(y) and all(igual(i, j) for i, j in zip(x, y)) for x, y in zip(ca, cb))


def processar(base):
    dados = base / DADOS
    erros, lacunas = validar(dados)
    if erros:
        sys.exit("Dados brutos inválidos:\n- " + "\n- ".join(erros))
    print("Dados brutos válidos." if not lacunas else "Dados brutos com lacunas (métrica NC):\n- " + "\n- ".join(lacunas))
    calcular(base)
    medidas = medidas_g1(dados) + medidas_g2(dados) + medidas_g3(dados)
    classificacoes = classificar(medidas, dados)
    gravar(dados / "consolidado/medidas.csv", COLUNAS_MEDIDAS, medidas)
    gravar(dados / "consolidado/classificacao.csv", COLUNAS_CLASSIFICACAO, classificacoes)
    return medidas, classificacoes


def main():
    if sys.argv[1:] not in ([], ["--verificar"]):
        sys.exit(__doc__)

    verificar = bool(sys.argv[1:])

    # O cálculo é sempre feito em uma cópia; no modo normal só são gravados os arquivos cujo
    # conteúdo mudou, para não gerar diferenças apenas de quebra de linha.
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(RAIZ / DADOS, Path(tmp) / DADOS)
        medidas, classificacoes = processar(Path(tmp))
        divergentes = []
        for nome in DERIVADOS:
            versionado, novo = RAIZ / DADOS / nome, Path(tmp) / DADOS / nome
            if versionado.exists() and iguais(versionado, novo):
                print(f"ok        {DADOS / nome}")
                continue
            divergentes.append(nome)
            print(f"{'DIVERGE ' if verificar else 'gravado '}  {DADOS / nome}")
            if not verificar:
                versionado.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(novo, versionado)
    if verificar:
        sys.exit(1 if divergentes else 0)

    nc = sum(l["pontos"] == "NC" for l in medidas)
    print(f"{len(medidas)} recortes: {len(medidas) - nc} classificados e {nc} NC.")
    for l in classificacoes:
        if l["tipo"] == "característica":
            print(f"{l['item']} {CARACTERISTICAS[l['item']]}: {l['pontos']} ({l['classificacao_final']})")
    print("\nRecortes cujo nível muda entre a mediana e o mínimo ou o máximo das execuções:")
    for l in medidas:
        if l["pontos_no_minimo"] != "" and {str(l["pontos_no_minimo"]), str(l["pontos_no_maximo"])} != {l["pontos"]}:
            print(f"- {l['metrica']} {l['recorte']}: {l['pontos']} na mediana, {l['pontos_no_minimo']} no mínimo, "
                  f"{l['pontos_no_maximo']} no máximo")


if __name__ == "__main__":
    main()
