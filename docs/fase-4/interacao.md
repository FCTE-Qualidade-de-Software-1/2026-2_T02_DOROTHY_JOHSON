# Análise e respostas GQM: capacidade de interação

Análise da rodada 01 da [coleta de G1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/capacidade-de-interacao/README.md),
conforme as [métricas da Fase 2](../fase-2/metricas.md),
o [método da Fase 3](../fase-3/metodo-interacao.md) e os
[níveis de pontuação](../fase-2/niveis-pontuacao.md). Os resultados de participantes usam códigos.
Formulários originais, termos e qualquer vínculo com nomes devem permanecer em acesso restrito;
confira a revisão das fichas individuais antes de compartilhar a coleta.

## 1. Coleta e validade

| Item | Resultado |
|---|---|
| Período | 22 a 24/11/2026 |
| Amostra | P01–P04; 4 de 5 participantes previstos. P05 indisponível |
| Tarefas | T1: território; T2: camada PRONAF; T3: documento PTDRS |
| Condições | Sessões remotas, em celulares e navegadores diferentes; versões de SO/navegador não registradas em parte das sessões |
| Evidências | [Dados brutos de G1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/capacidade-de-interacao/) e [protocolo de participantes](../fase-3/protocolo-participantes.md) |

O desvio mais relevante é que T2 e T3 não começaram consistentemente na página Início, como
exigem o método e os caminhos mínimos. Apenas uma observação de T2 registra início em Início;
nenhuma observação válida de T3 o faz. Por isso:

- M1.1.2 de T2 usa somente a observação iniciada em Início (0/1); M1.1.2 de T3 é NC.
- M1.2.1 de T2 usa somente essa mesma observação (0/1 sem conclusão sem ajuda); M1.2.1 de T3 é NC.
- M1.3.1 de T2 e T3 é NC: não há tarefa concluída com ponto de partida válido para comparar ao
  caminho mínimo. As razões brutas dessas tarefas não são usadas na classificação.

Outras ressalvas que afetam a interpretação: o início da gravação de P01 não cobre os primeiros
13 segundos; P04 recebeu um esclarecimento do enunciado em T2, registrado como não sendo ajuda
por consenso, decisão que deve ser revisada à luz da regra de ajuda da Fase 2; os casos MT/BT de
M1.4 foram simulados por bloqueio de requisições em vez de DevTools Offline; e o teste FC-03 foi
afetado pelo reCAPTCHA não carregado offline. Para M1.6, o viewport foi obtido em um quadro de
mesma origem, sem janela anônima ou modo responsivo. Esses desvios estão detalhados no
[README da coleta](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/capacidade-de-interacao/README.md).

## 2. Resultados das métricas

Os pontos seguem os limites da Fase 2 e são aplicados aos valores não arredondados. NC significa
que o recorte não pode ser classificado com a evidência disponível.

| Métrica | Recorte | Resultado observado | Pontos | Nível / situação |
|---|---|---:|:---:|---|
| M1.1.1 | 9 seções | 7/9 = 77,78% | 2 | Bom |
| M1.1.2 | T1 | 3/4 = 75% | 1 | Aceitável |
| M1.1.2 | T2 | 0/1 = 0% | 0 | Insatisfatório; amostra válida de 1 |
| M1.1.2 | T3 | — | NC | Início fora de Início |
| M1.2.1 | T1 | 4/4 = 100% | 3 | Excelente |
| M1.2.1 | T2 | 0/1 = 0% | 0 | Insatisfatório; amostra válida de 1 |
| M1.2.1 | T3 | — | NC | Início fora de Início |
| M1.3.1 | T1 | média de 7/16, 7/14, 7/13 e 7/12 = 0,5148 | 1 | Aceitável |
| M1.3.1 | T2 | — | NC | Sem tarefa concluída iniciada em Início |
| M1.3.1 | T3 | — | NC | Sem tarefa concluída iniciada em Início |
| M1.4.1 | Casos executados | 6/7 = 85,71% | 2 | Bom; procedimento com desvio |
| M1.4.2 | Casos com mensagem | 4/5 = 80% | 2 | Bom; procedimento com desvio |
| M1.5.1 | SUS, 4 respostas | média = 50,0/100 | 0 | Insatisfatório |
| M1.5.2 | Aparência, 4 respostas | média = 4,25/5 | 2 | Bom |

### Acessibilidade automática

| Página | M1.6.1: regras aprovadas | Pontos | M1.6.2: elementos críticos/sérios | Críticos | Sérios | Pontos |
|---|---:|:---:|---:|---:|---:|:---:|
| Início | 28/32 = 87,50% | 1 | 7 | 3 | 4 | 0 |
| Meu Território | 22/24 = 91,67% | 2 | 7 | 3 | 4 | 0 |
| SITGeo | 25/27 = 92,59% | 2 | 5 | 1 | 4 | 0 |
| Biblioteca Territorial | 26/28 = 92,86% | 2 | 39 | 6 | 33 | 0 |
| Fale Conosco | 26/28 = 92,86% | 2 | 5 | 1 | 4 | 0 |

