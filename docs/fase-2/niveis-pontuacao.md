# Níveis de Pontuação e Critérios de Julgamento

Esta seção define como os resultados das **19 métricas** dos objetivos GQM serão convertidos em níveis de pontuação e em juízos de qualidade para as três características selecionadas na [Fase 1](../fase-1/index.md): **capacidade de interação (G1)**, **flexibilidade (G2)** e **eficiência de desempenho (G3)**.

As regras complementam as fichas de [métricas](metricas.md), as [questões](questoes.md) e as [hipóteses](hipoteses.md). Os resultados observados somente serão julgados na Fase 4, após a coleta estabelecida na Fase 3.

!!! important "Natureza dos limiares"
    As normas ISO/IEC 25010:2023 e ISO/IEC 25023 fundamentam a escolha das características e das medidas, **mas não estabelecem os quatro níveis de pontuação abaixo**. Os cortes derivados de referências externas são identificados no texto; os demais são **critérios operacionais propostos pela equipe**, para uso no contexto desta avaliação, e precisam ser validados na revisão da Fase 2. Não devem ser apresentados como limites normativos nem como conclusões já verificadas sobre o SIT.

## 1. Escala comum e regras de aplicação

| Nível | Pontos | Significado para o julgamento |
|---|:---:|---|
| **Insatisfatório** | **0** | Desempenho aquém do patamar mínimo adotado; requer investigação e ação corretiva prioritária. |
| **Aceitável** | **1** | Atende apenas parcialmente à expectativa; merece melhoria e acompanhamento. |
| **Bom** | **2** | Atende à expectativa da avaliação, embora ainda haja oportunidades de melhoria. |
| **Excelente** | **3** | Alcança o patamar mais exigente definido para a métrica. |

**Regras gerais:**

1. Calcular o valor bruto exatamente como definido na [ficha da métrica](metricas.md), preservando unidade, população avaliada e procedimento de agregação (mediana nas cinco execuções de G3; média quando prescrita na ficha).
2. Aplicar os limites **ao valor não arredondado**. Nas tabelas, `≤` inclui o limite, `>` o exclui, e os intervalos foram construídos sem lacunas. Proporções são apresentadas em porcentagem por legibilidade, mas permanecem valores de 0 a 1 no cálculo.
3. Classificar cada **recorte aplicável** (tarefa, página, ambiente ou fase da execução), antes de consolidar uma métrica. Não substituir medições de recortes distintos pela média dos valores brutos: tempos, proporções, notas e contagens têm escalas diferentes.
4. Registrar, para cada resultado, o valor bruto, numerador/denominador quando pertinente, recorte, nível (0–3), evidência, versão da ferramenta/ambiente e eventual ressalva. Os recortes com pior nível devem aparecer nominalmente no relatório.
5. Quando um denominador for zero, faltar uma execução válida ou o comportamento exigido não puder ser observado, registrar **NC — não classificável** e justificar. Não atribuir automaticamente 0 nem 3. A classificação global permanece **pendente** se houver métrica obrigatória sem resultado válido; a exceção de tarefas nunca concluídas está especificada na seção 5.

O nível **Aceitável** é um nível intermediário de pontuação, **não** uma certificação de conformidade ou autorização para deixar um defeito sem tratamento.

## 2. G1 — Capacidade de interação

A pontuação cobre reconhecibilidade de adequação (Q1.1), apreensibilidade (Q1.2), operabilidade (Q1.3), proteção contra erros (Q1.4), engajamento (Q1.5) e assistência ao usuário (Q1.6).

