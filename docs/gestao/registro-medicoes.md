# Registro Semanal das Medições (PSM/CID)

Este registro aplica o [Plano de Medição](plano-medicao.md) a cada semana da Entrega 1: compara
os indicadores M1 a M4 com os critérios de decisão do plano, interpreta o resultado e anota as
decisões de gestão que ele motivou. Atende à Premissa 3 do enunciado (medições, interpretação e
decisões registradas) e à [issue #20](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/20).

| Item | Valor |
|---|---|
| Fonte dos dados | Snapshots diários em [`data/psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/psm) |
| Cálculo | `scripts/psm/indicadores.py INICIO FIM PRAZO`, que lê os CSVs da semana e imprime M1 a M4 |
| Escopo de M1 | Issues das milestones **Fase 1** e **Fase 2**, que formam a Entrega 1 (prazo das milestones: 26/10/2026) |
| Escopo de M2 a M4 | Issues fechadas e PRs mergeados dentro da semana, pelo fuso de Brasília |
| Ligação com as atas | Cada registro é levado à reunião da semana e citado na seção 5 da ata (issue #18) |

Para reproduzir os números da semana 1:

```bash
scripts/psm/indicadores.py 2026-10-20 2026-10-26 2026-10-26
```

## Resumo por semana

| Semana | % concluído (issues) | % concluído (pontos) | Horas registradas | Horas por ponto | Lead time médio | Revisão média de PR | Decisões |
|---|---|---|---|---|---|---|---|
| [1 (20/10 a 26/10)](#semana-1-2010-a-26102026) | 61% (27 de 44) | 89% (25 de 28) | 10,05 h | 0,40 h/ponto | 4,9 dias | 17,7 h | D1 a D4 |

---

## Semana 1: 20/10 a 26/10/2026

Primeira semana de medição. Os snapshots usados vão de `2026-10-20.csv` a `2026-10-26.csv`; o
último foi coletado em 26/10 às 04:23 (Brasília), portanto os merges da noite de 26/10 (PRs #55
e #56) entram no registro da semana 2.

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

## Próximo registro

A semana 2 (27/10 a 02/11) deve:

- comparar M3 com a base de 0,40 h/ponto;
- verificar se D3 aumentou a cobertura de `Estimate` e `Horas`;
- verificar se D4 fez aparecer reviews nos PRs;
- incluir os PRs #55 e #56, mergeados em 26/10 depois do último snapshot da semana 1.
