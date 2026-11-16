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

**Pendente.** `execucoes.csv` traz as 18 linhas da matriz (6 ambientes × 3 tarefas) para
preenchimento. Ao terminar, registrar aqui data, avaliadores e aparelhos usados.

## Arquivos

| Arquivo | Conteúdo | Métricas | Gerado por |
|---|---|---|---|
| `rolagem.csv` | Rolagem horizontal das 3 páginas em 5 larguras, 2 execuções (30 linhas) | M2.2.1 | `scripts/fase-4/flexibilidade/telas.js` |
| `funcoes.csv` | Situação das 25 funções em 1366 e 360 px, 2 execuções (100 linhas) | M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `capturas/` | `rolagem-<pagina>-<largura>-e<n>.jpg` (tela visível) e `funcoes-<pagina>-<largura>-e<n>.jpg` (página inteira) | M2.2.1, M2.2.2 | `scripts/fase-4/flexibilidade/telas.js` |
| `execucoes.csv` | Resultado de T1, T2 e T3 em cada ambiente da matriz | M2.1.1 | Preenchimento manual |
| `falhas.csv` | Registro de falhas, com gravidade, reprodução e evidência | M2.3.1 | Preenchimento manual |
| `pontuacao.csv` | Pontuação de cada recorte, questão e do G2 | Todas | `scripts/fase-4/flexibilidade/pontuar.py` |

Páginas: `meu-territorio` (Meu Território), `plataforma-geoespacial` (SITGeo) e `downloads`
(Biblioteca Territorial).

## Desvios em relação ao plano

- Nenhuma execução dos Procedimentos A e B falhou, e as 2 execuções deram o mesmo resultado
  em todas as combinações e funções.
- As falhas F01 a F03 foram vistas em emulação (Chrome em modo de dispositivo). Falta
  confirmá-las no celular de referência (coluna `confirmada_no_aparelho` de `falhas.csv`),
  como manda a seção 4.4 do método.
- O Playwright foi instalado fora do repositório (`npm install --no-save`) e encontrado pela
  variável `NODE_PATH`. Isso não altera a coleta.
