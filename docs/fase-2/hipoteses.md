# Hipóteses

*Nível operacional.*

Para cada questão, a resposta esperada é registrada como hipótese. As hipóteses apoiam a
interpretação dos resultados na Fase 4 e podem ser valores ou ideias comparativas
(RAMOS, 2026a).

---

## G1: Usabilidade

!!! info "Em construção"
    Seção da issue #24.

---

## G2: Portabilidade

!!! info "Em construção"
    Seção da issue #25.

---

## G3: Eficiência de desempenho

| ID | Questão | Hipótese | Base |
|---|---|---|---|
| H3.1 | Q3.1 | Nas três páginas, a primeira resposta visível (M3.1.1) chega em até 3,0 s, mas o conteúdo principal (M3.1.2) só é exibido depois de 4,0 s, ou seja, na faixa ruim do LCP. O SITGeo é a página mais lenta | Piloto; faixas de FCP e LCP (GOOGLE, 2023a; GOOGLE, 2025); renderização no navegador observada na Fase 1 (seção 3.4) |
| H3.2 | Q3.2 | T2 (ativar uma camada) é concluída entre 1 s e 10 s: interrompe o fluxo de pensamento do usuário, mas não a atenção. T1 (consultar um território) passa de 10 s | Piloto; limites de tempo de resposta de Nielsen (1993) |
| H3.3 | Q3.3 | O carregamento do SITGeo mantém a thread principal ocupada por mais de 4 s; Meu Território e Biblioteca Territorial ficam abaixo desse limite | Piloto; limite de sinalização do Lighthouse (GOOGLE, 2019) |
| H3.4 | Q3.4 | A memória ocupada pelo JavaScript aumenta depois das tarefas, e o aumento causado por T1 é maior que o causado por T2 | Piloto (hipótese comparativa: não há referência externa de limite) |

### Medição piloto

Para confirmar que as métricas podem ser coletadas e ter a ordem de grandeza dos valores, a
equipe fez uma medição piloto em 20/10/2026, seguindo as condições comuns de coleta descritas
em [Métricas](metricas.md#condicoes-comuns-de-coleta): 5 execuções por página ou tarefa, cache
vazio, perfil móvel do Lighthouse e mediana.

| Página | M3.1.1 Tempo de resposta (FCP) | M3.1.2 Execução do carregamento (LCP) | M3.3.1 CPU na thread principal |
|---|---|---|---|
| Meu Território | 1,54 s | 8,79 s | 2,52 s |
| SITGeo | 2,41 s | 23,69 s | 10,33 s |
| Biblioteca Territorial | 1,61 s | 4,40 s | 2,53 s |

| Tarefa | M3.2.1 Execução da tarefa | M3.4.1 Memória após o carregamento | M3.4.1 Memória após a tarefa |
|---|---|---|---|
| T1: consultar um território (Chapada dos Veadeiros, GO) | 15,5 s | 5,6 MB | 18,4 MB |
| T2: ativar uma camada (PRONAF, valor total de crédito acessado) | 6,6 s | 5,7 MB | 10,1 MB |

!!! warning "Limitações do piloto"
    - O piloto serve apenas para formular as hipóteses e **não substitui** a coleta da Fase 4.
    - Nas tarefas, o fim foi aproximado pelo término da última requisição de rede disparada pelo
      clique, de forma automatizada. Na Fase 4, o fim será identificado visualmente na gravação
      do painel Performance do DevTools, como define a ficha de M3.2.1.
    - A memória variou entre execuções por causa da coleta de lixo do navegador. Por isso, a
      ficha de M3.4.1 prevê forçar a coleta de lixo antes de cada registro.
    - Os valores do SITGeo variaram bastante entre execuções (LCP de 18,1 s a 23,8 s; CPU de
      6,4 s a 12,0 s), o que reforça a necessidade das 5 repetições e da mediana.

---

## Referências

GOOGLE. **Minimize main-thread work**. [S.l.]: Google, 2019. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown>. Acesso em: 20 out. 2026.

GOOGLE. **First Contentful Paint (FCP)**. [S.l.]: Google, 2023a. Disponível em: <https://web.dev/articles/fcp>. Acesso em: 20 out. 2026.

GOOGLE. **Largest Contentful Paint (LCP)**. [S.l.]: Google, 2025. Disponível em: <https://web.dev/articles/lcp>. Acesso em: 20 out. 2026.

NIELSEN, J. **Usability engineering**. Boston: Academic Press, 1993.

RAMOS, C. S. **Medição baseada em objetivos**: determinando o que medir. Aula 08 da disciplina Qualidade de Software 1. Brasília: FCTE/UnB, 2026a. Material de aula.
