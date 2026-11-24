# Oportunidades de melhoria

Lista priorizada dos problemas encontrados na avaliação, com a métrica e a evidência de origem, e
ações concretas para o requisitante (enunciado, seção 3.2, item 1;
[issue #81](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/81)).
Ela serve ao uso pretendido da [Fase 1](../fase-1/index.md#12-requisitante-e-objetivo): apoiar o
MDA na priorização do backlog de evolução do portal.

!!! warning "Cobertura da lista"
    A lista parte dos resultados de **eficiência de desempenho (G3)**, completos, e de
    **flexibilidade (G2)**, parciais: falta a matriz manual de ambientes
    ([#72](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/72)).
    **Capacidade de interação (G1) tem resultados parciais**: a análise da
    [rodada 01](interacao.md) encontrou barreiras críticas de acessibilidade, mas a amostra e
    alguns recortes ainda precisam ser completados ([#76](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/76)).
    Esta lista ainda precisa incorporar as oportunidades de G1; a ausência de itens não significa
    ausência de problemas.

## 1. Como a lista foi montada

**Entrada.** Entram todos os recortes com nível Insatisfatório (0) ou Aceitável (1) em
[`medidas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/consolidado/medidas.csv),
as falhas reproduzidas de
[`falhas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/flexibilidade/falhas.csv)
e os defeitos gerais registrados nas análises.

**Impacto.** Vem do resultado da métrica, e não de opinião:

| Impacto | Regra |
|:---:|---|
| 3 (alto) | Recorte Insatisfatório (0) |
| 2 (médio) | Recorte Aceitável (1) ou falha grave reproduzida |
| 1 (baixo) | Defeito que não rebaixou o nível de nenhuma métrica |

*Tabela 1: Escala de impacto.*

**Esforço.** É uma **estimativa externa da equipe**, feita sem acesso ao código nem ao servidor,
e deve ser revista pelo MDA:

| Esforço | Regra |
|:---:|---|
| 1 (baixo) | Troca de arquivo, marcação ou estilo de um elemento, com a solução já identificada |
| 2 (médio) | Mudança de layout ou de carregamento em uma página, com teste de regressão |
| 3 (alto) | Causa não observável de fora, ou mudança que envolve processamento, servidor ou dados |

*Tabela 2: Escala de esforço.*

**Ordem.** As oportunidades são divididas em ondas e, dentro de cada onda, seguem a ordem da
[seção 5.3 dos níveis de pontuação](../fase-2/niveis-pontuacao.md#53-da-pontuacao-a-decisao-de-qualidade)
(falha de tarefa e tempo muito alto; outros Insatisfatórios; Aceitáveis):

| Onda | Condição | Sentido |
|---|---|---|
| 1 | Impacto 2 ou 3 e esforço 1 | Ganho rápido |
| 2 | Impacto 3 e esforço 2 ou 3 | Projeto prioritário |
| 3 | Impacto 2 e esforço 2 ou 3 | Planejar |
| 4 | Impacto 1 | Corrigir quando houver oportunidade |

*Tabela 3: Ondas de priorização.*

A lista ordena ações e não cria uma nota global: as classificações de G2 e G3 continuam separadas.

## 2. Lista priorizada

| Ordem | ID | Problema | Métrica e nível | Impacto | Esforço | Onda |
|:---:|---|---|---|:---:|:---:|:---:|
| 1 | OM1 | SITGeo leva 23,45 s para exibir o conteúdo principal, por causa de imagens sem redimensionamento | M3.1.2: Insatisfatório (0) | 3 | 1 | 1 |
| 2 | OM2 | Setas da Mapoteca fora da tela do celular, com rolagem horizontal na Biblioteca Territorial (F01) | M2.2.1: Aceitável (1); M2.2.2: Bom (2); falha grave | 2 | 1 | 1 |
| 3 | OM3 | Consulta de território (T1) leva 20,39 s | M3.2.1: Insatisfatório (0) | 3 | 3 | 2 |
| 4 | OM4 | Meu Território leva 8,27 s para exibir o conteúdo principal | M3.1.2: Insatisfatório (0) | 3 | 2 | 2 |
| 5 | OM5 | SITGeo ocupa o processador do aparelho por 8,26 s no carregamento | M3.3.1: Insatisfatório (0) | 3 | 3 | 2 |
| 6 | OM6 | No celular, o SITGeo cobre o nome e os dados das camadas (F03) e os botões de zoom (F02) | M2.2.2: Aceitável (1); 2 falhas graves | 2 | 2 | 3 |
| 7 | OM7 | Ativar uma camada do mapa (T2) leva 6,45 s | M3.2.1: Aceitável (1) | 2 | 3 | 3 |
| 8 | OM8 | Biblioteca Territorial leva 3,91 s para exibir o conteúdo principal, no limite da faixa (4,0 s) | M3.1.2: Aceitável (1) | 2 | 2 | 3 |
| 9 | OM9 | Memória ocupada sobe de 5,73 para 15,01 MB depois da T1 | M3.4.1: Aceitável (1) | 2 | 3 | 3 |
| 10 | OM10 | A imagem da legenda da camada ativa não carrega no SITGeo, em 360 e em 1366 px | Sem pontuação: defeito geral, fora de M2.3.1 | 1 | 2 | 4 |

*Tabela 4: Oportunidades de melhoria em ordem de prioridade.*

|  | Esforço 1 | Esforço 2 | Esforço 3 |
|---|---|---|---|
| **Impacto 3** | OM1 | OM4 | OM3, OM5 |
| **Impacto 2** | OM2 | OM6, OM8 | OM7, OM9 |
| **Impacto 1** | — | OM10 | — |

*Tabela 5: Matriz impacto × esforço.*

OM1, OM3 e OM4 são os três recortes que acionam o
[limitador do G3](eficiencia.md#3-classificacao-do-g3). O limitador só deixa de valer quando **os
três** forem resolvidos; tratar apenas um melhora a página ou a tarefa, mas não o retira.

## 3. Ações propostas e meta de verificação

Cada meta usa a mesma métrica e o mesmo método da coleta, para que o efeito seja comparável.

| ID | Ação proposta ao MDA | Evidência de origem | Meta de verificação |
|---|---|---|---|
| OM1 | Implantar as versões redimensionadas de `capa_inicio.jpg` e `indicadores.png`, com `srcset` ([ação de melhoria](acao-melhoria.md#4-entrega-tecnica), já produzida pela equipe) | `eficiencia/lighthouse/plataforma-geoespacial-*.json`; `melhoria/diagnostico.csv` | LCP do SITGeo até 4,0 s (sai de Insatisfatório) |
| OM2 | Manter as setas do carrossel dentro da área visível em telas estreitas | `flexibilidade/rolagem.csv` (Biblioteca, 360 e 412 px); `funcoes.csv` (BIB-05); F01 | 15/15 combinações sem rolagem e 7/7 funções na Biblioteca |
| OM3 | Medir no servidor o tempo e o tamanho das respostas da consulta; conforme a causa, paginar, reduzir ou guardar em cache os dados, e mostrar primeiro os indicadores gerais | `eficiencia/tarefas.json` (T1) | T1 até 10 s |
| OM4 | Reduzir o JavaScript carregado no início (489 KiB não usados) e exibir o texto principal sem esperar pela execução dele | `eficiencia/lighthouse/meu-territorio-*.json` (`unused-javascript` e fases do LCP) | LCP de Meu Território até 4,0 s |
| OM5 | Investigar a execução de scripts no carregamento e adiar a inicialização do mapa até ele entrar na tela | `eficiencia/lighthouse/plataforma-geoespacial-*.json` (`mainthread-work-breakdown` e `bootup-time`) | CPU do SITGeo até 4,0 s |
| OM6 | Trocar a grade de 5 colunas por uma coluna em telas estreitas (painel acima do mapa) e tirar a legenda de cima dos botões de zoom | `flexibilidade/funcoes.csv` (GEO-04 e GEO-05); F02 e F03 | 6/6 funções do SITGeo em 360 px |
| OM7 | Investigar as requisições disparadas ao ativar a camada e indicar visualmente que ela está carregando | `eficiencia/tarefas.json` (T2) | T2 até 5 s (nível Bom) |
| OM8 | Exibir o texto principal sem esperar pela execução do JavaScript, como em OM4. Remover código não usado ajuda pouco aqui (20 KiB, contra 489 KiB em Meu Território) | `eficiencia/lighthouse/downloads-*.json` (`unused-javascript` e fases do LCP) | LCP até 2,5 s (nível Bom) |
| OM9 | Verificar, junto com OM3, se os dados da consulta são mantidos inteiros na memória | `eficiencia/tarefas.json` (`heap_tarefa_mb`) | Até 12 MB depois da T1 (nível Bom) |
| OM10 | Corrigir a resposta vazia do servidor de mapas para a legenda | [Flexibilidade, seção 5](flexibilidade.md#5-outros-achados-e-limitacoes) | Legenda exibida em 360 e 1366 px |

*Tabela 6: Ações, evidências (em `data/fase-4/`) e metas.*

**O que é fato e o que é hipótese.** As causas de OM1, OM2 e OM6 foram observadas. As dos demais
itens são hipóteses a confirmar pelo MDA:

- **OM3 e OM7:** o atraso ocorre nas requisições disparadas pelo clique, mas a avaliação
  caixa-preta não distingue consulta, volume de dados e servidor.
- **OM4 e OM8:** nas duas páginas o elemento do LCP é um parágrafo de texto, e a maior parte do
  tempo é atraso de renderização (mediana de 7,28 s em Meu Território e de 2,75 s na Biblioteca),
  o que aponta para a execução do JavaScript.
- **OM5:** na mediana das 5 execuções, a avaliação de scripts ocupa 4,27 s e a categoria "outros"
  3,67 s dos 8,26 s. O adiamento do mapa é uma hipótese de solução.
- **OM9:** as faixas de memória são internas e servem para triagem; é a última da onda 3.

**Cuidado com OM1.** A troca das imagens reduziu o LCP de 26,45 s para 1,87 s, mas em simulação
local e com outro instrumento
([ressalvas](acao-melhoria.md#52-efeito-medido)). A meta só é confirmada com a coleta do G3
repetida em produção.

## 4. Prevenção

| Medida | Evita a repetição de |
|---|---|
| Limite de peso por imagem (por exemplo, 200 kB), verificado antes de publicar | OM1 |
| Limite de LCP e de JavaScript por página na integração contínua (Lighthouse em perfil móvel) | OM1, OM4, OM5 e OM8 |
| Teste de rolagem horizontal e de controles cobertos em 360 px a cada publicação | OM2 e OM6 |

*Tabela 7: Medidas de prevenção.*

## 5. Ligação com as decisões do requisitante

| Decisão da [Fase 1](../fase-1/index.md#12-requisitante-e-objetivo) | O que a lista oferece |
|---|---|
| 1. Interface e fluxos | Só o layout móvel (OM2 e OM6). O redesenho de fluxos para usuários com pouca familiaridade digital depende de G1 |
| 2. Desempenho em condições reais | OM1, OM3, OM4, OM5, OM7, OM8 e OM9, começando por OM1 |
| 3. Cobertura de ambientes | Incluir 360 px na matriz de testes para o SITGeo e a Biblioteca. Navegadores e sistemas dependem da #72 |

*Tabela 8: Oportunidades por decisão do requisitante.*

## 6. Quando a lista deve ser revista

- **Matriz de ambientes (#72):** as falhas F01 a F03 foram vistas em emulação. Se as três forem
  confirmadas em um aparelho, o ambiente terá 3 falhas graves e será Insatisfatório (0) em
  M2.3.1; nesse caso OM2 e OM6 passam a impacto 3, e OM6 sobe para a onda 2. Se não forem
  confirmadas, as funções voltam a contar como preservadas.
- **Coleta de G1 (#71):** acrescentar as oportunidades de interação e acessibilidade.
- **Retorno do MDA:** rever o esforço e as causas que dependem do código e do servidor.
