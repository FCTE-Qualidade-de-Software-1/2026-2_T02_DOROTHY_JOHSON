# Fase 3 — Projetar a avaliação

A Fase 3 do processo de avaliação de produto transforma a especificação da
[Fase 2](../fase-2/index.md) em um plano executável: para cada métrica, define **como** a
medida é obtida, **com quais recursos**, **em que ambiente** e **quando**. O plano deve
permitir que outra pessoa repita a avaliação e chegue a medidas comparáveis.

| Item | Valor |
|---|---|
| Entrada | Requisitos da [Fase 1](../fase-1/index.md) e as 19 métricas, os níveis de pontuação e os critérios de classificação da [Fase 2](../fase-2/index.md) |
| Saída | Plano de avaliação executado na [Fase 4](../fase-4/index.md) |
| Versão do plano | 1.3 |
| Atualizado em | 23/11/2026 |

## 1. Partes do plano

| Parte | O que define | Página | Situação |
|---|---|---|---|
| Recursos e ambiente | Objeto avaliado, páginas, objetos de referência, hardware, software, rede e conhecimento exigido | [Recursos e ambiente](ambiente.md) | Concluída |
| Método de eficiência de desempenho (G3) | Passos para obter M3.1.1 a M3.4.1 e consolidar os dados | [Método de eficiência](metodo-eficiencia.md) | Concluída e executada em 08/11/2026 |
| Método de capacidade de interação (G1) | Roteiro das sessões com usuários, casos de inspeção e execução do axe-core | [Fichas de G1](../fase-2/metricas.md#g1-capacidade-de-interacao) e [ambiente, seção 3.2](ambiente.md#32-capacidade-de-interacao-g1) | Em elaboração ([#63](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/63)) |
| Método de flexibilidade (G2) | Larguras de tela, lista de funções, matriz de ambientes, roteiro das tarefas e registro de falhas | [Método de flexibilidade](metodo-flexibilidade.md) | Concluída; Procedimentos A e B executados em 15/11/2026 |
| Protocolo de participantes | Recrutamento, termo de consentimento, gravação e anonimização | [Condições comuns de G1](../fase-2/metricas.md#condicoes-comuns-de-coleta) | Em elaboração ([#68](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/68)) |
| Cronograma | Atividades da Fase 4 e datas | [Seção 4](#4-cronograma-da-avaliacao) desta página | Concluída |
| Rastreabilidade F2 → F3 | Método, recursos e dado bruto de cada métrica | [Seção 3](#3-rastreabilidade-da-fase-2-para-a-fase-3) desta página | Concluída |

*Tabela 1: Partes do plano de avaliação e situação de cada uma.*

Enquanto o método de G1 não tem página própria, valem os procedimentos de coleta das fichas
da Fase 2, que já descrevem os passos de cada métrica, e os recursos da página de ambiente.

## 2. Ligação com as Fases 1 e 2

O plano não acrescenta decisões novas sobre o que avaliar. Cada elemento vem de uma definição
anterior:

| Elemento do plano | Origem |
|---|---|
| Objeto avaliado e limites | [Fase 1, seção 5](../fase-1/index.md#5-escopo-e-limites-da-avaliacao): área pública do portal, avaliação caixa-preta |
| Páginas e tarefas T1, T2 e T3 | [Fase 1, seção 3.6](../fase-1/index.md#36-paginas-e-tarefas-avaliadas) |
| Perfil dos participantes e conhecimento exigido | [Fase 1, seção 3.3](../fase-1/index.md#33-usuarios-ambiente-e-conhecimento-exigido) |
| Contexto de uso simulado (celular de entrada, rede móvel lenta) | [Fase 2, objetivo G3](../fase-2/objetivos.md#g3-eficiencia-de-desempenho) |
| Matriz de navegadores, sistemas e larguras | [Fase 2, objetivo G2](../fase-2/objetivos.md#g2-flexibilidade) |
| Definição, cálculo e fonte de cada medida | [Fase 2, métricas](../fase-2/metricas.md) |
| Conversão das medidas em níveis e em classificação | [Fase 2, níveis de pontuação](../fase-2/niveis-pontuacao.md) |

*Tabela 2: Origem de cada elemento do plano.*

Os objetos de referência (território, camada e documento) foram deixados para esta fase pela
[Fase 1](../fase-1/index.md#36-paginas-e-tarefas-avaliadas) e estão fixados em
[Recursos e ambiente, seção 2](ambiente.md#2-paginas-tarefas-e-objetos-de-referencia).

## 3. Rastreabilidade da Fase 2 para a Fase 3

Para atender ao critério **F3-C8**, a Tabela 3 estabelece o mapeamento explícito entre cada métrica definida na [Fase 2](../fase-2/metricas/) e sua operacionalização na Fase 3, detalhando o **método**, a **instrução de execução**, os **recursos/instrumentos**, o **ambiente** e o **destino do dado bruto**.

| Métrica | Questão | Método | Instrução operacional | Recursos e instrumentos | Ambiente de execução | Dado bruto |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.1.1** | Q1.1 | Inspeção heurística por pares | Dois avaliadores inspecionam independentemente as 9 páginas de entrada verificando clareza de propósito e consolidam divergências. | Roteiro de inspeção, planilha de registro e ferramenta de captura de tela. | Desktop da equipe, navegador padrão em tela cheia (1366×768). | Planilha de inspeção e capturas de tela |
| **M1.1.2** | Q1.1 | Teste moderado com usuários | 5 participantes executam T1, T2 e T3; registra-se o alvo do 1º clique/toque antes de qualquer navegação secundária. | Roteiro de tarefas, gravador de tela/áudio e planilha de observação. | Celular único de referência, rede estável, ambiente silencioso. | Gravações e planilha de observação |
| **M1.2.1** | Q1.2 | Teste moderado com usuários | Nas mesmas sessões de M1.1.2, cronometra-se a conclusão de T1, T2 e T3 sem ajuda externa, respeitando o limite máximo de 5 min por tarefa. | Cronômetro, roteiro de tarefas e planilha de observação. | Mesmo ambiente de M1.1.2 (celular único, primeiro uso sem ajuda). | Gravações e planilha de observação |
| **M1.3.1** | Q1.3 | Análise de vídeo e contagem | Contagem do número de ações/passos executados por participante em cada tarefa a partir das gravações, auditada por um 2º avaliador. | Player de vídeo das gravações e planilha de contagem. | Estação de trabalho da equipe (análise *post-mortem*). | Planilha de passos por participante (P1 a P5) |
| **M1.4.1** | Q1.4 | Inspeção de resiliência (*fault injection*) | Submeter lista fixa de entradas inválidas nos formulários/buscas e simular perda de conexão durante requisições ativas. | Lista fixa de entradas inválidas e Chrome DevTools (aba *Network* em modo *Offline*). | Desktop da equipe, Google Chrome, portal em produção. | Planilha de casos e capturas de tela |
| **M1.4.2** | Q1.4 | Análise de conteúdo por pares | Extrair todas as mensagens exibidas nos testes de M1.4.1 e classificá-las por dois avaliadores quanto à clareza e orientação de correção. | Planilha contendo o texto literal das mensagens capturadas em M1.4.1. | Estação de trabalho da equipe. | A mesma planilha de M1.4.1, com classificação |
| **M1.5.1** | Q1.5 | Survey padronizado (SUS) | Aplicar o questionário *System Usability Scale* (10 itens, escala Likert 1–5) imediatamente após o término de T1, T2 e T3. | Formulário digital/impresso com a versão validada do SUS em português. | Mesmo local da sessão com os participantes P1 a P5. | Respostas brutas por participante (P1 a P5) |
| **M1.5.2** | Q1.5 | Survey de percepção visual | Coletar nota subjetiva de aparência visual (escala de 1 a 5) na seção final do mesmo formulário do SUS. | Mesmo formulário utilizado em M1.5.1. | Mesmo ambiente de M1.5.1. | As mesmas respostas (P1 a P5) |
| **M1.6.1** | Q1.6 | Análise estática automatizada | Executar varredura automatizada das regras WCAG 2.1 níveis A e AA sobre 5 páginas representativas do portal. | Biblioteca/extensão `axe-core`. | Desktop da equipe, navegador Chromium/Chrome. | Relatórios JSON do `axe-core` |
| **M1.6.2** | Q1.6 | Triagem e contagem de severidade | Filtrar nos relatórios JSON gerados em M1.6.1 exclusivamente as violações classificadas com impacto *Critical* e *Serious*. | Parser/inspeção estruturada dos relatórios JSON do `axe-core`. | Estação de trabalho da equipe. | Os mesmos relatórios JSON de M1.6.1 |
| **M2.1.1** | Q2.1 | Teste de compatibilidade cruzada | Executar manualmente T1, T2 e T3 nas 6 combinações de navegador e sistema operacional definidas na matriz ([Procedimento C](metodo-flexibilidade/#5-procedimento-c-tarefas-na-matriz-de-ambientes-m211)). | Matriz de ambientes, roteiro de T1–T3 e ferramenta de captura. | Aparelhos reais nos celulares (Android/iOS) e desktops Windows da matriz. | `data/fase-4/flexibilidade/execucoes.csv` e capturas |
| **M2.2.1** | Q2.2 | Teste automatizado de *viewport* | Executar script via DevTools Protocol verificando existência de *overflow* horizontal em 3 páginas × 5 larguras de tela, em 2 rodadas ([Procedimento A](metodo-flexibilidade/#3-procedimento-a-rolagem-horizontal-m221)). | Script automatizado e Chrome DevTools Protocol (*Device Mode*). | Desktop da equipe, Google Chrome em modo de dispositivo. | `data/fase-4/flexibilidade/rolagem.csv` e capturas |
| **M2.2.2** | Q2.2 | Auditoria automatizada + validação | Executar script verificando presença/visibilidade da lista fixa de 25 funções em 1366 px vs. 360 px e confirmar perdas no aparelho real ([Procedimento B](metodo-flexibilidade/#4-procedimento-b-funcoes-disponiveis-no-celular-m222)). | Script de DOM, lista de 25 funções e celular de referência. | Chrome Device Mode (desktop) e celular de referência físico. | `data/fase-4/flexibilidade/funcoes.csv` e capturas |
| **M2.3.1** | Q2.3 | Consolidação e reprodução | Consolidar as falhas detectadas em M2.1.1, M2.2.1 e M2.2.2, exigindo confirmação em 2ª execução e excluindo o ambiente de referência ([Procedimento D](metodo-flexibilidade/#6-procedimento-d-registro-de-falhas-m231)). | Logs e arquivos CSV gerados em M2.1.1 a M2.2.2. | Mesmos ambientes onde as falhas originais foram observadas. | `data/fase-4/flexibilidade/falhas.csv` |
| **M3.1.1** | Q3.1 | *Benchmark* sintético | Executar Google Lighthouse 5 vezes por página alvo e extrair a mediana do *First Contentful Paint* (FCP). | Google Lighthouse CLI / DevTools ([Ambiente, seção 3.1](ambiente/#31-eficiencia-de-desempenho-g3)). | Hardware controlado da equipe, emulação de celular de entrada e rede móvel lenta. | `data/fase-4/eficiencia/lighthouse/` |
| **M3.1.2** | Q3.1 | *Benchmark* sintético | Extrair a mediana do *Largest Contentful Paint* (LCP) a partir das mesmas 5 execuções do Lighthouse de M3.1.1. | Mesmos recursos de M3.1.1. | Mesmo ambiente simulado de M3.1.1. | O mesmo de M3.1.1 |
| **M3.2.1** | Q3.2 | Automação E2E cronometrada | Executar script Playwright realizando T1 e T2 (5 rodadas cada) e medir o tempo de conclusão/resposta via CDP. | Script Playwright e Chrome DevTools Protocol. | Mesmo ambiente simulado de celular de entrada e rede lenta (seção 3.1). | `data/fase-4/eficiencia/tarefas.json` |
| **M3.3.1** | Q3.3 | *Profiling* sintético de CPU | Extrair o tempo de execução de CPU na *main thread* a partir dos relatórios das 5 execuções do Lighthouse de M3.1.1. | Mesmos relatórios do Lighthouse de M3.1.1. | Mesmo ambiente de M3.1.1. | O mesmo de M3.1.1 |
| **M3.4.1** | Q3.4 | *Profiling* automatizado de memória | Coletar métricas de *JS Heap Size* após o carregamento e após a execução de T1 e T2 nas 5 rodadas do script Playwright. | Mesmo script Playwright + CDP de M3.2.1. | Mesmo ambiente de M3.2.1. | O mesmo de M3.2.1 |

*Tabela 3: Rastreabilidade entre as métricas da Fase 2 e os procedimentos, recursos e ambientes da Fase 3.*

### 3.1 Coerência com níveis de pontuação e critérios de julgamento

Os procedimentos da Fase 3 foram desenhados para produzir saídas diretamente compatíveis com as escalas e regras de agregação definidas nos [Níveis de Pontuação da Fase 2](../fase-2/niveis-pontuacao/):

* **Preservação de unidades e fórmulas:** Nenhuma instrução da Tabela 3 altera as unidades de medida (segundos, milissegundos, megabytes, percentuais, contagens absolutas ou escala SUS 0–100) nem os limites das faixas de classificação (*Inaceitável*, *Minimamente Aceitável*, *Satisfatório* e *Excelente*) fixados na Fase 2.
* **Rastreabilidade da consolidação (Fase 3 → Fase 4):**
  * **G1 (M1.1.1 a M1.6.2):** Os registros individuais de inspeção, gravações (P1–P5), formulários SUS e relatórios JSON do `axe-core` alimentam diretamente o cálculo das taxas de sucesso, tempos médios, escores SUS e contagens de violações, convertidos nos níveis de G1 na [Análise de Capacidade de Interação](../fase-4/).
  * **G2 (M2.1.1 a M2.3.1):** Os arquivos `execucoes.csv`, `rolagem.csv`, `funcoes.csv` e `falhas.csv` fornecem os numeradores e denominadores exatos para o cálculo de cobertura de ambientes e densidade de falhas, aplicados aos critérios de julgamento na [Análise de Flexibilidade](../fase-4/flexibilidade/).
  * **G3 (M3.1.1 a M3.4.1):** As medianas extraídas dos JSONs do Lighthouse e de `tarefas.json` eliminam *outliers* de rede e são comparadas diretamente com os limiares temporais e de memória definidos para G3 na [Análise de Eficiência](../fase-4/eficiencia/).

### 3.2 Verificação de suporte do ambiente e adequação do GQM

* **Cobertura do ambiente:** Todas as 19 métricas da Fase 2 possuem procedimento executável, recurso definido e ambiente validado na Fase 3 (detalhados em [Recursos e Ambiente](ambiente/)). Nenhum procedimento mede variáveis fora do escopo do GQM.
* **Adequações metodológicas registradas (F2 → F3):** Durante o planejamento experimental, duas coletas inicialmente previstas de forma manual na Fase 2 mostraram-se suscetíveis a viés operacional e baixa repetibilidade, gerando ajustes documentados tanto nesta fase quanto nas respectivas fichas da Fase 2:
  1. **Decisão GQM-01 (M3.2.1 e M3.4.1):** Substituição da gravação manual na aba *Performance* do Chrome DevTools por script automatizado em **Playwright** via *Chrome DevTools Protocol (CDP)*, garantindo precisão de milissegundos e repetibilidade nas 5 rodadas ([Método de eficiência, seção 6](metodo-eficiencia/#6-diferenca-em-relacao-a-fase-2)).
  2. **Decisão GQM-02 (M2.2.1, M2.2.2 e M2.3.1):** Substituição da inspeção visual manual de *viewport* e funções por scripts automatizados no modo de dispositivo do Chrome (`Procedimentos A e B`), com validação das perdas no celular de referência físico e exclusão do ambiente de referência no cálculo de `M2.3.1` ([Método de flexibilidade, seção 8](metodo-flexibilidade/#8-diferencas-em-relacao-a-fase-2)).

## 4. Cronograma da avaliação

| Período | Atividade |  Métrica ou resultado | Responsável e issue | Situação e contingência |
|---|---|---|---|---|
| 20/10 | Medição piloto de G3 | G3 | Felipe: [#26](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/26) | Concluída; referência da coleta |
| 08/11 | Ambiente e método de G3 | G3 | Felipe: [#66](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/66) | Concluída |
| 08/11 | Coleta de G3 | G3 | Felipe: [#73](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/73) | Concluída; cinco execuções por medida |
| 14/11 | Análise de G3 e escolha da melhoria | G3 | Felipe e Artur: [#78](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/78), [#82](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/82) | Concluída |
| 14 a 15/11 | Métodos de G1 e G2 e protocolo de participantes | G1 e G2 | Ana Luíza e Tales: [#63](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/63), [#68](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/68) | Em andamento |
| 14 a 16/11 | Entrega técnica da ação de melhoria | G3 — M3.1.2 | Artur: [#83](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/83) | Concluída; reteste antes × depois |
| 15/11 | Coleta de largura de tela e funções | G2 | Tales: [#72](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/72) | Concluída com duas execuções |
| 16/11 | Ponto de Controle 2 | Todas | Artur: [#97](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/97) | Concluído |
| 15 a 17/11 | Inspeções e acessibilidade de G1 | G1 | Ana Luíza: [#71](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/71) | Pendente; repetir inspeções ou o axe, se necessário |
| 16 a 17/11 | Matriz de ambientes e confirmação de falhas | G2 | Tales: [#72](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/72) | Pendente; folga para reteste de ambientes |
| 16 a 18/11 | Sessões com os participantes | G1 | Ana Luíza: [#71](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/71) | Pendente; folga para reagendamento |
| 17 a 18/11 | Folga para retestes de G1 e G2 | G1 e G2 | Ana Luíza: [#71](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/71)<br> e Tales: [#72](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/72) | Usada somente se houver dados incompletos, falhas inconsistentes ou necessidade de nova sessão |
| 18 a 20/11 | Consolidação e cálculo | G1, G2 e G3 | Cayo: [#74](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/74), [#75](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/75) | Concluída; revisar dados inconsistentes |
| 18 a 20/11 | Análise GQM e hipóteses | G1, G2 e G3 | Gabriel, Tales e Felipe: [#76](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/76), [#77](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/77), [#78](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/78) | G1 pendente; G2 parcial; G3 concluída |
| 19 a 20/11 | Julgamento, relações e melhorias | G1, G2 e G3 | Tales e Cayo: [#79](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/79), [#80](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/80), [#81](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/81) | Em andamento; considerar cobertura insuficiente |
| 20 a 21/11 | Folga para ajustes da melhoria e medições complementares | G3 e ações de melhoria | Artur: [#83](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/83) | Usada para corrigir a entrega técnica ou repetir a medição antes × depois |
| 20 a 24/11 | Artigo, GitPage e PSM/CID | Evidências de G1, G2 e G3 | Ana Luíza e Felipe: [#86](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/86), [#93](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/93), [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/94) | Pendente; folga para revisão cruzada |
| 20 a 21/11 | Revisão de navegação e estilo | Todas as páginas revisadas | Tales: [#91](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/91), [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/95) | Pendente; último reteste |
| 23/11 | Release E2 e submissão | Release entregue | Ana Luíza: [#96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/96) | Pendente |

*Tabela 4: Cronograma da avaliação (2026). Os períodos refletem as atividades da Fase 4, os responsáveis das issues e a folga necessária para retestes, correções e a ação de melhoria.*

As coletas de uma mesma métrica são feitas em uma única sessão, e cada execução registra data
e hora, porque o portal está em produção e pode mudar durante o período
([riscos do ambiente](ambiente.md#5-riscos-do-ambiente)).

## 5. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 08/11/2026 | Recursos e ambiente; método de eficiência de desempenho |
| 1.1 | 14/11/2026 | Visão geral do plano, ligação com as Fases 1 e 2, rastreabilidade F2 → F3 e cronograma |
| 1.2 | 15/11/2026 | Método de flexibilidade (G2) |
| 1.3 | 23/11/2026 | Cronograma da Fase 4 distribuído por data, responsável, issue e folga para retestes |
