# Gestão do projeto (PSM/CID)

A equipe acompanhou a execução do próprio projeto com medidas do PSM, organizadas pelo
*Continuous Iterative Development (CID) Measurement Framework*. Esta página resume os
indicadores, a interpretação e as decisões das Entregas 1 e 2
([issue #94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/94)).
Os detalhes ficam nas páginas abaixo.

| Página | Conteúdo |
|---|---|
| [Plano de Medição](plano-medicao.md) | Necessidades de informação, medidas M1 a M4, coleta e critérios de decisão |
| [Registro Semanal](registro-medicoes.md) | Medições de cada semana, interpretação e decisões D1 a D14 |
| [Painel PSM](painel.md) | Gráficos de M1 a M4 por entrega, recalculados a cada coleta diária |
| [Atas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/atas-de-reuniao) | Reuniões em que as medições foram discutidas |

*Tabela 1: Páginas da gestão do projeto.*

## 1. Como a medição funciona

| Medida | Categoria do PSM | O que mostra | Critério de decisão |
|---|---|---|---|
| M1 | Calendário e Progresso | Percentual do planejado ainda aberto, em issues e em pontos, comparado com a linha ideal até o prazo | Desvio de 5% leva a revisar os impedimentos; acima de 10%, a considerar o replanejamento |
| M2 | Recursos e Custos | Horas por membro nas issues concluídas | Informativa, sem limite de decisão |
| M3 | Recursos e Custos | Horas por ponto de `Estimate` | Variação acima de 10% em relação à semana anterior |
| M4 | Desempenho dos Processos | Lead time das issues e tempo até o merge dos PRs | Item mais de 10% acima da média da semana é investigado |

*Tabela 2: Medidas do plano. As definições completas estão no [plano](plano-medicao.md).*

Um workflow do GitHub Actions grava todo dia um snapshot das issues e dos PRs em
[`data/psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/psm).
O script `scripts/psm/indicadores.py` calcula M1 a M4 a partir desses arquivos, e o site é
publicado depois de cada coleta, o que mantém o painel atualizado.

## 2. Resultados por entrega

| Indicador | Entrega 1 (Fases 1 e 2) | Entrega 2 (Fases 3 e 4) |
|---|---|---|
| Período | 20/10 a 26/10/2026 | 05/11 a 24/11/2026 |
| Issues planejadas | 34 | 37 |
| Concluídas no prazo | 34 (100%) | 21 (57%) ao fim de 23/11; 25 (68%) no snapshot de 24/11 |
| Maior desvio do M1 | +33 p.p. em 25/10 | +46 p.p. em 21/11 |
| Horas registradas | 42,15 h | 28,0 h |
| Horas por ponto | 0,40 h/ponto | 0,36 h/ponto |
| Lead time médio | 8,3 dias | 13,0 dias |
| PRs mergeados por outro membro | 8 de 12 (semana 1) | 15 de 18 |

*Tabela 3: Indicadores consolidados. A série semana a semana está no
[resumo do registro](registro-medicoes.md#resumo-por-semana).*

- **Calendário e progresso:** nas duas entregas, o trabalho ficou concentrado perto do prazo.
  A E1 fechou 17 issues na última noite. A E2 ficou de 17/11 a 21/11 sem fechar nenhuma issue e
  fechou 11 nos três últimos dias; o prazo foi adiado de 22/11 para 24/11.
- **Recursos e custos:** a taxa de horas por ponto ficou estável, entre 0,36 e 0,40 h/ponto.
  `Estimate` e `Horas` foram quase sempre preenchidos depois do trabalho, e não ao criar a
  issue.
- **Desempenho dos processos:** o merge por outro membro se firmou como o padrão de revisão
  da equipe, e o tempo médio até o merge caiu de 28,8 h na semana 4 para 6,0 h na semana 5.

## 3. Decisões de gestão

| ID | Entrega | Decisão | Resultado |
|---|---|---|---|
| D1 | E1 | Redistribuir as issues de um membro sem disponibilidade | Executada |
| D2 | E1 | Priorizar as issues que fecham critérios da rubrica antes da release | Executada |
| D3 | E1 | Preencher `Estimate` e `Horas` das issues concluídas | Suprida por preenchimento retroativo |
| D4 | E1 | Exigir revisão de outro membro antes do merge | Cumprida em parte; virou o padrão de merge por outro membro |
| D5 | E1 → E2 | Criar as issues da E2 e configurar o painel para a nova entrega | Executada |
| D6 | E2 | Preencher `Horas` ao mover a issue para `Done` | Não cumprida |
| D7 | E2 | Manter o merge por outro membro e acompanhá-lo no painel | Cumprida |
| D8 | E2 | Atribuir responsável às issues sem dono | Cumprida em parte; todas com responsável no fim da E2 |
| D9 | E2 | Preencher `Estimate` das issues da E2 até 10/11 | Não cumprida no prazo |
| D10 | E2 | Combinar datas intermediárias | Não cumprida; o cronograma saiu no fim da entrega |
| D11 | E2 | Revisar e mergear PRs em até 24 h | Cumprida em parte |
| D12 | E2 | Priorizar G1, consolidação e artigo depois do Ponto de Controle 2 | Cumprida em parte |
| D13 | E2 | Atualizar o registro com o estado ao fim de 24/11 | A executar em 25/11 |
| D14 | E2 | Registrar as lições das duas entregas nesta página | Executada |

*Tabela 4: Decisões tomadas a partir das medições. Evidências e situação semana a semana no
[registro](registro-medicoes.md).*

## 4. Lições aprendidas

1. **Datas intermediárias desde o início.** O M1 mostrou atraso nas duas entregas, mas a
   decisão de criar marcos internos (D10) só foi executada no fim da E2. Os marcos devem ser
   definidos junto com as issues, no primeiro dia da entrega.
2. **Responsável e `Estimate` na criação da issue.** Issues sem dono e sem estimativa deixaram
   o M1 em pontos sem base durante a maior parte da E2 (D8 e D9).
3. **`Horas` no momento da conclusão.** O preenchimento posterior (D3 e D6) torna o M3 uma
   previsão, e não uma medida do esforço.
4. **Revisão rápida por outro membro.** O padrão de merge por outro membro funcionou; PRs
   parados por dias (como o #98) atrasaram o fechamento das issues ligadas a eles.
