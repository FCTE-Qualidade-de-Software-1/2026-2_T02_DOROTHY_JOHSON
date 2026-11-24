# Classificação final e coerência com o propósito da F1

Esta página consolida a decisão de qualidade por característica e a contribuição dos
resultados para o requisitante, atendendo aos critérios F4-C4 e F4-C5 da
[issue #79](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/79).
A base é a avaliação versionada até 24/11/2026: análises de
[capacidade de interação](interacao.md), [flexibilidade](flexibilidade.md) e
[eficiência de desempenho](eficiencia.md). Não houve nova coleta para esta síntese.

**Resultado:** flexibilidade **Bom (2,21)**; eficiência de desempenho **Aceitável (1,35)**;
capacidade de interação **sem classificação global calculável (NC), com relatório encerrado com ressalvas**, com barreiras críticas
já registradas que exigem tratamento prioritário. Não se atribui uma nota única ao SIT.

## 1. Aplicação dos critérios da F2

Aplicam-se os [critérios da F2](../fase-2/niveis-pontuacao.md#5-criterios-de-classificacao-por-caracteristica):
pontuar cada recorte, calcular a média dos pontos por métrica, a média das métricas por
questão e a média das questões por característica. Não há arredondamento intermediário.
Os intervalos são: Insatisfatório, de 0 a menos de 1; Aceitável, de 1 a menos de 2;
Bom, de 2 a menos de 2,75; Excelente, de 2,75 a 3. Esses cortes são critérios internos
da equipe, não limites normativos da ISO.

Depois da média, aplicam-se os limitadores de gravidade. Coleta obrigatória ausente ou
recorte NC impede a classificação final, observadas as exceções expressas na F2.
Os pesos de seleção das características usados na F1 não são pesos para agregar notas.

| Característica | Média das questões | Classe pela média | Limitador e cobertura | Classificação final |
|---|---|---|---|---|
| **G1 — Capacidade de interação** | NC: Q1.1–Q1.3 incompletas; Q1.4 = 2,00, Q1.5 = 1,00, Q1.6 = 0,90 | Não calculável | Violações críticas em cinco páginas; T2 com 0/1 conclusão válida. Há quatro recortes NC e amostra de 4/5 | **NC — relatório encerrado com ressalvas** |
| **G2 — Flexibilidade** | (3 + 11/6 + 9/5) / 3 = 199/90 ≈ **2,21** | **Bom** | Matriz completa; nenhuma bloqueante dependente de ambiente reproduzida; limitador não acionado | **Bom** |
| **G3 — Eficiência de desempenho** | (7/6 + 1/2 + 4/3 + 12/5) / 4 = **1,35** | **Aceitável** | LCP > 4 s em Meu Território e SITGeo; T1 > 10 s; teto Aceitável acionado | **Aceitável** |

*Tabela 1: Classificação, cobertura e limitadores. Valores conferíveis em
[`classificacao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/consolidado/classificacao.csv)
e [`medidas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/consolidado/medidas.csv).*

### 1.1 G1: relatório encerrado com ressalvas e ação já justificada

O SUS médio de **50/100** está no nível Insatisfatório; a aparência média de **4,25/5**
está no nível Bom. Assim, a avaliação visual positiva não permite concluir que o portal
é fácil de usar. Em T1, 4/4 concluíram sem ajuda, mas a eficiência média do caminho foi
0,5148 (Aceitável). T2 tem apenas uma observação iniciada em Início, sem conclusão sem
ajuda; T3 não tem observação válida com esse ponto de partida.

Os quatro recortes NC são M1.1.2/T3, M1.2.1/T3 e M1.3.1/T2–T3. A amostra é de quatro
dos cinco participantes previstos. Não se usa a média das três questões disponíveis
como se fosse G1 completo.

| Página | Elementos críticos | Elementos sérios |
|---|---:|---:|
| Início | 3 | 4 |
| Meu Território | 3 | 4 |
| SITGeo | 1 | 4 |
| Biblioteca Territorial | 6 | 33 |
| Fale Conosco | 1 | 4 |

*Tabela 2: Elementos distintos por gravidade de M1.6.2, conforme a
[análise de G1](interacao.md#acessibilidade-automatica) e os
[relatórios axe](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/capacidade-de-interacao/axe).*

As violações críticas acionam a regra que leva G1 a **Insatisfatório**, independentemente
da média, quando a classificação puder ser concluída com coleta válida. O estado formal
atual permanece pendente, coerente com o consolidado e a análise de G1: existem desvios
nas condições da inspeção e lacunas em outras métricas obrigatórias. A exceção da F2
para tarefa sem nenhuma conclusão não resolve a falta de observações válidas de T3.
Isso não justifica adiar a investigação e a correção das barreiras registradas.

A equipe encerrou a rodada com os quatro participantes disponíveis, sem possibilidade
de repetir as sessões. As conclusões observadas de T2/T3 e as intervenções da moderação
são descritas na [análise de G1](interacao.md#11-observacoes-de-t2-e-t3-preservadas-no-encerramento).
O relatório está concluído com ressalvas, mas a nota global não é calculável. O CSV
mantém o estado técnico `pendente` pela regra de cobertura da F2; isso não indica
recrutamento ou repetição agendados. As medidas parciais e as decisões justificadas
permanecem utilizáveis dentro dos limites registrados.

### 1.2 G2: Bom, com problemas localizados em celulares

As **18/18 tarefas** foram concluídas em Chrome/Android, Samsung Internet/Android,
Safari/iOS e Chrome, Edge e Firefox no Windows. Isso sustenta Q2.1 = 3,00.
A Biblioteca exige rolagem horizontal em 360 e 412 px: M2.2.1 = 13/15 combinações sem
rolagem, Aceitável (1). As funções preservadas são 12/12 em Meu Território, 6/6 no
SITGeo após conferência no aparelho e 6/7 na Biblioteca, que perde as setas da Mapoteca.

Em M2.3.1, Chrome/Android tem duas falhas graves reproduzidas e Samsung Internet e
Safari têm uma cada; Edge e Firefox no Windows não tiveram falhas registradas. São
F01 (Mapoteca) e F04 (tabela de PTDRS), ambas na Biblioteca. A ausência de bloqueantes
mantém a classe **Bom**, mas não elimina a necessidade de corrigir esses recortes.

A conferência das funções do SITGeo foi feita em 384 px, em outra data e versão do
navegador que a emulação de 360 px. Essa divergência permanece como limitação; a
reintegração segue a regra da F3. A [análise de G2](flexibilidade.md) descreve os cálculos,
as capturas e a deduplicação das falhas.

### 1.3 G3: Aceitável, com atraso em fluxos essenciais

As medianas de cinco execuções mostram LCP de **23,45 s no SITGeo** e **8,27 s em Meu
Território**, ambos Insatisfatórios. A consulta T1 demora **20,39 s**, também
Insatisfatório. Esses três recortes acionam o teto Aceitável. T2 demora 6,45 s e o
carregamento do SITGeo ocupa 8,26 s da thread principal; a primeira exibição rápida
(FCP entre 1,56 e 1,60 s) não representa disponibilidade do conteúdo principal.

A classe **Aceitável** expressa atendimento parcial aos critérios da equipe, com ação
necessária nos atrasos. Os resultados representam o perfil móvel simulado da coleta,
não todos os aparelhos ou conexões reais. A [análise de G3](eficiencia.md) apresenta os
valores brutos, a dispersão e os limites do instrumento.

## 2. Coerência com o propósito e o uso pretendido da F1

A [F1, seção 1.2](../fase-1/index.md#12-requisitante-e-objetivo), define o **MDA como
requisitante simulado**, o propósito de **indicar pontos de melhoria no produto** e o uso
dos resultados para **priorizar o backlog de evolução**. A pergunta é quais problemas
mais dificultam o acesso às informações territoriais e devem ser tratados primeiro.

| Decisão prevista na F1 | Evidência produzida pela avaliação | Contribuição ao propósito e limite |
|---|---|---|
| **1. Interface e fluxos de navegação** | SUS 50; caminho de T1 = 0,5148; dificuldades em T2 na observação válida; elementos críticos nas cinco páginas e 39 elementos críticos/sérios na Biblioteca | Sustenta investigar barreiras, corrigir elementos inacessíveis e revisar o fluxo de escolha de camadas. O redesenho de T2/T3 e seu efeito no uso sem ajuda ainda dependem de sessões válidas adicionais |
| **2. Desempenho em condições reais de acesso** | LCP SITGeo = 23,45 s; LCP Meu Território = 8,27 s; T1 = 20,39 s; CPU SITGeo = 8,26 s, no perfil móvel simulado | Sustenta investir em carregamento de páginas/mapas e investigar a consulta de território. O perfil simulado aproxima o contexto da F1; não comprova tempos em todas as redes rurais |
| **3. Cobertura de ambientes** | 18/18 conclusões em seis ambientes; rolagem em 360/412 px; F01/F04 em celulares; referência Chrome/Windows a 1366 px | Define casos de regressão reproduzíveis para celulares e Windows. A conclusão técnica da tarefa não elimina perda de controles ou conteúdo cortado |

*Tabela 3: Rastreabilidade F1 → evidência F4 → decisão do requisitante.*

Para colegiados e agentes territoriais, os resultados localizam atrasos na consulta e no
mapa; para gestores e organizações sociais, identificam dificuldade de leitura da tabela
de documentos; para agricultores e cidadãos, apontam barreiras no uso pelo celular e
na acessibilidade. Para a equipe de TI, fornecem métricas, ambientes e passos de reprodução.
Essas ligações correspondem às necessidades da [F1, seção 2](../fase-1/index.md#2-stakeholders).
Não foi medido o efeito das correções sobre esses públicos.

**O propósito de indicar melhorias é atendido pela evidência disponível:** existem
problemas localizados e ações justificadas para as três decisões. **O relatório é encerrado com ressalvas em G1**,
aceitando a amostra de quatro participantes e os desvios documentados, sem atribuir
nota global aos recortes que não permitem esse cálculo. Apoiar decisões de backlog não equivale a demonstrar
que as melhorias foram implantadas ou que todos os critérios de sucesso do público foram atingidos.

## 3. Decisões apoiadas para o requisitante

A tabela abaixo distingue decisões já sustentadas de verificações necessárias para
aceitar sua resolução. Ela complementa a [lista de oportunidades](oportunidades-melhoria.md),
cuja priorização histórica ainda precisa incorporar os achados de G1 e F04.

| Decisão recomendada ao MDA | Evidência e prioridade | Verificação para aceitar a melhoria |
|---|---|---|
| **Tratar barreiras críticas de acessibilidade nas cinco páginas**, com atenção à Biblioteca | M1.6.2: ao menos um elemento crítico por página; Biblioteca com 6 críticos e 33 sérios. Prioridade de barreira crítica pela F2 | Confirmar as ocorrências nas condições planejadas, corrigir elementos identificados nos JSONs, repetir o axe e complementar com inspeção manual; aprovação automática não certifica WCAG/eMAG |
| **Investigar a consulta de território T1 e otimizar o carregamento do SITGeo e de Meu Território** | T1 = 20,39 s; LCP = 23,45 s e 8,27 s; recortes Insatisfatórios que acionam o teto de G3 | Repetir o método de G3 com cinco execuções; LCP ≤ 4 s nas duas páginas e T1 ≤ 10 s retiram esses gatilhos, mas a classe deve ser recalculada |
| **Avaliar a implantação da otimização de imagens já demonstrada localmente** | A [ação de melhoria](acao-melhoria.md#52-efeito-medido) reduziu o LCP de 26,45 s para 1,87 s na demonstração local | Revisar e implantar pelo fornecedor, depois medir em produção com o método de G3; o ensaio local não altera o LCP oficial de 23,45 s |
| **Corrigir a tabela de PTDRS e as setas da Mapoteca em celulares** | F04 em três ambientes móveis e F01 no Chrome/Android; problemas de leitura e controle mesmo com T3 concluída | Repetir os passos das falhas em 384/440 px e a inspeção de 360/412 px; tabela legível, setas operáveis e recálculo de M2.2.1/M2.2.2/M2.3.1 |
| **Manter os seis ambientes e acrescentar os casos de falha à regressão** | G2 Bom não elimina recortes Aceitáveis; falhas concentradas em telas de celular | T1–T3 em cada ambiente, rolagem nas cinco larguras e funções móveis comparadas à referência, com versões e capturas; repetir F05 antes de pontuá-la |
| **Usar as observações de G1 para investigar os fluxos de primeira utilização** | 4/5 participantes; T2/T3 com pontos de partida divergentes; SUS baixo sem isolamento da causa | Em futura avaliação do fornecedor, observar o uso após as alterações com ponto de partida e moderação padronizados; não há repetição prevista nesta entrega |

*Tabela 4: Decisões práticas apoiadas nos dados, com condições de verificação.*

A ordem acima usa gravidade e prejuízo ao acesso, conforme a F2. Não estima custo de
implantação nem retorno financeiro; esses elementos dependem do fornecedor. Corrigir
acessibilidade, layout e desempenho são frentes complementares. Nenhuma classe autoriza
ignorar um defeito localizado, nem permite inferir a qualidade de características que
ficaram fora da avaliação.

## 4. Rastreabilidade e encerramento

| Critério da #79 | Evidência nesta entrega | Situação |
|---|---|---|
| F4-C4: classificação por característica segundo a F2 | Seção 1: classe pela média, limitadores, classe final e recortes comprometidos; CSV consolidado | G2 e G3 classificados; G1 encerrado com ressalvas e NC global; não há classe de qualidade atribuída a G1, portanto o requisito de classificar todas as características tem essa limitação |
| F4-C5: coerência com o propósito da F1 | Seções 2 e 3: propósito, necessidades, três decisões e condições de verificação | Relação explícita e fundamentada nos dados |

Para refazer os números, executar `python3 scripts/fase-4/consolidar.py --verificar` na
raiz do repositório, conforme a [consolidação](consolidacao.md). A versão analisada tem
55 recortes: 51 classificados e quatro NC de G1. Não se calcula uma média global de
qualidade entre G1, G2 e G3.

**Encerramento da síntese:** a equipe aceita o relatório com a amostra e as condições
registradas. G2 e G3 têm classificação final; G1 tem conclusão descritiva e nota global
NC. Essa aceitação encerra o trabalho documental com ressalvas, sem equivaler ao
atendimento integral da exigência de atribuir uma classe a todas as características.
Uma classificação numérica de G1 exigiria dados adicionais; eles não serão coletados
nesta entrega. As limitações ficam disponíveis para a revisão acadêmica e para o requisitante.
