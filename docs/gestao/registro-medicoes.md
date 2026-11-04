# Registro Semanal das Medições (PSM/CID)

Este registro aplica o [Plano de Medição](plano-medicao.md) a cada semana da Entrega 1: compara
os indicadores M1 a M4 com os critérios de decisão do plano, interpreta o resultado e anota as
decisões de gestão que ele motivou. Atende à Premissa 3 do enunciado (medições, interpretação e
decisões registradas) e à [issue #20](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/20).

| Item | Valor |
|---|---|
| Fonte dos dados | Snapshots diários em [`data/psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/psm) |
| Cálculo | `scripts/psm/indicadores.py INICIO FIM PRAZO`, que lê os CSVs e imprime M1 a M4 da semana |
| Visualização | [Painel PSM](painel.md), com os mesmos cálculos em gráficos |
| Escopo de M1 | Issues das milestones **Fase 1** e **Fase 2**, que formam a Entrega 1 (prazo das milestones: 26/10/2026) |
| Escopo de M2 a M4 | Issues fechadas e PRs mergeados dentro da semana, pelo fuso de Brasília |
| Ligação com as atas | Cada registro é levado à reunião da semana e citado na seção 5 da ata (issue #18) |

Para reproduzir os números de cada semana:

```bash
scripts/psm/indicadores.py 2026-10-20 2026-10-26 2026-10-26   # semana 1
scripts/psm/indicadores.py 2026-10-27 2026-11-02 2026-10-26   # semana 2
```

## Resumo por semana

| Semana | % concluído (issues) | % concluído (pontos) | Horas registradas | Horas por ponto | Lead time médio | Revisão média de PR | Decisões |
|---|---|---|---|---|---|---|---|
| [1 (20/10 a 26/10)](#semana-1-2010-a-26102026) | 100% (34 de 34)¹ | 100% (28 de 28)¹ | 42,15 h² | 0,40 h/ponto² | 8,3 dias¹ | 13,2 h¹ | D1 a D4 |
| [2 (27/10 a 02/11)](#semana-2-2710-a-02112026) | 100% (34 de 34) | 100% (28 de 28) | 0 h | Sem dado | Sem dado | Sem dado | D5 a D7 |

¹ Valores recalculados em 04/11/2026 com o estado ao fim de 26/10 (ver a
[correção da semana 1](#correcao-de-04112026)). No registro original: 61% (27 de 44), 89% (25 de 28),
lead time de 4,9 dias e revisão de 17,7 h. Desde 04/11, as 10 issues duplicadas fechadas como
*not planned* (#1 a #4, #7, #8, #10, #12 a #14) ficam fora de todos os indicadores, em todos os
dias; por isso a entrega passa a ter 34 issues, e não 44.
² Inclui o preenchimento retroativo de `Estimate` e `Horas` feito em 04/11/2026 (ver a
[semana 2](#preenchimento-retroativo-de-estimate-e-horas-d3)). No registro original: 10,05 h,
todas de um único membro.

---

## Semana 1: 20/10 a 26/10/2026

Primeira semana de medição. Os snapshots usados vão de `2026-10-20.csv` a `2026-10-26.csv`; o
último foi coletado em 26/10 às 04:23 (Brasília), portanto os merges da noite de 26/10 (PRs #55
e #56) entram no registro da semana 2.

### Correção de 04/11/2026

!!! warning "O texto abaixo descreve o estado de 26/10 às 04:23"
    A coleta agendada para 23:00 roda, na prática, na madrugada seguinte (entre 04:00 e 06:30
    de Brasília). Assim, cada snapshot representa o **fim do dia anterior**, e o arquivo
    `2026-10-26.csv` não continha o que aconteceu durante 26/10. Na noite de 26/10, entre 21:40
    e 23:39, fecharam 17 issues (#5, #9, #11, #15, #17, #18, #20, #27, #28, #31, #33, #34, #37,
    #45, #46, #47 e #49) e foram mergeados os PRs #55, #56 e #57. Pela data, eles pertencem à
    semana 1; pelo método antigo, não entravam em semana nenhuma.

    O `indicadores.py` passou a usar, para cada dia, o primeiro snapshot coletado depois das
    23:59 desse dia (issue #58). Com isso, **a semana 1 termina com 34 de 34 issues concluídas e
    desvio de 0 p.p.**, lead time médio de 8,3 dias (13 issues acima do limite de 9,2 dias) e
    tempo médio até o merge de 13,2 h (#43 e #51 acima do limite de 14,6 h). Pelo padrão de
    revisão da equipe, o merge feito por outro membro, 8 de 12 PRs foram revisados; nenhum tem
    review formal do GitHub. A análise a seguir foi mantida como registrada, porque foi a base das decisões D1
    a D4; os números corrigidos estão no resumo e no [Painel PSM](painel.md).

### M1: progresso da entrega

| Snapshot | Issues | Concluídas | % | Issues com `Estimate` | Pontos | Pontos concluídos | % |
|---|---|---|---|---|---|---|---|
| 20/10 | 37 | 17 | 46% | 5 | 24 | 19 | 79% |
| 21/10 | 37 | 18 | 49% | 6 | 27 | 19 | 70% |
| 22/10 | 37 | 21 | 57% | 6 | 27 | 19 | 70% |
| 23/10 | 43 | 21 | 49% | 6 | 27 | 19 | 70% |
| 24/10 | 43 | 22 | 51% | 6 | 27 | 22 | 81% |
| 25/10 | 44 | 26 | 59% | 7 | 28 | 23 | 82% |
| 26/10 | 44 | 27 | 61% | 7 | 28 | 25 | 89% |

*Tabela 1: Burndown da Entrega 1 por snapshot diário.*

- **Resultado:** no dia do prazo das milestones, a linha ideal está em zero e ainda restam 17 de
  44 issues (39%) e 3 de 28 pontos (11%). O desvio é de **39 p.p. em issues** e **11 p.p. em
  pontos**.
- **Critério do plano:** desvio acima de 10% leva a equipe a considerar o replanejamento. Os dois
  desvios passam do limite.
- **Interpretação:** o desvio vem de duas causas. A primeira é o **aumento de escopo**: entre 22/10
  e 25/10 entraram 7 issues (#45 a #50 e #52), vindas de ajustes no artigo e na GitPage, como o
  modelo da SBC, a retirada do PSM do artigo e a adoção dos termos da ISO/IEC 25010:2023. A
  segunda é a **perda de ritmo depois de 21/10**: 21 das 27 issues concluídas fecharam até
  21/10. Dessas, 10 foram encerradas em lote, em dois minutos, na noite de 19/10: eram issues
  genéricas abertas no início do projeto (entre #1 e #14) e substituídas por issues detalhadas. De 22/10 a 26/10 fecharam só 6 issues, menos
  que as 7 que entraram. O percentual em pontos (89%) é otimista porque só 7 das 44 issues
  têm `Estimate`, quase todas já concluídas; o percentual em issues (61%) representa melhor o
  trabalho aberto.

### M2: esforço em horas

| Membro | Horas nas issues concluídas na semana |
|---|---|
| Felipe | 10,05 h (issues #6, #19, #23, #26, #38 e #52) |
| Demais membros | Não registradas |

- **Resultado:** 10,05 h registradas. Das 15 issues concluídas na semana, **9 estão sem `Horas`**
  (#16, #24, #25, #29, #30, #32, #35, #48 e #50).
- **Critério do plano:** medida informativa, sem limite de decisão.
- **Interpretação:** o total não representa o esforço da equipe: todas as horas vêm de um único
  membro. A regra 2 da Seção 5 do plano (preencher `Horas` ao mover para `Done`) e a regra 4
  (preenchimento retroativo) não foram seguidas pelos demais. Sem essa correção, a medida não serve
  para a tabela de contribuição (#33).

### M3: horas por ponto

- **Resultado:** 10,05 h em 25 pontos = **0,40 h/ponto**, calculado sobre as 6 issues com
  `Estimate` e `Horas` preenchidos.
- **Critério do plano:** variação de ±10% em relação à semana anterior. Como esta é a primeira
  semana, o valor serve de base para a comparação da semana 2.
- **Interpretação:** a base reflete as estimativas de um único membro. Se os outros passarem a
  preencher os campos, a variação da semana 2 vai misturar mudança de precisão com mudança de
  amostra. Isso deve ser lembrado na leitura.

### M4: lead time e tempo de revisão

| Item | Valor | Média da semana | Limite (média + 10%) | Situação |
|---|---|---|---|---|
| Issue #6 (Gráfico GQM) | 19,6 dias | 4,9 dias | 5,4 dias | Acima do limite |
| Issue #35 (Páginas Fase 1 e Fase 2) | 8,2 dias | 4,9 dias | 5,4 dias | Acima do limite |
| PR #43 (ODS 9.c e 16.10) | 59,7 h | 17,7 h | 19,4 h | Acima do limite |
| PR #51 (termos da ISO/IEC 25010:2023) | 61,2 h | 17,7 h | 19,4 h | Acima do limite |

*Tabela 2: Itens de M4 acima do critério de investigação. As outras 13 issues e 7 PRs ficaram
abaixo do limite.*

- **Critério do plano:** item mais de 10% acima da média é investigado.
- **Interpretação:**
    - **#6:** a issue foi criada em 05/10, junto com as issues da rubrica, e só foi iniciada
      depois que os três GQM ficaram prontos (21/10). O lead time mede principalmente espera no
      backlog por dependência, e não demora de execução.
    - **#35, #43 e #51:** o PR ficou aberto mais de 2 dias aguardando merge. O lead time da #35
      é consequência do PR #51.
    - **Revisão:** nenhum dos 9 PRs mergeados na semana tem review registrada no GitHub. O tempo
      até o merge é tempo de espera, e não de revisão. Além disso, o critério "revisado por outro
      membro", presente em várias issues, não deixa evidência no repositório.

### Decisões e encaminhamentos

| ID | Medida | Decisão ou encaminhamento | Responsável | Situação |
|---|---|---|---|---|
| D1 | M1 | Redistribuir as issues pendentes de um membro sem disponibilidade: #5, #9 e #20 foram reatribuídas em 26/10 (commit `11c627d` e [tabela de contribuição](../contribuicao.md)) | Equipe | Executada |
| D2 | M1 | Priorizar, até a release (#15), as issues que fecham critérios da rubrica (#11, #27, #31, #34) e tratar #45, #46, #47 e #49 como ajustes do artigo no Overleaf | Equipe | Proposta: confirmar na reunião |
| D3 | M2/M3 | Cada membro preenche `Estimate` e `Horas` das próprias issues concluídas, como manda a regra 4 do plano, antes do registro da semana 2 | Cada responsável | Proposta: confirmar na reunião |
| D4 | M4 | Exigir ao menos uma aprovação de outro membro no PR antes do merge, para que a revisão fique registrada e o tempo de revisão passe a ser medido | Equipe | Proposta: confirmar na reunião |

!!! warning "Registro na ata"
    Ainda não há ata de reunião posterior a 20/10. As decisões D2 a D4 só valem como
    **decisões da equipe** depois de aprovadas na próxima reunião e registradas na seção 5 da
    ata (issue #18). Até lá, são encaminhamentos propostos a partir das medições.

---

## Semana 2: 27/10 a 02/11/2026

Semana posterior ao prazo da Entrega 1. Registro feito em 04/11/2026 com os snapshots de
`2026-10-28.csv` a `2026-11-03.csv`, que representam o fim de cada dia de 27/10 a 02/11.

### M1: progresso da entrega

- **Resultado:** 34 de 34 issues (100%) e 28 de 28 pontos (100%) concluídos em todos os dias
  da semana. Desvio de **0 p.p.** em issues e em pontos.
- **Critério do plano:** desvio acima de 10% leva a considerar o replanejamento. Não se aplica.
- **Interpretação:** a Entrega 1 terminou na noite de 26/10 (ver a correção da semana 1). As
  milestones Fase 3 e Fase 4 existem, mas estão vazias, então o M1 não tem trabalho novo para
  acompanhar. Os oito snapshots de 27/10 a 03/11 são idênticos, a não ser pela coluna
  `coletado_em`.

### M2 a M4

- **Resultado:** nenhuma issue foi fechada e nenhum PR foi mergeado na semana. O único commit
  fora da coleta foi o documento de retrospectiva (`018e799`, 28/10), feito direto na `main`.
- **Interpretação:** sem itens concluídos, M2, M3 e M4 não têm valor nesta semana. A versão
  anterior do `indicadores.py` terminava com erro (divisão por zero) nesse caso; a versão da
  issue #58 imprime "nenhuma issue concluída na semana".

### Preenchimento retroativo de `Estimate` e `Horas` (D3)

A decisão D3 pedia que cada membro preenchesse os campos das próprias issues concluídas antes
deste registro, o que não aconteceu. Para que M2 e M3 tenham alguma base, os campos das 28
issues concluídas como *completed* que estavam vazios foram preenchidos em 04/11/2026. As 10
issues fechadas como *not planned* (#1 a #4, #7, #8, #10, #12 a #14) ficaram de fora: são
duplicatas das issues detalhadas e foram retiradas do Project em 04/11/2026. A exclusão das
issues no repositório depende de permissão do dono da organização.

**Método:**

1. **Horários de status:** foram consultados, mas não servem para estimar esforço. Em 18 das
   28 issues, a issue foi para `Done` poucos minutos depois de entrar em `In progress`, ou
   direto do `Backlog`, quase sempre na noite de 26/10.
2. **Estimate:** atribuído por analogia com as issues que já tinham o campo preenchido:
   1 ponto para um ajuste pontual (como a #52), 2 para uma página ou um diagrama (#6), 3 para
   uma seção com pesquisa (#23, #38), 5 para uma seção extensa e 8 para um GQM ou plano
   completo (#19, #26). O tamanho do entregável no repositório (linhas alteradas) e a
   quantidade de critérios da rubrica serviram de apoio.
3. **Horas:** `Estimate` × 0,40 h/ponto, a base do M3 na semana 1, que é a única taxa medida na
   equipe. Quando os commits mostram um tempo de trabalho maior, vale o valor observado: só a
   #33, com commits das 22:49 às 23:43 de 26/10 (0,9 h).

| Issue | Responsável | Estimate | Horas | Evidência no repositório |
|---|---|---|---|---|
| #5 Níveis de pontuação | analufernanndess | 5 | 2,0 | `2f4e7db` (+178 linhas) |
| #9 Declaração de uso de IA | TalesRG | 2 | 0,8 | `5a85a98` e texto no artigo |
| #11 Rastreabilidade F1 → F2 | feliperodri0, Cayoalencar | 3 (já preenchido) | 1,2 | PR #57 |
| #15 Release da E1 | analufernanndess | 1 | 0,4 | Sem release publicada no GitHub |
| #16 Kanban, labels e milestones | analufernanndess | 2 | 0,8 | Configuração do Project |
| #17 Estrutura de pastas | TalesRG | 2 | 0,8 | Commits de 05/10 (estrutura do site) |
| #18 Template de ata e atas | analufernanndess | 2 | 0,8 | `6fd2026` (+164 linhas) |
| #20 Registro semanal (E1) | Cayoalencar | 5 | 2,0 | PR #57 |
| #21 Propósito da avaliação | H0lzz | 3 | 1,2 | PR #36 |
| #22 Tipo de produto | H0lzz | 2 | 0,8 | PR #36 |
| #24 GQM capacidade de interação | Cayoalencar | 8 | 3,2 | PR #44 |
| #25 GQM flexibilidade | Cayoalencar, H0lzz | 5 | 2,0 | PR #44 |
| #27 Fichas das métricas | Cayoalencar | 3 | 1,2 | `6797a86` e PR #44 |
| #28 Modelo LaTeX e esqueleto | TalesRG | 3 | 1,2 | Overleaf |
| #29 Introdução | H0lzz | 3 | 1,2 | `0654728` e `1a11202` |
| #30 Referencial teórico | Cayoalencar | 5 | 2,0 | PR #44 |
| #31 Metodologia | Cayoalencar | 3 | 1,2 | PR #57 |
| #32 Seções Fase 1 e Fase 2 (artigo) | H0lzz | 5 | 2,0 | Overleaf |
| #33 Tabela de contribuição | TalesRG | 2 | 0,9 | `11c627d` a `1fc710b` |
| #34 Revisão final da E1 | analufernanndess | 3 | 1,2 | Sem commit associado |
| #35 Páginas Fase 1 e Fase 2 | H0lzz | 3 | 1,2 | PR #51 |
| #37 Seleção e priorização | analufernanndess | 5 | 2,0 | PR #55 (+104 linhas) |
| #45 Artigo no formato SBC | TalesRG | 2 | 0,8 | Overleaf |
| #46 Retirar o PSM do artigo | TalesRG | 1 | 0,4 | Overleaf |
| #47 Declaração de IA no artigo | TalesRG | 1 | 0,4 | Overleaf |
| #48 Termos 2023 no site | H0lzz | 3 | 1,2 | `0316118` |
| #49 Termos 2023 no artigo | TalesRG | 2 | 0,8 | Overleaf |
| #50 Tabelas de objetivo de medição | H0lzz | 1 | 0,4 | `dd010cb` |

*Tabela 3: Valores preenchidos retroativamente em 04/11/2026.*

- **Limitação:** essas horas são **previstas**, não medidas. Por construção, elas reproduzem a
  taxa de 0,40 h/ponto, então o M3 da semana 1 recalculado não é uma medição independente. Os
  valores servem para dar ordem de grandeza ao M2 e devem ser corrigidos por cada responsável
  que tiver o tempo real.

### Situação das decisões da semana 1

| ID | Situação em 04/11 | Evidência |
|---|---|---|
| D1 | Executada | #5, #9 e #20 concluídas pelos novos responsáveis |
| D2 | Executada | #11, #27, #31 e #34 concluídas em 26/10; #45 a #49 tratadas no Overleaf |
| D3 | Não cumprida pelos responsáveis; suprida pelo preenchimento retroativo | Cobertura de `Estimate` e `Horas` passou de 7 e 6 para 34 e 34 das 34 issues concluídas como *completed* (as 10 *not planned* não entram na cobertura) |
| D4 | Parcialmente cumprida | A equipe adota como revisão o merge feito por outro membro, que não exige aprovação formal no GitHub. Por esse critério, 8 de 12 PRs da semana 1 foram revisados; #42, #44, #53 e #57 foram mergeados pelo próprio autor |

### Decisões e encaminhamentos

| ID | Medida | Decisão ou encaminhamento | Responsável | Situação |
|---|---|---|---|---|
| D5 | M1 | Criar as issues da Fase 3 na milestone correspondente, com `Estimate`, e atualizar `extra.psm` no `mkdocs.yml` (início, prazo e milestones) para o painel acompanhar a nova entrega | Equipe | Proposta: confirmar na reunião |
| D6 | M2/M3 | Cada responsável confere a Tabela 3 e corrige `Horas` quando tiver o tempo real; a partir da Fase 3, `Horas` é preenchido ao mover a issue para `Done` (regra 2) | Cada responsável | Proposta: confirmar na reunião |
| D7 | M4 | Manter o padrão de revisão da equipe (merge feito por outro membro) e evitar o merge pelo próprio autor; o indicador "PRs mergeados por outra pessoa" passa a acompanhar isso no [Painel PSM](painel.md) | Equipe | Proposta: confirmar na reunião |

!!! warning "Registro na ata"
    Como na semana 1, as decisões D5 a D7 só valem como decisões da equipe depois de aprovadas
    em reunião e registradas na seção 5 da ata (issue #18).

---

## Próximo registro

O registro da semana 3 deve:

- verificar se D5 criou trabalho novo para o M1 e se o `mkdocs.yml` foi atualizado;
- verificar se D6 corrigiu algum valor da Tabela 3;
- verificar se D7 reduziu os PRs mergeados pelo próprio autor.
