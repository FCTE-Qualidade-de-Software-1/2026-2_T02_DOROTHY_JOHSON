# Hipóteses

*Nível operacional.*

Para cada questão, a resposta esperada é registrada como hipótese. As hipóteses apoiam a
interpretação dos resultados na Fase 4 e podem ser valores ou ideias comparativas
(RAMOS, 2026a).

---

## G1: Capacidade de interação

| ID | Questão | Hipótese | Base |
|---|---|---|---|
| H1.1 | Q1.1 | Pelo menos dois terços das seções explicam a própria finalidade na página de entrada (M1.1.1). No primeiro clique a partir da página Início (M1.1.2), a maioria dos participantes acerta a seção de T1 (Meu Território) e de T3 (Biblioteca Territorial), mas a minoria acerta a de T2, porque o nome "SITGeo" é uma sigla que não indica que a seção contém mapas | Textos de abertura observados na Fase 1 (seção 4.2); nome das seções no menu (Fase 1, seção 3.1) |
| H1.2 | Q1.2 | T1 e T3 atingem taxa de conclusão sem ajuda (M1.2.1) de pelo menos 78%, a média de referência de testes de usabilidade; T2 fica abaixo desse valor | Média de conclusão de tarefas (SAURO; LEWIS, 2016); SITGeo exige ativar camadas e interpretar legendas (Fase 1, seção 3.3) |
| H1.3 | Q1.3 | T2 tem a menor eficiência de caminho (M1.3.1) das três tarefas, abaixo de 0,5: os participantes executam mais que o dobro dos passos mínimos | Hipótese comparativa; mesma base de H1.2 |
| H1.4 | Q1.4 | Seleções incompletas e campos obrigatórios vazios são bloqueados, mas formatos inválidos (e-mail e telefone) nem sempre: a prevenção de erros (M1.4.1) fica entre 50% e 100%. Menos da metade das mensagens identifica o campo e diz como corrigir (M1.4.2) | Botões desabilitados até a seleção estar completa, observados na Fase 1 (seção 4.2) |
| H1.5 | Q1.5 | A pontuação SUS média (M1.5.1) fica entre 51 e 68: acima do adjetivo "OK", mas abaixo da média de referência. A nota de aparência (M1.5.2) fica acima do ponto neutro (3) | Média de referência do SUS (SAURO; LEWIS, 2016); escala de adjetivos (BANGOR; KORTUM; MILLER, 2009) |
| H1.6 | Q1.6 | Todas as páginas aprovam pelo menos 80% das regras automáticas aplicáveis (M1.6.1), mas nenhuma fica livre de violações críticas ou sérias (M1.6.2). O SITGeo tem o maior número delas, por causa do mapa interativo | Hipótese comparativa; critérios WCAG 2.1 (W3C, 2018) e eMAG (BRASIL, 2014) |

!!! warning "Hipóteses sem medição piloto"
    Diferentemente de G3, as hipóteses de G1 foram formuladas a partir das observações da Fase 1 e
    de valores de referência da literatura, sem medição piloto. Antes da Fase 4, recomenda-se um
    piloto com um participante (que não entra na amostra) e uma execução do axe em cada página,
    para conferir o roteiro e a ordem de grandeza dos valores.

---

## G2: Flexibilidade

| ID | Questão | Hipótese | Base |
|---|---|---|---|
| H2.1 | Q2.1 | Nos navegadores baseados em Chromium (Chrome, Edge e Samsung Internet), todas as execuções são concluídas (M2.1.1 = 100%). No Safari/iOS e no Firefox, pelo menos uma execução falha, com maior chance em T2 (SITGeo) | Hipótese comparativa; predominância do Chrome no Brasil (Fase 1, seção 1.3), o que sugere ser esse o navegador mais testado pelo fornecedor |
| H2.2 | Q2.2 | Em 768 px ou mais, nenhuma página tem rolagem horizontal; em 360 px, pelo menos uma das três páginas tem (M2.2.1 < 100%). Meu Território e Biblioteca Territorial mantêm todas as funções no celular, e o SITGeo não (M2.2.2 < 100% apenas no SITGeo) | Hipótese comparativa; o SITGeo combina mapa, painel de camadas e legenda na mesma tela (Fase 1, seção 3.1) |
| H2.3 | Q2.3 | As falhas dependentes de ambiente (M2.3.1) se concentram no SITGeo, nas larguras de celular e no Safari/iOS. Chrome/Android, o ambiente de maior participação, não tem falhas bloqueantes | Consequência de H2.1 e H2.2 |

!!! warning "Hipóteses sem medição piloto"
    As hipóteses de G2 também foram formuladas sem medição piloto. Um piloto rápido (as três
    páginas em 360 px e 1366 px, no Chrome e no Firefox) permite ajustá-las antes da Fase 4.

---

## G3: Eficiência de desempenho

