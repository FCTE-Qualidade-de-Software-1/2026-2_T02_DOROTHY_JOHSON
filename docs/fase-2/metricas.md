# Métricas

*Nível quantitativo.*

Cada métrica responde a uma questão e é documentada com definição, procedimento de cálculo,
fonte dos dados, procedimento de coleta e critério de interpretação (premissa 2 do enunciado).

---

## G1: Usabilidade

As métricas de G1 operacionalizam medidas de usabilidade da ISO/IEC 25023 (ISO/IEC, 2011b). As
medidas M1.1.2, M1.2.1, M1.3.1, M1.5.1 e M1.5.2 vêm de testes com usuários; M1.1.1, M1.4.1 e
M1.4.2 vêm de inspeção pela equipe; M1.6.1 e M1.6.2 vêm de verificação automática com o axe-core
(DEQUE SYSTEMS, 2026).

| ID | Questão | Métrica (ISO/IEC 25023) | Operacionalização | Instrumento |
|---|---|---|---|---|
| M1.1.1 | Q1.1 | Autodescrição dos pontos de entrada | Proporção de seções do menu cuja página de entrada explica a própria finalidade | Inspeção com roteiro |
| M1.1.2 | Q1.1 | Autodescrição dos pontos de entrada (percebida) | Proporção de participantes que acertam a seção no primeiro clique a partir da página Início | Teste com usuários |
| M1.2.1 | Q1.2 | Interface autoexplicativa | Proporção de participantes que concluem a tarefa sem ajuda | Teste com usuários |
| M1.3.1 | Q1.3 | Eficiência da operação | Razão entre os passos mínimos e os passos executados na tarefa | Teste com usuários (gravação) |
| M1.4.1 | Q1.4 | Prevenção de erros de operação | Proporção de entradas inválidas bloqueadas ou sinalizadas antes do envio | Inspeção com casos de teste |
| M1.4.2 | Q1.4 | Correção de erros de entrada | Proporção de mensagens de erro que identificam o campo e dizem como corrigir | Inspeção com casos de teste |
| M1.5.1 | Q1.5 | Satisfação com o uso | Pontuação do *System Usability Scale* (SUS) | Questionário |
| M1.5.2 | Q1.5 | Estética da aparência da interface | Nota média de aparência, de 1 a 5 | Questionário |
| M1.6.1 | Q1.6 | Acessibilidade para usuários com deficiência | Proporção de regras automáticas WCAG 2.1 A e AA aprovadas | axe-core |
| M1.6.2 | Q1.6 | Acessibilidade para usuários com deficiência | Número de violações de impacto crítico ou sério | axe-core |

### Condições comuns de coleta

Valem para as métricas de teste com usuários (M1.1.2, M1.2.1, M1.3.1, M1.5.1 e M1.5.2) e serão
detalhadas no plano de avaliação da Fase 3:

- **Participantes:** 5 pessoas que nunca usaram o portal, número suficiente para encontrar a maior
  parte dos problemas de usabilidade em um teste qualitativo (NIELSEN, 2000). O recrutamento mistura
  níveis de familiaridade digital, e o perfil de cada participante é registrado sem identificá-lo.
- **Consentimento e gravação:** cada participante assina um termo de consentimento, e a sessão é
  gravada (tela e áudio), conforme a premissa 6 do enunciado.
- **Anonimização:** os participantes são identificados como P1 a P5 nos dados e nas gravações
  versionadas; o vínculo entre código e nome não é publicado (premissa 5).
- **Roteiro:** cada tarefa começa na página Início. O moderador lê a tarefa, não dá dicas e não
  responde perguntas sobre a interface. O participante fala em voz alta o que está pensando.
- **Limite de tempo:** 5 minutos por tarefa. Desistência, estouro do limite ou qualquer ajuda do
  moderador contam como tarefa não concluída.
- **Dispositivo:** o mesmo para todos os participantes, definido na Fase 3, com prioridade para o
  celular (Fase 1, seção 1.3).

### M1.1.1: Autodescrição dos pontos de entrada

| Campo | Especificação |
|---|---|
| Questão | Q1.1 |
| Definição | Na ISO/IEC 25023, proporção de pontos de entrada do produto que explicam o que ele faz (ISO/IEC, 2011b). Nesta avaliação, cada uma das 9 seções do menu principal (Fase 1, seção 3.1) é um ponto de entrada. A seção é contada quando sua página de entrada tem um texto visível sem rolagem que diz o que o usuário encontra nela |
| Procedimento de cálculo | X = A / B, em que A = seções que atendem ao critério e B = 9 |
| Fonte dos dados | Planilha de inspeção com uma linha por seção, captura de tela da página de entrada e a decisão de cada avaliador |
| Procedimento de coleta | Dois avaliadores inspecionam as 9 páginas de entrada, de forma independente, no dispositivo do teste. Divergências são resolvidas por consenso, e a decisão final é registrada |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que todas as seções se apresentam ao usuário |

