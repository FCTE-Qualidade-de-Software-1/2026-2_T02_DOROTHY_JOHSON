#!/usr/bin/env python3
"""Extrai dos relatórios do Lighthouse a evidência que motiva a ação de melhoria.

Para cada execução do SITGeo (data/fase-4/eficiencia/lighthouse/plataforma-geoespacial-<n>.json),
registra o elemento do LCP, as fases do LCP, o peso da página, o peso das imagens da página e a
economia estimada pelo Lighthouse com imagens no tamanho de exibição. Não acessa o portal.

Uso: scripts/fase-4/melhoria/diagnostico.py [DIR_LIGHTHOUSE] [PAGINA]
Grava data/fase-4/melhoria/diagnostico.csv e imagens-pagina.csv e imprime as medianas.

Requisitos: apenas Python 3 (biblioteca padrão).
"""

import csv
import json
import sys
from pathlib import Path
from statistics import median

DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "data/fase-4/eficiencia/lighthouse")
PAGINA = sys.argv[2] if len(sys.argv) > 2 else "plataforma-geoespacial"
SAIDA = Path("data/fase-4/melhoria")
FASES = ["TTFB", "Load Delay", "Load Time", "Render Delay"]


def ler(arquivo):
    auditorias = json.loads(arquivo.read_text())["audits"]
    itens = auditorias["largest-contentful-paint-element"]["details"]["items"]
    no = itens[0]["items"][0]["node"]
    fases = {i["phase"]: i["timing"] for i in itens[1]["items"]}
    requisicoes = auditorias["network-requests"]["details"]["items"]
    imagens = {
        r["url"]: r.get("transferSize", 0)
        for r in requisicoes
        if r.get("resourceType") == "Image"
    }
    origem = no["snippet"].split('src="')[1].split('"')[0] if 'src="' in no["snippet"] else ""
    linha = {
        "execucao": int(arquivo.stem.rsplit("-", 1)[1]),
        "lcp_s": round(auditorias["largest-contentful-paint"]["numericValue"] / 1000, 3),
        "elemento_lcp": origem or no.get("nodeLabel", "")[:60],
        "largura_exibida_px": no.get("boundingRect", {}).get("width", ""),
        "altura_exibida_px": no.get("boundingRect", {}).get("height", ""),
        **{f"fase_{f.lower().replace(' ', '_')}_s": round(fases.get(f, 0) / 1000, 3) for f in FASES},
        "peso_pagina_kb": round(sum(r.get("transferSize", 0) for r in requisicoes) / 1000, 1),
        "peso_imagens_kb": round(sum(imagens.values()) / 1000, 1),
        "economia_estimada_s": round(
            auditorias["uses-responsive-images"]["details"].get("overallSavingsMs", 0) / 1000, 2
        ),
    }
    return linha, imagens


def main():
    arquivos = sorted(DIR.glob(f"{PAGINA}-*.json"))
    if not arquivos:
        sys.exit(f"nenhum relatório {PAGINA}-*.json em {DIR}")
    linhas, pesos = [], {}
    for arquivo in arquivos:
        linha, imagens = ler(arquivo)
        linhas.append(linha)
        for url, tamanho in imagens.items():
            pesos.setdefault(url, []).append(tamanho)

    SAIDA.mkdir(parents=True, exist_ok=True)
    with open(SAIDA / "diagnostico.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), quoting=csv.QUOTE_NONNUMERIC)
        w.writeheader()
        w.writerows(linhas)

    # Só as imagens do próprio portal; os blocos do mapa (OpenStreetMap) ficam de fora.
    proprias = sorted(
        ((u, median(v)) for u, v in pesos.items() if "/img/" in u), key=lambda x: -x[1]
    )
    with open(SAIDA / "imagens-pagina.csv", "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(["imagem", "transferencia_mediana_kb"])
        for url, tamanho in proprias:
            w.writerow([url.split("/img/")[1], round(tamanho / 1000, 1)])

    print(f"Página: {PAGINA} ({len(linhas)} execuções)\n")
    print("| Medida | Mediana | Mínimo | Máximo |")
    print("|---|---:|---:|---:|")
    for chave in [c for c in linhas[0] if c.endswith(("_s", "_kb"))]:
        v = [l[chave] for l in linhas]
        print(f"| {chave} | {median(v)} | {min(v)} | {max(v)} |")
    print("\nElemento do LCP:", sorted({l["elemento_lcp"] for l in linhas}))
    print("\n| Imagem do portal | Transferência (kB) |")
    print("|---|---:|")
    for url, tamanho in proprias:
        print(f"| {url.split('/img/')[1]} | {round(tamanho / 1000, 1)} |")


if __name__ == "__main__":
    main()
