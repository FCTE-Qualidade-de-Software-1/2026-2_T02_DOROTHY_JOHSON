#!/usr/bin/env python3
"""Pontua o GQM G2 (flexibilidade) a partir dos dados de data/fase-4/flexibilidade/.

Aplica os níveis e os critérios de julgamento de docs/fase-2/niveis-pontuacao.md (seções 1,
3 e 5): cada recorte recebe de 0 (Insatisfatório) a 3 (Excelente); a métrica é a média dos
recortes, a questão é a média das métricas e o G2 é a média das questões. Depois aplica o
limitador de gravidade do G2 (falha bloqueante reproduzida).

Entradas (método: docs/fase-3/metodo-flexibilidade.md):
  rolagem.csv     M2.2.1, gerado por scripts/fase-4/flexibilidade/telas.js (Procedimento A)
  funcoes.csv     M2.2.2, gerado pelo mesmo script (Procedimento B)
  execucoes.csv   M2.1.1, preenchido na matriz manual de ambientes (Procedimento C)
  falhas.csv      M2.3.1, registro de falhas (Procedimento D)

Uma métrica sem dados válidos fica NC (não classificável), e o juízo do G2 fica pendente
(seção 5.2, "cobertura insuficiente").

Uso: scripts/fase-4/flexibilidade/pontuar.py [DIR]
  DIR  pasta com os CSV (padrão: data/fase-4/flexibilidade)
Grava DIR/pontuacao.csv e imprime as tabelas em Markdown.

Requisitos: apenas Python 3 (biblioteca padrão).
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

NIVEIS = {0: "Insatisfatório", 1: "Aceitável", 2: "Bom", 3: "Excelente"}
PAGINAS = {
    "meu-territorio": "Meu Território",
    "plataforma-geoespacial": "SITGeo",
    "downloads": "Biblioteca Territorial",
}
# Matriz de ambientes (docs/fase-3/ambiente.md, seção 3.3). A referência não entra em M2.3.1,
# porque, por definição, uma falha dependente de ambiente é a que não ocorre nela.
AMBIENTES = {
    "AND-CHROME": "Chrome/Android",
    "AND-SAMSUNG": "Samsung Internet/Android",
    "IOS-SAFARI": "Safari/iOS",
    "WIN-CHROME": "Chrome/Windows (referência)",
    "WIN-EDGE": "Edge/Windows",
    "WIN-FIREFOX": "Firefox/Windows",
}
REFERENCIA = "WIN-CHROME"
TAREFAS = ["T1", "T2", "T3"]
LARGURA_REF, LARGURA_CEL = "1366", "360"


def ler(arquivo):
    if not arquivo.exists():
        return []
    with arquivo.open(encoding="utf-8") as f:
        return [l for l in csv.DictReader(f) if any((v or "").strip() for v in l.values())]


def fmt(x, casas=2):
    return "NC" if x is None else f"{x:.{casas}f}".replace(".", ",")


def pct(x):
    return "NC" if x is None else f"{100 * x:.1f}%".replace(".", ",")


def nivel_proporcao(x, excelente=1.0, bom=0.85, aceitavel=2 / 3):
    """Faixas de M2.1.1 e M2.2.2: o limite pertence à faixa melhor (≥)."""
    if x >= excelente:
        return 3
    if x >= bom:
        return 2
    if x >= aceitavel:
        return 1
    return 0


def nivel_rolagem(sem_rolagem):
    """M2.2.1: 15 combinações = 3; 14 = 2; 12 a 13 = 1; 0 a 11 = 0."""
    return 3 if sem_rolagem >= 15 else 2 if sem_rolagem == 14 else 1 if sem_rolagem >= 12 else 0


def nivel_falhas(bloqueantes, graves, cosmeticas):
    """M2.3.1 por ambiente."""
    if bloqueantes >= 1 or graves >= 3:
        return 0
    if graves >= 1:
        return 1
    if cosmeticas >= 1:
        return 2
    return 3


def juizo(media):
    if media < 1:
        return "Insatisfatório"
    if media < 2:
        return "Aceitável"
    if media < 2.75:
        return "Bom"
    return "Excelente"


def m221(linhas):
    """Combinação com rolagem só se a rolagem aparece em todas as execuções (reprodução)."""
    por_combinacao = defaultdict(list)
    for l in linhas:
        por_combinacao[(l["pagina"], l["largura"])].append(l["rolagem_horizontal"] == "sim")
    if not por_combinacao:
        return None, [], []
    com_rolagem = sorted(k for k, v in por_combinacao.items() if all(v) and len(v) >= 2)
    nao_reproduzida = sorted(k for k, v in por_combinacao.items() if any(v) and not (all(v) and len(v) >= 2))
    sem = len(por_combinacao) - len(com_rolagem)
    return (sem, len(por_combinacao)), com_rolagem, nao_reproduzida


def m222(linhas):
    """Por página: B = funções disponíveis em 1366 px em todas as execuções; A = dessas, as
    que não ficam indisponíveis em 360 px em todas as execuções."""
    estado = defaultdict(lambda: defaultdict(list))
    nomes = {}
    for l in linhas:
        estado[(l["pagina"], l["funcao"])][l["largura"]].append(l["disponivel"] == "sim")
        nomes[l["funcao"]] = l["nome"]
    paginas = {}
    for (pagina, funcao), por_largura in estado.items():
        ref = por_largura.get(LARGURA_REF, [])
        cel = por_largura.get(LARGURA_CEL, [])
        if not ref or not all(ref):
            continue  # fora de B: não foi possível usar a função nem no computador
        perdida = bool(cel) and not any(cel)
        p = paginas.setdefault(pagina, {"b": 0, "a": 0, "perdidas": []})
        p["b"] += 1
        if perdida:
            p["perdidas"].append(f"{funcao} {nomes[funcao]}")
        else:
            p["a"] += 1
    return paginas


def m211(linhas):
    """Por ambiente: X = tarefas concluídas sem falha / 3. Uma falha só conta se a reexecução
    (2ª linha da mesma tarefa) também falhar; se a reexecução conclui, a tarefa é concluída e a
    falha fica registrada como não reproduzida. Falha sem reexecução deixa o ambiente NC."""
    por_amb = defaultdict(lambda: defaultdict(list))
    for l in linhas:
        if l.get("resultado") in ("concluida", "falha"):
            por_amb[l["ambiente"]][l["tarefa"]].append(l["resultado"])
    resultado = {}
    for amb, tarefas in por_amb.items():
        if not all(t in tarefas for t in TAREFAS):
            continue  # matriz incompleta neste ambiente: NC
        if any(tarefas[t] == ["falha"] for t in TAREFAS):
            continue  # falha ainda sem reexecução: NC
        resultado[amb] = sum(1 for t in TAREFAS if "concluida" in tarefas[t])
    return resultado


def m231(falhas, ambientes_executados):
    contagem = {a: {"bloqueante": 0, "grave": 0, "cosmetica": 0} for a in ambientes_executados if a != REFERENCIA}
    vistos = set()
    for f in falhas:
        if f.get("reproduzida") != "sim" or f.get("tambem_na_referencia") == "sim":
            continue
        amb = f["ambiente"]
        if amb not in contagem or (amb, f["id"]) in vistos:
            continue
        vistos.add((amb, f["id"]))
        contagem[amb][f["gravidade"]] += 1
    return contagem


def main():
    pasta = Path(sys.argv[1] if len(sys.argv) > 1 else "data/fase-4/flexibilidade")
    saida = []  # linhas de pontuacao.csv
    pontos_metrica = {}

    # Q2.1 / M2.1.1
    execs = m211(ler(pasta / "execucoes.csv"))
    print("## M2.1.1 — tarefas concluídas por ambiente\n")
    if execs:
        print("| Ambiente | Tarefas concluídas | X | Nível |\n|---|---:|---:|---|")
        niveis = []
        for amb in AMBIENTES:
            if amb not in execs:
                print(f"| {AMBIENTES[amb]} | — | NC | NC |")
                continue
            x = execs[amb] / 3
            n = nivel_proporcao(x)
            niveis.append(n)
            saida.append(["M2.1.1", AMBIENTES[amb], f"{execs[amb]}/3", f"{x:.4f}", n, NIVEIS[n]])
            print(f"| {AMBIENTES[amb]} | {execs[amb]}/3 | {pct(x)} | {NIVEIS[n]} ({n}) |")
        geral = sum(execs.values()) / (3 * len(execs))
        print(f"\nGeral: {sum(execs.values())}/{3 * len(execs)} = {pct(geral)} "
              f"({NIVEIS[nivel_proporcao(geral)]}; informado, não entra na média)")
        pontos_metrica["M2.1.1"] = mean(niveis) if len(execs) == len(AMBIENTES) else None
    else:
        print("Sem execuções registradas em execucoes.csv: NC.")
        pontos_metrica["M2.1.1"] = None

    # Q2.2 / M2.2.1
    r, com_rolagem, nao_rep = m221(ler(pasta / "rolagem.csv"))
    print("\n## M2.2.1 — combinações sem rolagem horizontal\n")
    if r:
        sem, total = r
        n = nivel_rolagem(sem)
        pontos_metrica["M2.2.1"] = n
        saida.append(["M2.2.1", "3 páginas × 5 larguras", f"{sem}/{total}", f"{sem / total:.4f}", n, NIVEIS[n]])
        print(f"{sem} de {total} combinações sem rolagem ({pct(sem / total)}): {NIVEIS[n]} ({n})")
        for pagina, largura in com_rolagem:
            print(f"- com rolagem reproduzida: {PAGINAS[pagina]}, {largura} px")
        for pagina, largura in nao_rep:
            print(f"- rolagem não reproduzida (não conta): {PAGINAS[pagina]}, {largura} px")
    else:
        pontos_metrica["M2.2.1"] = None
        print("Sem dados: NC.")

    # Q2.2 / M2.2.2
    paginas = m222(ler(pasta / "funcoes.csv"))
    print("\n## M2.2.2 — funções preservadas em 360 px\n")
    if paginas:
        print("| Página | Preservadas | X | Nível | Funções perdidas |\n|---|---:|---:|---|---|")
        niveis = []
        for pagina, nome in PAGINAS.items():
            p = paginas.get(pagina)
            if not p:
                print(f"| {nome} | — | NC | NC | |")
                continue
            x = p["a"] / p["b"]
            n = nivel_proporcao(x, 1.0, 0.8, 0.6)
            niveis.append(n)
            saida.append(["M2.2.2", nome, f"{p['a']}/{p['b']}", f"{x:.4f}", n, NIVEIS[n]])
            print(f"| {nome} | {p['a']}/{p['b']} | {pct(x)} | {NIVEIS[n]} ({n}) | {'; '.join(p['perdidas']) or '—'} |")
        pontos_metrica["M2.2.2"] = mean(niveis) if len(niveis) == len(PAGINAS) else None
    else:
        pontos_metrica["M2.2.2"] = None
        print("Sem dados: NC.")

    # Q2.3 / M2.3.1
    falhas = ler(pasta / "falhas.csv")
    print("\n## M2.3.1 — falhas dependentes de ambiente\n")
    if execs:
        contagem = m231(falhas, execs.keys())
        print("| Ambiente | Bloqueantes | Graves | Cosméticas | Nível |\n|---|---:|---:|---:|---|")
        niveis = []
        for amb, c in contagem.items():
            n = nivel_falhas(c["bloqueante"], c["grave"], c["cosmetica"])
            niveis.append(n)
            saida.append(["M2.3.1", AMBIENTES[amb], f"{c['bloqueante']}/{c['grave']}/{c['cosmetica']}", "", n, NIVEIS[n]])
            print(f"| {AMBIENTES[amb]} | {c['bloqueante']} | {c['grave']} | {c['cosmetica']} | {NIVEIS[n]} ({n}) |")
        completos = len(contagem) == len(AMBIENTES) - 1
        pontos_metrica["M2.3.1"] = mean(niveis) if niveis and completos else None
    else:
        pontos_metrica["M2.3.1"] = None
        print("Sem execuções da matriz de ambientes: NC.")
    pre = [f for f in falhas if f["ambiente"] not in AMBIENTES]
    if pre:
        print("\nFalhas pré-registradas em emulação (a atribuir aos ambientes após confirmação):\n")
        print("| ID | Ambiente | Página | Gravidade | Reproduzida | Descrição |\n|---|---|---|---|---|---|")
        for f in pre:
            print(f"| {f['id']} | {f['ambiente']} | {PAGINAS.get(f['pagina'], f['pagina'])} | {f['gravidade']} | {f['reproduzida']} | {f['descricao']} |")

    # Consolidação
    questoes = {"Q2.1": ["M2.1.1"], "Q2.2": ["M2.2.1", "M2.2.2"], "Q2.3": ["M2.3.1"]}
    print("\n## Consolidação do G2\n")
    print("| Questão | Métricas | Pontos |\n|---|---|---:|")
    pontos_q = {}
    for q, ms in questoes.items():
        vals = [pontos_metrica[m] for m in ms]
        pontos_q[q] = mean(vals) if all(v is not None for v in vals) else None
        desc = "; ".join(f"{m} = {fmt(pontos_metrica[m])}" for m in ms)
        print(f"| {q} | {desc} | {fmt(pontos_q[q])} |")
        saida.append([q, "", "", "", "" if pontos_q[q] is None else f"{pontos_q[q]:.4f}", ""])
    bloqueante = any(f.get("gravidade") == "bloqueante" and f.get("reproduzida") == "sim"
                     and f.get("tambem_na_referencia") != "sim" for f in falhas)
    if all(v is not None for v in pontos_q.values()):
        g2 = mean(pontos_q.values())
        preliminar = juizo(g2)
        final = "Insatisfatório" if bloqueante else preliminar
        print(f"| **G2** | Média das três questões | **{fmt(g2)}** |")
        print(f"\nJuízo preliminar: {preliminar}. Limitador (falha bloqueante): "
              f"{'acionado' if bloqueante else 'não acionado'}. Juízo final: {final}.")
        saida.append(["G2", "", "", "", f"{g2:.4f}", final])
    else:
        print("| **G2** | | **pendente** |")
        print("\nJuízo do G2 pendente: há métrica obrigatória sem resultado válido "
              "(seção 5.2, cobertura insuficiente).")
        if bloqueante:
            print("Já há falha bloqueante reproduzida: o juízo final será Insatisfatório.")
        saida.append(["G2", "", "", "", "", "pendente"])

    with (pasta / "pontuacao.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item", "recorte", "valor", "x", "pontos", "nivel"])
        w.writerows(saida)


if __name__ == "__main__":
    main()