### M1.1.2: Acerto do primeiro clique

| Campo | Especificação |
|---|---|
| Questão | Q1.1 |
| Definição | Proporção de participantes cujo primeiro clique a partir da página Início leva à seção correta da tarefa. Mede se o usuário reconhece, pelo menu e pelos links, qual seção atende à sua necessidade |
| Procedimento de cálculo | Para cada tarefa, X = A / B, em que A = participantes cujo primeiro clique leva à seção correta e B = participantes |
| Fonte dos dados | Gravação da sessão e planilha de observação |
| Procedimento de coleta | O observador registra o destino do primeiro clique de cada participante em cada tarefa, conferindo depois na gravação |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. Não foi encontrada referência externa de limite: a interpretação é comparativa entre as tarefas |

### M1.2.1: Conclusão de tarefas sem ajuda

| Campo | Especificação |
|---|---|
| Questão | Q1.2 |
| Definição | Na ISO/IEC 25023, interface autoexplicativa: proporção de tarefas que um usuário de primeira vez conclui sem consultar ajuda ou documentação (ISO/IEC, 2011b). A tarefa é concluída quando o participante chega ao resultado esperado (dados do território em T1, camada visível em T2, arquivo baixado em T3) dentro do limite de tempo |
| Procedimento de cálculo | Para cada tarefa, X = A / B, em que A = participantes que concluem sem ajuda e B = participantes. Também é calculada a média das três tarefas |
| Fonte dos dados | Gravação da sessão e planilha de observação |
| Procedimento de coleta | O observador registra, para cada tarefa, se o participante concluiu, desistiu, estourou o limite ou recebeu ajuda |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. Referência externa: a taxa média de conclusão em testes de usabilidade é de cerca de 78% (SAURO; LEWIS, 2016) |

### M1.3.1: Eficiência do caminho

| Campo | Especificação |
|---|---|
| Questão | Q1.3 |
| Definição | Razão entre o número mínimo de passos para concluir a tarefa e o número de passos que o participante executou. Um passo é um clique, uma seleção em lista ou o preenchimento de um campo. O caminho mínimo de cada tarefa é definido pela equipe na Fase 3, a partir da página Início |
| Procedimento de cálculo | Para cada participante que concluiu a tarefa, e = passos mínimos / passos executados. X = média de e entre os participantes que concluíram |
| Fonte dos dados | Gravação da sessão |
| Procedimento de coleta | Um avaliador conta os passos de cada participante na gravação; um segundo avaliador confere a contagem |
| Unidade e escala | Razão de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que o participante seguiu o caminho mínimo; 0,5 significa que executou o dobro dos passos necessários |

!!! note "Tentativas não concluídas"
    A eficiência do caminho só é calculada para as tentativas concluídas, porque sem conclusão não
    há caminho completo para comparar. As tentativas não concluídas já são captadas por M1.2.1.

### M1.4.1: Prevenção de erros de operação

| Campo | Especificação |
|---|---|
| Questão | Q1.4 |
| Definição | Na ISO/IEC 25023, proporção de ações e entradas do usuário protegidas contra erro de operação (ISO/IEC, 2011b). Nesta avaliação, é a proporção de casos de entrada inválida que o portal bloqueia ou sinaliza antes de enviar os dados |
| Procedimento de cálculo | X = A / B, em que A = casos bloqueados ou sinalizados e B = casos executados |
| Fonte dos dados | Planilha de casos de teste, com o resultado de cada caso e captura de tela |
| Procedimento de coleta | Executar uma lista fixa de casos, definida na Fase 3. Exemplos no Fale Conosco: enviar com todos os campos vazios, e-mail sem "@", telefone com letras, mensagem vazia. Exemplos na Biblioteca Territorial e em Meu Território: buscar sem escolher a UF ou o território. Os casos são executados com a rede do navegador em modo offline (Chrome DevTools), para que nenhuma mensagem chegue ao MDA (Fase 1, seção 5.1); uma tentativa de envio registrada no painel Network conta como caso não bloqueado |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que nenhuma entrada inválida da lista chega a ser enviada |

### M1.4.2: Correção de erros de entrada

