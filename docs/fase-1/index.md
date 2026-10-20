# Fase 1 — Estabelecer os requisitos de avaliação

A Fase 1 do processo de avaliação de produto da série SQuaRE define **por que** o produto
será avaliado, **o que** é o produto e **com qual modelo de qualidade** ele será analisado.
As decisões registradas aqui orientam diretamente a [Fase 2 (GQM)](../fase-2/index.md).

| Item | Valor |
|---|---|
| Produto | Plataforma Territórios da Cidadania — Sistema de Informações Territoriais (SIT) |
| Endereço | <https://territoriosdacidadania.mda.gov.br> |
| Responsável pelo produto | Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA) |
| Versão avaliada | Versão em produção na data de acesso (o portal não exibe número de versão) |
| Primeiro acesso para esta avaliação | 19/10/2026 |
| Modelo de qualidade | ISO/IEC 25010:2011, modelo de qualidade de produto (ISO/IEC, 2011a) |
| Tipo de avaliação | Externa (caixa-preta), restrita à área pública do portal |

---

## 1. Propósito da avaliação

### 1.1 Contexto

A Plataforma Territórios da Cidadania foi instituída como instrumento do Programa Nacional
de Desenvolvimento Territorial Sustentável ([BRASIL, 2025](../referencias.md)) e recupera o
SIT, desativado em 2016. Seu papel é reunir, em um único lugar, dados socioeconômicos e
ambientais dos territórios rurais (população, estabelecimentos agropecuários, Cadastro da
Agricultura Familiar, acesso a políticas públicas), além de mapas, atos normativos e o
registro das atividades dos Colegiados Territoriais.

Por ser um sistema **relançado recentemente** e voltado a um público heterogêneo, que inclui
agentes territoriais e agricultores familiares em áreas rurais, este é o momento em que uma
avaliação de qualidade tem maior potencial de influenciar a evolução do produto.

### 1.2 Requisitante e objetivo

| Elemento | Definição |
|---|---|
| Requisitante (simulado) | MDA, como órgão gestor da política territorial e responsável pela evolução do SIT |
| Avaliadores | Equipe Dorothy Johnson (avaliação independente, sem vínculo com o desenvolvimento) |
| Objetivo da avaliação | **Indicar pontos de melhoria no produto** (categoria do processo de avaliação de produto, conforme Ramos, 2026c) |
| Uso pretendido dos resultados | Apoiar o requisitante na **priorização do backlog de evolução** do portal |

A avaliação deve responder a uma pergunta de gestão: **quais problemas de qualidade mais
dificultam o acesso do público-alvo às informações territoriais e, portanto, devem ser
tratados primeiro?** Os resultados apoiarão três decisões concretas do requisitante:

1. **Interface e fluxos de navegação** — quais telas e tarefas precisam ser redesenhadas
   para usuários com pouca familiaridade digital (usabilidade).
2. **Desempenho em condições reais de acesso** — se é necessário otimizar o carregamento
   das páginas e dos mapas para conexões móveis e aparelhos modestos (eficiência de desempenho).
3. **Cobertura de ambientes** — quais combinações de navegador, sistema operacional e
   tamanho de tela devem entrar na matriz de testes do fornecedor (portabilidade).

### 1.3 Ênfase por característica

A ênfase segue a escala do processo de avaliação de produto (RAMOS, 2026c), em que 1 = nenhum interesse e 5 = grande interesse,
e considera o propósito acima, os stakeholders (Seção 2) e a viabilidade de medição em uma
avaliação caixa-preta.

