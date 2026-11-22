# Relações entre as características

Esta discussão cruza os resultados de capacidade de interação (G1), flexibilidade (G2) e
eficiência de desempenho (G3), conforme a
[issue #80](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/80).
O objetivo é apoiar as três decisões do requisitante na
[Fase 1](../fase-1/index.md#12-requisitante-e-objetivo): redesenho de interface, otimização
de desempenho e cobertura de ambientes de teste.

## 1. Critério de cruzamento e evidências

O cruzamento usa a mesma página ou tarefa como unidade de comparação, mantendo os objetos de
referência da [Fase 3](../fase-3/ambiente.md#2-paginas-tarefas-e-objetos-de-referencia).
São distinguidos três tipos de afirmação:

- **Achado observado:** resultado medido ou falha reproduzida no ambiente declarado.
- **Coocorrência:** problemas de características diferentes encontrados na mesma página,
  em coletas distintas. Não demonstra que um problema causou o outro.
- **Hipótese de efeito na interação:** consequência possível para o uso, ainda sem
  confirmação pelos resultados de G1.

| Base | Evidência disponível | Limite para o cruzamento |
|---|---|---|
| [Eficiência de desempenho](eficiencia.md), coleta de 08/11 | Medianas de 5 execuções de FCP, LCP, CPU, tempos de T1/T2 e memória; dados em `data/fase-4/eficiencia/` | Perfil móvel simulado; não mede a percepção, o caminho ou a conclusão sem ajuda de usuários |
| [Flexibilidade](flexibilidade.md), coleta de 15/11 | 2 execuções por combinação e função; `rolagem.csv`, `funcoes.csv`, `falhas.csv` e capturas em `data/fase-4/flexibilidade/` | Resultados em emulação; `execucoes.csv` ainda não contém resultados da matriz manual |
| [Plano de G1](../fase-3/index.md#3-rastreabilidade-da-fase-2-para-a-fase-3) | Métricas e procedimentos especificados para primeiro clique, conclusão, passos, percepção e acessibilidade | Especificação de coleta não constitui resultado; faltam dados para confirmar relações com G1 |
| [Ação de melhoria](acao-melhoria.md#52-efeito-medido), medição de 14/11 | Comparação antes/depois da troca de duas imagens do SITGeo | Demonstração local; não houve implantação no portal nem reavaliação de G1 ou G2 |

*Tabela 1: Fontes e limites da análise conjunta.*

## 2. Flexibilidade × eficiência de desempenho

| Página | Flexibilidade observada em 15/11 | Desempenho medido em 08/11 | O que o cruzamento permite afirmar |
|---|---|---|---|
| Meu Território | 12/12 funções preservadas em 360 px; sem rolagem horizontal nas 5 larguras | LCP de 8,27 s e resposta de T1 de 20,39 s | A preservação das funções na tela estreita pode coexistir com lentidão; o resultado de G2 não assegura bom desempenho |
| SITGeo | 4/6 funções preservadas em 360 px; nome e dados das camadas e botões de zoom cobertos (F02/F03); sem rolagem horizontal | LCP de 23,45 s, CPU de 8,26 s e resposta de T2 de 6,45 s | Há coocorrência de perdas de funções e lentidão na mesma página; a ausência de rolagem não garante acesso aos controles |
| Biblioteca Territorial | 6/7 funções preservadas em 360 px; setas da Mapoteca fora da tela; rolagem horizontal em 360 e 412 px (F01) | LCP de 3,91 s, o menor das 3 páginas | Uma página pode carregar mais rapidamente que as demais e ainda apresentar barreira de adaptação à tela |

*Tabela 2: Cruzamento por página de M2.2.1/M2.2.2 com M3.1.2, M3.2.1 e M3.3.1.*

O SITGeo concentra os piores valores de LCP e CPU de G3 e duas das três falhas distintas
registradas em G2. Essa convergência sustenta a recomendação de tratar tanto o carregamento
quanto o layout móvel da página. Entretanto, **não demonstra que a perda de funções seja
causada pela lentidão**, nem que corrigir o layout reduza o tempo de carregamento. A análise
de G2 localiza sobreposições na grade mantida em telas estreitas, enquanto o diagnóstico da
[ação de melhoria](acao-melhoria.md#2-justificativa-o-que-as-medidas-mostram) identifica a
transferência de imagens como a maior parcela do LCP do SITGeo.

Os resultados de Meu Território e da Biblioteca reforçam a necessidade de avaliar as duas
características separadamente. Os dados disponíveis **não estabelecem uma relação geral ou
estatística entre adaptabilidade e desempenho**: há apenas três páginas, medidas em datas,
larguras e versões de navegador diferentes. A comparação é descritiva, por página; não é um
experimento que isola o efeito do tamanho da tela sobre o desempenho.

## 3. Flexibilidade × capacidade de interação

As falhas F01 a F03 documentam barreiras concretas de acesso a conteúdo e controles na
emulação móvel. Sua possível repercussão na capacidade de interação deve ser examinada nas
sessões de G1:

| Achado de G2 | Hipótese de efeito na interação | Evidência necessária em G1 |
|---|---|---|
| F03: nome, fonte e unidade das camadas cobertos no SITGeo (GEO-04) | A dificuldade de identificar a camada pode prejudicar a conclusão de T2 ou exigir mais passos | Conclusão sem ajuda (M1.2.1), eficiência do caminho nas tentativas concluídas (M1.3.1) e gravação que mostre a dificuldade de localizar a camada |
| F02: botões de zoom cobertos no SITGeo (GEO-05) | O usuário pode ter dificuldade para explorar o mapa ou precisar recorrer ao gesto de pinça | Observação de tentativas de usar o zoom, quando ocorrerem; ativar a camada em T2 não exige necessariamente usar esses botões |
| F01: setas da Mapoteca fora da tela (BIB-05) | O acesso ao carrossel pode exigir ações adicionais ou passar despercebido | Observação específica do carrossel; T3 busca um PTDRS por outro fluxo e, sozinha, não testa essa hipótese |

*Tabela 3: Barreiras observadas de adaptação e efeitos sobre a interação ainda não medidos.*

No Procedimento B, T2 pôde ser executada pelo script sem clique forçado, embora o SITGeo
tenha perdido duas funções em 360 px. Isso mostra o limite de considerar apenas a conclusão
técnica: o controle para ativar a camada pode continuar acessível enquanto o texto necessário
para escolhê-la fica coberto. **O sucesso da automação não permite concluir que um usuário
de primeira vez consiga identificar e ativar a camada sem ajuda.**

Também não se deve atribuir automaticamente a F03 um efeito sobre M1.1.2: essa métrica conta
o primeiro clique a partir da página Início, anterior à escolha da camada. O vínculo mais
direto a verificar está na conclusão e no caminho de T2. Da mesma forma, sobreposição e
rolagem não substituem as medições de acessibilidade M1.6.1 e M1.6.2, nem permitem antecipar
seus níveis ou afirmar conformidade completa com WCAG/eMAG.

## 4. Eficiência de desempenho × capacidade de interação

Em Meu Território, o FCP de 1,56 s contrasta com o LCP de 8,27 s e a resposta de T1 de
20,39 s. No SITGeo, o FCP é de 1,60 s, mas o LCP chega a 23,45 s, com 8,26 s de CPU no
carregamento. Esses resultados mostram que a primeira exibição da página não representa a
disponibilidade rápida de seu conteúdo principal.

**Hipótese a verificar:** a espera pode levar participantes a repetir ações, procurar outro
caminho, pedir ajuda ou desistir, com possível repercussão em M1.2.1 e M1.5.1. Essa hipótese
exige gravações e registros que situem a dificuldade no período de espera; a lentidão, por
si só, não confirma que qualquer desses comportamentos ocorreu. Mesmo após a coleta de G1,
uma associação descritiva não isolará a lentidão de fatores como clareza dos rótulos,
familiaridade digital e adaptação do layout.

Há três cuidados para interpretar o cruzamento:

1. **M3.2.1 não mede a sessão inteira de G1.** O tempo começa no clique que dispara a
   operação e termina pelo critério de ociosidade de rede; G1 começa na página Início e
   observa a conclusão sem ajuda. Não se devem somar LCP e tempo de tarefa para estimar a
   duração total da sessão.
2. **M1.3.1 conta passos, não segundos.** Esperar sem executar ações não reduz essa razão.
   Só haverá repercussão no caminho se forem observados passos adicionais, e a métrica é
   calculada apenas nas tentativas concluídas.
3. **O SUS é aplicado após as três tarefas.** Seu resultado expressa a percepção da sessão;
   não permite atribuir uma nota baixa exclusivamente à lentidão de T1 ou do SITGeo.

## 5. O que a ação de melhoria permite concluir

Na comparação local da troca das imagens, o LCP do SITGeo passou de 26,45 s para 1,87 s e
o peso da página de 5 338 para 1 033 kB (medianas de 5 execuções por condição). Essa evidência
sustenta a otimização das imagens no cenário testado, conforme as ressalvas da
[ação de melhoria](acao-melhoria.md#52-efeito-medido).

O resultado **não demonstra melhora da capacidade de interação ou da flexibilidade**: não
houve novas sessões com usuários, verificação de funções ou teste de layout depois da troca.
A demonstração altera duas imagens, e não os controles sobrepostos. Além disso, foi usado o
modo local com transferência simulada, em outra máquina e com outro instrumento; o resultado
não substitui o LCP de 23,45 s de G3 nem altera sua classificação final.

## 6. Limitações e implicações para a decisão

As principais limitações do cruzamento são:

- **Cobertura incompleta:** G1 ainda não tem resultados publicados; G2 permanece parcial,
  sem a matriz manual e sem confirmação das perdas no celular real. Não se antecipam as
  classificações dessas características nem se confirmam hipóteses apenas pela ausência de dados.
- **Coletas distintas:** G3 foi medido em 08/11 e G2 em 15/11, com versões de navegador e
  perfis diferentes. O portal não informa versão e pode ter mudado entre as coletas.
- **Unidades e alcances diferentes:** tempo de resposta, disponibilidade de função,
  conclusão por usuário e percepção de uso não são medidas intercambiáveis. As repetições
  técnicas não são participantes independentes e não demonstram causalidade entre atributos.
- **Tarefas e controles diferentes:** G3 não mede o tempo de T3; os resultados de G2 na
  Biblioteca incluem o carrossel, que não é o fluxo do PTDRS. Não se deve estender o achado
  de uma função a toda a página ou a todas as tarefas.
- **Observação externa:** sem código e dados internos do portal, não é possível atribuir
  uma causa comum aos problemas de layout, CPU e resposta do servidor. Também não há base
  para relações com características excluídas, como segurança ou confiabilidade.

Para as decisões da Fase 1, os dados sustentam **investigar a resposta de T1 e otimizar o
carregamento do SITGeo**, além de **corrigir e confirmar as perdas de funções no layout
móvel do SITGeo e da Biblioteca**. A necessidade de redesenhar os fluxos por dificuldade de
usuários de primeira vez e o efeito das correções sobre sua percepção dependem de G1.
Melhorar o desempenho e adaptar a interface são frentes complementares; nenhuma das duas
dispensa a verificação da outra.

As classificações continuam separadas, como definido nos
[critérios da Fase 2](../fase-2/niveis-pontuacao.md#53-da-pontuacao-a-decisao-de-qualidade).
O cruzamento não cria uma nota global do SIT. Quando G1 e a matriz de G2 forem publicados,
esta discussão deve ser atualizada com as evidências correspondentes, registrando quais
hipóteses receberam apoio, quais foram contrariadas e quais continuam sem dados suficientes.
