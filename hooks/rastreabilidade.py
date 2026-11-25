"""Hook do MkDocs: rastreabilidade entre objetivos, questões, métricas e resultados do GQM.

Faz duas coisas a cada build:

1. Gera o conteúdo da página rastreabilidade.md, no lugar do marcador
   <!-- rastreabilidade -->, a partir de data/fase-4/consolidado/medidas.csv e
   classificacao.csv: para cada objetivo, as questões, as métricas, os recortes com valor e
   nível, os pontos e a classificação, com links para as páginas que detalham cada parte.
2. Transforma em link cada menção a um objetivo (G1), questão (Q1.1) ou métrica (M1.1.1) no
   texto das páginas, apontando para a definição na Fase 2. Títulos, código, links já
   existentes e a página da própria definição ficam como estão.

As âncoras são lidas dos títulos das páginas, então continuam válidas se um título mudar.
"""

import csv
import os
import re
from pathlib import Path

from markdown.extensions.toc import slugify
from mkdocs.utils import get_relative_url

RAIZ = Path(__file__).resolve().parents[1]
CONSOLIDADO = RAIZ / "data" / "fase-4" / "consolidado"
MARCADOR = "<!-- rastreabilidade -->"

OBJETIVOS = "fase-2/objetivos.md"
QUESTOES = "fase-2/questoes.md"
METRICAS = "fase-2/metricas.md"
CLASSIFICACAO_FINAL = "fase-4/classificacao-final.md"
CARACTERISTICAS = {
    "G1": ("Capacidade de interação", "fase-3/metodo-interacao.md", "fase-4/interacao.md"),
    "G2": ("Flexibilidade", "fase-3/metodo-flexibilidade.md", "fase-4/flexibilidade.md"),
    "G3": ("Eficiência de desempenho", "fase-3/metodo-eficiencia.md", "fase-4/eficiencia.md"),
}
NIVEIS = {"0": "Insatisfatório", "1": "Aceitável", "2": "Bom", "3": "Excelente"}

