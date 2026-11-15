# Análise e respostas GQM: eficiência de desempenho

Esta página responde às questões Q3.1 a Q3.4 e ao objetivo G3 com os dados coletados conforme o
[método de eficiência](../fase-3/metodo-eficiencia.md). Cada recorte foi pontuado pelos
[níveis de G3](../fase-2/niveis-pontuacao.md#4-g3-eficiencia-de-desempenho), de 0
(Insatisfatório) a 3 (Excelente), e consolidado pelos
[critérios de julgamento](../fase-2/niveis-pontuacao.md#5-criterios-de-julgamento-por-caracteristica).

## 1. Coleta

| Item | Valor |
|---|---|
| Data e horário | 08/11/2026, das 21:24 às 21:36 (horário de Brasília) |
| Ambiente | [Recursos e ambiente, seção 3.1](../fase-3/ambiente.md#31-eficiencia-de-desempenho-g3) |
| Execuções | 5 por página ou tarefa, consolidadas pela mediana; nenhuma falhou |
| Dados brutos | [`data/fase-4/eficiencia/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/eficiencia) (relatórios do Lighthouse, `tarefas.json` e `resumo.csv`) |
| Pontuação | `data/fase-4/eficiencia/pontuacao.csv`, gerado por `scripts/fase-4/eficiencia/pontuar.py` |
| Desvios do plano | Nenhum |

Nas tabelas a seguir, "mín.–máx." é o menor e o maior valor das 5 execuções.

## 2. Resultados por questão

### Q3.1 Quanto tempo as páginas levam para dar a primeira resposta visível e para exibir o conteúdo principal?

| Página | FCP (M3.1.1) | Nível | LCP (M3.1.2) | Nível |
|---|---|---|---|---|
| Meu Território | 1,56 s (1,52–1,63) | Bom (2) | **8,27 s** (7,80–8,97) | Insatisfatório (0) |
| SITGeo | 1,60 s (1,55–1,78) | Bom (2) | **23,45 s** (17,21–23,95) | Insatisfatório (0) |
| Biblioteca Territorial | 1,56 s (1,56–1,76) | Bom (2) | 3,91 s (3,89–4,43) | Aceitável (1) |

*Tabela 1: Primeira resposta (FCP) e conteúdo principal (LCP), perfil móvel limitado.*

**Resposta:** a primeira resposta visível chega rápido nas três páginas, em cerca de 1,6 s,
dentro da faixa boa do Google (até 1,8 s). O conteúdo principal, porém, demora: em Meu
Território leva mais de 8 s e no SITGeo mais de 23 s, muito além do limite de 4 s da faixa
ruim. A Biblioteca Territorial fica logo abaixo desse limite (3,91 s) e o ultrapassou em uma
das cinco execuções. O usuário vê a página começar a carregar, mas espera muito pelo conteúdo
que procura. **Pontos de Q3.1: 1,17** (M3.1.1 = 2,00; M3.1.2 = 0,33).

### Q3.2 Quanto tempo o portal leva para concluir as tarefas T1 e T2 depois da ação do usuário?

| Tarefa | Tempo (M3.2.1) | Nível |
|---|---|---|
| T1, consultar Chapada dos Veadeiros - GO em Meu Território | **20,39 s** (19,90–20,73) | Insatisfatório (0) |
| T2, ativar a camada PRONAF no SITGeo | 6,45 s (6,30–7,18) | Aceitável (1) |

*Tabela 2: Tempo entre o clique e o fim da última requisição disparada pela ação.*

**Resposta:** a consulta de um território (T1) leva cerca de 20 s depois do clique em
"Selecionar", o dobro do limite de 10 s a partir do qual o usuário tende a perder a atenção na
tarefa (NIELSEN, 1993). Ativar uma camada (T2) leva cerca de 6,5 s: interrompe o fluxo de
pensamento, mas fica dentro do limite de atenção. A variação entre execuções é pequena, o que
indica um atraso sistemático, e não instabilidade. **Pontos de Q3.2: 0,50.**

### Q3.3 Quanto tempo de processamento (CPU) o carregamento das páginas exige do aparelho?

| Página | CPU na thread principal (M3.3.1) | Nível |
|---|---|---|
| Meu Território | 2,34 s (2,32–2,78) | Bom (2) |
| SITGeo | **8,26 s** (6,26–11,41) | Insatisfatório (0) |
| Biblioteca Territorial | 2,23 s (1,62–4,60) | Bom (2) |

*Tabela 3: Tempo de CPU na thread principal durante o carregamento.*

**Resposta:** o SITGeo ocupa a thread principal por mais de 8 s, o dobro do patamar de 4 s
que o Lighthouse sinaliza como trabalho excessivo (GOOGLE, 2019), e é a página com maior
variação entre execuções. Meu Território e a Biblioteca ficam perto de 2,3 s. Em um celular
de entrada, o mapa do SITGeo deixa o aparelho ocupado e sem resposta por vários segundos.
**Pontos de Q3.3: 1,33.**

### Q3.4 Quanta memória as páginas e as tarefas ocupam no aparelho?

| Momento | *JS heap* (M3.4.1) | Nível |
|---|---|---|
| Biblioteca Territorial, após o carregamento | 4,60 MB (4,58–4,79) | Excelente (3) |
| Meu Território, após o carregamento | 5,73 MB (5,73–5,94) | Excelente (3) |
| SITGeo, após o carregamento | 5,70 MB (5,64–5,71) | Excelente (3) |
| Após T1 | 15,01 MB (14,88–15,14) | Aceitável (1) |
| Após T2 | 9,37 MB (9,37–9,41) | Bom (2) |

*Tabela 4: Memória ocupada pelo JavaScript depois de forçar a coleta de lixo.*

**Resposta:** as páginas carregam ocupando entre 4,6 e 5,7 MB. As tarefas aumentam esse
valor: a T1 acrescenta 9,28 MB (de 5,73 para 15,01 MB) e a T2 acrescenta 3,67 MB (de 5,70 para
9,37 MB). A consulta de um território é, portanto, a operação que mais pesa na memória. As
faixas de 8, 12 e 20 MB são internas e servem para triagem; não indicam o limite de um
aparelho. **Pontos de Q3.4: 2,40.**

## 3. Julgamento do G3

| Questão | Métricas | Pontos |
|---|---|---:|
| Q3.1 | M3.1.1 = 2,00; M3.1.2 = 0,33 | 1,17 |
| Q3.2 | M3.2.1 = 0,50 | 0,50 |
| Q3.3 | M3.3.1 = 1,33 | 1,33 |
| Q3.4 | M3.4.1 = 2,40 | 2,40 |
| **G3** | Média das quatro questões | **1,35** |

*Tabela 5: Consolidação da pontuação do G3.*

- **Juízo preliminar:** média de 1,35, na faixa de 1,00 a 2,00: **Aceitável**.
- **Limitador (seção 5.2):** acionado, porque o LCP passa de 4 s em Meu Território e no SITGeo
  e a T1 passa de 10 s. O juízo fica limitado a Aceitável.
- **Juízo final: Aceitável.** O portal atende parcialmente à expectativa de eficiência no
  contexto do G3, o acesso por celular de entrada com rede móvel lenta.

**Onde a qualidade ficou comprometida** (recortes com nível 0, em ordem de prioridade da seção
5.3):

1. **T1, consulta de território: 20,39 s.** É a tarefa central de Meu Território e o principal
   uso do portal pelo público final.
2. **LCP do SITGeo: 23,45 s**, somado a **8,26 s de CPU** no carregamento.
3. **LCP de Meu Território: 8,27 s.**

Para o requisitante, o resultado responde à decisão 2 da Fase 1, que é decidir se é necessário
otimizar páginas e mapas sob conexão móvel: **é necessário**. As otimizações devem começar pelo
carregamento do SITGeo e pela resposta da consulta de território, e não pela primeira exibição
das páginas, que já está na faixa boa.

## 4. Hipóteses

| Hipótese | Resultado | Evidência |
|---|---|---|
| H3.1: FCP até 3,0 s nas três páginas; LCP acima de 4,0 s em Meu Território e no SITGeo; Biblioteca próxima desse limite; SITGeo a mais lenta | **Confirmada** | FCP entre 1,56 e 1,60 s; LCP de 8,27 s e 23,45 s; Biblioteca com 3,91 s (4,43 s em uma execução); SITGeo com o maior LCP |
| H3.2: T2 entre 1 e 10 s; T1 acima de 10 s | **Confirmada** | T2 com 6,45 s; T1 com 20,39 s |
| H3.3: SITGeo acima de 4 s de CPU; as outras abaixo | **Confirmada** | SITGeo com 8,26 s; Meu Território com 2,34 s; Biblioteca com 2,23 s |
| H3.4: memória aumenta depois das tarefas, mais em T1 que em T2 | **Confirmada** | Aumento de 9,28 MB na T1 e de 3,67 MB na T2 |

*Tabela 6: Situação das hipóteses de G3.*

## 5. Comparação com o piloto e limitações

| Medida | Piloto (20/10) | Coleta (08/11) |
|---|---:|---:|
| FCP do SITGeo | 2,82 s | 1,60 s |
| LCP do SITGeo | 24,40 s | 23,45 s |
| LCP de Meu Território | 8,39 s | 8,27 s |
| CPU do SITGeo | 7,01 s | 8,26 s |
| CPU da Biblioteca Territorial | 1,16 s | 2,23 s |
| T1 | 18,84 s | 20,39 s |
| T2 | 7,83 s | 6,45 s |
| *JS heap* após T1 | 15,37 MB | 15,01 MB |

*Tabela 7: Medianas do piloto e da coleta da Fase 4.*

Os resultados repetem o quadro do piloto: as mesmas medidas ficam nas mesmas faixas, com
exceção do FCP do SITGeo, que melhorou e passou de Aceitável para Bom. A estabilidade entre as
duas medições, com 19 dias de intervalo, reforça que os problemas encontrados são do produto, e
não de uma sessão de coleta.

**Limitações:**

- **Produto em produção:** a coleta reflete o portal e a carga do servidor em 08/11/2026, à
  noite; outro horário pode ter outra carga.
- **Limitação simulada:** o Lighthouse aplica a limitação de rede e de CPU por simulação, e o
  script das tarefas aplica a limitação no próprio navegador. Os valores representam um celular
  de entrada em rede móvel lenta, e não um aparelho específico.
- **Memória sem referência externa:** as faixas de M3.4.1 são internas, e o *JS heap* não
  mede toda a memória usada pela página.
- **Biblioteca em navegador automatizado:** o seletor de UF da Biblioteca fica desabilitado em
  navegador automatizado ([ambiente, seção 2](../fase-3/ambiente.md#2-paginas-tarefas-e-objetos-de-referencia)),
  então o carregamento medido pode não incluir tudo o que um usuário carrega nessa página.
- **Fim da tarefa:** o tempo vai até a rede ficar 1 s ociosa, o que pode incluir requisições
  que não alteram o que o usuário vê.

## Referências

GOOGLE. **Minimize main-thread work**. [S.l.]: Google, 2019. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown>. Acesso em: 08 nov. 2026.

NIELSEN, J. **Usability engineering**. Boston: Academic Press, 1993.
