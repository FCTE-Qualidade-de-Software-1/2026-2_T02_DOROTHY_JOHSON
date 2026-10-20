#!/usr/bin/env bash
# Piloto das métricas M3.1.1, M3.1.2 e M3.3.1 (GQM G3): Lighthouse, perfil móvel padrão,
# 5 execuções sequenciais por página, relatórios JSON em data/fase-2/piloto/lighthouse/.
set -euo pipefail

LIGHTHOUSE_VERSAO="${LIGHTHOUSE_VERSAO:-12.8.2}"
BASE="${BASE:-https://territoriosdacidadania.mda.gov.br}"
EXECUCOES="${EXECUCOES:-5}"
SAIDA="${SAIDA:-data/fase-2/piloto/lighthouse}"
export CHROME_PATH="${CHROME_PATH:-$(command -v google-chrome || command -v chromium)}"

mkdir -p "$SAIDA"
for pagina in meu-territorio plataforma-geoespacial downloads; do
  for i in $(seq 1 "$EXECUCOES"); do
    npx -y "lighthouse@${LIGHTHOUSE_VERSAO}" "${BASE}/${pagina}" \
      --only-categories=performance \
      --output=json --output-path="${SAIDA}/${pagina}-${i}.json" \
      --chrome-flags="--headless=new --no-sandbox" --quiet
  done
done