| Característica (ISO/IEC 25010:2011) | Ênfase | Justificativa |
|---|:---:|---|
| Usabilidade | **5** | Público com níveis muito diferentes de letramento digital; o valor do SIT depende de o usuário encontrar e interpretar os dados sozinho. |
| Eficiência de desempenho | **4** | Uso em áreas rurais, com conexões móveis limitadas; o portal carrega mapas interativos e renderiza o conteúdo no navegador. |
| Portabilidade | **4** | Acesso predominante por celular (no Brasil, o Chrome para Android responde por cerca de 39% das versões de navegador em uso) e diversidade de navegadores e telas. |
| Adequação funcional | 3 | Relevante, mas não há especificação de requisitos pública que sirva de referência para medir completude e correção. |
| Confiabilidade | 2 | Medir disponibilidade exigiria monitoramento contínuo por um período maior que o da disciplina. |
| Segurança | 2 | A área restrita (Espaço do Colegiado) exige credenciais que a equipe não possui. |
| Compatibilidade | 2 | Interoperabilidade com outros sistemas do governo não é observável externamente. |
| Manutenibilidade | 1 | Sem acesso ao código-fonte nem à documentação técnica. |

Foram selecionadas as características com ênfase **4 ou 5**: usabilidade, eficiência de
desempenho e portabilidade. As demais ficam fora do escopo pelos motivos indicados.

!!! note "Compatibilidade × portabilidade"
    O funcionamento do portal em diferentes navegadores e dispositivos é tratado como
    **adaptabilidade** (subcaracterística de portabilidade), e não como compatibilidade.
    Na ISO/IEC 25010:2011, compatibilidade trata de coexistência e interoperabilidade
    com outros produtos, o que não é observável nesta avaliação.

---

## 2. Stakeholders

| Stakeholder | Papel | Necessidade principal | Critério de sucesso | Característica que motiva |
|---|---|---|---|---|
| MDA (área gestora da política territorial) | Requisitante | Saber onde investir na evolução do SIT | Lista priorizada de melhorias apoiada em evidências | Todas |
| Equipe de desenvolvimento e TI do SIT | Fornecedor | Saber o que corrigir e em quais ambientes testar | Defeitos reproduzíveis, com ambiente e passos | Portabilidade, eficiência |
| Colegiados e agentes territoriais | Usuários frequentes | Consultar dados do território para planejar e prestar contas | Encontrar a informação rapidamente, inclusive no celular | Usabilidade, portabilidade |
| Gestores públicos e organizações sociais | Usuários eventuais | Subsidiar projetos e políticas com dados territoriais | Dados acessíveis e baixáveis | Usabilidade, eficiência |
| Agricultores familiares e cidadãos | Público final | Conhecer as políticas que chegam ao seu território | Uso sem ajuda, em aparelho e conexão modestos | Usabilidade, eficiência, portabilidade |
| Equipe Dorothy Johnson | Avaliadora | Executar uma avaliação repetível | Métricas objetivas e coleta reprodutível | — |

---

## 3. Tipo de produto

### 3.1 Descrição geral

O SIT é uma **aplicação web pública** do governo federal. A navegação principal oferece
**nove seções**, levantadas no menu do portal (BRASIL, 2026) em 19/10/2026:

| Seção | Função principal | Acesso |
|---|---|---|
| Início | Apresentação da plataforma e mapa da área de abrangência (Territórios da Cidadania, PDHC, PAS Nordeste) | Público |
| Meu Território | Consulta de indicadores consolidados de um território | Público |
| SITGeo | Plataforma geoespacial com cerca de 30 variáveis em 5 temas, exibidas como camadas de mapa | Público |
| Biblioteca Territorial | Download de documentos, mapas e atos normativos | Público |
| Homologações de Territórios | Consulta às homologações e modelos de documentos | Público |
| Território em Foco | Informativo institucional | Público |
| Fale Conosco | Canal de contato | Público |
| Sobre | Informações sobre a plataforma e a política | Público |
| Espaço do Colegiado | Registro das ações dos Colegiados Territoriais | **Restrito** (e-mail e senha; conta solicitada a um administrador) |

<!-- TODO (equipe): completar a contagem de funções e de janelas de interação
     dentro de cada seção (filtros, camadas, formulários) durante a exploração. -->

### 3.2 Classificação

