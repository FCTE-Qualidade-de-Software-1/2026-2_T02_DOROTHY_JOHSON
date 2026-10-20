# Métricas

*Nível quantitativo.*

Cada métrica responde a uma questão e é documentada com definição, procedimento de cálculo,
fonte dos dados, procedimento de coleta e critério de interpretação (premissa 2 do enunciado).

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

As métricas de G3 seguem os nomes e as definições das medidas de eficiência de desempenho da
ISO/IEC 25023 (ISO/IEC, 2011b). As ferramentas Lighthouse e Chrome DevTools são apenas os
**instrumentos de coleta**: cada ficha explica como a medida da norma foi operacionalizada com
elas.

| ID | Questão | Métrica (ISO/IEC 25023) | Operacionalização | Instrumento |
|---|---|---|---|---|
| M3.1.1 | Q3.1 | Tempo médio de resposta | *First Contentful Paint* (FCP) | Lighthouse |
| M3.1.2 | Q3.1 | Tempo médio de execução (*turnaround*) do carregamento | *Largest Contentful Paint* (LCP) | Lighthouse |
| M3.2.1 | Q3.2 | Tempo médio de execução (*turnaround*) da tarefa | Tempo entre a ação do usuário e a exibição do resultado de T1 e T2 | Chrome DevTools (painel Performance) |
| M3.3.1 | Q3.3 | Utilização média de CPU | Tempo de CPU na thread principal durante o carregamento | Lighthouse |
| M3.4.1 | Q3.4 | Utilização média de memória | Memória ocupada pelo JavaScript (*JS heap*) após o carregamento e após cada tarefa | Chrome DevTools |

### Condições comuns de coleta

Valem para todas as métricas de G3 e serão detalhadas no plano de avaliação da Fase 3:

- **Perfil de acesso:** celular simulado, com a limitação de rede e de CPU do perfil móvel padrão
  do Lighthouse, aplicada também no DevTools.
- **Cache:** sempre vazio no início de cada execução.
- **Repetições:** 5 execuções por página ou tarefa, consolidadas pela **mediana**. A documentação
  do Lighthouse indica que a mediana de 5 execuções é duas vezes mais estável que uma única
  execução e recomenda valores agregados, como a mediana, em vez de resultados isolados
  (GOOGLE, 2023b).
- **Execuções isoladas:** nunca simultâneas na mesma máquina e sem outros programas pesados
  abertos (GOOGLE, 2023b).
- **Registro:** cada execução registra data e hora, e os relatórios brutos são versionados no
  repositório.

### M3.1.1: Tempo médio de resposta

| Campo | Especificação |
|---|---|
| Questão | Q3.1 |
| Definição | Na ISO/IEC 25023, tempo entre o comando do usuário e o recebimento da primeira resposta (ISO/IEC, 2011b). Em uma página web, a primeira resposta é o primeiro conteúdo exibido, medido pelo FCP: tempo entre o início da navegação e a renderização de qualquer parte do conteúdo da página (GOOGLE, 2023a) |
| Procedimento de cálculo | Mediana do FCP das 5 execuções de cada página |
| Fonte dos dados | Relatório JSON do Lighthouse, métrica `first-contentful-paint` |
| Procedimento de coleta | Executar o Lighthouse pela linha de comando, categoria desempenho, perfil móvel padrão, 5 vezes por página |
| Unidade e escala | Segundos; escala de razão |
| Critério de interpretação | Quanto menor, melhor. Referência externa: FCP de até 1,8 s é bom e acima de 3,0 s é ruim (GOOGLE, 2023a) |

### M3.1.2: Tempo médio de execução do carregamento

| Campo | Especificação |
|---|---|
| Questão | Q3.1 |
| Definição | Na ISO/IEC 25023, tempo entre o início de um trabalho e a sua conclusão (ISO/IEC, 2011b). No carregamento de uma página, a conclusão é a exibição do conteúdo principal, medida pelo LCP: tempo de renderização da maior imagem, bloco de texto ou vídeo visível, contado a partir do início do carregamento (GOOGLE, 2025) |
| Procedimento de cálculo | Mediana do LCP das 5 execuções de cada página |
| Fonte dos dados | Relatório JSON do Lighthouse, métrica `largest-contentful-paint` |
| Procedimento de coleta | O mesmo de M3.1.1 (mesmas execuções) |
| Unidade e escala | Segundos; escala de razão |
| Critério de interpretação | Quanto menor, melhor. Referência externa: LCP de até 2,5 s é bom e acima de 4,0 s é ruim (GOOGLE, 2025) |

### M3.2.1: Tempo médio de execução da tarefa