ID = re.compile(r"(?<![\w.])(G[1-3]|Q[1-3]\.[1-9]|M[1-3]\.[1-9]\.[1-9])(?![\w]|\.\d)")
TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*(?:\{#([\w-]+)\})?\s*$")
SEM_LINK = {"a", "h1", "h2", "h3", "h4", "h5", "h6", "code", "pre", "script", "style", "svg", "title", "kbd"}
ETIQUETA = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*?(/?)>")

_estado = {"arquivos": None, "docs": None, "repo": "", "alvos": {}, "titulos": {}}


def _titulos(caminho):
    """Lista (texto, âncora) dos títulos de um .md, com a âncora gerada pelo toc."""
    if caminho in _estado["titulos"]:
        return _estado["titulos"][caminho]
    resultado, em_codigo = [], False
    arquivo = _estado["docs"] / caminho
    if arquivo.exists():
        for linha in arquivo.read_text(encoding="utf-8").splitlines():
            if linha.lstrip().startswith(("```", "~~~")):
                em_codigo = not em_codigo
            if em_codigo:
                continue
            m = TITULO.match(linha)
            if m and len(m.group(1)) > 1:
                texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", m.group(2)).replace("`", "").replace("*", "")
                resultado.append((texto, m.group(3) or slugify(texto, "-")))
    _estado["titulos"][caminho] = resultado
    return resultado


def _ancora(caminho, *termos):
    """Âncora do primeiro título que contém algum dos termos (por ordem de preferência)."""
    for termo in termos:
        padrao = re.compile(rf"(?<![\w.]){re.escape(termo)}(?![\w]|\.\d)", re.I)
        for texto, ancora in _titulos(caminho):
            if padrao.search(texto):
                return ancora
    return ""


def _alvos():
    """Mapa de cada ID para (arquivo, âncora) da definição na Fase 2."""
    alvos = {}
    for g in CARACTERISTICAS:
        alvos[g] = (OBJETIVOS, _ancora(OBJETIVOS, g))
        for n in range(1, 10):
            alvos[f"Q{g[1]}.{n}"] = (QUESTOES, f"q{g[1]}{n}")
    for texto, ancora in _titulos(METRICAS):
        m = re.match(r"(M[1-3]\.[1-9]\.[1-9])\b", texto)
        if m:
            alvos[m.group(1)] = (METRICAS, ancora)
    return alvos


def _url(origem, caminho, ancora=""):
    arquivo = _estado["arquivos"].get_file_from_path(caminho)
    if arquivo is None:
        return ""
    destino = get_relative_url(arquivo.url, origem)
    return f"{destino}#{ancora}" if ancora else destino


def on_config(config):
    _estado["docs"] = Path(config["docs_dir"])
    _estado["repo"] = (config.get("repo_url") or "").rstrip("/")
    _estado["titulos"] = {}
    return config


def on_files(files, config):
    _estado["arquivos"] = files
    _estado["alvos"] = _alvos()
    return files


# --- Página de rastreabilidade ---------------------------------------------------------


def _ler(nome):
    with open(CONSOLIDADO / nome, encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def _numero(valor, casas=2):
    return f"{valor:.{casas}f}".replace(".", ",")


def _valor(linha):
    if not linha["valor"]:
        return "sem valor"
    unidade = linha["unidade"]
    try:
        v = float(linha["valor"])
    except ValueError:
        return f"{linha['valor']} {unidade}"
    if unidade == "proporção":
        return f"{_numero(100 * v, 0)}%"
    if unidade in ("s", "MB"):
        return f"{_numero(v)} {unidade}"
    if unidade == "razão":
        return _numero(v)
    texto = _numero(v, 0) if v == int(v) else _numero(v)
    return f"{texto} ({unidade})"


def _pontos(texto):
    return "NC" if texto in ("", "NC") else _numero(float(texto))


def _link(texto, url):
    return f'<a href="{url}">{texto}</a>' if url else texto


def _pagina(origem):
    medidas, classificacao = _ler("medidas.csv"), _ler("classificacao.csv")
    pontos = {linha["item"]: linha for linha in classificacao}
    repo = _estado["repo"]
    partes = []
    for g, (nome, metodo, analise) in CARACTERISTICAS.items():
        linha_g = pontos.get(g, {})
        final = linha_g.get("classificacao_final") or "pendente"
        resumo_g = f"{final} ({_pontos(linha_g.get('pontos', ''))})" if final != "pendente" else "NC (ver a classificação final)"
        alvo_g = _estado["alvos"][g]
        cabecalho = " · ".join(
            [
                _link("Objetivo (F2)", _url(origem, *alvo_g)),
                _link("Método (F3)", _url(origem, metodo)),
                _link("Análise (F4)", _url(origem, analise, _ancora(analise, f"Classificação do {g}", f"Classificação de {g}", "Classificação"))),
                _link("Classificação final", _url(origem, CLASSIFICACAO_FINAL, _ancora(CLASSIFICACAO_FINAL, g))),
            ]
        )
        linhas = []
        questoes = sorted({m["questao"] for m in medidas if m["caracteristica"] == g})
        for q in questoes:
            metricas = sorted({m["metrica"] for m in medidas if m["questao"] == q})
            for i, metrica in enumerate(metricas):
                recortes = [m for m in medidas if m["metrica"] == metrica]
                itens = []
                for r in recortes:
                    nivel = NIVEIS.get(r["pontos"], "NC")
                    itens.append(f"{r['recorte']}: {_valor(r)} → {nivel}")
                brutos = sorted(
                    str(Path(c).parent) if "<" in c else c
                    for c in {c.strip() for r in recortes for c in r["dado_bruto"].split(";") if c.strip()}
                )
                brutos = sorted(set(brutos))
                detalhes = [
                    _link("Ficha", _url(origem, *_estado["alvos"].get(metrica, (METRICAS, "")))),
                    _link("Método", _url(origem, metodo, _ancora(metodo, metrica))),
                    _link("Resultado", _url(origem, analise, _ancora(analise, metrica, q, "Respostas", "Resultados"))),
                ]
                if brutos and repo:
                    caminho = brutos[0] if len(brutos) == 1 else os.path.commonpath(brutos)
                    tipo = "blob" if len(brutos) == 1 and Path(caminho).suffix else "tree"
                    detalhes.append(_link("Dado bruto", f"{repo}/{tipo}/main/{caminho}"))
                coluna_q = ""
                if i == 0:
                    coluna_q = (
                        f"{_link(q, _url(origem, *_estado['alvos'][q]))}<br>"
                        f"{_link(_pontos(pontos.get(q, {}).get('pontos', '')), _url(origem, analise, _ancora(analise, q, 'Respostas', 'Resultados')))}"
                    )
                linhas.append(
                    "<tr>"
                    f"<td>{coluna_q}</td>"
                    f"<td>{_link(metrica, _url(origem, *_estado['alvos'].get(metrica, (METRICAS, ''))))}</td>"
                    f"<td>{'<br>'.join(itens)}</td>"
                    f"<td>{_pontos(pontos.get(metrica, {}).get('pontos', ''))}</td>"
                    f"<td>{' · '.join(detalhes)}</td>"
                    "</tr>"
                )
        partes.append(
            f'<details class="rastreio" open>\n'
            f"<summary><strong>{g} {nome}</strong>: {resumo_g}</summary>\n"
            f'<p class="rastreio__links">{cabecalho}</p>\n'
            '<div class="rastreio__tabela"><table>\n'
            "<thead><tr><th>Questão e pontos</th><th>Métrica</th><th>Recortes: valor → nível</th>"
            "<th>Pontos</th><th>Detalhes</th></tr></thead>\n"
            f"<tbody>{''.join(linhas)}</tbody>\n"
            "</table></div>\n</details>\n"
        )
    return "\n".join(partes)


def on_page_markdown(markdown, page, config, files):
    if MARCADOR in markdown:
        return markdown.replace(MARCADOR, _pagina(page.file.url))
    return markdown


# --- Links automáticos nos IDs ---------------------------------------------------------


def _questoes_com_ancora(html):
    """Põe id="qNN" na célula que abre cada linha da tabela de questões."""
    return re.sub(
        r"<td>(Q([1-3])\.([1-9]))</td>",
        lambda m: f'<td id="q{m.group(2)}{m.group(3)}">{m.group(1)}</td>',
        html,
    )


def on_page_content(html, page, config, files):
    if page.file.src_uri == QUESTOES:
        html = _questoes_com_ancora(html)
    origem = page.file.url
    pedacos = re.split(r"(<[^>]+>)", html)
    pilha = []
    for i, pedaco in enumerate(pedacos):
        if pedaco.startswith("<"):
            m = ETIQUETA.match(pedaco)
            if m and m.group(2).lower() in SEM_LINK and not m.group(3):
                nome = m.group(2).lower()
                if m.group(1):
                    if nome in pilha:
                        del pilha[len(pilha) - 1 - pilha[::-1].index(nome)]
                else:
                    pilha.append(nome)
            continue
        if pilha or not ID.search(pedaco):
            continue

        def trocar(m):
            alvo = _estado["alvos"].get(m.group(1))
            if not alvo or alvo[0] == page.file.src_uri:
                return m.group(1)
            url = _url(origem, *alvo)
            return f'<a class="rastreio-id" href="{url}">{m.group(1)}</a>' if url else m.group(1)

        pedacos[i] = ID.sub(trocar, pedaco)
    return "".join(pedacos)
