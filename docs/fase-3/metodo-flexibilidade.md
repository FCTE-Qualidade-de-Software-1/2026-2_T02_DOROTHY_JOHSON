# Método e instruções de medição: flexibilidade

Esta página descreve como obter as quatro métricas do objetivo G2
([Fase 2](../fase-2/metricas.md#g2-flexibilidade)) de forma repetível: outra pessoa da equipe
deve conseguir executar a coleta só lendo estas instruções (critério F3-C1). O ambiente está
em [Recursos e ambiente](ambiente.md#33-flexibilidade-g2).

## 1. Visão geral

| Métrica | O que mede | Método | Instrumento | Dado bruto |
|---|---|---|---|---|
| M2.2.1 | Combinações página × largura sem rolagem horizontal | Procedimento A (automático) | Script com Playwright no modo de dispositivo do Chrome | `rolagem.csv` e `capturas/rolagem-*.jpg` |
| M2.2.2 | Funções de 1366 px que continuam operáveis em 360 px | Procedimento B (automático, com confirmação no celular) | O mesmo script; celular de referência | `funcoes.csv`, `capturas/funcoes-*.jpg` e `falhas.csv` |
| M2.1.1 | Tarefas T1, T2 e T3 concluídas em cada navegador e sistema | Procedimento C (manual) | Matriz de 6 ambientes, com aparelhos reais nos celulares | `execucoes.csv` e capturas |
| M2.3.1 | Falhas que só ocorrem fora do ambiente de referência | Procedimento D (registro) | Registro de falhas, alimentado por A, B e C | `falhas.csv` |

Os dados brutos ficam em `data/fase-4/flexibilidade/`. A ordem recomendada é A e B (que
levam cerca de 20 minutos e não exigem aparelhos), depois C e, por último, a revisão do
registro de falhas (D).

**Reprodução.** Seguindo as [condições comuns de G2](../fase-2/metricas.md#condicoes-comuns-de-coleta),
uma falha só é atribuída ao ambiente se aparecer de novo em uma segunda execução. Por isso, A e
B rodam 2 vezes, e cada tarefa que falha em C é executada uma segunda vez.

## 2. Preparação

1. Conferir no navegador que o portal abre e que os
   [objetos de referência](ambiente.md#2-paginas-tarefas-e-objetos-de-referencia) existem: UF
   GO, território Chapada dos Veadeiros - GO, camada PRONAF - Valor Total de Crédito Acessado e
   o PTDRS de Estrada de Ferro - GO.
2. Para A e B, instalar o Playwright sem baixar navegadores (é usado o Chrome instalado):

    ```bash
    PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install --no-save playwright@1.48.2
    ```

3. Para C, separar os aparelhos da [matriz de ambientes](#51-matriz-de-ambientes) e atualizar
   os navegadores para a versão estável do dia.
4. Criar ou atualizar `data/fase-4/flexibilidade/README.md` com data, horário, avaliador,
   conexão e as versões do Chrome, do Node.js e do Playwright.

## 3. Procedimento A: rolagem horizontal (M2.2.1)

Na raiz do repositório:

```bash
node scripts/fase-4/flexibilidade/telas.js
```

O script abre cada uma das 3 páginas (Meu Território, SITGeo e Biblioteca Territorial) em cada
uma das 5 larguras, sempre em um contexto novo (cache vazio), espera a rede ficar ociosa e mais
2 s, e então:

1. lê `document.documentElement.scrollWidth` e `clientWidth`. Há rolagem horizontal quando o
   primeiro é maior, que é o teste da ficha de M2.2.1;
2. identifica os elementos que ultrapassam a largura sem estar recortados por um contêiner e
   os registra na coluna `elementos`. Se **todos** estiverem dentro do mapa
   (`.leaflet-container`), a combinação é marcada como `excecao_mapa` e **não** conta como
   rolagem, pela exceção do critério 1.4.10 da WCAG 2.1 prevista na ficha;
3. salva uma captura da tela em `capturas/rolagem-<pagina>-<largura>-e<execucao>.jpg`.

| Largura | Altura | Emulação |
|---:|---:|---|
| 360 px | 800 px | Móvel (toque e *viewport* de celular) |
| 412 px | 915 px | Móvel |
| 768 px | 1024 px | Móvel (tablet) |
| 1366 px | 768 px | Computador |
| 1920 px | 1080 px | Computador |

*Tabela 1: Larguras e emulação do Procedimento A, em zoom de 100% e orientação retrato nos
celulares.*

**Contagem.** Uma combinação só conta como "com rolagem" se a rolagem aparecer nas 2
execuções. A métrica é X = combinações sem rolagem / 15.

**Conferência.** Abrir as capturas das combinações com rolagem e confirmar o elemento indicado.
Se o portal estiver fora do ar em alguma execução, a falha aparece no terminal; repetir o
script inteiro e anotar a repetição no README.

## 4. Procedimento B: funções disponíveis no celular (M2.2.2)

O mesmo comando do Procedimento A executa, em seguida, o Procedimento B.

### 4.1 Estado da página

Algumas funções só aparecem depois de uma ação. Antes da verificação, o script leva cada
página ao mesmo estado nas duas larguras:

| Página | Estado verificado |
|---|---|
| Meu Território | Depois de T1: UF GO, Chapada dos Veadeiros - GO, "Selecionar" e o resultado carregado |
| SITGeo | Depois de T2: camada PRONAF - Valor Total de Crédito Acessado ativa. Se o clique normal na camada falhar, o script força o clique para seguir e registra isso na coluna `observacao` |
| Biblioteca Territorial | Página recém-carregada |

### 4.2 Lista fixa de funções

A lista abaixo foi levantada em 1366 px em 15/11/2026, com a página no estado da seção 4.1.
Ficam fora o cabeçalho, o rodapé e os botões flutuantes, que são comuns a todas as páginas e
não são funções da página avaliada.

| ID | Página | Função | Tipo |
|---|---|---|---|
| MT-01 | Meu Território | Seletores de UF e de território | Controle |
| MT-02 | Meu Território | Botão Selecionar (consulta) | Controle |
| MT-03 | Meu Território | Indicadores gerais do território | Conteúdo |
| MT-04 | Meu Território | Zoom do mapa de abrangência | Controle |
| MT-05 | Meu Território | Botão Municípios em Dados | Controle |
| MT-06 | Meu Território | Botão Baixar Mapa | Controle |
| MT-07 | Meu Território | Abas do Colegiado Territorial | Controle |
| MT-08 | Meu Território | Abas de Políticas Públicas (8 programas) | Controle |
| MT-09 | Meu Território | Botão Analisar do programa | Controle |
| MT-10 | Meu Território | Gráficos do programa | Conteúdo |
| MT-11 | Meu Território | Abas de Principais Produtos | Controle |
| MT-12 | Meu Território | Zoom do mapa de produtos | Controle |
| GEO-01 | SITGeo | Cartões de tema (5) | Controle |
| GEO-02 | SITGeo | Grupos de camadas base (5) | Controle |
| GEO-03 | SITGeo | Ativar e desativar camada do tema | Controle |
| GEO-04 | SITGeo | Nome e dados da camada (fonte e unidade) | Conteúdo |
| GEO-05 | SITGeo | Zoom do mapa | Controle |
| GEO-06 | SITGeo | Legenda da camada ativa | Conteúdo |
| BIB-01 | Biblioteca Territorial | Abas de programa (3) | Controle |
| BIB-02 | Biblioteca Territorial | Botões Baixar das listas e shapefiles | Controle |
| BIB-03 | Biblioteca Territorial | Links de Legislação | Controle |
| BIB-04 | Biblioteca Territorial | Links de Documentos de Apoio | Controle |
| BIB-05 | Biblioteca Territorial | Setas do carrossel da Mapoteca | Controle |
| BIB-06 | Biblioteca Territorial | Buscador de Mapas (programa, UF, território e botão) | Controle |
| BIB-07 | Biblioteca Territorial | Busca do PTDRS (programa, UF e botão) | Controle |

*Tabela 2: Funções verificadas em M2.2.2 (12 em Meu Território, 6 no SITGeo e 7 na
Biblioteca Territorial).*

### 4.3 Critério de função disponível

Para cada elemento da função, o script centraliza o elemento na tela (inclusive dentro de
listas roláveis, como as abas) e verifica se ele está:

1. **visível:** exibido, com largura e altura maiores que zero;
2. **dentro da largura:** sem ultrapassar a borda direita ou esquerda da tela, ou seja, sem
   exigir rolagem horizontal da página para ser alcançado;
3. **livre:** o ponto central do elemento não está coberto por outro elemento;
4. **habilitado e clicável (só controles):** habilitado sempre que estiver habilitado em
   1366 px e aceita o clique (teste de clique do Playwright, que não executa a ação).

A função está **disponível** em uma largura se todos os seus elementos atendem aos critérios e
se nenhum elemento existente em 1366 px falta em 360 px. Entram no denominador (B) apenas as
funções disponíveis em 1366 px nas 2 execuções; uma função é **perdida** em 360 px quando fica
indisponível nas 2 execuções. A métrica, por página, é X = (B − perdidas) / B.

### 4.4 Confirmação no celular de referência

A verificação automática é feita em emulação. Cada função perdida é conferida pelo avaliador
no celular de referência (Chrome/Android), que tenta usá-la sem rolar a página para os lados.
O resultado vai para `falhas.csv` (Procedimento D), na coluna `confirmada_no_aparelho`. Se o
aparelho não confirmar a perda, a função volta a contar como preservada, e a divergência fica
registrada no README.

## 5. Procedimento C: tarefas na matriz de ambientes (M2.1.1)

### 5.1 Matriz de ambientes

| ID | Navegador e sistema | Dispositivo | Largura |
|---|---|---|---|
| AND-CHROME | Chrome/Android | Celular Android real (celular de referência) | Tela do aparelho, retrato |
| AND-SAMSUNG | Samsung Internet/Android | O mesmo celular Android, com o Samsung Internet instalado | Tela do aparelho, retrato |
| IOS-SAFARI | Safari/iOS | iPhone real | Tela do aparelho, retrato |
| WIN-CHROME | Chrome/Windows (**referência**) | Computador com Windows | Janela de 1366 px |
| WIN-EDGE | Edge/Windows | O mesmo computador | Janela de 1366 px |
| WIN-FIREFOX | Firefox/Windows | O mesmo computador | Janela de 1366 px |

*Tabela 3: Ambientes de M2.1.1, da [Fase 2, objetivo G2](../fase-2/objetivos.md#g2-flexibilidade).*

Se um aparelho real não estiver disponível, o ambiente é executado em emulação (por exemplo,
modo de dispositivo do navegador), com `tipo_dispositivo = emulado` e a limitação registrada no
README.

### 5.2 Roteiro das tarefas

Cada tarefa começa na página Início (`/`), com o navegador recém-aberto, zoom de 100% e o
limite de 5 minutos usado no G1.

| Tarefa | Passos | Concluída quando |
|---|---|---|
| T1, consultar um território | Menu → Meu Território; UF **GO**; território **Chapada dos Veadeiros - GO**; Selecionar | Aparecem os Indicadores Gerais e o mapa de abrangência de Chapada dos Veadeiros - GO |
| T2, ativar uma camada no mapa | Menu → SITGeo; tema **Políticas Públicas**; no painel de camadas, ativar **PRONAF - Valor Total de Crédito Acessado** | A camada é desenhada no mapa e a legenda dela aparece |
| T3, baixar um documento | Menu → Biblioteca Territorial; na seção do PTDRS, com o programa **Territorios da Cidadania** (já selecionado), escolher a UF **GO** e clicar em Buscar PTDRS; na tabela, clicar no PTDRS da linha **Estrada De Ferro - GO** | O PTDRS abre ou é baixado |

*Tabela 4: Roteiro de M2.1.1.*

### 5.3 Registro

Para cada ambiente e tarefa, preencher uma linha de `execucoes.csv` (o arquivo já traz as 18
linhas da matriz, com `execucao = 1`):

| Coluna | Conteúdo |
|---|---|
| `resultado` | `concluida` ou `falha` |
| `falha_id` | Se falhou, o ID da falha em `falhas.csv` |
| `navegador_versao`, `sistema_versao` | Versões exatas (menu "Sobre" do navegador e configurações do sistema) |
| `dispositivo`, `tipo_dispositivo` | Modelo do aparelho e `real` ou `emulado` |
| `largura` | Largura da janela em px (no celular, a largura CSS da tela) |
| `avaliador`, `coletado_em`, `captura` | Nome, data e hora, e nome do arquivo da captura do resultado em `capturas/` |

**Falha.** Quando a tarefa falha, o avaliador registra a falha (Procedimento D) e executa a
tarefa de novo no mesmo ambiente, em uma nova linha com `execucao = 2`. A tarefa só conta como
não concluída se a segunda execução também falhar.

## 6. Procedimento D: registro de falhas (M2.3.1)

Toda falha observada em A, B ou C vira uma linha de `falhas.csv`:

| Coluna | Conteúdo |
|---|---|
| `id` | F01, F02, ... (a mesma falha em ambientes diferentes repete o ID, uma linha por ambiente) |
| `ambiente` | ID da matriz (Tabela 3) ou, para falhas vistas em emulação, a emulação e a largura |
| `largura`, `pagina`, `tarefa`, `funcao` | Onde a falha aparece |
| `gravidade` | `bloqueante` (impede a tarefa ou a função), `grave` (dificulta, mas há contorno) ou `cosmetica` (não afeta a tarefa) |
| `descricao`, `passos` | O que acontece e como reproduzir |
| `reproduzida` | `sim` se apareceu na segunda execução |
| `tambem_na_referencia` | `sim` se também ocorre no Chrome/Windows em 1366 px; nesse caso é defeito geral, e não falha de ambiente |
| `confirmada_no_aparelho` | Para falhas vistas em emulação, `sim` ou `não` depois da conferência no aparelho real |
| `origem`, `evidencia` | Métrica que revelou a falha e captura ou arquivo de evidência |

Falhas vistas em emulação são atribuídas aos ambientes móveis da matriz (AND-CHROME,
AND-SAMSUNG e IOS-SAFARI) quando confirmadas no aparelho: nesse caso, o avaliador acrescenta
uma linha por ambiente em que a falha se repete. A métrica é calculada por ambiente, sem o
ambiente de referência, que por definição não tem falhas dependentes de ambiente.

## 7. Consolidação

```bash
scripts/fase-4/flexibilidade/pontuar.py
```

Lê os quatro arquivos, aplica os [níveis de G2](../fase-2/niveis-pontuacao.md#3-g2-flexibilidade)
e as regras de consolidação e grava `pontuacao.csv`. Métricas sem dados ficam **NC** e, nesse
caso, o juízo do G2 fica **pendente**, como manda a regra de cobertura insuficiente
([seção 5.2](../fase-2/niveis-pontuacao.md#52-regras-de-gravidade-e-excecoes)). O script pode
ser executado a qualquer momento: à medida que a matriz manual é preenchida, as métricas
deixam de ser NC.

## 8. Diferenças em relação à Fase 2

- **M2.2.1:** a ficha prevê o modo de dispositivo do Chrome DevTools com o teste no console. O
  script faz o mesmo teste, no mesmo modo de emulação, pelo protocolo do DevTools, e identifica
  o elemento que transborda. Isso evita 30 verificações manuais (15 combinações × 2 execuções)
  e torna a coleta repetível, a mesma decisão tomada no
  [método de eficiência](metodo-eficiencia.md#6-diferenca-em-relacao-a-fase-2).
- **M2.2.2:** a ficha prevê o uso no celular de referência. A verificação passa a ser feita
  primeiro em emulação, com critérios explícitos (seção 4.3), e o celular confirma as perdas
  (seção 4.4). A lista de funções, que a ficha deixava para a Fase 3, está na seção 4.2.
- **M2.3.1:** o ambiente de referência fica fora da contagem por ambiente, porque a ficha
  define a falha de ambiente como a que não ocorre nele.

## 9. Ferramentas, versões e tempo estimado

| Item | Versão |
|---|---|
| Google Chrome | 151.0.7922.108 (modo *headless* novo) |
| Playwright | 1.48.2 |
| Node.js | 24.21.0 |
| Python | 3 (biblioteca padrão), para `pontuar.py` |

Os Procedimentos A e B levam cerca de 20 minutos, a maior parte esperando a consulta de T1,
que leva cerca de 20 s por carregamento ([análise de eficiência](../fase-4/eficiencia.md)). O
Procedimento C leva cerca de 5 minutos por ambiente, ou 30 minutos para a matriz completa,
sem contar a reexecução das falhas.