| Métrica e unidade | Insatisfatório — 0 | Aceitável — 1 | Bom — 2 | Excelente — 3 |
|---|---|---|---|---|
| **M1.1.1** — seções que explicam a própria finalidade (de 9) | 0–5 seções | 6 seções | 7–8 seções | 9 seções |
| **M1.1.2** — acerto do primeiro clique, **por tarefa** (%) | < 60% | ≥ 60% e < 80% | ≥ 80% e < 100% | 100% |
| **M1.2.1** — conclusão sem ajuda, **por tarefa** (%) | < 60% | ≥ 60% e < 80% | ≥ 80% e < 100% | 100% |
| **M1.3.1** — eficiência do caminho, **por tarefa** (0–1) | < 0,50 | ≥ 0,50 e < 0,70 | ≥ 0,70 e < 0,90 | ≥ 0,90 |
| **M1.4.1** — casos inválidos bloqueados/sinalizados (%) | < 50% | ≥ 50% e < 80% | ≥ 80% e < 100% | 100% |
| **M1.4.2** — mensagens que explicam campo e correção (%) | < 50% | ≥ 50% e < 80% | ≥ 80% e < 100% | 100% |
| **M1.5.1** — média do *System Usability Scale* (SUS; 0–100 pontos) | < 51 | ≥ 51 e < 71 | ≥ 71 e < 85 | ≥ 85 |
| **M1.5.2** — média da nota de aparência (1–5) | < 3,0 | ≥ 3,0 e < 3,5 | ≥ 3,5 e < 4,5 | ≥ 4,5 |
| **M1.6.1** — regras automáticas WCAG 2.1 A/AA aprovadas, **por página** (%) | < 80% | ≥ 80% e < 90% | ≥ 90% e < 100% | 100% |
| **M1.6.2** — elementos com violação crítica ou séria, **por página** | ≥ 1 crítica **ou** ≥ 6 sérias | 0 críticas e 3–5 sérias | 0 críticas e 1–2 sérias | 0 críticas e 0 sérias |

### Justificativas e particularidades de G1

- **M1.1.1:** os limites usam os nove pontos de entrada descritos na ficha. Seis de nove (66,7%) corresponde ao patamar de dois terços da hipótese H1.1; cobertura total representa o nível Excelente.
- **M1.1.2 e M1.2.1:** com **cinco participantes**, os resultados por tarefa variam de 20 em 20 pontos percentuais: 3/5 = Aceitável, 4/5 = Bom e 5/5 = Excelente. O corte de 80% é a aproximação realizável acima da referência de cerca de 78% de conclusão mencionada em M1.2.1; os demais limites são internos. A média das três tarefas também é informada, mas **não substitui o julgamento por tarefa**.
- **M1.3.1:** uma razão de 0,50 significa o dobro do caminho mínimo; o limiar explicita a hipótese H1.3. **Somente tentativas concluídas** compõem a média. Um caminho curto não compensa uma tarefa fracassada: interpretar M1.3.1 sempre junto de M1.2.1.
- **M1.4.1 e M1.4.2:** são julgadas separadamente. Em M1.4.2, o denominador inclui **somente** os casos de M1.4.1 nos quais alguma mensagem apareceu. Casos bloqueados silenciosamente não contam como mensagem boa nem ruim; devem ser discutidos como ressalva. Se nenhuma mensagem aparecer (denominador zero), M1.4.2 é **NC**, exigindo inspeção complementar antes do juízo de G1.
- **M1.5.1:** 51, 71 e 85 são aproximações dos adjetivos *OK*, *bom* e *excelente* citados por Bangor, Kortum e Miller (2009), conforme a ficha. A média de referência de **68 pontos** continua como comparação descritiva, não como limite adicional de classe. **M1.5.2:** o ponto 3,0 é neutro, portanto uma nota apenas neutra não significa percepção positiva.
- **M1.6.1 e M1.6.2:** a faixa de 80% vem da hipótese H1.6, **não** de uma exigência da WCAG. Em M1.6.2, contar **elementos distintos afetados** pelas violações `critical` e `serious` do axe-core, e não apenas a quantidade de regras violadas. Se um elemento aparecer em várias violações, contá-lo uma só vez e classificá-lo pela **maior gravidade**. Registrar as duas gravidades separadamente, mesmo quando a pontuação é apresentada como um único nível. **Uma única violação crítica força Insatisfatório nesse recorte.** Aprovação de todas as regras automáticas não equivale à conformidade completa com WCAG/eMAG; verificações manuais continuam necessárias.

**Recortes esperados:** M1.1.2, M1.2.1 e M1.3.1: T1, T2 e T3; M1.6.1 e M1.6.2: Início, Meu Território, SITGeo, Biblioteca Territorial e Fale Conosco; as demais métricas seguem a agregação definida em suas fichas.

