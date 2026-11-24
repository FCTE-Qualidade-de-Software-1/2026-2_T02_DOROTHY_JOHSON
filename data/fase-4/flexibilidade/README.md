# Coleta do GQM G2 (flexibilidade)

Coleta da Fase 4 (issue #72), feita conforme o
[método de flexibilidade](../../../docs/fase-3/metodo-flexibilidade.md) e o
[ambiente da Fase 3](../../../docs/fase-3/ambiente.md).

## Sessão dos Procedimentos A e B (automáticos)

| Item | Valor |
|---|---|
| Data | 15/11/2026 |
| Início e fim | 20:24 a 20:38 (horário de Brasília) |
| Avaliador | Cayo Felipe Alencar Câmara |
| Conexão | Rede residencial |
| Chrome | 151.0.7922.108 (modo *headless* novo), Linux |
| Playwright | 1.48.2 |
| Node.js | 24.21.0 |
| Execuções | 2 (a segunda confirma a primeira) |
| Objetos de referência | T1: UF GO, Chapada dos Veadeiros - GO; T2: camada PRONAF - Valor Total de Crédito Acessado |

## Procedimento C (matriz manual de ambientes)

| Item | Valor |
|---|---|
| Data | 24/11/2026 |
| Início e fim | 00:56 a 01:21 (horário de Brasília) |
| Avaliador | Tales |
| Aparelhos | Samsung Galaxy S24+ (Android 17, largura CSS 384 px) e iPhone 17 Pro Max (iOS 27.0.1, 440 px), ambos reais, em retrato |
| Navegadores | Chrome 158.0.8127.42 e Samsung Internet 31.0.0.81 no Android; Safari no iOS 27.0.1 |
| Ambientes executados | AND-CHROME, AND-SAMSUNG e IOS-SAFARI (9 de 18 linhas) |
| Ambientes não executados | WIN-CHROME, WIN-EDGE e WIN-FIREFOX (ver Desvios) |
| Capturas | `capturas/tarefa-<ambiente>-<tarefa>-e1.jpg` |

## Procedimento D (confirmação das falhas no aparelho)

Feita no Chrome do Galaxy S24+ (384 px), como manda a seção 4.4 do método:

| Falha | Função | Confirmada no aparelho | Observação | Captura |
|---|---|---|---|---|
| F01 | BIB-05, setas do carrossel da Mapoteca | sim | No aparelho as setas ficam totalmente fora da tela; os outros mapas só são alcançados arrastando o carrossel | `f01-and-chrome-384.jpg` |
| F02 | GEO-05, zoom do mapa | não | Os botões + e – ficam livres e funcionam | `tarefa-and-chrome-t2-e1.jpg` |
| F03 | GEO-04, nome e dados da camada | não | O painel abre como gaveta larga; nome, fonte, unidade e recorte aparecem inteiros | `f03-and-chrome-384.jpg` |

Falhas novas, vistas na matriz manual: F04 (tabela de resultados do PTDRS cortada na lateral,
nos três ambientes de celular) e F05 (modo escuro do Samsung Internet). As duas não ocorrem no
Chrome a 1366 px (macOS), conforme `referencia-downloads-1366-macos.jpg` e
`referencia-plataforma-geoespacial-1366-macos.jpg`. F04 foi reproduzida nos três ambientes
(capturas `f04-<ambiente>-e1.jpg` e `-e2.jpg`).

## Arquivos

| Arquivo | Conteúdo | Métricas | Gerado por |
|---|---|---|---|
| `rolagem.csv` | Rolagem horizontal das 3 páginas em 5 larguras, 2 execuções (30 linhas) | M2.2.1 | `scripts/fase-4/flexibilidade/telas.js` |
| `funcoes.csv` | Situação das 25 funções em 1366 e 360 px, 2 execuções (100 linhas) | M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `capturas/` | `rolagem-<pagina>-<largura>-e<n>.jpg` (tela visível) e `funcoes-<pagina>-<largura>-e<n>.jpg` (página inteira) | M2.2.1, M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `capturas/` | `tarefa-<ambiente>-<tarefa>-e1.jpg`, `f0<n>-<ambiente>-*.jpg` e `referencia-*-1366-macos.jpg` | M2.1.1, M2.3.1 | Capturas manuais (Procedimentos C e D) |
| `execucoes.csv` | Resultado de T1, T2 e T3 em cada ambiente da matriz | M2.1.1 | Preenchimento manual |
| `falhas.csv` | Registro de falhas, com gravidade, reprodução e evidência | M2.3.1 | Preenchimento manual |
| `pontuacao.csv` | Pontuação de cada recorte, questão e do G2 | Todas | `scripts/fase-4/flexibilidade/pontuar.py` |

Páginas: `meu-territorio` (Meu Território), `plataforma-geoespacial` (SITGeo) e `downloads`
(Biblioteca Territorial).

## Desvios em relação ao plano

- Nenhuma execução dos Procedimentos A e B falhou, e as 2 execuções deram o mesmo resultado
  em todas as combinações e funções.
- As falhas F01 a F03 foram vistas em emulação (Chrome em modo de dispositivo, 360 px). No
  aparelho real (384 px), só F01 se confirmou. F02 e F03 não se repetiram: pela seção 4.4 do
  método, GEO-04 e GEO-05 voltam a contar como preservadas. O `pontuar.py` não lê a coluna
  `confirmada_no_aparelho`, então a M2.2.2 do SITGeo em `pontuacao.csv` ainda conta as duas como
  perdidas e precisa desse ajuste.
- **Ambientes Windows não executados; coleta encerrada assim.** O avaliador não tem computador
  com Windows, só um MacBook (macOS), então WIN-CHROME, WIN-EDGE e WIN-FIREFOX não puderam ser
  executados e ficaram sem resultado em `execucoes.csv`. A coleta da #72 foi encerrada com os
  3 ambientes de celular. Consequência: a M2.1.1 e a M2.3.1 ficam NC e o G2 fica pendente
  (cobertura insuficiente, seção 5.2), o que precisa ser tratado na análise (#77).
- **Referência trocada.** Sem o WIN-CHROME, a coluna `tambem_na_referencia` de F04 e F05 foi
  conferida no Chrome do macOS com janela de 1366 px.
- **T1 refeita no IOS-SAFARI.** A primeira tentativa abriu outro território por erro de seleção
  do avaliador. Foi refeita às 01:17 com Chapada dos Veadeiros - GO; vale a segunda.
- **Modo escuro no AND-SAMSUNG.** O Samsung Internet estava com o modo escuro ativo (padrão
  quando o sistema está escuro), o que gerou a F05.
- O Playwright foi instalado fora do repositório (`npm install --no-save`) e encontrado pela
  variável `NODE_PATH`. Isso não altera a coleta.
