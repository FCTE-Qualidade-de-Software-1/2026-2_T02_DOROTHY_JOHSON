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

Os 6 ambientes da matriz foram executados em 24/11/2026, em duas sessões:

| Item | Celulares | Windows |
|---|---|---|
| Ambientes | AND-CHROME, AND-SAMSUNG, IOS-SAFARI | WIN-CHROME, WIN-EDGE, WIN-FIREFOX |
| Horário (Brasília) | 00:56 a 01:21 | cerca de 16:40 a 16:55 |
| Avaliador | Tales | Gabriel Augusto |
| Aparelho | Samsung Galaxy S24+ (Android 17, 384 px) e iPhone 17 Pro Max (iOS 27.0.1, 440 px), em retrato | Computador com Windows 10 22H2, janela de 1366 px |
| Navegadores | Chrome 158.0.8127.42, Samsung Internet 31.0.0.81, Safari (iOS 27.0.1) | Chrome 157.0.8103.80, Edge 158.0.4370.33, Firefox 161.0 |

Resultado: 18 de 18 execuções concluídas. Capturas em `capturas/tarefa-<ambiente>-<tarefa>-e1.jpg`.

## Procedimento D (confirmação das falhas no aparelho)

Feita no Chrome do Galaxy S24+ (384 px), como manda a seção 4.4 do método:

| Falha | Função | Confirmada no aparelho | Observação | Captura |
|---|---|---|---|---|
| F01 | BIB-05, setas do carrossel da Mapoteca | sim | No aparelho as setas ficam totalmente fora da tela; os outros mapas só são alcançados arrastando o carrossel | `f01-and-chrome-384.jpg` |
| F02 | GEO-05, zoom do mapa | não | Os botões + e – ficam livres e funcionam | `tarefa-and-chrome-t2-e1.jpg` |
| F03 | GEO-04, nome e dados da camada | não | O painel abre como gaveta larga; nome, fonte, unidade e recorte aparecem inteiros | `f03-and-chrome-384.jpg` |

Falhas novas, vistas na matriz manual: F04 (tabela de resultados do PTDRS cortada na lateral,
nos três ambientes de celular) e F05 (modo escuro do Samsung Internet). A tabela de PTDRS
aparece sem o corte no Chrome/Windows a 1366 px (referência), conforme
`referencia-downloads-1366-win-chrome.jpg`. F04 foi reproduzida nos três ambientes móveis
(capturas `f04-<ambiente>-e1.jpg` e `-e2.jpg`). Para a comparação visual de F05 em Meu
Território, a captura pertinente é `tarefa-win-chrome-t1-e1.jpg`, que mostra os Indicadores
Gerais no ambiente de referência; a captura da Biblioteca não documenta essa página.

As referências anteriores em macOS foram mantidas como histórico. A nova comparação em
Windows complementa essas evidências, sem alterar os registros originais dos celulares.

## Arquivos

| Arquivo | Conteúdo | Métricas | Gerado por |
|---|---|---|---|
| `rolagem.csv` | Rolagem horizontal das 3 páginas em 5 larguras, 2 execuções (30 linhas) | M2.2.1 | `scripts/fase-4/flexibilidade/telas.js` |
| `funcoes.csv` | Situação das 25 funções em 1366 e 360 px, 2 execuções (100 linhas) | M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `capturas/` | `rolagem-<pagina>-<largura>-e<n>.jpg` (tela visível) e `funcoes-<pagina>-<largura>-e<n>.jpg` (página inteira) | M2.2.1, M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `capturas/` | `tarefa-<ambiente>-<tarefa>-e1.jpg`, `f0<n>-<ambiente>-*.jpg` e `referencia-downloads-1366-win-chrome.jpg` | M2.1.1, M2.3.1 | Capturas manuais (Procedimentos C e D) |
| `execucoes.csv` | Resultado de T1, T2 e T3 em cada ambiente da matriz | M2.1.1 | Preenchimento manual |
| `falhas.csv` | Registro de falhas, com gravidade, reprodução e evidência | M2.3.1 | Preenchimento manual |
| `pontuacao.csv` | Pontuação de cada recorte, questão e do G2 | Todas | `scripts/fase-4/flexibilidade/pontuar.py` |

Páginas: `meu-territorio` (Meu Território), `plataforma-geoespacial` (SITGeo) e `downloads`
(Biblioteca Territorial).

## Validação da atualização da #72

O pacote `issue72 (1).zip` acrescenta nove capturas de tarefas no Windows e uma captura
da tabela de PTDRS no Chrome/Windows. Os 18 pares ambiente × tarefa têm resultado e
captura associados. As imagens mostram os indicadores/mapa de T1, a camada PRONAF com
legenda de T2 e o PDF de Estrada de Ferro aberto em T3. Versões de navegador, sistema,
avaliadores e horários seguem os registros fornecidos no pacote; os horários do Windows
são aproximados, como indicado em `execucoes.csv`.

`pontuacao.csv` e os arquivos de `data/fase-4/consolidado/` foram regenerados com
`scripts/fase-4/consolidar.py`, incluindo a conferência de F02/F03 prevista na F3.
Com a matriz completa, M2.1.1 = 3,00, M2.2.2 = 8/3, Q2.2 = 11/6 e M2.3.1 = 1,80.
**G2 = 199/90 ≈ 2,21, classificação final Bom**, sem limitador de gravidade acionado.
O valor 2,10 do ZIP usava o cálculo anterior, que ainda contava duas funções do SITGeo
como perdidas. As respostas e hipóteses estão na [análise da #77](../../../docs/fase-4/flexibilidade.md).

## Desvios em relação ao plano

- Nenhuma execução dos Procedimentos A e B falhou, e as 2 execuções deram o mesmo resultado
  em todas as combinações e funções.
- As falhas F01 a F03 foram vistas em emulação (Chrome em modo de dispositivo, 360 px). No
  aparelho real (384 px), só F01 se confirmou. F02 e F03 não se repetiram: pela seção 4.4 do
  método, GEO-04 e GEO-05 voltam a contar como preservadas. O `pontuar.py` aplica
  `confirmada_no_aparelho`, reintegrando GEO-04/GEO-05. Os registros originais de emulação
  permanecem preservados; a conferência em 384 px não comprova correção em 360 px.
- **Coleta em duas sessões e por dois avaliadores.** Os celulares foram testados por Tales
  (madrugada de 24/11) e os ambientes Windows por Gabriel Augusto (tarde de 24/11), no
  computador dele, porque Tales só tem um MacBook.
- **Largura no Windows pelo modo Responsive.** A largura de 1366 px foi fixada pelo modo
  Responsive das ferramentas de desenvolvedor de cada navegador (1366 × 1221), e não
  redimensionando a janela. A largura útil é a mesma; os horários do Windows são aproximados.
- **T1 refeita no IOS-SAFARI.** A primeira tentativa abriu outro território por erro de seleção
  do avaliador. Foi refeita às 01:17 com Chapada dos Veadeiros - GO; vale a segunda.
- **Modo escuro no AND-SAMSUNG.** O Samsung Internet estava com o modo escuro ativo (padrão
  quando o sistema está escuro), o que gerou a F05. Como não há segunda reprodução
  registrada, F05 não entra na pontuação de M2.3.1.
- O Playwright foi instalado fora do repositório (`npm install --no-save`) e encontrado pela
  variável `NODE_PATH`. Isso não altera a coleta.