| ID | Questão | Hipótese | Base |
|---|---|---|---|
| H3.1 | Q3.1 | Nas três páginas, a primeira resposta visível (M3.1.1) chega em até 3,0 s. O conteúdo principal (M3.1.2) de Meu Território e do SITGeo só é exibido depois de 4,0 s, na faixa ruim do LCP, e o da Biblioteca Territorial fica próximo desse limite. O SITGeo é a página mais lenta | Piloto; faixas de FCP e LCP (GOOGLE, 2023a; GOOGLE, 2025); renderização no navegador observada na Fase 1 (seção 3.4) |
| H3.2 | Q3.2 | T2 (ativar uma camada) é concluída entre 1 s e 10 s: interrompe o fluxo de pensamento do usuário, mas não a atenção. T1 (consultar um território) passa de 10 s | Piloto; limites de tempo de resposta de Nielsen (1993) |
| H3.3 | Q3.3 | O carregamento do SITGeo mantém a thread principal ocupada por mais de 4 s; Meu Território e Biblioteca Territorial ficam abaixo desse limite | Piloto; limite de sinalização do Lighthouse (GOOGLE, 2019) |
| H3.4 | Q3.4 | A memória ocupada pelo JavaScript aumenta depois das tarefas, e o aumento causado por T1 é maior que o causado por T2 | Piloto (hipótese comparativa: não há referência externa de limite) |

### Medição piloto

Para confirmar que as métricas podem ser coletadas e ter a ordem de grandeza dos valores, a
equipe fez uma medição piloto em 20/10/2026, entre 14h20 e 14h32 (horário de Brasília),
seguindo as condições comuns de coleta descritas em
[Métricas](metricas.md#condicoes-comuns-de-coleta-g3): 5 execuções por página ou tarefa, cache
vazio, perfil móvel do Lighthouse e mediana.

Os dados brutos, o resumo e os scripts estão versionados no repositório, para que qualquer
valor abaixo possa ser conferido ou recalculado:

- relatórios do Lighthouse: [`data/fase-2/piloto/lighthouse/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-2/piloto/lighthouse)
- resultado das tarefas e da memória: [`data/fase-2/piloto/tarefas.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-2/piloto/tarefas.json)
- medianas: [`data/fase-2/piloto/resumo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-2/piloto/resumo.csv)
- scripts de coleta e de cálculo: [`scripts/fase-2/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/scripts/fase-2)

| Página | M3.1.1 Tempo de resposta (FCP) | M3.1.2 Execução do carregamento (LCP) | M3.3.1 CPU na thread principal |
|---|---|---|---|
| Meu Território | 1,56 s | 8,39 s | 2,85 s |
| SITGeo | 2,82 s | 24,40 s | 7,01 s |
| Biblioteca Territorial | 1,56 s | 3,83 s | 1,16 s |

| Tarefa | M3.2.1 Execução da tarefa | M3.4.1 Memória após o carregamento | M3.4.1 Memória após a tarefa |
|---|---|---|---|
| T1: consultar um território (Chapada dos Veadeiros, GO) | 18,84 s | 6,0 MB | 15,4 MB |
| T2: ativar uma camada (PRONAF, valor total de crédito acessado) | 7,83 s | 5,7 MB | 9,5 MB |

!!! warning "Limitações do piloto"
    - O piloto serve apenas para formular as hipóteses e **não substitui** a coleta da Fase 4.
    - Nas tarefas, o fim foi aproximado pelo término da última requisição de rede disparada pelo
      clique, de forma automatizada. Na Fase 4, o fim será identificado visualmente na gravação
      do painel Performance do DevTools, como define a ficha de M3.2.1.
    - A memória foi registrada depois de forçar a coleta de lixo do navegador, como prevê a
      ficha de M3.4.1.
    - O LCP do SITGeo variou de 19,1 s a 24,8 s entre as execuções, e o da Biblioteca
      Territorial ficou entre 3,8 s e 4,0 s, muito perto do limite da faixa ruim. Isso reforça a
      necessidade das 5 repetições e da mediana.

---

## Referências

BANGOR, A.; KORTUM, P.; MILLER, J. Determining what individual SUS scores mean: adding an adjective rating scale. **Journal of Usability Studies**, v. 4, n. 3, p. 114-123, 2009.

BRASIL. Ministério do Planejamento, Orçamento e Gestão. **eMAG**: Modelo de Acessibilidade em Governo Eletrônico. Versão 3.1. Brasília: MP, 2014. Disponível em: <https://emag.governoeletronico.gov.br>. Acesso em: 20 out. 2026.

GOOGLE. **Minimize main-thread work**. [S.l.]: Google, 2019. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown>. Acesso em: 20 out. 2026.

GOOGLE. **First Contentful Paint (FCP)**. [S.l.]: Google, 2023a. Disponível em: <https://web.dev/articles/fcp>. Acesso em: 20 out. 2026.

GOOGLE. **Largest Contentful Paint (LCP)**. [S.l.]: Google, 2025. Disponível em: <https://web.dev/articles/lcp>. Acesso em: 20 out. 2026.

NIELSEN, J. **Usability engineering**. Boston: Academic Press, 1993.

RAMOS, C. S. **Medição baseada em objetivos**: determinando o que medir. Notas de aula da disciplina Qualidade de Software 1. Brasília: FCTE/UnB, 2026a.

SAURO, J.; LEWIS, J. R. **Quantifying the user experience**: practical statistics for user research. 2. ed. Cambridge: Morgan Kaufmann, 2016.

WORLD WIDE WEB CONSORTIUM. **Web Content Accessibility Guidelines (WCAG) 2.1**. [S.l.]: W3C, 2018. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: 20 out. 2026.
