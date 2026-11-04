"""Hook do MkDocs: gera assets/psm/painel.json, lido pela página Gestão > Painel PSM.

Os dados vêm de scripts/psm/indicadores.py e são recalculados a cada build, então o painel
acompanha a coleta diária sem versionar o JSON. Período, prazo e milestones ficam em
extra.psm no mkdocs.yml.
"""

import importlib.util
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "psm" / "indicadores.py"


def _indicadores():
    spec = importlib.util.spec_from_file_location("indicadores", SCRIPT)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def on_post_build(config, **kwargs):
    psm = config["extra"]["psm"]
    indicadores = _indicadores()
    hoje = datetime.now(indicadores.BRASILIA).date()
    saida = Path(config["site_dir"]) / "assets" / "psm" / "painel.json"
    indicadores.main(
        [
            "--json",
            str(saida),
            date.fromisoformat(str(psm["inicio"])).isoformat(),
            hoje.isoformat(),
            date.fromisoformat(str(psm["prazo"])).isoformat(),
            *psm["milestones"],
        ]
    )
