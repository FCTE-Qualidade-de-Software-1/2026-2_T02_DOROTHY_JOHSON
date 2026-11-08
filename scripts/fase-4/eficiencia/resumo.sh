#!/usr/bin/env bash
# Consolida a coleta do GQM G3 pela mediana das execuções, com mínimo e máximo, e grava
# data/fase-4/eficiencia/resumo.csv (valores em segundos e MB).
# Procedimento: docs/fase-3/metodo-eficiencia.md (seção "Consolidação").
set -euo pipefail

DIR="${DIR:-data/fase-4/eficiencia}"
SAIDA="${DIR}/resumo.csv"

estat='sort | {mediana: (if length % 2 == 1 then .[length / 2 | floor] else (.[length / 2 - 1] + .[length / 2]) / 2 end), minimo: .[0], maximo: .[-1], n: length}'

{
  echo '"objeto","metrica","mediana","minimo","maximo","execucoes"'
  for pagina in meu-territorio plataforma-geoespacial downloads; do
    jq -rs --arg p "$pagina" "
      def est: ${estat};
      def linha(nome; valores): (valores | est) as \$e | [\$p, nome, \$e.mediana, \$e.minimo, \$e.maximo, \$e.n] | @csv;
      linha(\"M3.1.1 FCP (s)\"; map(.audits[\"first-contentful-paint\"].numericValue / 1000)),
      linha(\"M3.1.2 LCP (s)\"; map(.audits[\"largest-contentful-paint\"].numericValue / 1000)),
      linha(\"M3.3.1 CPU thread principal (s)\"; map(.audits[\"mainthread-work-breakdown\"].numericValue / 1000))
    " "${DIR}"/lighthouse/"${pagina}"-*.json
  done
  jq -r "
    def est: ${estat};
    def linha(obj; nome; valores): (valores | est) as \$e | [obj, nome, \$e.mediana, \$e.minimo, \$e.maximo, \$e.n] | @csv;
    group_by(.objeto)[] | . as \$g |
    if \$g[0].tarefa == null then
      linha(\$g[0].objeto; \"M3.4.1 JS heap após carregamento (MB)\"; map(.heap_carga_mb))
    else
      linha(\$g[0].tarefa; \"M3.2.1 execução da tarefa (s)\"; map(.tempo_s)),
      linha(\$g[0].tarefa; \"M3.4.1 JS heap após carregamento (MB)\"; map(.heap_carga_mb)),
      linha(\$g[0].tarefa; \"M3.4.1 JS heap após tarefa (MB)\"; map(.heap_tarefa_mb))
    end" "${DIR}/tarefas.json"
} > "$SAIDA"

cat "$SAIDA"
