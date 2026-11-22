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
| Atualizado em | 22/11/2026 |

## 1. Partes do plano

| Parte | O que define | Página | Situação |
|---|---|---|---|
| Recursos e ambiente | Objeto avaliado, páginas, objetos de referência, hardware, software, rede e conhecimento exigido | [Recursos e ambiente](ambiente.md) | Concluída |
| Método de eficiência de desempenho (G3) | Passos para obter M3.1.1 a M3.4.1 e consolidar os dados | [Método de eficiência](metodo-eficiencia.md) | Concluída e executada em 08/11/2026 |
| Método de capacidade de interação (G1) | Roteiro das sessões, inspeções e execução do axe-core | [Método de interação](metodo-interacao.md) e [formulários](formularios-interacao.md) | Documentado ([#63](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/63)) |
| Método de flexibilidade (G2) | Larguras de tela, lista de funções, matriz de ambientes, roteiro das tarefas e registro de falhas | [Método de flexibilidade](metodo-flexibilidade.md) | Concluída; Procedimentos A e B executados em 15/11/2026 |
| Protocolo de participantes | Recrutamento, termo de consentimento, gravação e anonimização | [Protocolo](protocolo-participantes.md) e [termo](termo-consentimento.md) | Documentado, aguardando aprovação da equipe ([#68](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/68)) |
| Cronograma | Atividades da Fase 4 e datas | [Seção 4](#4-cronograma-da-avaliacao) desta página | Concluída |
| Rastreabilidade F2 → F3 | Método, recursos e dado bruto de cada métrica | [Seção 3](#3-rastreabilidade-da-fase-2-para-a-fase-3) desta página | Concluída |

*Tabela 1: Partes do plano de avaliação e situação de cada uma.*

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

A Tabela 3 mostra, para cada métrica, o método previsto, os recursos e onde o dado bruto é
guardado. As faixas de cada nível e as regras de classificação não mudam nesta fase: são as da
[Fase 2](../fase-2/niveis-pontuacao.md).

| Métrica | Questão | Método | Recursos e ambiente | Dado bruto |
|---|---|---|---|---|
| M1.1.1 | Q1.1 | Inspeção das 9 páginas de entrada por dois avaliadores | Mesmo celular dos testes com usuários | Planilha de inspeção e capturas de tela |
| M1.1.2 | Q1.1 | Teste com 5 usuários: destino do primeiro clique em T1, T2 e T3 | Celular único, gravação de tela e áudio | Gravações e planilha de observação |
| M1.2.1 | Q1.2 | Teste com 5 usuários: conclusão sem ajuda, limite de 5 min por tarefa | Os mesmos de M1.1.2 | Gravações e planilha de observação |
| M1.3.1 | Q1.3 | Contagem de passos nas gravações, conferida por um segundo avaliador | Gravações das sessões | Planilha de passos por participante |
| M1.4.1 | Q1.4 | Inspeção com lista fixa de entradas inválidas, com a rede em modo offline | Chrome DevTools | Planilha de casos e capturas de tela |
| M1.4.2 | Q1.4 | Classificação das mensagens de erro por dois avaliadores | As mesmas execuções de M1.4.1 | A mesma planilha, com o texto das mensagens |
| M1.5.1 | Q1.5 | Questionário SUS ao fim da sessão | Formulário em português | Respostas por participante (P01 a P05) |
| M1.5.2 | Q1.5 | Nota de aparência, de 1 a 5, no mesmo formulário | O mesmo de M1.5.1 | As mesmas respostas |
| M1.6.1 | Q1.6 | Verificação automática das regras WCAG 2.1 A e AA em 5 páginas | axe-core | Relatórios JSON do axe-core |
| M1.6.2 | Q1.6 | Contagem das violações críticas e sérias | As mesmas execuções de M1.6.1 | Os mesmos relatórios |
| M2.1.1 | Q2.1 | Execução manual de T1, T2 e T3 em 6 combinações de navegador e sistema ([Procedimento C](metodo-flexibilidade.md#5-procedimento-c-tarefas-na-matriz-de-ambientes-m211)) | Matriz de ambientes; aparelhos reais nos celulares | `data/fase-4/flexibilidade/execucoes.csv` e capturas |
| M2.2.1 | Q2.2 | Script de rolagem horizontal em 3 páginas × 5 larguras, 2 execuções ([Procedimento A](metodo-flexibilidade.md#3-procedimento-a-rolagem-horizontal-m221)) | Modo de dispositivo do Chrome, pelo protocolo do DevTools | `data/fase-4/flexibilidade/rolagem.csv` e capturas |
| M2.2.2 | Q2.2 | Script com a lista fixa de 25 funções, em 1366 e 360 px, e confirmação das perdas no celular ([Procedimento B](metodo-flexibilidade.md#4-procedimento-b-funcoes-disponiveis-no-celular-m222)) | O mesmo de M2.2.1; celular de referência | `data/fase-4/flexibilidade/funcoes.csv` e capturas |
| M2.3.1 | Q2.3 | Registro das falhas das três métricas anteriores, confirmadas em segunda execução ([Procedimento D](metodo-flexibilidade.md#6-procedimento-d-registro-de-falhas-m231)) | Os mesmos de M2.1.1 a M2.2.2 | `data/fase-4/flexibilidade/falhas.csv` |
| M3.1.1 | Q3.1 | Lighthouse, 5 execuções por página, mediana do FCP | [Ambiente, seção 3.1](ambiente.md#31-eficiencia-de-desempenho-g3) | `data/fase-4/eficiencia/lighthouse/` |
| M3.1.2 | Q3.1 | As mesmas execuções, mediana do LCP | O mesmo de M3.1.1 | O mesmo de M3.1.1 |
| M3.2.1 | Q3.2 | Script com Playwright, 5 execuções de T1 e de T2 | O mesmo de M3.1.1 | `data/fase-4/eficiencia/tarefas.json` |
| M3.3.1 | Q3.3 | As mesmas execuções do Lighthouse, tempo de CPU na thread principal | O mesmo de M3.1.1 | O mesmo de M3.1.1 |
| M3.4.1 | Q3.4 | O mesmo script de M3.2.1, *JS heap* após o carregamento e após a tarefa | O mesmo de M3.1.1 | O mesmo de M3.2.1 |

*Tabela 3: Rastreabilidade entre as métricas da Fase 2 e o plano da Fase 3.*

**Verificação da consistência.** As 19 métricas da Fase 2 têm método, recursos e destino do
dado bruto. Nenhum método mede algo que não esteja em uma ficha da Fase 2.

**Diferença registrada em relação à Fase 2.** As fichas de M3.2.1 e M3.4.1 previam a gravação
manual no painel Performance do Chrome DevTools. O plano usa um script que lê as mesmas
grandezas pelo protocolo do DevTools, o que torna a medição repetível. A justificativa está no
[método de eficiência, seção 6](metodo-eficiencia.md#6-diferenca-em-relacao-a-fase-2), e as
fichas da Fase 2 foram atualizadas. Pelo mesmo motivo, M2.2.1 e M2.2.2 passam a ser
verificadas por script no modo de dispositivo do Chrome, com as perdas de função confirmadas
no celular de referência, e o ambiente de referência fica fora da contagem de M2.3.1
([método de flexibilidade, seção 8](metodo-flexibilidade.md#8-diferencas-em-relacao-a-fase-2)).

## 4. Cronograma da avaliação

| Período | Atividade | Métricas | Situação |
|---|---|---|---|
| 20/10 | Medição piloto de eficiência de desempenho | M3.x | Concluída |
| 08/11 | Ambiente, objetos de referência e método de eficiência | — | Concluída |
| 08/11 | Coleta de eficiência de desempenho | M3.1.1 a M3.4.1 | Concluída |
| 14 a 15/11 | Métodos de G1 e G2, protocolo de participantes e termo de consentimento | — | Em andamento |
| 15 a 17/11 | Inspeções e verificação automática de G1 | M1.1.1, M1.4.1, M1.4.2, M1.6.1 e M1.6.2 | Prevista |
| 15/11 | Larguras de tela de G2 (Procedimentos A e B) | M2.2.1 e M2.2.2 | Concluída |
| 16 a 17/11 | Matriz de ambientes de G2 (Procedimento C) e confirmação das falhas no celular | M2.1.1 e M2.3.1 | Prevista |
| 15/11 | Sessão piloto do roteiro de G1 com uma pessoa da equipe | — | Prevista |
| 16 a 18/11 | Sessões com os 5 participantes | M1.1.2, M1.2.1, M1.3.1, M1.5.1 e M1.5.2 | Prevista |
| 18 a 19/11 | Consolidação e respostas às questões de G1 e G2 | M1.x e M2.x | Prevista |
| 19 a 20/11 | Classificação final, relações entre as características e oportunidades de melhoria | — | Prevista |
| 14 a 20/11 | [Ação de melhoria](../fase-4/acao-melhoria.md): entrega técnica e medição do efeito | M3.1.2 | Em andamento |
| 20 a 21/11 | Artigo, GitPage e revisão final | — | Prevista |
| 22/11 | Release da Entrega 2 | — | Prevista |

*Tabela 4: Cronograma da avaliação (2026).*

As coletas de uma mesma métrica são feitas em uma única sessão, e cada execução registra data
e hora, porque o portal está em produção e pode mudar durante o período
([riscos do ambiente](ambiente.md#5-riscos-do-ambiente)).

## 5. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 08/11/2026 | Recursos e ambiente; método de eficiência de desempenho |
| 1.1 | 14/11/2026 | Visão geral do plano, ligação com as Fases 1 e 2, rastreabilidade F2 → F3 e cronograma |
| 1.2 | 15/11/2026 | Método de flexibilidade (G2) |
| 1.3 | 22/11/2026 | Método e formulários de capacidade de interação (G1) |