| Taxonomia | Classificação | Justificativa |
|---|---|---|
| Pressman (2002) | **Aplicação web (WebApp) de sistema de informação** | Organiza e apresenta dados de bases oficiais (IBGE, Datasus, CadÚnico etc.) para consulta e apoio à decisão. Não se encaixa em "software comercial", pois não é comercializado. |
| IEEE 1062 (IEEE, 1998) | **Customizado (*Fully Developed*)** | Desenvolvido especificamente para o MDA e para a política territorial; não é um produto de prateleira (COTS) nem uma adaptação de um produto-padrão (MOTS). Classificação inferida, pois a avaliação é caixa-preta. |
| Domínio | Governo digital / desenvolvimento rural | Política pública de desenvolvimento territorial sustentável |

### 3.3 Usuários, ambiente e conhecimento exigido

- **Principais usuários:** colegiados e agentes territoriais, gestores públicos, organizações
  sociais, pesquisadores e cidadãos (com destaque para agricultores familiares).
- **Conhecimento de informática exigido:** básico (navegar na web, usar menus, filtros e mapas).
  O SITGeo exige um pouco mais: ativar camadas e interpretar legendas.
- **Conhecimento do domínio exigido:** baixo para consultas gerais; médio para interpretar
  indicadores e documentos da política territorial.
- **Ambiente de uso:** navegador web em computador ou celular, muitas vezes em áreas rurais
  com conexão móvel instável.

### 3.4 Requisitos de hardware e software

Até a data de acesso, a equipe não encontrou requisitos mínimos documentados no portal.
Pelas observações feitas, o acesso exige:

- navegador atualizado com **JavaScript habilitado**: sem execução de scripts, páginas como
  Meu Território e Biblioteca Territorial retornam praticamente vazias, o que indica
  renderização no lado do cliente;
- conexão com a internet;
- leitor de PDF para os documentos da Biblioteca Territorial (a confirmar na Fase 4).

### 3.5 Componentes avaliados e massa de dados

- **Avaliados:** todas as seções públicas listadas na Seção 3.1, com prioridade para Meu Território,
  SITGeo e Biblioteca Territorial, que concentram a finalidade do sistema.
- **Fora do escopo:** Espaço do Colegiado (área restrita, sem credenciais), servidores,
  APIs internas e código-fonte.
- **Massa de dados:** não é necessário criar dados de teste. O portal já disponibiliza dados
  reais de todos os territórios, e a avaliação usa um conjunto fixo de territórios de
  referência, definido na Fase 3, para garantir a repetibilidade.

### 3.6 Diagrama de contexto (inferido)

```mermaid
flowchart LR
    U1[Colegiados e agentes territoriais]
    U2[Gestores públicos e organizações sociais]
    U3[Cidadãos e agricultores familiares]
    SIT[Plataforma Territórios da Cidadania - SIT]
    F1[(IBGE: censos agropecuário e demográfico)]
    F2[(Datasus)]
    F3[(CadÚnico e outras bases oficiais)]
    MDA[MDA: gestão de conteúdo e homologações]

    U1 -- consulta e registro de ações --> SIT
    U2 -- consulta e download --> SIT
    U3 -- consulta --> SIT
    F1 --> SIT
    F2 --> SIT
    F3 --> SIT
    MDA -- documentos, atos e homologações --> SIT
```

*Figura 1 — Diagrama de contexto do SIT, inferido a partir da área pública do portal e da
descrição oficial da plataforma.*

---

## 4. Modelo de qualidade

A avaliação usa o modelo de qualidade de produto da **ISO/IEC 25010:2011** (ISO/IEC, 2011a). A nomenclatura
desta edição é mantida em todo o projeto (no artigo, nesta página e no GQM).

Seguindo a orientação de adaptar o modelo de qualidade ao contexto do software e ao objetivo
do requisitante (RAMOS, 2026c), o modelo foi adaptado ao SIT a partir de dois filtros: a ênfase de cada característica
(Seção 1.3) e a possibilidade de medir cada subcaracterística de fora do sistema, apenas pela
área pública do portal (Seção 3.5). Cada subcaracterística mantida foi conferida no portal (BRASIL, 2026) em
20/10/2026, identificando onde ela pode ser observada.

### 4.1 Representação do modelo adaptado

