#!/usr/bin/env python3
"""Pontua o GQM G3 a partir de data/fase-4/eficiencia/resumo.csv.

Aplica os níveis e os critérios de julgamento de docs/fase-2/niveis-pontuacao.md (seções 1,
4 e 5): cada recorte recebe de 0 (Insatisfatório) a 3 (Excelente); a métrica é a média dos
recortes, a questão é a média das métricas e o G3 é a média das questões. Depois aplica o
limitador de gravidade do G3 e confere as hipóteses H3.1 a H3.4.

Uso: scripts/fase-4/eficiencia/pontuar.py [DIR]
  DIR  pasta com resumo.csv (padrão: data/fase-4/eficiencia)
Grava DIR/pontuacao.csv e imprime as tabelas em Markdown.

Requisitos: apenas Python 3 (biblioteca padrão).
"""

import csv
import sys
from pathlib import Path
from statistics import mean

EXECUCOES = 5
NIVEIS = {0: "Insatisfatório", 1: "Aceitável", 2: "Bom", 3: "Excelente"}

# (métrica, rótulo no resumo.csv, limites de Excelente, Bom e Aceitável; menor é melhor)
METRICAS = {
    "M3.1.1": ("M3.1.1 FCP (s)", (1.0, 1.8, 3.0)),
    "M3.1.2": ("M3.1.2 LCP (s)", (1.5, 2.5, 4.0)),
    "M3.2.1": ("M3.2.1 execução da tarefa (s)", (1.0, 5.0, 10.0)),
    "M3.3.1": ("M3.3.1 CPU thread principal (s)", (2.0, 3.0, 4.0)),
    "M3.4.1": (None, (8.0, 12.0, 20.0)),
}
PAGINAS = {
    "meu-territorio": "Meu Território",
    "plataforma-geoespacial": "SITGeo",
    "downloads": "Biblioteca Territorial",
}
# Recortes de M3.4.1: após o carregamento das três páginas e após T1 e T2 (seção 4).
RECORTES_MEMORIA = [
    ("downloads", "M3.4.1 JS heap após carregamento (MB)", "Biblioteca Territorial, após o carregamento"),
    ("T1", "M3.4.1 JS heap após carregamento (MB)", "Meu Território, após o carregamento"),
    ("T2", "M3.4.1 JS heap após carregamento (MB)", "SITGeo, após o carregamento"),
    ("T1", "M3.4.1 JS heap após tarefa (MB)", "Após T1"),
    ("T2", "M3.4.1 JS heap após tarefa (MB)", "Após T2"),
]
QUESTOES = {"Q3.1": ["M3.1.1", "M3.1.2"], "Q3.2": ["M3.2.1"], "Q3.3": ["M3.3.1"], "Q3.4": ["M3.4.1"]}


def nivel(valor, limites):
    """0 a 3 pelos limites da seção 4; o limite pertence à faixa melhor (≤)."""
    excelente, bom, aceitavel = limites
    if valor <= excelente:
        return 3
    if valor <= bom:
        return 2
    if valor <= aceitavel:
        return 1
    return 0


def juizo(media):
    if media < 1.0:
        return "Insatisfatório"
    if media < 2.0:
        return "Aceitável"
    if media < 2.75:
        return "Bom"
    return "Excelente"


def sim(condicao):
    return "sim" if condicao else "não"


def numero(valor, casas=2):
    return f"{valor:.{casas}f}".replace(".", ",")


