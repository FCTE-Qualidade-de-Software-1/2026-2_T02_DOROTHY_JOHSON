# Fase 4 — Executar a avaliação

Nesta fase a equipe coleta as medidas conforme o plano da [Fase 3](../fase-3/index.md),
calcula as métricas, responde às questões e aos objetivos do GQM e atribui a classificação de cada
característica.

## Resultados e classificação

| Característica | Resultado | Classificação final | Análise |
|---|---|---|---|
| **G1 — Capacidade de interação** | Q1.4 = 2,00, Q1.5 = 1,00 e Q1.6 = 0,90; Q1.1–Q1.3 com recortes NC; SUS 50/100; violações críticas de acessibilidade nas cinco páginas; amostra de 4/5 participantes | **NC — relatório encerrado com ressalvas** | [Interação](interacao.md) |
| **G2 — Flexibilidade** | 18/18 tarefas concluídas em seis ambientes; rolagem horizontal na Biblioteca em 360 e 412 px; falhas graves F01 e F04 em celulares, sem bloqueante | **Bom (2,21)** | [Flexibilidade](flexibilidade.md) |
| **G3 — Eficiência de desempenho** | LCP de 23,45 s no SITGeo e 8,27 s em Meu Território; consulta T1 em 20,39 s; teto Aceitável acionado | **Aceitável (1,35)** | [Eficiência](eficiencia.md) |

*Tabela 1: Classificação por característica, conforme os
[critérios da Fase 2](../fase-2/niveis-pontuacao.md#5-criterios-de-classificacao-por-caracteristica).
As classificações são separadas: não se calcula uma nota global do SIT.*

A [classificação final](classificacao-final.md) detalha o cálculo, os limitadores de
gravidade e a coerência com o propósito da [Fase 1](../fase-1/index.md#12-requisitante-e-objetivo).
As [relações entre as características](relacoes-caracteristicas.md) cruzam os três
resultados por página e indicam o que os dados permitem ou não afirmar em conjunto.

## Páginas da fase

1. [Análise e respostas GQM: flexibilidade](flexibilidade.md): matriz completa, Q2.1–Q2.3 e hipóteses respondidas.
2. [Análise e respostas GQM: eficiência de desempenho](eficiencia.md): medianas de cinco execuções por página e tarefa.
3. [Análise e respostas GQM: capacidade de interação](interacao.md): rodada com P01–P04, acessibilidade automática e recortes NC.
4. [Relações entre as características](relacoes-caracteristicas.md): cruzamento de G1, G2 e G3 por página.
5. [Consolidação e cálculo dos resultados](consolidacao.md): como refazer os números a partir dos dados brutos.
6. [Classificação final e coerência com o propósito da F1](classificacao-final.md): classificação por característica e decisões apoiadas para o MDA.
7. [Oportunidades de melhoria](oportunidades-melhoria.md): lista priorizada de G2 e G3.
8. [Ação de melhoria: imagens do SITGeo](acao-melhoria.md): troca de duas imagens, com LCP de 26,45 s para 1,87 s na
   [medição local](acao-melhoria.md#52-efeito-medido), sem implantação no portal.

## Dados

O [mapa dos dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/README.md)
liga cada arquivo bruto à sua métrica e à sua questão, e explica os nomes dos arquivos e as
condições de acesso.

| Conjunto | Conteúdo | Pasta |
|---|---|---|
| Consolidado | Valores por recorte e classificação por característica (`medidas.csv`, `classificacao.csv`) | [`data/fase-4/consolidado/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/consolidado) |
| Capacidade de interação (G1) | Coleta da rodada 01, inspeções, relatórios axe e capturas | [`data/fase-4/capacidade-de-interacao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/capacidade-de-interacao) |
| Flexibilidade (G2) | Execuções, rolagem, funções, falhas, pontuação e capturas | [`data/fase-4/flexibilidade/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/flexibilidade) |
| Eficiência de desempenho (G3) | Relatórios Lighthouse, tempos de tarefa e pontuação | [`data/fase-4/eficiencia/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/eficiencia) |
| Ação de melhoria | Diagnóstico das imagens e medição antes/depois | [`data/fase-4/melhoria/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/melhoria) |

*Tabela 2: Dados brutos e consolidados da Fase 4.*

Para recalcular o consolidado, executar `python3 scripts/fase-4/consolidar.py --verificar`
na raiz do repositório, conforme a [consolidação](consolidacao.md).