| Campo | Especificação |
|---|---|
| Questão | Q1.4 |
| Definição | Na ISO/IEC 25023, proporção de erros de entrada para os quais o sistema sugere uma correção (ISO/IEC, 2011b). Nesta avaliação, é a proporção de mensagens de erro que identificam o campo com problema **e** dizem o que é esperado nele |
| Procedimento de cálculo | X = A / B, em que A = mensagens que atendem aos dois requisitos e B = casos de M1.4.1 em que alguma mensagem foi exibida |
| Fonte dos dados | A mesma planilha de M1.4.1, com o texto de cada mensagem |
| Procedimento de coleta | Nas mesmas execuções de M1.4.1, dois avaliadores classificam cada mensagem de forma independente; divergências são resolvidas por consenso |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. Casos bloqueados sem nenhuma mensagem (por exemplo, botão desabilitado) entram em M1.4.1, mas não em M1.4.2 |

### M1.5.1: Pontuação SUS

| Campo | Especificação |
|---|---|
| Questão | Q1.5 |
| Definição | Percepção de usabilidade do participante, medida pelo *System Usability Scale*: questionário de 10 itens com respostas de 1 (discordo totalmente) a 5 (concordo totalmente) (BROOKE, 1996) |
| Procedimento de cálculo | Para cada participante: nos itens ímpares, subtrair 1 da resposta; nos pares, subtrair a resposta de 5; somar e multiplicar por 2,5. X = média das pontuações dos participantes |
| Fonte dos dados | Questionário SUS respondido por cada participante |
| Procedimento de coleta | Aplicado ao final da sessão, depois das três tarefas, em versão em português, sem ajuda do moderador |
| Unidade e escala | Pontos de 0 a 100; tratada como escala intervalar |
| Critério de interpretação | Quanto maior, melhor. Referências externas: a média de referência é 68 (SAURO; LEWIS, 2016); na escala de adjetivos, cerca de 51 corresponde a "OK", 71 a "bom" e 85 a "excelente" (BANGOR; KORTUM; MILLER, 2009) |

### M1.5.2: Nota de aparência

| Campo | Especificação |
|---|---|
| Questão | Q1.5 |
| Definição | Na ISO/IEC 25023, estética da aparência da interface: o quanto os usuários consideram a aparência agradável (ISO/IEC, 2011b). Medida por um item adicional, aplicado após o SUS: "A aparência das páginas é agradável e organizada", com respostas de 1 (discordo totalmente) a 5 (concordo totalmente) |
| Procedimento de cálculo | X = média das respostas dos participantes |
| Fonte dos dados | O mesmo formulário do SUS |
| Procedimento de coleta | Na mesma aplicação de M1.5.1 |
| Unidade e escala | Pontos de 1 a 5; escala ordinal tratada como intervalar |
| Critério de interpretação | Quanto maior, melhor. Acima de 3 (ponto neutro), a aparência é percebida como positiva |

### M1.6.1: Conformidade automática de acessibilidade

| Campo | Especificação |
|---|---|
| Questão | Q1.6 |
| Definição | Proporção das regras automáticas de acessibilidade aplicáveis à página que ela aprova. As regras são as do axe-core marcadas com os níveis A e AA da WCAG 2.1 (W3C, 2018), critérios que o eMAG, modelo de acessibilidade do governo federal, também segue (BRASIL, 2014) |
| Procedimento de cálculo | Para cada página, X = A / (A + B), em que A = regras aprovadas e B = regras violadas. Regras marcadas como "incompletas" (que exigem revisão manual) ficam fora do cálculo |
| Fonte dos dados | Relatório JSON do axe-core, campos `passes` e `violations` |
| Procedimento de coleta | Com a página totalmente carregada (o portal renderiza no navegador), executar o axe-core com as marcações `wcag2a`, `wcag2aa`, `wcag21a` e `wcag21aa` nas páginas Início, Meu Território, SITGeo, Biblioteca Territorial e Fale Conosco, registrando a versão do axe |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que a página não tem violações detectáveis automaticamente, o que não equivale a conformidade total, pois parte dos critérios exige avaliação manual |

### M1.6.2: Violações críticas e sérias

| Campo | Especificação |
|---|---|
| Questão | Q1.6 |
| Definição | Número de violações de acessibilidade que o axe-core classifica com impacto "crítico" ou "sério", ou seja, que bloqueiam ou dificultam muito o uso por pessoas com deficiência |
| Procedimento de cálculo | Para cada página, X = número de elementos com violação de impacto crítico ou sério |
| Fonte dos dados | O mesmo relatório JSON de M1.6.1, campo `violations` com `impact` igual a `critical` ou `serious` |
| Procedimento de coleta | As mesmas execuções de M1.6.1 |
| Unidade e escala | Contagem; escala absoluta |
| Critério de interpretação | Quanto menor, melhor. Qualquer violação crítica indica uma barreira que pode impedir o uso da página por parte do público |