```mermaid
flowchart LR
    Q["Qualidade do produto<br/>ISO/IEC 25010:2011"]

    Q --> US[Usabilidade]
    Q --> EF[Eficiência de desempenho]
    Q --> PO[Portabilidade]
    Q -.->|sem especificação pública| AF[Adequação funcional]
    Q -.->|exige monitoramento contínuo| CF[Confiabilidade]
    Q -.->|área restrita| SE[Segurança]
    Q -.->|não observável externamente| CO[Compatibilidade]
    Q -.->|sem código-fonte| MA[Manutenibilidade]

    US --> US1[Reconhecibilidade de adequação]
    US --> US2[Apreensibilidade]
    US --> US3[Operabilidade]
    US --> US4[Proteção contra erros do usuário]
    US --> US5[Estética da interface]
    US --> US6[Acessibilidade]

    EF --> EF1[Comportamento temporal]
    EF --> EF2[Utilização de recursos]
    EF -.->|exige teste de carga| EF3[Capacidade]

    PO --> PO1[Adaptabilidade]
    PO -.->|aplicação web| PO2[Instalabilidade]
    PO -.->|sem produto equivalente| PO3[Substituibilidade]

    classDef selecionada stroke-width:3px
    classDef fora stroke-dasharray:5 5,opacity:0.55
    class US,EF,PO selecionada
    class AF,CF,SE,CO,MA,EF3,PO2,PO3 fora
```

*Figura 2: Modelo de qualidade adaptado ao SIT. Linhas contínuas e bordas grossas indicam as
características e subcaracterísticas avaliadas; linhas e bordas tracejadas indicam o que ficou
fora do escopo, com o motivo resumido na ligação (detalhado na Seção 5).*

### 4.2 Subcaracterísticas avaliadas

A coluna **Decisão que apoia** remete às três decisões do requisitante (Seção 1.2) e a coluna
**Stakeholder** remete à Seção 2.

| Característica | Subcaracterística | Onde é observável no SIT | Decisão que apoia | Stakeholder |
|---|---|---|---|---|
| Usabilidade | Reconhecibilidade de adequação | Textos de abertura que explicam a finalidade de cada seção (ex.: Meu Território, SITGeo, Biblioteca Territorial) | 1. Interface e fluxos | Agricultores familiares e cidadãos; gestores públicos e organizações sociais |
| Usabilidade | Apreensibilidade | Fluxo de seleção UF → Território → Selecionar (Meu Território e Biblioteca Territorial); escolha de tema e ativação de camadas no SITGeo | 1. Interface e fluxos | Agricultores familiares e cidadãos; colegiados e agentes territoriais |
| Usabilidade | Operabilidade | Caixas de seleção, abas de programas (CAF, PRONAF, PAA etc.) e controles do mapa (zoom, camadas) | 1. Interface e fluxos | Colegiados e agentes territoriais |
| Usabilidade | Proteção contra erros do usuário | Formulário do Fale Conosco (nome, e-mail, telefone, assunto, mensagem) e botões desabilitados até a seleção estar completa (ex.: "Buscar PTDRS" na Biblioteca Territorial) | 1. Interface e fluxos | Agricultores familiares e cidadãos |
| Usabilidade | Estética da interface | Todas as seções públicas | 1. Interface e fluxos | Agricultores familiares e cidadãos |
| Usabilidade | Acessibilidade | Todas as seções públicas, com prioridade para Meu Território, SITGeo e Biblioteca Territorial | 1. Interface e fluxos | Agricultores familiares e cidadãos; MDA |
| Eficiência de desempenho | Comportamento temporal | Carregamento das páginas renderizadas no navegador (Seção 3.4) e das camadas do SITGeo | 2. Desempenho em condições reais | Agricultores familiares e cidadãos; equipe de desenvolvimento e TI |
| Eficiência de desempenho | Utilização de recursos | Volume de dados transferidos e processamento exigido do aparelho (mapas e scripts) | 2. Desempenho em condições reais | Agricultores familiares e cidadãos; equipe de desenvolvimento e TI |
| Portabilidade | Adaptabilidade | Execução das mesmas tarefas em diferentes navegadores, sistemas operacionais e tamanhos de tela | 3. Cobertura de ambientes | Equipe de desenvolvimento e TI; colegiados e agentes territoriais |

