#!/usr/bin/env bash
# Coleta de M3.1.1 (FCP), M3.1.2 (LCP) e M3.3.1 (CPU na thread principal) do GQM G3:
# Lighthouse com o perfil móvel padrão, 5 execuções sequenciais por página.
# Procedimento: docs/fase-3/metodo-eficiencia.md (seção "Procedimento A").
#
# Uso: scripts/fase-4/eficiencia/lighthouse.sh
# Variáveis opcionais: SAIDA, EXECUCOES, BASE, LIGHTHOUSE_VERSAO, CHROME_PATH
set -euo pipefail

LIGHTHOUSE_VERSAO="${LIGHTHOUSE_VERSAO:-12.8.2}"
BASE="${BASE:-https://territoriosdacidadania.mda.gov.br}"
EXECUCOES="${EXECUCOES:-5}"
SAIDA="${SAIDA:-data/fase-4/eficiencia/lighthouse}"
export CHROME_PATH="${CHROME_PATH:-$(command -v google-chrome || command -v chromium)}"

mkdir -p "$SAIDA"
for pagina in meu-territorio plataforma-geoespacial downloads; do
  for i in $(seq 1 "$EXECUCOES"); do
    echo "$(date -Iseconds) ${pagina} execução ${i}"
    npx -y "lighthouse@${LIGHTHOUSE_VERSAO}" "${BASE}/${pagina}" \
      --only-categories=performance \
      --output=json --output-path="${SAIDA}/${pagina}-${i}.json" \
      --chrome-flags="--headless=new --no-sandbox" --quiet
  done
done
