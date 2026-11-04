#!/usr/bin/env bash
# Coleta snapshot diário do kanban e dos PRs para as medidas PSM/CID.
# Gera dois CSVs em $SAIDA_DIR:
#   AAAA-MM-DD.csv      itens do projeto (issues/PRs) com Status, Estimate, Horas, datas e
#                       motivo do fechamento (COMPLETED ou NOT_PLANNED)
#   prs-AAAA-MM-DD.csv  PRs do repositório com datas de abertura, primeira review e merge e
#                       quem fez o merge
# A coluna coletado_em é sempre a última (ver descartar_se_repetido).
# A data do arquivo segue o fuso de Brasília (America/Sao_Paulo).
#
# Requisitos: gh e jq. O token (GH_TOKEN) precisa apenas do escopo read:project;
# usa-se `gh api graphql` porque `gh project` exige também read:org.
#
# Uso: scripts/psm/coletar.sh
# Variáveis opcionais: ORG, REPO, PROJETO, SAIDA_DIR, DATA

set -euo pipefail

ORG="${ORG:-FCTE-Qualidade-de-Software-1}"
REPO="${REPO:-2026-2_T02_DOROTHY_JOHSON}"
PROJETO="${PROJETO:-7}"
SAIDA_DIR="${SAIDA_DIR:-data/psm}"
DATA="${DATA:-$(TZ=America/Sao_Paulo date +%F)}"
COLETADO_EM="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

mkdir -p "$SAIDA_DIR"

# Itens do projeto (paginação via $endCursor do gh api --paginate).
QUERY_ITENS='
query($org: String!, $projeto: Int!, $endCursor: String) {
  organization(login: $org) {
    projectV2(number: $projeto) {
      items(first: 100, after: $endCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          type
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldNumberValue {
                number
                field { ... on ProjectV2FieldCommon { name } }
              }
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field { ... on ProjectV2FieldCommon { name } }
              }
              ... on ProjectV2ItemFieldDateValue {
                date
                field { ... on ProjectV2FieldCommon { name } }
              }
            }
          }
          content {
            ... on Issue {
              number title state stateReason createdAt closedAt
              milestone { title }
              assignees(first: 10) { nodes { login } }
            }
            ... on PullRequest {
              number title state createdAt closedAt mergedAt
              milestone { title }
              assignees(first: 10) { nodes { login } }
            }
            ... on DraftIssue { title createdAt }
          }
        }
      }
    }
  }
}'

# Converte fieldValues em objeto {nome_do_campo: valor}.
JQ_ITENS='
  .data.organization.projectV2.items.nodes[]
  | (.fieldValues.nodes
      | map(select(.field.name != null)
            | {key: .field.name,
               value: ((.number | if . != null and . == floor then floor else . end)
                       // .name // .date)})
      | from_entries) as $f
  | .content as $c
  | [ $c.number, .type, $c.title, $c.state, $f["Status"], $f["Estimate"], $f["Horas"],
      $f["Start date"], $c.milestone.title,
      ([$c.assignees.nodes[]?.login] | join(";")),
      $c.createdAt, $c.closedAt, $c.mergedAt, $c.stateReason, $coletado ]
  | @csv'

ARQ_ITENS="$SAIDA_DIR/$DATA.csv"
{
  echo '"numero","tipo","titulo","estado","status","estimate","horas","start_date","milestone","responsaveis","criado_em","fechado_em","mergeado_em","motivo_fechamento","coletado_em"'
  gh api graphql --paginate \
    -f query="$QUERY_ITENS" -F org="$ORG" -F projeto="$PROJETO" \
    | jq -r --arg coletado "$COLETADO_EM" "$JQ_ITENS" \
    | sort -t, -k1,1n
} > "$ARQ_ITENS"

# PRs do repositório; reviews(first: 1) retorna a primeira review em ordem cronológica.
QUERY_PRS='
query($org: String!, $repo: String!, $endCursor: String) {
  repository(owner: $org, name: $repo) {
    pullRequests(first: 100, after: $endCursor, orderBy: {field: CREATED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number title state createdAt mergedAt closedAt
        author { login }
        mergedBy { login }
        reviews(first: 1) { nodes { submittedAt } }
      }
    }
  }
}'

JQ_PRS='
  .data.repository.pullRequests.nodes[]
  | [ .number, .title, .state, .author.login, .createdAt,
      .reviews.nodes[0].submittedAt, .mergedAt, .closedAt, .mergedBy.login, $coletado ]
  | @csv'

ARQ_PRS="$SAIDA_DIR/prs-$DATA.csv"
{
  echo '"numero","titulo","estado","autor","criado_em","primeira_review_em","mergeado_em","fechado_em","mergeado_por","coletado_em"'
  gh api graphql --paginate \
    -f query="$QUERY_PRS" -F org="$ORG" -F repo="$REPO" \
    | jq -r --arg coletado "$COLETADO_EM" "$JQ_PRS"
} > "$ARQ_PRS"

# Descarta o arquivo do dia quando ele repete o último snapshot, desconsiderando a coluna
# coletado_em: sem mudança nos dados, não há o que versionar. Se o arquivo do dia já existia
# no repositório, ele é restaurado em vez de removido.
sem_coletado_em() { sed 's/,"[^"]*"$//' "$1"; }

descartar_se_repetido() {
  local novo="$1" padrao="$2" anterior
  anterior="$(find "$SAIDA_DIR" -maxdepth 1 -name "$padrao" ! -name "$(basename "$novo")" | sort | tail -n 1)"
  if [[ -n "$anterior" ]] && cmp -s <(sem_coletado_em "$anterior") <(sem_coletado_em "$novo"); then
    git checkout -- "$novo" 2>/dev/null || rm "$novo"
    echo "Sem mudança em relação a $anterior: $novo descartado."
    return 0
  fi
  echo "Gerado: $novo ($(($(wc -l < "$novo") - 1)) linhas)"
}

descartar_se_repetido "$ARQ_ITENS" "????-??-??.csv"
descartar_se_repetido "$ARQ_PRS" "prs-????-??-??.csv"
