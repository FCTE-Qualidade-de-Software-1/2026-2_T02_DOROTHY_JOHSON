# Relações entre as características

Esta discussão cruza os resultados de capacidade de interação (G1), flexibilidade (G2) e
eficiência de desempenho (G3), conforme a
[issue #80](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/80).
O objetivo é apoiar as três decisões do requisitante na
[Fase 1](../fase-1/index.md#12-requisitante-e-objetivo): redesenho de interface, otimização
de desempenho e cobertura de ambientes de teste.

## 1. Critério de cruzamento e evidências

!!! note "Base adotada"
    O cruzamento usa os resultados versionados até 24/11/2026: G1 com o relatório encerrado
    com ressalvas (P01–P04), G2 com a matriz completa e a conferência no aparelho, e G3 com a
    coleta de 08/11. As classificações são as da [classificação final](classificacao-final.md).
    As falhas F02 e F03 do SITGeo, observadas na emulação de 15/11 e não confirmadas no
    aparelho, são citadas apenas como observações da emulação.

O cruzamento usa a mesma página ou tarefa como unidade de comparação, mantendo os objetos de
referência da [Fase 3](../fase-3/ambiente.md#2-paginas-tarefas-e-objetos-de-referencia).
São distinguidos três tipos de afirmação:

- **Achado observado:** resultado medido ou falha reproduzida no ambiente declarado.
- **Coocorrência:** problemas de características diferentes encontrados na mesma página,
  em coletas distintas. Não demonstra que um problema causou o outro.
- **Hipótese de efeito na interação:** consequência possível para o uso, examinada contra as
  observações de G1, que podem apoiá-la, contrariá-la ou não ter dados suficientes.

| Base | Evidência disponível | Limite para o cruzamento |
|---|---|---|
| [Eficiência de desempenho](eficiencia.md), coleta de 08/11 | Medianas de 5 execuções de FCP, LCP, CPU, tempos de T1/T2 e memória; dados em `data/fase-4/eficiencia/` | Perfil móvel simulado; não mede a percepção, o caminho ou a conclusão sem ajuda de usuários |
| [Flexibilidade](flexibilidade.md), emulação de 15/11 e matriz manual até 24/11 | Rolagem e funções em 5 larguras; 18/18 tarefas em seis ambientes; falhas F01 e F04 reproduzidas; `execucoes.csv`, `rolagem.csv`, `funcoes.csv`, `falhas.csv` e capturas em `data/fase-4/flexibilidade/` | Conferência das funções do SITGeo em 384 px, com data e versão de navegador diferentes da emulação de 360 px |
| [Análise de G1](interacao.md), sessões de 22 a 24/11 | Primeiro clique, conclusão, passos, SUS, aparência e acessibilidade automática; observações de T2/T3 preservadas | Amostra de 4/5; recortes NC em T2/T3 por ponto de partida divergente; sessões em celulares e navegadores diferentes, sem versões registradas em parte delas |
| [Ação de melhoria](acao-melhoria.md#52-efeito-medido), medição de 14/11 | Comparação antes/depois da troca de duas imagens do SITGeo | Demonstração local; não houve implantação no portal nem reavaliação de G1 ou G2 |

*Tabela 1: Fontes e limites da análise conjunta.*

## 2. Flexibilidade × eficiência de desempenho

| Página | Flexibilidade (resultado adotado em 24/11) | Desempenho medido em 08/11 | O que o cruzamento permite afirmar |
|---|---|---|---|
| Meu Território | 12/12 funções preservadas em 360 px; sem rolagem horizontal nas 5 larguras | LCP de 8,27 s e resposta de T1 de 20,39 s | A preservação das funções na tela estreita pode coexistir com lentidão; o resultado de G2 não assegura bom desempenho |
| SITGeo | 6/6 funções após a conferência no aparelho; sem rolagem horizontal; F02/F03 observadas só na emulação | LCP de 23,45 s, CPU de 8,26 s e resposta de T2 de 6,45 s | A página com o pior desempenho não tem perda de função confirmada; o resultado de G2 não assegura bom desempenho |
| Biblioteca Territorial | 6/7 funções; setas da Mapoteca fora da tela (F01); rolagem horizontal em 360 e 412 px; tabela de PTDRS cortada em celulares (F04) | LCP de 3,91 s, o menor das 3 páginas | Uma página pode carregar mais rapidamente que as demais e ainda concentrar as barreiras de adaptação à tela |

*Tabela 2: Cruzamento por página de M2.2.1/M2.2.2 com M3.1.2, M3.2.1 e M3.3.1.*

As duas características se distribuem de forma oposta entre as páginas. O SITGeo concentra
os piores valores de LCP e CPU de G3, mas não tem perda de função confirmada em G2. A
Biblioteca tem o menor LCP e concentra as duas falhas contadas em G2 (F01 e F04) e a
rolagem horizontal. Não há, portanto, coocorrência confirmada de perda de funções e
lentidão na mesma página. O diagnóstico da
[ação de melhoria](acao-melhoria.md#2-justificativa-o-que-as-medidas-mostram) atribui a
maior parcela do LCP do SITGeo à transferência de imagens, causa que não envolve o layout.

Os resultados das três páginas reforçam a necessidade de avaliar as duas
características separadamente. Os dados disponíveis **não estabelecem uma relação geral ou
estatística entre adaptabilidade e desempenho**: há apenas três páginas, medidas em datas,
larguras e versões de navegador diferentes. A comparação é descritiva, por página; não é um
experimento que isola o efeito do tamanho da tela sobre o desempenho.

## 3. Flexibilidade × capacidade de interação

As falhas F01 e F04 documentam barreiras de acesso a controles e conteúdo da Biblioteca em
celulares. F02 e F03, observadas no SITGeo apenas na emulação, ficam como hipóteses
secundárias. A tabela compara cada achado com as observações das sessões de G1
([seção 1.1 da análise de G1](interacao.md#11-observacoes-de-t2-e-t3-preservadas-no-encerramento)):

| Achado de G2 | Hipótese de efeito na interação | O que G1 mostrou | Situação da hipótese |
|---|---|---|---|
| F04: tabela de PTDRS cortada em três ambientes móveis (Biblioteca) | A leitura da tabela pode dificultar a obtenção do documento em T3 | P03 obteve o PTDRS sem ajuda registrada e P02 com dicas; P01 não acessou a Biblioteca e P04 baixou a imagem do mapa em vez do documento | Sem dados suficientes: as dificuldades observadas ocorreram antes da tabela ou em outro fluxo, e T3 é NC em M1.2.1 |
| F01: setas da Mapoteca fora da tela (BIB-05) | O acesso ao carrossel pode exigir ações adicionais ou passar despercebido | T3 busca o PTDRS por outro fluxo; as sessões não registram uso do carrossel | Sem dados: a tarefa não testa essa hipótese |
| F02/F03: zoom e dados da camada cobertos no SITGeo (só na emulação) | A dificuldade de identificar a camada pode prejudicar a conclusão de T2 | P01, P02 e P03 permaneceram em Meu Território, na aba Crédito Rural, sem chegar ao SITGeo; P04 ativou a camada | Não apoiada: as dificuldades de T2 ocorreram na escolha da seção, antes do SITGeo |

*Tabela 3: Barreiras de adaptação e o que as sessões de G1 permitem verificar.*

O principal obstáculo observado em T2 é de **navegação entre seções**, não de adaptação à
tela: três participantes buscaram a camada em Meu Território. Isso é coerente com o primeiro
clique de T2 (0/1 na observação válida) e com o SUS de 50, mas não se relaciona com as falhas
de G2. No Procedimento B, T2 foi executada pelo script sem clique forçado. **O sucesso da
automação não permite concluir que um usuário de primeira vez encontre e ative a camada sem
ajuda**, como as sessões de G1 confirmam.

Também não se deve atribuir a F03 um efeito sobre M1.1.2: essa métrica conta o primeiro
clique a partir da página Início, anterior à escolha da camada. Da mesma forma, sobreposição
e rolagem não substituem as medições de acessibilidade M1.6.1 e M1.6.2. A Biblioteca, porém,
concentra tanto as falhas de G2 quanto o maior número de elementos críticos e sérios de
M1.6.2 (6 críticos e 33 sérios), o que é uma **coocorrência** relevante para priorizar a
página, sem relação causal demonstrada.

## 4. Eficiência de desempenho × capacidade de interação

Em Meu Território, o FCP de 1,56 s contrasta com o LCP de 8,27 s e a resposta de T1 de
20,39 s. No SITGeo, o FCP é de 1,60 s, mas o LCP chega a 23,45 s, com 8,26 s de CPU no
carregamento. Esses resultados mostram que a primeira exibição da página não representa a
disponibilidade rápida de seu conteúdo principal.

**Hipótese a verificar:** a espera pode levar participantes a repetir ações, procurar outro
caminho, pedir ajuda ou desistir, com possível repercussão em M1.2.1 e M1.5.1. Essa hipótese
exige gravações e registros que situem a dificuldade no período de espera; a lentidão, por
si só, não confirma que qualquer desses comportamentos ocorreu. As sessões de G1 não isolam
o período de espera: em T1, a tarefa mais lenta de G3, os quatro participantes concluíram sem
ajuda (M1.2.1 = 4/4), com eficiência média do caminho de 0,5148. **A hipótese permanece sem
dados suficientes**; a associação descritiva não separa a lentidão de fatores como clareza dos
rótulos, familiaridade digital e adaptação do layout.

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

- **Cobertura de G1:** o relatório foi encerrado com ressalvas, com 4/5 participantes,
  recortes NC em T2/T3 e classificação global NC. As hipóteses que dependem de T2/T3 ficam
  sem dados suficientes; não são confirmadas nem descartadas pela ausência de observação.
- **Coletas distintas:** G3 foi medido em 08/11, G2 entre 15/11 e 24/11 e G1 entre 22 e
  24/11, com versões de navegador e perfis diferentes. O portal não informa versão e pode ter mudado entre as coletas.
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
carregamento do SITGeo**, além de **corrigir a tabela de PTDRS e as setas da Mapoteca na
Biblioteca em celulares**. As sessões de G1 sustentam investigar a distinção entre Meu
Território e o SITGeo no fluxo de T2. O efeito das correções sobre a percepção de usuários
de primeira vez não foi medido e depende de uma futura avaliação.
Melhorar o desempenho e adaptar a interface são frentes complementares; nenhuma das duas
dispensa a verificação da outra.

As classificações continuam separadas, como definido nos
[critérios da Fase 2](../fase-2/niveis-pontuacao.md#53-da-pontuacao-a-decisao-de-qualidade).
O cruzamento não cria uma nota global do SIT. As classificações por característica estão na
[classificação final](classificacao-final.md), e as ações priorizadas, nas
[oportunidades de melhoria](oportunidades-melhoria.md).