## 3. G2 — Flexibilidade

A adaptabilidade é examinada por navegador/sistema operacional, larguras de tela, disponibilidade de funções no celular e falhas dependentes de ambiente.

| Métrica e unidade | Insatisfatório — 0 | Aceitável — 1 | Bom — 2 | Excelente — 3 |
|---|---|---|---|---|
| **M2.1.1** — tarefas concluídas, **por ambiente** e no geral (%) | < 2/3 (66,7%) | ≥ 2/3 e < 85% | ≥ 85% e < 100% | 100% |
| **M2.2.1** — combinações página × largura sem rolagem horizontal (de 15) | 0–11 combinações | 12–13 combinações | 14 combinações | 15 combinações |
| **M2.2.2** — funções preservadas em 360 px, **por página** (%) | < 60% | ≥ 60% e < 80% | ≥ 80% e < 100% | 100% |
| **M2.3.1** — falhas dependentes de ambiente, **por ambiente**, classificadas por gravidade | ≥ 1 **bloqueante** ou ≥ 3 **graves** | 0 bloqueantes e 1–2 graves | 0 bloqueantes, 0 graves e ≥ 1 cosmética | Nenhuma falha reproduzida |

### Justificativas e particularidades de G2

- **M2.1.1:** as três tarefas T1–T3 devem ser executadas em cada um dos **seis ambientes de software** inicialmente propostos em [G2](objetivos.md#g2-flexibilidade). O julgamento é apresentado por ambiente (0/3, 1/3, 2/3 ou 3/3) **e** no geral (18 execuções, se a matriz não mudar). Na classificação por ambiente, a faixa Bom não é alcançável com apenas três tarefas; permanece útil para o agregado geral. Os cortes são operacionais, não limiares de norma.
- **M2.2.1:** 15 combinações resultam de **3 páginas × 5 larguras**. Usar as exceções de conteúdo bidimensional previstas na ficha (por exemplo, área do mapa), evitando classificar como falha uma rolagem necessária para operar esse conteúdo.
- **M2.2.2:** examinar cada página em 360 px contra a lista de suas funções em 1366 px. Uma função invisível ou não operável no celular **não** pode ser considerada preservada. Reportar também quais funções se perderam, independentemente da porcentagem.
- **M2.3.1:** a classificação segue a **maior gravidade** e, quando pertinente, a quantidade de falhas graves **reproduzidas duas vezes**. Se há falha grave ou bloqueante, a presença de falhas cosméticas não reduz sua severidade. A mesma falha pode aparecer em vários ambientes, conforme a ficha, mas não deve ser duplicada dentro do mesmo ambiente.
- Falha que ocorre também no Chrome/Windows de referência pode indicar defeito geral do produto, e não **dependência de ambiente**; registrar separadamente e não forçar seu enquadramento em M2.3.1.

**Recortes esperados:** M2.1.1 e M2.3.1: ambientes da matriz da Fase 3; M2.2.2: Meu Território, SITGeo e Biblioteca Territorial; M2.2.1: as 15 combinações consolidadas em uma proporção. Para priorizar ambientes no relatório, considerar primeiro a gravidade e a reprodução e, em seguida, a participação de mercado, conforme Q2.3.

## 4. G3 — Eficiência de desempenho

As faixas de FCP, LCP, tempo de resposta à ação e CPU usam referências discutidas nas fichas, complementadas por patamares internos para distinguir **Bom** de **Excelente**. Para memória, não foi identificado limite externo universal aplicável: a escala é **exploratória e interna**, baseada na ordem de grandeza observada no [piloto](hipoteses.md#medicao-piloto), e deverá ser revista se o dispositivo de referência mudar.

| Métrica e unidade | Insatisfatório — 0 | Aceitável — 1 | Bom — 2 | Excelente — 3 |
|---|---|---|---|---|
| **M3.1.1** — FCP mediano, **por página** (s) | > 3,0 | > 1,8 e ≤ 3,0 | > 1,0 e ≤ 1,8 | ≤ 1,0 |
| **M3.1.2** — LCP mediano, **por página** (s) | > 4,0 | > 2,5 e ≤ 4,0 | > 1,5 e ≤ 2,5 | ≤ 1,5 |
| **M3.2.1** — duração mediana, **por tarefa** (s) | > 10,0 | > 5,0 e ≤ 10,0 | > 1,0 e ≤ 5,0 | ≤ 1,0 |
| **M3.3.1** — CPU na thread principal, **por página** (s) | > 4,0 | > 3,0 e ≤ 4,0 | > 2,0 e ≤ 3,0 | ≤ 2,0 |
| **M3.4.1** — JS heap mediano, **por momento de coleta** (MB) | > 20,0 | > 12,0 e ≤ 20,0 | > 8,0 e ≤ 12,0 | ≤ 8,0 |

### Justificativas e particularidades de G3

- **M3.1.1 (FCP):** o Google define até **1,8 s** como bom e mais de **3,0 s** como ruim. O corte em 1,0 s para Excelente é um objetivo adicional da equipe.
- **M3.1.2 (LCP):** o Google define até **2,5 s** como bom e acima de **4,0 s** como ruim. O corte em 1,5 s para Excelente é um objetivo adicional da equipe.
- **M3.2.1:** os limites de **1 s** e **10 s** são referências de resposta percebida apresentadas por Nielsen (1993). O limite intermediário de 5 s é proposto pela equipe; a duração inclui o intervalo entre a ação e a exibição do resultado, como prescrito na ficha.
- **M3.3.1:** **4 s** é o patamar de sinalização de trabalho excessivo na thread principal adotado pelo Lighthouse, conforme a ficha. As divisões em 2 e 3 s são critérios internos. Esta é uma **medida absoluta de tempo de CPU**, não percentual de utilização.
- **M3.4.1:** os cortes **8, 12 e 20 MB** são faixas internas de triagem, **não limites de segurança nem requisitos para todos os celulares**. O piloto encontrou aproximadamente **6,0 MB** após carregamento de T1, **15,4 MB** após T1, **5,7 MB** após carregamento de T2 e **9,5 MB** após T2; esses valores apenas contextualizam a escolha das faixas. Não inferir desempenho aceitável do dispositivo inteiro a partir do *JS heap*. Reportar adicionalmente a diferença de memória **antes/depois** de T1 e T2, mas pontuar as medições absolutas conforme a ficha.

**Recortes esperados:** M3.1.1, M3.1.2 e M3.3.1: Meu Território, SITGeo e Biblioteca Territorial; M3.2.1: T1 e T2; M3.4.1: após o carregamento de cada uma das três páginas e após T1 e T2 (**cinco observações**). Cada recorte de G3 usa a **mediana de cinco execuções**, nunca um resultado isolado.

### Exemplo de aplicação — dados do piloto, não avaliação final

| Medida e recorte | Valor do piloto | Nível segundo estas regras |
|---|---:|---|
| M3.1.1 — FCP do SITGeo | 2,82 s | Aceitável (1) |
| M3.1.2 — LCP do SITGeo | 24,40 s | Insatisfatório (0) |
| M3.2.1 — execução de T1 | 18,84 s | Insatisfatório (0) |
| M3.2.1 — execução de T2 | 7,83 s | Aceitável (1) |
| M3.3.1 — CPU do SITGeo | 7,01 s | Insatisfatório (0) |
| M3.4.1 — memória após T1 | 15,4 MB | Aceitável (1) |

Esses exemplos demonstram o procedimento de conversão, **não** constituem o juízo final: o próprio piloto tem limitações metodológicas descritas em [Hipóteses](hipoteses.md#medicao-piloto).

## 5. Critérios de julgamento por característica

O juízo de cada característica deve indicar **onde a qualidade ficou comprometida**; uma nota média isolada não basta para orientar as três decisões do requisitante descritas na Fase 1.

### 5.1 Consolidação das pontuações

1. **Resultado por recorte:** converter cada medição aplicável em pontos `0`, `1`, `2` ou `3`, de acordo com as tabelas anteriores. Quando a ficha determina um resultado único (por exemplo, SUS médio), classificá-lo uma vez.
2. **Métrica:** calcular a **média aritmética dos pontos dos seus recortes válidos**, sem arredondar para inteiro. Exemplos: três tarefas de M1.2.1, cinco páginas de M1.6.1, seis ambientes de M2.1.1 ou três páginas de M3.1.2. O valor global de M2.1.1 deve ser informado também, mas não entrar **novamente** na média (evita contagem dupla).
3. **Questão GQM:** calcular a média aritmética das pontuações das métricas associadas à questão. Assim, por exemplo, Q1.1 combina M1.1.1 e M1.1.2; Q1.6 combina M1.6.1 e M1.6.2; Q3.1 combina M3.1.1 e M3.1.2.
4. **Característica:** calcular a média aritmética das pontuações de suas questões: **G1 = média de Q1.1 a Q1.6 (6 questões)**; **G2 = média de Q2.1 a Q2.3 (3 questões)**; **G3 = média de Q3.1 a Q3.4 (4 questões)**. Este método dá o mesmo peso a cada questão, evitando que uma subcaracterística tenha mais influência apenas por possuir mais métricas ou páginas.
5. **Juízo final:** converter a média da característica segundo a tabela abaixo e **aplicar as regras de gravidade** da seção 5.2. Exibir o valor com duas casas decimais, mas usar o valor completo para decidir a faixa.

| Média das questões (0–3) | Juízo preliminar |
|---|---|
| 0,00 ≤ média < 1,00 | **Insatisfatório** |
| 1,00 ≤ média < 2,00 | **Aceitável** |
| 2,00 ≤ média < 2,75 | **Bom** |
| 2,75 ≤ média ≤ 3,00 | **Excelente** |

O limite **2,75** para Excelência é deliberadamente exigente e **interno**: requer que quase todos os aspectos avaliados recebam pontuação alta. A consolidação produz um **índice de julgamento construído para esta avaliação**, não uma pontuação de qualidade padronizada pela ISO.

### 5.2 Regras de gravidade e exceções

As médias não podem esconder falhas que impedem o acesso à informação ou a conclusão de tarefas. Aplicar os seguintes limitadores **depois** do cálculo da média:

| Característica | Condição observada | Regra para o juízo final |
|---|---|---|
| **G1 — Capacidade de interação** | Qualquer página contém pelo menos **uma violação crítica de acessibilidade** em M1.6.2 | **Insatisfatório**, independentemente da média; indicar página, elemento e evidência. |
| **G1 — Capacidade de interação** | Qualquer tarefa tem **menos de 60% de conclusão sem ajuda** (M1.2.1) | Juízo **no máximo Aceitável**. Se nenhuma tentativa de determinada tarefa foi concluída, M1.3.1 dessa tarefa fica NC, mas G1 recebe juízo **Insatisfatório** por falha do fluxo essencial. |
| **G2 — Flexibilidade** | Pelo menos **uma falha bloqueante dependente de ambiente**, reproduzida conforme M2.3.1 | **Insatisfatório**, independentemente da média; identificar navegador/SO, largura, página e tarefa. |
| **G3 — Eficiência de desempenho** | LCP **acima de 4 s** em qualquer página avaliada (M3.1.2) **ou** execução de T1/T2 **acima de 10 s** (M3.2.1) | Juízo **no máximo Aceitável**: há atraso significativo em pelo menos um fluxo ou página essencial. |

Quando mais de uma regra se aplicar, prevalece a **mais restritiva**. Registrar sempre o **juízo preliminar**, o **limitador acionado** e o **juízo final**, para que a decisão seja auditável.

**Cobertura insuficiente:** se faltar coleta obrigatória ou houver medida NC não resolvida (por exemplo, M1.4.2 sem mensagens para análise), **não atribuir juízo final à característica** até complementar a medição. A exceção é uma tarefa sem nenhuma conclusão: a ausência de caminho completo em M1.3.1 não impede registrar G1 como Insatisfatório, pois o fracasso integral da tarefa é evidência suficiente de não atendimento do fluxo avaliado. Toda exceção precisa ser explicada no relatório.

### 5.3 Da pontuação à decisão de qualidade

| Característica | Questões que sustentam o julgamento | Interpretação e ação derivada |
|---|---|---|
| **G1 — Capacidade de interação** | Q1.1–Q1.6 | Identificar tarefas com pouca conclusão ou primeiro clique incorreto, caminhos longos, falhas de validação, baixa percepção SUS e barreiras de acessibilidade. **Insatisfatório:** priorizar correção de barreiras críticas e redesenho de fluxos fracassados. **Aceitável:** melhorar telas/mensagens com pior nota. **Bom/Excelente:** manter e monitorar, sem ignorar defeitos localizados. |
| **G2 — Flexibilidade** | Q2.1–Q2.3 | Identificar quais combinações de navegador/SO/largura impedem tarefas, criam rolagem indevida ou removem funções. **Insatisfatório:** corrigir falhas bloqueantes e cobrir o ambiente na matriz de regressão. **Aceitável:** priorizar falhas graves e funções ausentes. **Bom/Excelente:** manter cobertura e registrar falhas cosméticas. Priorizar ambientes também pela participação do público-alvo, sem dispensar a gravidade. |
| **G3 — Eficiência de desempenho** | Q3.1–Q3.4 | Separar lentidão de carregamento (FCP/LCP), demora de T1/T2, uso de CPU e memória. **Insatisfatório:** investigar gargalos com evidências e priorizar otimização das páginas/tarefas de pior resultado. **Aceitável:** mitigar atrasos e consumo elevado. **Bom/Excelente:** monitorar regressões, sobretudo em perfil móvel. |

A ordem para tratar problemas **dentro** de uma característica é: (1) bloqueio ao usuário ou violação crítica; (2) falha de tarefa e tempo muito alto; (3) outros resultados Insatisfatórios; (4) Aceitáveis; (5) melhorias incrementais. **Não** calcular uma nota global única de qualidade do SIT a partir de G1, G2 e G3: as três características atendem a decisões distintas, e os pesos de priorização da Fase 1 **não são pesos de agregação de qualidade**.

## 6. Rastreabilidade e revisão

| Objetivo | Questões | Métricas cobertas | Fonte para cálculo e coleta |
|---|---|---|---|
| **G1** | Q1.1–Q1.6 | M1.1.1; M1.1.2; M1.2.1; M1.3.1; M1.4.1; M1.4.2; M1.5.1; M1.5.2; M1.6.1; M1.6.2 (**10**) | [Métricas — G1](metricas.md#g1-capacidade-de-interacao) |
| **G2** | Q2.1–Q2.3 | M2.1.1; M2.2.1; M2.2.2; M2.3.1 (**4**) | [Métricas — G2](metricas.md#g2-flexibilidade) |
| **G3** | Q3.1–Q3.4 | M3.1.1; M3.1.2; M3.2.1; M3.3.1; M3.4.1 (**5**) | [Métricas — G3](metricas.md#g3-eficiencia-de-desempenho) |

**Situação da revisão por outro membro:** **pendente**. Antes de encerrar a [issue #5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/5), registrar na issue ou no PR: **nome do revisor, data, comentários, aprovação e eventuais mudanças de limiares**. Conferir em especial os critérios internos de CPU, memória, severidade, a regra de agregação e os limitadores por falhas críticas.

## Referências e fundamentação

As referências completas constam das páginas de [Métricas](metricas.md#referencias) e [Hipóteses](hipoteses.md#referencias):

- **BANGOR; KORTUM; MILLER (2009):** faixas adjetivais para pontuação SUS.
- **GOOGLE (2019, 2023a, 2025):** sinalização do tempo de CPU na thread principal, FCP e LCP.
- **NIELSEN (1993):** referências de 1 s e 10 s para tempo de resposta.
- **SAURO; LEWIS (2016):** valores de referência para conclusão de tarefas e SUS.
- **W3C (2018), BRASIL (2014) e DEQUE SYSTEMS (2026):** diretrizes de acessibilidade e verificações automatizadas.
- **ISO/IEC 25010:2023 e ISO/IEC 25023 (edição utilizada nas fichas):** estrutura de qualidade e definição das medidas; **não** fornecem a tabela de quatro níveis criada neste documento.

---

*Documento elaborado para atender ao critério F2-C5 da Fase 2; sujeito à revisão e aprovação por outro integrante da equipe.*
