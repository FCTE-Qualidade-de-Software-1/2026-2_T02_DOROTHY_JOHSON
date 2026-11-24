# Protocolo de participantes e consentimento

Este protocolo se aplica às entrevistas e aos testes com participantes na avaliação da área pública da Plataforma Territórios da Cidadania (SIT). Para as sessões de interação, use o [método de G1](metodo-interacao.md) e os [formulários de coleta](formularios-interacao.md). O [termo de consentimento](termo-consentimento.md) foi aprovado pela equipe em 24/11/2026, na versão do commit `f9f354b`, no contexto da [atividade #68](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/68).

## Antes da sessão

1. Designe um responsável pela guarda e um moderador. A equipe aprova a versão do termo e registra a decisão na #68, em ata ou no PR, com data e versão. Registre a aprovação sem anexar termos preenchidos.
2. Preencha todos os campos entre colchetes no termo antes de entregar a cópia ao participante. Confirme o curso, a orientação, o local, a duração aproximada, o armazenamento, o prazo e o contato do responsável. Em sessões planejadas sem gravação, retire da cópia a frase que menciona gravar tela e áudio e a linha de autorização de gravação, conforme o modelo da disciplina. Use como prazo até 30 dias após a divulgação da nota final da disciplina. Confirme quem terá acesso e configure a pasta restrita antes da coleta.
3. Reserve um código sequencial com dois dígitos, como `P01`, `P02` e `P03`. Use `P01` a `P05` como referência para as cinco pessoas da amostra. Se houver substituição, atribua o próximo código livre. Guarde a relação código–nome separadamente, com acesso apenas do responsável pela guarda. Use o código nas fichas e nos nomes dos arquivos de trabalho. O código permite relacionar registros da mesma sessão e exige proteção enquanto existir esse vínculo.
4. Entregue uma cópia do termo, explique tarefas e registros, tire dúvidas e colha a assinatura antes de começar. Se houver previsão de gravação, peça também que a pessoa marque a opção de autorização. A pessoa pode aceitar participar e recusar a gravação. Sem autorização específica, mantenha o gravador desligado. A participação sem gravação pode ocorrer com observação direta se a pessoa aceitar os registros escritos. Registre o desvio e os recortes afetados na Fase 4.

## Durante e depois da sessão

1. Quando houver autorização, grave somente a tela usada na tarefa e o áudio. Use um aparelho sem contas pessoais abertas, silencie notificações e pause se aparecer informação identificável ou se a pessoa pedir. Encerre a gravação antes da conversa final ou de qualquer dado de contato.
2. Transfira os arquivos para o espaço restrito, confira a leitura e remova a cópia temporária do aparelho. Registre o código, a versão do termo, a autorização de gravação quando aplicável e a ocorrência de gravação no controle restrito.
3. Se uma sessão presencial já ocorreu sem gravação, use apenas registros existentes, com autorização de uso documentada e a indicação de que houve observação direta. Se o uso dos registros ainda não estiver autorizado, mantenha-os restritos até obter autorização específica para uso futuro. Registre a data efetiva da autorização para uso dos registros e identifique a data da sessão original. Use um documento que descreva as anotações ou respostas já coletadas e sua finalidade, em vez de apresentar o termo de participação como se tivesse sido assinado antes da sessão. Marque como NC as medidas que ficaram sem evidência suficiente, conforme os [níveis de pontuação](../fase-2/niveis-pontuacao.md).
4. Em caso de desistência ou pedido de retirada, interrompa a atividade e localize os arquivos pelo código. Até a data de descarte, exclua os registros identificáveis ou vinculáveis e retire os dados da pessoa dos arquivos de trabalho e das publicações que ainda permitam identificá-los. Informe que resultados já agregados e sem vínculo individual podem ser mantidos. O responsável registra a ação no controle restrito.
5. Na data definida, elimine termos assinados, relação código–nome, gravações originais e formulários preenchidos restritos. Revogue o acesso à pasta e remova cópias locais e itens da lixeira sob controle da equipe.

## Guarda, acesso e publicação

| Material | Local | Acesso |
|---|---|---|
| Termo em branco e fichas de coleta | `docs/fase-3/termo-consentimento.md` e `docs/fase-3/formularios-interacao.md` | Público |
| Termos assinados e relação código–nome | Pastas separadas `consentimentos/` e `identificacao/` no armazenamento privado da equipe, fora do Git | Responsável pela guarda |
| Gravações originais e fichas preenchidas | Pastas privadas `gravacoes/` e `formularios/`, fora do Git | Moderador e avaliadores designados. Professor responsável apenas para conferência, por acesso restrito quando necessário. |
| Dados revisados e consolidados | `data/fase-4/capacidade-de-interacao/`, somente tabelas anonimizadas e resultados agregados | Público após revisão |
| Evidências derivadas das gravações | `data/fase-4/capacidade-de-interacao/capturas/`, somente recortes anonimizados cuja publicação específica tenha sido autorizada | Público após revisão |

Configure a pasta privada com acesso por contas indicadas e compartilhamento público desativado. Antes de subir arquivos para o GitHub, dois integrantes conferem se a exportação removeu nomes, contatos, assinaturas, voz, rostos, notificações, metadados e outros detalhes que possam identificar alguém. Para formulários, publique apenas campos necessários às métricas. Quando uma combinação de perfil e respostas puder identificar alguém, publique o resultado agregado. Prefira tabelas de observação e capturas anonimizadas como evidência pública. Mantenha os originais fora de commits, PRs, issues e GitHub Pages.
