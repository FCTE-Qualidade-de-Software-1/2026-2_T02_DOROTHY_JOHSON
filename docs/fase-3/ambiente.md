# Recursos e ambiente de avaliação

Esta página especifica o objeto avaliado, as páginas e os objetos de referência, o hardware, o
software, as condições de rede e o conhecimento exigido de avaliadores e participantes. O
objetivo é que outra pessoa consiga repetir a avaliação nas mesmas condições (critério F3-C2).

## 1. Objeto avaliado

| Item | Especificação |
|---|---|
| Produto | Plataforma Territórios da Cidadania (SIT), área pública |
| Endereço | <https://territoriosdacidadania.mda.gov.br> |
| Versão | A versão em produção no período de coleta. O portal não exibe número de versão, por isso cada medição registra data e hora ([Fase 1, seção 5](../fase-1/index.md#5-escopo-e-limites-da-avaliacao)) |
| Fora do escopo | Espaço do Colegiado (área restrita), servidores, APIs internas e código-fonte ([Fase 1, seção 3.5](../fase-1/index.md#35-componentes-avaliados-e-massa-de-dados)) |

## 2. Páginas, tarefas e objetos de referência

As páginas e as tarefas de cada característica estão na
[Fase 1, seção 3.6](../fase-1/index.md#36-paginas-e-tarefas-avaliadas):

| Página | Endereço | G1 | G2 | G3 |
|---|---|:---:|:---:|:---:|
| Início | `/` | Sim | | |
| Meu Território | `/meu-territorio` | Sim | Sim | Sim |
| SITGeo | `/plataforma-geoespacial` | Sim | Sim | Sim |
| Biblioteca Territorial | `/downloads` | Sim | Sim | Sim |
| Fale Conosco | `/contato` | Sim | | |

As três seções prioritárias concentram a finalidade do sistema (consulta de dados, mapas e
documentos dos territórios); Início é o ponto de partida das tarefas de G1 e G2, e o Fale
Conosco é onde a proteção contra erros do usuário é observável.

**Objetos de referência.** As tarefas usam sempre os mesmos objetos, para que os resultados
de G1, G2 e G3 sejam comparáveis entre si e entre execuções:

| Tarefa | Objeto de referência | Situação |
|---|---|---|
| T1, consultar um território | UF **GO**, território **Chapada dos Veadeiros - GO** | Confirmado em 08/11/2026 |
| T2, ativar uma camada no mapa | Camada **PRONAF - Valor Total de Crédito Acessado** | Confirmado em 08/11/2026 |
| T3, baixar um documento | UF **GO**, **PTDRS** do território **Estrada de Ferro - GO** | Confirmado em 08/11/2026 |

T1 e T2 usam os mesmos objetos da medição piloto do G3 (20/10/2026), o que permite comparar a
coleta da Fase 4 com o piloto. O território de T1 é o primeiro da lista de GO no portal, e a
camada mostra dados do PRONAF, um dos programas que o portal destaca nas abas de Meu Território
([Fase 1, seção 4.2](../fase-1/index.md#42-subcaracteristicas-avaliadas)).

A T3 usa outro território porque Chapada dos Veadeiros - GO não tem PTDRS disponível na
Biblioteca Territorial: em 08/11/2026, o único PTDRS de GO para download era o de Estrada de
Ferro - GO. Manter a UF GO nas três tarefas preserva o mesmo caminho de seleção. Nos testes com
usuários (G1) e na matriz de ambientes (G2), o roteiro informa em cada tarefa qual território
usar.

!!! note "Biblioteca Territorial em navegador automatizado"
    Em navegador controlado por automação (Playwright), o seletor de UF da Biblioteca
    Territorial permaneceu desabilitado em 08/11/2026, enquanto na navegação manual ele
    funciona normalmente. Por isso a T3 é executada manualmente, e medições automáticas na
    Biblioteca (como as do G3) avaliam apenas o carregamento da página.

## 3. Ambiente por característica

### 3.1 Eficiência de desempenho (G3)

| Recurso | Especificação |
|---|---|
| Máquina | Notebook com AMD Ryzen 5 5600H (6 núcleos, 12 threads) e 22 GB de RAM, a mesma do piloto |
| Sistema operacional | Ubuntu 26.04.1 LTS (Linux 7.0, x86_64) |
| Navegador | Google Chrome 138.0.7204.157, em modo *headless* |
| Ferramentas | Lighthouse 12.8.2 (versão fixada), Node.js 24.22.1, Playwright 1.48.2 e `jq` |
| Scripts | `scripts/fase-4/eficiencia/` (ver o [método](metodo-eficiencia.md)) |
| Perfil de acesso | Celular simulado em 412 × 823 px, com a limitação do perfil móvel padrão do Lighthouse: latência de 150 ms, 1,6 Mbit/s de download, 675 kbit/s de upload e CPU 4 vezes mais lenta |
| Rede de base | Conexão do avaliador, mais rápida que o perfil simulado; o tipo de conexão (cabo ou Wi-Fi) é registrado em cada sessão |
| Cache | Vazio no início de cada execução (cada execução usa um perfil novo do navegador) |
| Isolamento | Uma execução por vez, sem outros programas pesados abertos ([GOOGLE, 2023](#referencias)) |

O perfil limitado reproduz o contexto do objetivo G3: celular de entrada em área rural, com
rede móvel lenta ou instável ([Fase 2, objetivo G3](../fase-2/objetivos.md#g3-eficiencia-de-desempenho)).
Como a limitação é aplicada pela ferramenta, a velocidade real da conexão do avaliador afeta
pouco o resultado, desde que seja maior que a do perfil.

### 3.2 Capacidade de interação (G1)

| Recurso | Especificação |
|---|---|
| Dispositivo dos testes com usuários | Um celular, o mesmo para todos os participantes ([Fase 2, métricas de G1](../fase-2/metricas.md#condicoes-comuns-de-coleta)) |
| Inspeções (M1.1.1, M1.4.1, M1.4.2) | Navegador de computador da equipe |
| Acessibilidade (M1.6.1, M1.6.2) | axe-core, regras WCAG 2.1 níveis A e AA |
| Questionários (M1.5.1, M1.5.2) | Formulário com o SUS e a nota de aparência |
| Gravação | Tela e áudio, só com termo de consentimento assinado (protocolo da #68) |

### 3.3 Flexibilidade (G2)

| Recurso | Especificação |
|---|---|
| Navegadores e sistemas | Chrome/Android, Samsung Internet/Android, Safari/iOS, Chrome/Windows, Edge/Windows e Firefox/Windows ([Fase 2, objetivo G2](../fase-2/objetivos.md#g2-flexibilidade)) |
| Larguras | 360, 412, 768, 1366 e 1920 px |
| Ambiente de referência | Chrome/Windows em 1366 px |
| Dispositivos | Aparelhos reais para os celulares de maior participação; larguras pelo modo de dispositivo do Chrome DevTools |
| Registro | Data e hora, versões do navegador e do sistema, largura, dispositivo real ou emulado e captura de tela |

!!! note "Itens que dependem dos métodos de G1 e G2"
    O modelo do celular dos testes com usuários, a versão do axe-core, a ferramenta de
    gravação, os aparelhos reais da matriz de G2 e o local das sessões com participantes são
    definidos nos métodos de capacidade de interação (#63) e de flexibilidade (#64) e no
    protocolo de participantes (#68). Esta página é atualizada quando eles forem fixados.

## 4. Conhecimento exigido

| Papel | Informática | Domínio |
|---|---|---|
| Avaliador de G3 | Linha de comando, Node.js e leitura de relatórios do Lighthouse | Nenhum além das tarefas descritas |
| Avaliador de G2 | Modo de dispositivo do Chrome DevTools e instalação de navegadores | Nenhum além das tarefas descritas |
| Moderador de G1 | Condução de teste com usuários sem interferir (roteiro e protocolo) | Conhecer as tarefas e o objeto de referência |
| Participantes de G1 | Básico: navegar na web e usar menus, filtros e mapas ([Fase 1, seção 3.3](../fase-1/index.md#33-usuarios-ambiente-e-conhecimento-exigido)) | Baixo; não podem ter usado o portal antes |

## 5. Riscos do ambiente

- **Produto em produção:** o portal pode mudar durante a coleta. Cada execução registra data
  e hora, e as execuções de uma mesma métrica são feitas em uma única sessão.
- **Variação da rede e do servidor:** a limitação aplicada reduz o efeito da rede do
  avaliador, mas não o da carga do servidor. Por isso cada medida usa a mediana de 5
  execuções.
- **Diferença entre ferramentas:** o Lighthouse aplica a limitação de rede por simulação,
  enquanto o script das tarefas aplica a limitação no próprio navegador. Os valores de
  carregamento (Lighthouse) e de tarefa (script) não são somados nem comparados diretamente.

## Referências

GOOGLE. **Lighthouse variability**. [S.l.]: Google, 2023. Disponível em: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md>. Acesso em: 08 nov. 2026.
