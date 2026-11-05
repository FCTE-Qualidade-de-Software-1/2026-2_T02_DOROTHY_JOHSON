"""Hook do MkDocs: acrescenta ?v=<hash do conteúdo> ao CSS e ao JavaScript próprios do site.

O GitHub Pages permite que o navegador reutilize esses arquivos por 10 minutos e o tema usa
navegação instantânea, então um deploy novo podia exibir o HTML atual com o CSS anterior.
Com o hash no endereço, o arquivo só é reaproveitado enquanto o conteúdo não muda.
"""

import hashlib
from pathlib import Path


def _versionar(caminho, docs_dir):
    if "://" in caminho or "?" in caminho:
        return caminho
    arquivo = Path(docs_dir) / caminho
    if not arquivo.is_file():
        return caminho
    versao = hashlib.sha256(arquivo.read_bytes()).hexdigest()[:10]
    return f"{caminho}?v={versao}"


def on_config(config, **kwargs):
    docs_dir = config["docs_dir"]
    config["extra_css"] = [_versionar(c, docs_dir) for c in config["extra_css"]]
    config["extra_javascript"] = [
        _versionar(str(j), docs_dir) if isinstance(j, str) else j for j in config["extra_javascript"]
    ]
    return config
