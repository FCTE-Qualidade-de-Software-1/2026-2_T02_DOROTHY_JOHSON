# Coleta do GQM G3 (eficiência de desempenho)

Coleta da Fase 4 (issue #73), feita conforme o
[método de eficiência](../../../docs/fase-3/metodo-eficiencia.md) e o
[ambiente da Fase 3](../../../docs/fase-3/ambiente.md).

## Sessão

| Item | Valor |
|---|---|
| Data | 08/11/2026 |
| Início e fim | 21:24 a 21:36 (horário de Brasília) |
| Avaliador | Felipe Rodrigues |
| Conexão | Wi-Fi residencial |
| Chrome | 138.0.7204.157 (modo *headless* novo) |
| Lighthouse | 12.8.2 |
| Node.js | 24.22.1 |
| Playwright | 1.48.2 |
| Objetos de referência | T1: UF GO, Chapada dos Veadeiros - GO; T2: camada PRONAF - Valor Total de Crédito Acessado |

## Arquivos

| Arquivo | Conteúdo | Métricas | Gerado por |
|---|---|---|---|
| `lighthouse/<pagina>-<n>.json` | Relatório completo do Lighthouse, 5 execuções por página | M3.1.1, M3.1.2, M3.3.1 | `scripts/fase-4/eficiencia/lighthouse.sh` |
| `tarefas.json` | Tempo de T1 e T2 e JS heap após o carregamento e após a tarefa, 5 execuções cada; JS heap após o carregamento da Biblioteca Territorial | M3.2.1, M3.4.1 | `scripts/fase-4/eficiencia/tarefas.js` |
| `resumo.csv` | Mediana, mínimo e máximo de cada métrica | Todas | `scripts/fase-4/eficiencia/resumo.sh` |

Páginas: `meu-territorio` (Meu Território), `plataforma-geoespacial` (SITGeo) e `downloads`
(Biblioteca Territorial).

## Desvios em relação ao plano

- Nenhuma execução falhou: as 15 execuções do Lighthouse terminaram sem `runtimeError`, e as 15
  execuções do script de tarefas não precisaram ser repetidas.
- O Playwright foi instalado com `npm install --no-save` e ficou em `~/node_modules`, porque já
  existia um `package.json` na pasta pessoal do avaliador. Isso não altera a coleta.
