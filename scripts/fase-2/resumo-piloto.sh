#!/usr/bin/env bash
# Consolida o piloto do GQM G3 pela mediana das execuções e grava
# data/fase-2/piloto/resumo.csv (valores em segundos e MB).
set -euo pipefail

DIR="${DIR:-data/fase-2/piloto}"
SAIDA="${DIR}/resumo.csv"

mediana='sort | if length % 2 == 1 then .[length / 2 | floor] else (.[length / 2 - 1] + .[length / 2]) / 2 end'

{
  echo '"objeto","metrica","mediana","execucoes"'
  for pagina in meu-territorio plataforma-geoespacial downloads; do
    jq -rs --arg p "$pagina" "
      def med: ${mediana};
      [
        [\$p, \"M3.1.1 FCP (s)\", (map(.audits[\"first-contentful-paint\"].numericValue / 1000) | med), length],
        [\$p, \"M3.1.2 LCP (s)\", (map(.audits[\"largest-contentful-paint\"].numericValue / 1000) | med), length],
        [\$p, \"M3.3.1 CPU thread principal (s)\", (map(.audits[\"mainthread-work-breakdown\"].numericValue / 1000) | med), length]
      ][] | @csv" "${DIR}"/lighthouse/"${pagina}"-*.json
  done
  jq -r "
    def med: ${mediana};
    group_by(.tarefa)[] | . as \$g |
    [
      [\$g[0].tarefa, \"M3.2.1 execução da tarefa (s)\", (map(.tempo_s) | med), length],
      [\$g[0].tarefa, \"M3.4.1 JS heap após carregamento (MB)\", (map(.heap_carga_mb) | med), length],
      [\$g[0].tarefa, \"M3.4.1 JS heap após tarefa (MB)\", (map(.heap_tarefa_mb) | med), length]
    ][] | @csv" "${DIR}/tarefas.json"
} > "$SAIDA"

cat "$SAIDA"