| Campo | Especificação |
|---|---|
| Questão | Q3.2 |
| Definição | Na ISO/IEC 25023, tempo entre o início de um trabalho e a sua conclusão (ISO/IEC, 2011b). Em T1, vai do clique em "Selecionar" até a exibição dos dados do território; em T2, vai do clique para ativar a camada até a camada aparecer no mapa |
| Procedimento de cálculo | Para cada tarefa, mediana das 5 execuções |
| Fonte dos dados | Gravação do painel Performance do Chrome DevTools: instante do clique e instante do último quadro em que o resultado termina de aparecer |
| Procedimento de coleta | Com a página já carregada e o mesmo perfil móvel, iniciar a gravação, executar a tarefa com o território ou a camada de referência (fixados na Fase 3) e encerrar a gravação; repetir 5 vezes com cache vazio |
| Unidade e escala | Segundos; escala de razão |
| Critério de interpretação | Quanto menor, melhor. Referência externa: até 1 s o fluxo de pensamento do usuário não é interrompido; acima de 10 s o usuário tende a perder a atenção na tarefa (NIELSEN, 1993) |

### M3.3.1: Utilização média de CPU

| Campo | Especificação |
|---|---|
| Questão | Q3.3 |
| Definição | Na ISO/IEC 25023, quanto tempo de CPU é usado para executar uma tarefa (ISO/IEC, 2011b). No carregamento de uma página, é o tempo de CPU gasto na thread principal do navegador (avaliação de scripts, estilo e layout, renderização, análise de HTML e CSS, coleta de lixo) |
| Procedimento de cálculo | Mediana, nas 5 execuções de cada página, da soma dos tempos de todas as categorias da thread principal |
| Fonte dos dados | Relatório JSON do Lighthouse, auditoria `mainthread-work-breakdown` |
| Procedimento de coleta | O mesmo de M3.1.1 (mesmas execuções) |
| Unidade e escala | Segundos; escala de razão |
| Critério de interpretação | Quanto menor, melhor. Referência externa: o Lighthouse sinaliza páginas que mantêm a thread principal ocupada por mais de 4 s durante o carregamento (GOOGLE, 2019) |

!!! note "Adaptação da medida"
    A ISO/IEC 25023 define a utilização de CPU como razão entre o tempo de CPU usado e o tempo de
    operação (ISO/IEC, 2011b). Esta métrica usa o tempo de CPU absoluto, que é o valor para o qual
    existe referência externa de interpretação.

### M3.4.1: Utilização média de memória

| Campo | Especificação |
|---|---|
| Questão | Q3.4 |
| Definição | Na ISO/IEC 25023, quanto espaço de memória é usado para executar uma tarefa (ISO/IEC, 2011b). Nesta avaliação, é a memória ocupada pelo JavaScript da página (*JS heap* usado) |
| Procedimento de cálculo | Mediana das 5 execuções, medida em dois momentos: após o carregamento de cada página e após a conclusão de T1 e de T2 |
| Fonte dos dados | Valor de *JS heap* usado informado pelo Chrome DevTools |
| Procedimento de coleta | Com o mesmo perfil e cache vazio, carregar a página, aguardar o fim da atividade de rede, forçar a coleta de lixo pelo DevTools e registrar o *JS heap* usado; repetir após executar a tarefa |
| Unidade e escala | Megabytes; escala de razão |
| Critério de interpretação | Quanto menor, melhor. Não foi encontrada referência externa de limite para esta medida: a interpretação é comparativa entre as páginas e tarefas |

!!! note "Adaptação da medida"
    A ISO/IEC 25023 define a utilização de memória como razão entre a memória usada e a memória
    total (ISO/IEC, 2011b). No navegador, a memória total disponível para a página não é um valor
    fixo, por isso esta métrica usa a memória ocupada em valor absoluto.

---

## Referências

GOOGLE. **Minimize main-thread work**. [S.l.]: Google, 2019. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown>. Acesso em: 20 out. 2026.

GOOGLE. **First Contentful Paint (FCP)**. [S.l.]: Google, 2023a. Disponível em: <https://web.dev/articles/fcp>. Acesso em: 20 out. 2026.

GOOGLE. **Lighthouse variability**. [S.l.]: Google, 2023b. Disponível em: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md>. Acesso em: 20 out. 2026.

GOOGLE. **Largest Contentful Paint (LCP)**. [S.l.]: Google, 2025. Disponível em: <https://web.dev/articles/lcp>. Acesso em: 20 out. 2026.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC WD 25023**: systems and software engineering — systems and software quality requirements and evaluation (SQuaRE) — measurement of system and software product quality. Working Draft, version 0.1.0. Genebra: ISO, 2011b.

NIELSEN, J. **Usability engineering**. Boston: Academic Press, 1993.
