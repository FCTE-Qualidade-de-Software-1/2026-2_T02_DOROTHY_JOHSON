# Método de capacidade de interação (G1)

Protocolo de coleta para o critério F3-C1 ([atividade #63](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/63)). Use as [fichas de G1](../fase-2/metricas.md#g1-capacidade-de-interacao), os [recursos e objetos de referência](ambiente.md) e os [formulários de coleta](formularios-interacao.md).

## 1. Escolha dos métodos

| Métricas | Método e justificativa |
|---|---|
| M1.1.1 | Inspeção independente por dois avaliadores. Uma captura da primeira dobra permite conferir se a finalidade da seção está visível no aparelho do teste. |
| M1.1.2, M1.2.1 e M1.3.1 | Teste moderado com usuários de primeiro acesso. O primeiro destino, a conclusão e os passos vêm de ações observáveis, conferidas na gravação. |
| M1.4.1 e M1.4.2 | Inspeção com entradas fixas e rede offline. A inspeção reproduz o mesmo erro, verifica o bloqueio antes do envio e permite comparar o texto das mensagens. |
| M1.5.1 e M1.5.2 | Questionário pós-sessão. O SUS mede a percepção de usabilidade e o item adicional mede a percepção da aparência. |
| M1.6.1 e M1.6.2 | Verificação com axe-core. A mesma versão e o mesmo conjunto de regras permitem comparar os resultados automáticos das cinco páginas. |

## 2. Preparação e participantes

1. Separe **cinco adultos que nunca usaram o SIT**, com conhecimento básico de navegação móvel e pouca familiaridade com o domínio territorial. Inclua, quando possível, pessoas dos públicos de G1, como cidadãos, agricultores familiares e agentes territoriais. Recrute pelo menos duas pessoas que usam principalmente mensagens e navegação simples e duas que também usam filtros, formulários ou mapas com autonomia. Registre o perfil por código P01 a P05. A amostra segue a Fase 2 e serve à identificação de problemas de primeira utilização.
2. Use o **mesmo celular Android e Chrome** para todos, em modo retrato, zoom e tamanho de texto padrão, na mesma sala e rede Wi-Fi. Antes do piloto, registre o aparelho, as versões do sistema e navegador e o gravador nativo de tela com microfone. Mantenha essas condições durante a coleta e guarde os registros do ambiente junto da rodada.
3. Nomeie um moderador e um observador. Faça um piloto com uma pessoa da equipe, fora da amostra. Confirme a gravação e execute as três rotas da seção 3. Conte os toques necessários no aparelho, incluindo a abertura do menu quando recolhido, e registre o caminho mínimo e os totais no formulário antes de P01. Se houver atalho visível, compare os caminhos e fixe o menor que reproduz o mesmo resultado. Use a mesma regra para contar todos os participantes.
4. Antes da sessão, confirme a participação e a escolha sobre gravação conforme o [protocolo de participantes](protocolo-participantes.md). Use somente os códigos nos dados de trabalho. Guarde gravações e termos em acesso restrito e publique apenas os dados anonimizados e as evidências autorizadas. Use o modo Não Perturbe e dispense contas pessoais no aparelho.

## 3. Sessão com usuários

Leia na abertura: “Estamos avaliando o portal. Faça cada tarefa como faria normalmente e diga em voz alta o que está procurando ou pensando. Você pode encerrar qualquer tarefa.”

Execute **T1 → T2 → T3** para todos. Antes de cada tarefa feche as abas anteriores, abra uma nova sessão anônima com Início carregada, no topo e com o menu recolhido, e leia apenas o enunciado da segunda coluna. Inicie o cronômetro ao dizer “Pode começar”. Se pedirem uma dica, responda “Faça como faria se estivesse usando o portal sozinho”. Pare ao observar o resultado, em caso de desistência, ou aos **5 minutos**. Caso ocorra ajuda ou consulta a instruções externas, marque a tentativa como não concluída sem ajuda. Anote o horário na gravação e o motivo. Se houver interrupção externa, como queda da rede da sala, registre a tentativa como interrompida e reaplique se o participante ainda não tiver visto o caminho. Se tiver visto, registre o recorte afetado como NC até completar cinco observações válidas com participantes elegíveis e sem experiência prévia na tarefa. Erros do próprio portal durante a tentativa são registrados como comportamento do produto.

| Tarefa | Enunciado para leitura | Caminho de referência para o avaliador | Evidência de conclusão |
|---|---|---|---|
| T1 | Consulte os indicadores de Chapada dos Veadeiros, em Goiás. | Meu Território → UF GO → Chapada dos Veadeiros - GO → Selecionar. | Indicadores Gerais e mapa de abrangência do território carregados. |
| T2 | No mapa do portal, exiba a camada “PRONAF - Valor Total de Crédito Acessado”. | SITGeo → Políticas Públicas → abrir o painel de camadas se recolhido → ativar a camada indicada. | Camada desenhada e legenda correspondente visível. |
| T3 | Baixe o PTDRS do território Estrada de Ferro, em Goiás. | Biblioteca Territorial → seção PTDRS → programa Territórios da Cidadania (padrão) → UF GO → Buscar PTDRS → documento da linha Estrada de Ferro - GO. | Arquivo correto baixado. Se o navegador abrir o PDF, a tentativa termina quando o arquivo for salvo pelo participante. |

### M1.1.2 — Primeiro clique

Na gravação, localize o primeiro toque que escolhe um destino a partir de Início. Abrir o menu e rolar são ações preparatórias para esta métrica. Registre o destino escolhido mesmo se a página falhar ao carregar. Se nenhum destino for escolhido, marque erro. Compare com Meu Território (T1), SITGeo (T2) e Biblioteca Territorial (T3). Calcule acertos ÷ 5 por tarefa.

### M1.2.1 — Conclusão sem ajuda

Confronte o estado final gravado com a última coluna do roteiro. Marque sucesso apenas se o resultado aparecer em até 300 segundos sem ajuda. Registre desistência, limite atingido ou ajuda como falha. Calcule sucessos ÷ 5 em cada tarefa e reporte também a média das três proporções.

### M1.3.1 — Eficiência do caminho

Reveja a gravação do início até a evidência de sucesso. Conte cada toque em um controle, seleção ou preenchimento de campo. Abrir uma lista e escolher uma opção são dois passos quando exigem dois toques. Conte abertura do menu, voltas e toques em controles errados. Cada preenchimento de campo conta uma vez por edição contínua. Rolagem, espera e zoom por gesto ficam fora da contagem. Um segundo avaliador revê a sequência. Registre as duas contagens e a decisão por consenso. Se surgir um caminho válido mais curto que o do piloto, confirme-o no mesmo aparelho, documente a revisão e recalcule toda a tarefa com o novo mínimo. Para cada conclusão sem ajuda, divida os passos mínimos pelos observados. Calcule a média das razões por tarefa. Use NC se a tarefa tiver zero conclusões.

### M1.5.1 e M1.5.2 — Questionário após as tarefas

Entregue o [questionário em português](formularios-interacao.md#questionario) depois de T3, inclusive se alguma tarefa falhar. Peça que a pessoa responda individualmente pensando no portal que acabou de usar. Para cada SUS completo, calcule a soma de (resposta − 1) nos itens ímpares e (5 − resposta) nos pares, multiplicada por 2,5. Calcule a média dos escores completos. Para aparência, tire a média das respostas válidas ao item 11. Registre itens em branco como ausentes, sem imputar valores, e informe o número de respostas válidas de cada média. Sem respostas válidas, registre NC.

## 4. Inspeção de autodescrição (M1.1.1)

1. Dois avaliadores inspecionam separadamente, no mesmo aparelho da sessão, as nove seções listadas no [formulário](formularios-interacao.md#autodescricao). Acessem cada página pelo menu, em sessão anônima nova, no topo e com o menu fechado. Em Espaço do Colegiado, observem apenas a tela pública de entrada.
2. Com a primeira tela carregada, façam uma captura antes de qualquer rolagem. Marquem “sim” quando um texto legível na captura descreve o que a pessoa pode encontrar ou fazer naquela seção. Título isolado, logotipo ou itens do menu sem descrição recebem “não”. Erro de carregamento deve ser registrado e a disponibilidade conferida antes de concluir a inspeção.
3. Comparem as decisões e resolvam as divergências por consenso usando as capturas. Preservem as duas avaliações originais e a decisão final. Dividam o total de “sim” por 9 e guardem também o numerador para a tabela de níveis.

## 5. Inspeção de entradas inválidas (M1.4.1 e M1.4.2)

1. Use Chrome de computador, zoom a 100%, DevTools aberto em **Network**, com **Preserve log**. Para cada caso da [lista fixa](formularios-interacao.md#entradas-invalidas), abra a página online para carregar os controles. Prepare os valores de referência ou seleções válidas necessárias. Antes de inserir o valor sob teste ou tentar prosseguir, mude Network para **Offline** e limpe o log.
2. Preencha apenas a variação do caso, observe o campo ao perder o foco e tente a ação uma vez. Se o botão estiver desabilitado, capture esse estado. Registre o valor aceito, o estado do controle, a mensagem literal (inclusive validações nativas) e se houve uma requisição correspondente à ação testada. Ignore requisições de fundo sem relação com a ação.
3. Marque protegido se a interface impedir a entrada/ação ou alertar antes do envio. Se o log mostrar uma tentativa de envio da ação indicada, marque não protegido, mesmo com erro de rede. Guarde captura do estado final e do log. Antes de restaurar a rede, descarte a aba e a sessão anônima do caso. Repita com estado inicial limpo.
4. Calcule **M1.4.1 = casos protegidos ÷ casos executados**. Registre casos indisponíveis com motivo e informe a cobertura. Sem execuções válidas, use NC.
5. Para **M1.4.2**, os dois avaliadores codificam separadamente os casos com mensagem de validação. Marque “sim” se a mensagem, pelo texto ou associação visual ao controle, identificar o campo e informar a correção esperada. Quando houver várias mensagens, conte o caso uma vez e exija que as mensagens, em conjunto, cubram as entradas que sinalizaram. Resolva divergências por consenso. Divida os casos com correção adequada pelos casos com mensagem. Sem mensagens, registre NC e siga a orientação de inspeção complementar da Fase 2.

## 6. Verificação automática (M1.6.1 e M1.6.2)

1. Use Chrome de computador em janela anônima, zoom 100%, viewport **1366 × 768 px** (modo Responsivo no DevTools, com tipo de dispositivo Desktop). Use o estado inicial das páginas, no topo, sem filtros nem menus abertos. Registre o ambiente. Obtenha o arquivo local `axe.min.js` do pacote com `npm pack axe-core@4.10.3` e extraia o arquivo `package/axe.min.js` do pacote gerado. No Chrome DevTools, crie um snippet em **Sources → Snippets** com o conteúdo do arquivo. [API do axe-core 4.10.3](https://github.com/dequelabs/axe-core/blob/v4.10.3/doc/API.md)
2. Abra, uma por vez, as cinco URLs do [ambiente](ambiente.md#2-paginas-tarefas-e-objetos-de-referencia). Confirme que os controles iniciais renderizaram e que os indicadores de carregamento desapareceram. Registre erro e recorte como NC se a página ou o relatório estiver indisponível, em vez de medir uma tela de erro.
3. Em cada página, execute o snippet no contexto principal e rode o trecho abaixo no Console. Salve o conteúdo copiado como `axe-<pagina>.json` em UTF-8. Confirme URL, data, versão e presença dos quatro grupos de resultado no JSON antes de avançar.

```javascript
if (axe.version !== "4.10.3") throw new Error("Versão inesperada do axe-core")
const resultadoG1 = await axe.run(document, {
  runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"] },
  ancestry: true
})
copy(JSON.stringify(resultadoG1, null, 2))
```

4. Para **M1.6.1**, conte as regras em `passes` e `violations`. Divida o primeiro total pela soma dos dois. Registre também `incomplete` e `inapplicable` para rastreabilidade. Se a soma for zero, use NC.
5. Para **M1.6.2**, percorra `nodes` de cada regra em `violations` com `impact` igual a `critical` ou `serious`. Use a cadeia completa de `ancestry` (ou `target` quando ausente) para identificar o elemento, incluindo o caminho do frame quando houver. Agrupe ocorrências do mesmo elemento na página, preservando os IDs das regras e o maior impacto. Registre contagens distintas de críticos e sérios, além da soma. O resultado descreve somente as verificações automáticas executadas.

## 7. Conferência e consolidação

Preencha o [resumo de coleta](formularios-interacao.md#consolidacao) a partir dos registros originais, com uma linha por métrica e recorte. Informe numerador e denominador quando houver, valor, nível e referência da evidência. Compare os valores sem arredondamento com os [níveis e regras de classificação de G1](../fase-2/niveis-pontuacao.md#2-g1-capacidade-de-interacao). Registre os recortes NC e seus motivos, verificando em especial as regras de conclusão de tarefas e de violações críticas. Peça ao segundo avaliador para reproduzir os cálculos a partir dos registros e conferir divergências antes de consolidar.