---

## G2: Portabilidade

As métricas de G2 operacionalizam as medidas de adaptabilidade da ISO/IEC 25023 (ISO/IEC, 2011b).
Todas são coletadas pela equipe, sem participantes externos, seguindo as tarefas T1, T2 e T3 de
[G1](objetivos.md#g1-usabilidade).

| ID | Questão | Métrica (ISO/IEC 25023) | Operacionalização | Instrumento |
|---|---|---|---|---|
| M2.1.1 | Q2.1 | Adaptabilidade ao ambiente de software do sistema | Proporção de execuções (tarefa × ambiente) concluídas sem falha | Execução manual com roteiro |
| M2.2.1 | Q2.2 | Adaptabilidade ao ambiente de hardware | Proporção de combinações (página × largura de tela) sem rolagem horizontal | Chrome DevTools e inspeção visual |
| M2.2.2 | Q2.2 | Adaptabilidade ao ambiente de hardware | Proporção das funções do computador disponíveis no celular | Inspeção com lista de funções |
| M2.3.1 | Q2.3 | Falhas dependentes de ambiente | Número de falhas que só ocorrem em um ambiente, por gravidade | Registro de falhas |

### Condições comuns de coleta

Valem para todas as métricas de G2 e serão detalhadas no plano de avaliação da Fase 3:

- **Ambientes:** a matriz de navegadores, sistemas operacionais e larguras definida no
  [objetivo G2](objetivos.md#g2-portabilidade).
- **Ambiente de referência:** Chrome/Windows em 1366 px. Um comportamento é considerado falha
  quando difere do ambiente de referência a ponto de impedir ou prejudicar a tarefa.
- **Registro:** cada execução registra data e hora, versão do navegador e do sistema, largura da
  janela e se o dispositivo é real ou emulado, além de uma captura de tela do resultado.
- **Reprodução:** uma falha só é atribuída ao ambiente se for reproduzida em uma segunda execução,
  para separar problemas de ambiente de instabilidade da rede ou do servidor.
- **Zoom e orientação:** zoom de 100% e orientação retrato, salvo nos casos previstos na Fase 3.

### M2.1.1: Adaptabilidade ao ambiente de software

| Campo | Especificação |
|---|---|
| Questão | Q2.1 |
| Definição | Na ISO/IEC 25023, proporção de funções que podem ser concluídas em diferentes ambientes de software do sistema (ISO/IEC, 2011b). Nesta avaliação, os ambientes são as combinações de navegador e sistema operacional da matriz, e as funções são as tarefas T1, T2 e T3 |
| Procedimento de cálculo | Para cada ambiente, X = A / B, em que A = tarefas concluídas sem falha e B = 3. Também é calculado o valor geral, com todas as execuções da matriz |
| Fonte dos dados | Planilha de execuções, com o resultado de cada tarefa em cada ambiente e capturas de tela |
| Procedimento de coleta | Em cada ambiente, um avaliador executa T1, T2 e T3 seguindo o roteiro e o caminho mínimo de M1.3.1, com os mesmos território, camada e documento de referência |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que as três tarefas funcionam no ambiente |

### M2.2.1: Ausência de rolagem horizontal

| Campo | Especificação |
|---|---|
| Questão | Q2.2 |
| Definição | Proporção das combinações de página e largura de janela em que o conteúdo se ajusta à largura, sem exigir rolagem horizontal. Segue o critério de refluxo da WCAG 2.1 (critério 1.4.10), que exclui conteúdos que precisam de duas dimensões, como mapas (W3C, 2018). Por isso, a área do mapa do SITGeo não conta como rolagem horizontal |
| Procedimento de cálculo | X = A / B, em que A = combinações sem rolagem horizontal e B = 3 páginas × 5 larguras = 15 |
| Fonte dos dados | Planilha com o resultado de cada combinação e captura de tela |
| Procedimento de coleta | No modo de dispositivo do Chrome DevTools, ajustar a largura e carregar a página. No console, verificar se `document.documentElement.scrollWidth > document.documentElement.clientWidth`; se sim, confirmar visualmente qual elemento transborda |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que nenhuma página exige rolagem horizontal em nenhuma largura |

### M2.2.2: Funções disponíveis no celular

| Campo | Especificação |
|---|---|
| Questão | Q2.2 |
| Definição | Na ISO/IEC 25023, proporção de funções que podem ser concluídas em diferentes ambientes de hardware (ISO/IEC, 2011b). Nesta avaliação, é a proporção das funções que a página oferece no computador (1366 px) que continuam visíveis e operáveis no celular (360 px). Exemplos: filtros, abas de programas, controles do mapa, painel de camadas e legenda |
| Procedimento de cálculo | Para cada página, X = A / B, em que A = funções operáveis em 360 px e B = funções levantadas em 1366 px |
| Fonte dos dados | Lista de funções por página, com o resultado em cada largura e capturas de tela |
| Procedimento de coleta | Levantar as funções de cada página em 1366 px (lista fixada na Fase 3) e tentar usar cada uma em 360 px, no celular de referência |
| Unidade e escala | Proporção de 0 a 1; escala de razão |
| Critério de interpretação | Quanto maior, melhor. 1 significa que o celular oferece tudo o que o computador oferece |

### M2.3.1: Falhas dependentes de ambiente

| Campo | Especificação |
|---|---|
| Questão | Q2.3 |
| Definição | Número de falhas distintas que ocorrem em um ambiente e não ocorrem no ambiente de referência, classificadas por gravidade: **bloqueante** (impede a tarefa), **grave** (dificulta a tarefa, mas há contorno) e **cosmética** (não afeta a tarefa) |
| Procedimento de cálculo | Para cada ambiente, contagem de falhas por gravidade. A mesma falha em vários ambientes é contada uma vez em cada um |
| Fonte dos dados | Registro de falhas: ambiente, página, tarefa, gravidade, passos para reproduzir e captura de tela |
| Procedimento de coleta | Registrada durante as execuções de M2.1.1, M2.2.1 e M2.2.2, e confirmada pela segunda execução prevista nas condições comuns |
| Unidade e escala | Contagem por gravidade; escala absoluta |
| Critério de interpretação | Quanto menor, melhor. Ambientes com falha bloqueante ou grave são candidatos à matriz de testes do fornecedor; a prioridade entre eles considera a participação de mercado (STATCOUNTER, 2026) |

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

BANGOR, A.; KORTUM, P.; MILLER, J. Determining what individual SUS scores mean: adding an adjective rating scale. **Journal of Usability Studies**, v. 4, n. 3, p. 114-123, 2009.

BRASIL. Ministério do Planejamento, Orçamento e Gestão. **eMAG**: Modelo de Acessibilidade em Governo Eletrônico. Versão 3.1. Brasília: MP, 2014. Disponível em: <https://emag.governoeletronico.gov.br>. Acesso em: 20 out. 2026.

BROOKE, J. SUS: a "quick and dirty" usability scale. In: JORDAN, P. W. et al. (ed.). **Usability evaluation in industry**. London: Taylor & Francis, 1996. p. 189-194.

DEQUE SYSTEMS. **axe-core**: accessibility engine for automated web UI testing. [S.l.]: Deque Systems, 2026. Disponível em: <https://github.com/dequelabs/axe-core>. Acesso em: 20 out. 2026.

GOOGLE. **Minimize main-thread work**. [S.l.]: Google, 2019. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown>. Acesso em: 20 out. 2026.

GOOGLE. **First Contentful Paint (FCP)**. [S.l.]: Google, 2023a. Disponível em: <https://web.dev/articles/fcp>. Acesso em: 20 out. 2026.

GOOGLE. **Lighthouse variability**. [S.l.]: Google, 2023b. Disponível em: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md>. Acesso em: 20 out. 2026.

GOOGLE. **Largest Contentful Paint (LCP)**. [S.l.]: Google, 2025. Disponível em: <https://web.dev/articles/lcp>. Acesso em: 20 out. 2026.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC WD 25023**: systems and software engineering — systems and software quality requirements and evaluation (SQuaRE) — measurement of system and software product quality. Working Draft, version 0.1.0. Genebra: ISO, 2011b.

NIELSEN, J. **Usability engineering**. Boston: Academic Press, 1993.

NIELSEN, J. **Why you only need to test with 5 users**. [S.l.]: Nielsen Norman Group, 2000. Disponível em: <https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/>. Acesso em: 20 out. 2026.

SAURO, J.; LEWIS, J. R. **Quantifying the user experience**: practical statistics for user research. 2. ed. Cambridge: Morgan Kaufmann, 2016.

STATCOUNTER. **Browser market share Brazil**. [S.l.]: StatCounter Global Stats, 2026. Disponível em: <https://gs.statcounter.com/browser-market-share/all/brazil>. Acesso em: 20 out. 2026.

WORLD WIDE WEB CONSORTIUM. **Web Content Accessibility Guidelines (WCAG) 2.1**. [S.l.]: W3C, 2018. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: 20 out. 2026.
