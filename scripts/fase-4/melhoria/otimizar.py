#!/usr/bin/env python3
"""Gera as versões otimizadas das duas imagens mais pesadas do SITGeo (ação de melhoria da Fase 4).

Baixa as imagens originais do portal, redimensiona para as larguras de exibição e converte
para WebP. As originais ficam em data/fase-4/melhoria/originais/ (fora do versionamento, por
causa do tamanho) e as otimizadas em docs/fase-4/melhoria/img/ (publicadas na GitPage, de onde
o script de medição as carrega). O inventário, com tamanho e hash de cada arquivo, vai para
data/fase-4/melhoria/imagens.csv.

Uso: scripts/fase-4/melhoria/otimizar.py
Variáveis opcionais: BASE, LARGURAS (ex.: "480,960"), QUALIDADE (padrão 80)

Requisitos: Python 3 e Pillow (pip install pillow).
"""

import csv
import hashlib
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow não encontrado: pip install pillow")

BASE = os.environ.get("BASE", "https://territoriosdacidadania.mda.gov.br")
LARGURAS = [int(x) for x in os.environ.get("LARGURAS", "480,960").split(",")]
QUALIDADE = int(os.environ.get("QUALIDADE", "80"))
IMAGENS = ["capa_inicio.jpg", "indicadores.png"]

ORIGINAIS = Path("data/fase-4/melhoria/originais")
OTIMIZADAS = Path("docs/fase-4/melhoria/img")
INVENTARIO = Path("data/fase-4/melhoria/imagens.csv")


def kb(n):
    """Tamanho em kB (1 kB = 1000 bytes), com vírgula decimal."""
    return f"{n / 1000:.1f}".replace(".", ",")


def baixar(nome):
    destino = ORIGINAIS / nome
    if destino.exists():
        return destino
    pedido = urllib.request.Request(f"{BASE}/img/{nome}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(pedido, timeout=120) as resposta:
        destino.write_bytes(resposta.read())
    return destino


def registro(arquivo, tipo, origem):
    with Image.open(arquivo) as img:
        largura, altura = img.size
        formato = img.format
    dados = arquivo.read_bytes()
    return {
        "arquivo": arquivo.name,
        "tipo": tipo,
        "origem": origem,
        "formato": formato,
        "largura_px": largura,
        "altura_px": altura,
        "bytes": len(dados),
        "sha256": hashlib.sha256(dados).hexdigest(),
    }


def main():
    ORIGINAIS.mkdir(parents=True, exist_ok=True)
    OTIMIZADAS.mkdir(parents=True, exist_ok=True)
    linhas = []
    for nome in IMAGENS:
        original = baixar(nome)
        linhas.append(registro(original, "original", f"{BASE}/img/{nome}"))
        with Image.open(original) as img:
            tem_alfa = img.mode in ("RGBA", "LA") or "transparency" in img.info
            img = img.convert("RGBA" if tem_alfa else "RGB")
            for largura in LARGURAS:
                # Nunca amplia: se a original for menor que a largura pedida, mantém o tamanho.
                alvo = min(largura, img.width)
                altura = round(img.height * alvo / img.width)
                reduzida = img.resize((alvo, altura), Image.LANCZOS)
                destino = OTIMIZADAS / f"{Path(nome).stem}-{largura}.webp"
                reduzida.save(destino, "WEBP", quality=QUALIDADE, method=6)
                linhas.append(registro(destino, "otimizada", nome))

    with open(INVENTARIO, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), quoting=csv.QUOTE_NONNUMERIC)
        w.writeheader()
        w.writerows(linhas)

    print(f"Gerado em {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n")
    print("| Arquivo | Tipo | Formato | Dimensões (px) | Tamanho (kB) |")
    print("|---|---|---|---|---:|")
    for l in linhas:
        print(
            f"| `{l['arquivo']}` | {l['tipo']} | {l['formato']} | "
            f"{l['largura_px']} × {l['altura_px']} | {kb(l['bytes'])} |"
        )
    maior = max(LARGURAS)
    antes = sum(l["bytes"] for l in linhas if l["tipo"] == "original")
    depois = sum(l["bytes"] for l in linhas if l["arquivo"].endswith(f"-{maior}.webp"))
    reducao = f"{100 * (1 - depois / antes):.1f}".replace(".", ",")
    print(
        f"\nAs duas imagens: {kb(antes)} kB antes, {kb(depois)} kB depois "
        f"(versões de {maior} px), redução de {reducao}%."
    )


if __name__ == "__main__":
    main()