M1.6.1 tem média de **1,80 ponto** entre páginas; M1.6.2 tem média de **0 ponto**. A Biblioteca
concentra o maior número de elementos afetados: 29 links de miniaturas sem nome acessível,
além dos controles e links recorrentes nas páginas. O SITGeo não é o recorte com mais violações.
Os achados são automatizados e não substituem inspeção manual de WCAG/eMAG.

## 3. Respostas às questões

| Questão | Resposta com os dados disponíveis |
|---|---|
| **Q1.1 — As seções explicam sua finalidade e são reconhecidas?** | Parcial. Sete de nove seções se autodescrevem. Em T1, 3/4 participantes escolheram a seção correta no primeiro clique; em T2, a única observação válida não acertou SITGeo. T3 é NC, então a questão não tem pontuação completa. |
| **Q1.2 — As tarefas são concluídas sem ajuda?** | Parcial. T1: 4/4. T2: 0/1 na única observação iniciada em Início. T3 é NC. Os resultados brutos 1/4 de T2/T3 não são usados como resultado classificável porque os pontos de partida não seguiram o método. |
| **Q1.3 — Quanto o caminho se afasta do mínimo?** | Parcial. Em T1, a eficiência média é 0,5148. T2 e T3 são NC, pois não há conclusão válida a partir de Início; não se pode confirmar a hipótese comparativa entre as três tarefas. |
| **Q1.4 — O portal previne entradas inválidas e explica como corrigi-las?** | Os casos protegidos foram 6/7 (85,71%); 4/5 mensagens atenderam aos dois critérios (80%). O segundo resultado supera a previsão de menos de 50% da hipótese. Há desvios no modo de simular a rede e no caso FC-03. |
| **Q1.5 — Como os participantes percebem o uso e a aparência?** | SUS médio 50, abaixo de 51 e da referência descritiva de 68; aparência média 4,25, acima do ponto neutro 3. Pontuação da questão: (0 + 2)/2 = **1,00**. |
| **Q1.6 — As páginas atendem aos critérios automáticos de acessibilidade?** | Todas aprovam ao menos 87,50% das regras testadas, mas todas têm elementos com impacto crítico e sério. Pontuação da questão: (1,80 + 0)/2 = **0,90**. O limitador de violação crítica foi acionado. |

Pontuações completas por questão: Q1.4 = **2,00**, Q1.5 = **1,00** e Q1.6 = **0,90**. Q1.1, Q1.2 e
Q1.3 permanecem pendentes pelos recortes NC; portanto, não se calcula a média global de G1.

## 4. Classificação de G1

**Classificação final: pendente por cobertura insuficiente.** Há recortes NC em M1.1.2, M1.2.1 e
M1.3.1, além de uma amostra de quatro participantes em vez dos cinco planejados. Pela regra da
Fase 2, não se atribui uma média global enquanto houver métrica obrigatória sem resultado válido.

**Limitadores já observados:** qualquer página com violação crítica leva G1 a Insatisfatório,
independentemente da média; T2 também ficou abaixo de 60% de conclusão sem ajuda na observação
válida disponível, o que limita a classificação a no máximo Aceitável. O primeiro limitador é o
mais restritivo. Assim, a evidência atual já exige tratar G1 como **Insatisfatório se os achados
críticos forem confirmados**, mas isso não substitui a conclusão formal após completar a coleta.

## 5. Hipóteses

| Hipótese | Resultado | Evidência |
|---|---|---|
| H1.1 | Parcial; conclusão pendente | M1.1.1 confirma 7/9. T1 confirma maioria (3/4); T2 tem apenas 0/1 observação válida e T3 é NC. |
| H1.2 | Parcial; conclusão pendente | T1 confirma a expectativa (100%); T2 fica abaixo (0/1), como previsto; T3 é NC. |
| H1.3 | Inconclusiva | Só T1 tem eficiência válida. Os valores brutos de T2/T3 não são comparáveis porque o ponto de partida divergiu do método. |
| H1.4 | Parcial | M1.4.1 fica entre 50% e 100%, como previsto; M1.4.2 = 80%, contrariando a previsão de menos de 50%. |
| H1.5 | Parcial | SUS = 50, abaixo da faixa prevista; aparência = 4,25, acima do ponto neutro, como previsto. |
| H1.6 | Parcial | Todas as páginas superam 80% em M1.6.1 e todas têm violações críticas/sérias; a maior contagem está na Biblioteca, não no SITGeo. |

## 6. Pendências para fechar a análise

1. Completar a amostra planejada, se possível, e repetir T2/T3 a partir de Início, em sessões com o
   mesmo ponto de partida, limite de tempo e regra de moderação.
2. Revisar a classificação do esclarecimento dado em T2 e preservar a decisão na ficha.
3. Reexecutar M1.4 conforme o procedimento offline previsto, incluindo FC-03 em condições que
   permitam distinguir validação do formulário de falha do reCAPTCHA.
4. Repetir ou confirmar M1.6 no viewport e nas condições estabelecidas no método; manter as
   violações críticas como prioridade de correção.

Os dados e as condições de acesso estão no [mapa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/README.md) e no
[README da coleta G1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/capacidade-de-interacao/README.md).
