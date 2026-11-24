"""Hook do MkDocs: calcula a versão e a data de publicação exibidas no rodapé (critério AG-C4).

A versão vem da última tag de release (v*) alcançável a partir do commit publicado. Quando há
commits depois da tag, o rodapé mostra quantos são e o commit, com link para a comparação com a
tag, para não apresentar como release um conteúdo que mudou depois dela. A data é a do build, no fuso de Brasília. O deploy roda a cada
push na main e ao fim de cada coleta PSM diária, então o rodapé acompanha uma release nova em até
um dia.

O workflow faz checkout com fetch-depth: 0, que traz o histórico e as tags. Sem git ou sem tags
(por exemplo, num clone raso), o rodapé mostra só o commit, ou nada além da data.
"""

import subprocess
from datetime import datetime
from zoneinfo import ZoneInfo


def _git(*args):
    try:
        saida = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True, timeout=10
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return saida.stdout.strip() or None


def on_config(config, **kwargs):
    repo = (config.get("repo_url") or "").rstrip("/")
    commit = _git("rev-parse", "--short", "HEAD")
    tag = _git("describe", "--tags", "--abbrev=0", "--match", "v*")
    depois = _git("rev-list", "--count", f"{tag}..HEAD") if tag else None

    if tag:
        texto = tag
        url = f"{repo}/releases/tag/{tag}"
        if depois and depois != "0":
            sufixo = "commit" if depois == "1" else "commits"
            texto = f"{tag} + {depois} {sufixo} ({commit})"
            url = f"{repo}/compare/{tag}...{commit}"
    elif commit:
        texto = f"commit {commit}"
        url = f"{repo}/commit/{commit}"
    else:
        texto, url = None, None

    agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
    config["extra"]["versao"] = {
        "texto": texto,
        "url": url,
        "data": agora.strftime("%d/%m/%Y"),
        "data_iso": agora.strftime("%Y-%m-%d"),
    }
    return config