def main():
    pasta = Path(sys.argv[1] if len(sys.argv) > 1 else "data/fase-4/eficiencia")
    resumo = {(r["objeto"], r["metrica"]): r for r in csv.DictReader(open(pasta / "resumo.csv", encoding="utf-8"))}

    recortes = []  # (métrica, recorte, mediana, n, nível ou None)

    def registrar(metrica, objeto, rotulo, descricao):
        linha = resumo.get((objeto, rotulo))
        if linha is None or int(linha["execucoes"]) < EXECUCOES:
            n = int(linha["execucoes"]) if linha else 0
            recortes.append((metrica, descricao, float(linha["mediana"]) if linha else None, n, None))
            return
        valor = float(linha["mediana"])
        recortes.append((metrica, descricao, valor, EXECUCOES, nivel(valor, METRICAS[metrica][1])))

    for metrica in ("M3.1.1", "M3.1.2", "M3.3.1"):
        for objeto, nome in PAGINAS.items():
            registrar(metrica, objeto, METRICAS[metrica][0], nome)
    for tarefa in ("T1", "T2"):
        registrar("M3.2.1", tarefa, METRICAS["M3.2.1"][0], tarefa)
    for objeto, rotulo, descricao in RECORTES_MEMORIA:
        registrar("M3.4.1", objeto, rotulo, descricao)

    with open(pasta / "pontuacao.csv", "w", newline="", encoding="utf-8") as arquivo:
        saida = csv.writer(arquivo, quoting=csv.QUOTE_NONNUMERIC)
        saida.writerow(["metrica", "recorte", "mediana", "execucoes", "pontos", "nivel"])
        for metrica, descricao, valor, n, pontos in recortes:
            saida.writerow([metrica, descricao, valor, n, "NC" if pontos is None else pontos,
                            "NC" if pontos is None else NIVEIS[pontos]])

    print("## Pontuação por recorte\n")
    print("| Métrica | Recorte | Mediana | Execuções | Nível |")
    print("|---|---|---:|---:|---|")
    for metrica, descricao, valor, n, pontos in recortes:
        texto = "NC (não classificável)" if pontos is None else f"{NIVEIS[pontos]} ({pontos})"
        print(f"| {metrica} | {descricao} | {'–' if valor is None else numero(valor)} | {n} | {texto} |")

    pendente = any(p is None for *_, p in recortes)
    pontos_metrica = {
        m: mean(p for mm, _, _, _, p in recortes if mm == m and p is not None)
        for m in METRICAS
        if any(mm == m and p is not None for mm, _, _, _, p in recortes)
    }
    pontos_questao = {
        q: mean(pontos_metrica[m] for m in ms) for q, ms in QUESTOES.items() if all(m in pontos_metrica for m in ms)
    }

    print("\n## Consolidação\n")
    print("| Questão | Métricas | Pontos |")
    print("|---|---|---:|")
    for q, ms in QUESTOES.items():
        detalhe = "; ".join(f"{m} = {numero(pontos_metrica[m])}" if m in pontos_metrica else f"{m} = NC" for m in ms)
        print(f"| {q} | {detalhe} | {numero(pontos_questao[q]) if q in pontos_questao else 'NC'} |")

    if pendente or len(pontos_questao) < len(QUESTOES):
        print("\n**G3:** pendente. Há recorte sem 5 execuções válidas (regra 5 da seção 1).")
        return

    media = mean(pontos_questao.values())
    preliminar = juizo(media)
    lentos = [d for m, d, v, _, _ in recortes if (m == "M3.1.2" and v > 4.0) or (m == "M3.2.1" and v > 10.0)]
    final = preliminar
    if lentos and preliminar in ("Bom", "Excelente"):
        final = "Aceitável"
    print(f"\n**G3:** média {numero(media)}, juízo preliminar **{preliminar}**.")
    if lentos:
        print(f"Limitador da seção 5.2 acionado (LCP acima de 4 s ou tarefa acima de 10 s em: {', '.join(lentos)}): "
              f"juízo final no máximo Aceitável, portanto **{final}**.")
    else:
        print(f"Nenhum limitador acionado: juízo final **{final}**.")

    v = {(m, d): valor for m, d, valor, _, _ in recortes}
    lcp = {nome: v[("M3.1.2", nome)] for nome in PAGINAS.values()}
    cpu = {nome: v[("M3.3.1", nome)] for nome in PAGINAS.values()}
    delta_t1 = v[("M3.4.1", "Após T1")] - v[("M3.4.1", "Meu Território, após o carregamento")]
    delta_t2 = v[("M3.4.1", "Após T2")] - v[("M3.4.1", "SITGeo, após o carregamento")]
    print("\n## Conferência das hipóteses\n")
    print(f"- **H3.1:** FCP até 3,0 s nas três páginas: {sim(all(v[('M3.1.1', n)] <= 3.0 for n in PAGINAS.values()))}; "
          f"LCP acima de 4,0 s em Meu Território e no SITGeo: {sim(lcp['Meu Território'] > 4.0 and lcp['SITGeo'] > 4.0)}; "
          f"SITGeo é a página mais lenta: {sim(max(lcp, key=lcp.get) == 'SITGeo')}; "
          f"LCP da Biblioteca Territorial: {numero(lcp['Biblioteca Territorial'])} s (avaliar se está próximo de 4,0 s).")
    print(f"- **H3.2:** T2 entre 1 e 10 s: {sim(1.0 < v[('M3.2.1', 'T2')] <= 10.0)}; T1 acima de 10 s: {sim(v[('M3.2.1', 'T1')] > 10.0)}.")
    print(f"- **H3.3:** SITGeo acima de 4 s: {sim(cpu['SITGeo'] > 4.0)}; "
          f"Meu Território e Biblioteca abaixo de 4 s: {sim(cpu['Meu Território'] < 4.0 and cpu['Biblioteca Territorial'] < 4.0)}.")
    print(f"- **H3.4:** memória aumenta após T1 ({numero(delta_t1)} MB) e após T2 ({numero(delta_t2)} MB): "
          f"{sim(delta_t1 > 0 and delta_t2 > 0)}; aumento de T1 maior que o de T2: {sim(delta_t1 > delta_t2)}.")


if __name__ == "__main__":
    main()
