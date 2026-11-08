"""Hook do MkDocs: gera os dados da página Gestão > Painel PSM em assets/psm/.

Os dados vêm de scripts/psm/indicadores.py e são recalculados a cada build, então o painel
acompanha a coleta diária sem versionar o JSON. Cada entrega de extra.psm.entregas no
mkdocs.yml gera um arquivo entrega-N.json, e painel.json lista as entregas para o seletor.
"""

import importlib.util
import json
from datetime import date, datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "psm" / "indicadores.py"


def _indicadores():
    spec = importlib.util.spec_from_file_location("indicadores", SCRIPT)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def on_post_build(config, **kwargs):
    entregas = config["extra"]["psm"]["entregas"]
    indicadores = _indicadores()
    hoje = datetime.now(indicadores.BRASILIA).date()
    pasta = Path(config["site_dir"]) / "assets" / "psm"
    indice = []
    for numero, entrega in enumerate(entregas, start=1):
        inicio = date.fromisoformat(str(entrega["inicio"]))
        if "fim" in entrega:
            fim = date.fromisoformat(str(entrega["fim"]))
        elif numero < len(entregas):
            fim = date.fromisoformat(str(entregas[numero]["inicio"])) - timedelta(days=1)
        else:
            fim = hoje
        arquivo = f"entrega-{numero}.json"
        indicadores.main(
            [
                "--json",
                str(pasta / arquivo),
                inicio.isoformat(),
                min(fim, hoje).isoformat(),
                date.fromisoformat(str(entrega["prazo"])).isoformat(),
                *entrega["milestones"],
            ]
        )
        indice.append({"nome": entrega["nome"], "arquivo": arquivo})
    (pasta / "painel.json").write_text(
        json.dumps({"entregas": indice}, ensure_ascii=False), encoding="utf-8"
    )