---

## 5. Escopo e limites da avaliação

- **Profundidade:** avaliação externa, com medições feitas a partir do navegador, de
  ferramentas públicas e de testes com usuários.
- **Objeto:** a versão em produção no período de coleta; como o portal não exibe versão,
  cada medição registra data e hora.

### 5.1 O que ficou fora do escopo

| O que ficou fora | Motivo | Efeito na validade dos resultados |
|---|---|---|
| Adequação funcional | Não há especificação de requisitos pública que sirva de referência para medir completude e correção | Os resultados não indicam se as funções do SIT estão completas ou corretas |
| Confiabilidade | Medir disponibilidade e tolerância a falhas exigiria monitoramento contínuo por um período maior que o da disciplina | Nenhuma conclusão sobre disponibilidade ou recuperação de falhas |
| Segurança | A área restrita exige credenciais que a equipe não possui, e testes de segurança em um sistema de governo em produção dependeriam de autorização do responsável | Nenhuma conclusão sobre confidencialidade, integridade ou autenticação |
| Compatibilidade | A interoperabilidade com outros sistemas do governo não é observável externamente | Os resultados não cobrem a troca de dados com as bases de origem (IBGE, Datasus, CadÚnico) |
| Manutenibilidade | Sem acesso ao código-fonte nem à documentação técnica | Nenhuma conclusão sobre a facilidade de evolução do sistema |
| Capacidade (eficiência de desempenho) | Exigiria testes de carga no servidor de produção, com risco de afetar usuários reais | Os resultados de desempenho valem para acessos individuais, não para picos de uso |
| Instalabilidade (portabilidade) | Aplicação web, sem instalação pelo usuário | Não se aplica ao produto |
| Substituibilidade (portabilidade) | Não há produto equivalente que o SIT substitua para o mesmo público | Não se aplica ao produto |
| Espaço do Colegiado | Área restrita, sem credenciais | Os resultados não valem para o registro de atividades dos colegiados |
| Servidores, APIs internas e código-fonte | Avaliação caixa-preta | Os resultados descrevem apenas o comportamento observável no navegador |
| Envio real de mensagens pelo Fale Conosco | A avaliação não deve gerar demandas reais ao MDA | A proteção contra erros é avaliada na validação do formulário antes do envio, sem cobrir o tratamento da mensagem |

### 5.2 Limites de validade

Os resultados valem para a área pública do portal e para os ambientes testados (navegadores,
sistemas operacionais e tamanhos de tela definidos na Fase 3). Mudanças no portal durante a
coleta serão registradas como ameaça à validade.

## Referências

BRASIL. Ministério do Desenvolvimento Agrário e Agricultura Familiar. Portaria MDA nº 35, de 15 de setembro de 2025. Institui o Programa Nacional de Desenvolvimento Territorial Sustentável. **Diário Oficial da União**: seção 1, Brasília, DF, ed. 176, p. 29, 16 set. 2025. Disponível em: <https://www.in.gov.br/en/web/dou/-/portaria-mda-n-35-de-15-de-setembro-de-2025-656044670>. Acesso em: 20 out. 2026.

BRASIL. Ministério do Desenvolvimento Agrário e Agricultura Familiar. **Plataforma Territórios da Cidadania**: Sistema de Informações Territoriais (SIT). Brasília: MDA, 2026. Disponível em: <https://territoriosdacidadania.mda.gov.br>. Acesso em: 20 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **IEEE Std 1062-1998**: IEEE recommended practice for software acquisition. New York: IEEE, 1998.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: systems and software engineering — systems and software quality requirements and evaluation (SQuaRE) — system and software quality models. Genebra: ISO, 2011a.

PRESSMAN, R. S. **Engenharia de software**. 5. ed. Rio de Janeiro: McGraw-Hill, 2002.

RAMOS, C. S. **Processo de avaliação de produto de software**. Notas de aula da disciplina Qualidade de Software 1. Brasília: FCTE/UnB, 2026c.

---

Próximo passo: [Fase 2 — Modelagem GQM](../fase-2/index.md).
