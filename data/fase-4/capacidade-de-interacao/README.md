# Dados brutos — G1 Capacidade de interação (rodada 01)

Coleta da [#71](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/71), conforme o [método de G1](../../../docs/fase-3/metodo-interacao.md) e os [formulários de coleta](../../../docs/fase-3/formularios-interacao.md).

| Campo | Valor |
|---|---|
| Período | 22/11/2026 a 24/11/2026 |
| Participantes | P01 a P04 (cidadãos, primeiro acesso); P05 indisponível |
| Objetos de referência | T1: UF GO, Chapada dos Veadeiros - GO; T2: camada PRONAF - Valor Total de Crédito Acessado; T3: PTDRS de Estrada de Ferro - GO |
| Passos mínimos (#70/#115) | T1 = 7, T2 = 5, T3 = 6 |
| axe-core | 4.10.3, regras WCAG 2.1 A e AA, viewport 1366 × 768 |

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `coleta_G1_rodada01.csv` | Ambiente, participantes, tentativas das tarefas, questionários e consolidação de todas as métricas |
| `inspecoes_G1_rodada01.csv` | Ambiente e registros das inspeções M1.1.1, M1.4.1/M1.4.2 e M1.6.1/M1.6.2 |
| `fichas/` | Fichas de observação de P01 a P04, com evidências por tarefa e desvios |
| `axe/` | Resultados completos do axe-core por página |
| `capturas/` | Capturas da autodescrição (`M111_*`) e dos casos de entradas inválidas (`MT-*`, `BT-*`, `FC-*`) |

Gravações, transcrições e termos de consentimento ficam em acesso restrito e não são versionados ([#68](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/68)).
Antes de publicar as fichas individuais de `fichas/`, confirme que são cópias revisadas e
anonimizadas, não os formulários originais preenchidos; originais e qualquer vínculo com nomes
devem permanecer no armazenamento privado, conforme o [protocolo](../../../docs/fase-3/protocolo-participantes.md).

## Resultados

| Métrica | Recorte | Valor |
|---|---|---|
| M1.1.1 Autodescrição | 9 seções | 7/9 = 0,78 |
| M1.1.2 Primeiro clique | T1 / T2 / T3 | 0,75 / 0,00 (0/1 válido) / NC |
| M1.2.1 Conclusão sem ajuda | T1 / T2 / T3 | 1,00 / 0,00 (0/1 válido) / NC |
| M1.3.1 Eficiência do caminho | T1 / T2 / T3 | 0,5148 / NC / NC |
| M1.4.1 Prevenção de erros | 7 casos | 6/7 = 0,86 |
| M1.4.2 Correção de erros | 5 casos com mensagem | 4/5 = 0,80 |
| M1.5.1 SUS | 4 respostas | 50,0 |
| M1.5.2 Aparência | 4 respostas | 4,25 |
| M1.6.1 Regras aprovadas | por página | 0,88 a 0,93 |
| M1.6.2 Críticos + sérios | por página | 5 a 39 (Biblioteca Territorial = 39) |

Os resultados T2/T3 na tabela acima seguem apenas registros cujo ponto de partida atende ao
método. A planilha `coleta_G1_rodada01.csv`, na seção `consolidacao`, preserva também os cálculos
brutos iniciais; eles não devem ser usados para classificar recortes iniciados fora de Início.
Os níveis de pontuação e as respostas GQM estão na
[análise de interação](../../../docs/fase-4/interacao.md) ([#76](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/76)).

## Desvios em relação ao método

- Amostra de 4 participantes; proporções calculadas sobre as observações válidas.
- Sessões remotas por videochamada, com aparelhos e navegadores diferentes entre participantes.
- Navegação contínua entre tarefas, sem nova sessão em Início antes de T2 e T3.
- Enunciados lidos com palavras da moderação e dicas em algumas tarefas (detalhadas nas fichas).
- Piloto (#70) realizado depois das sessões; passos mínimos aplicados às contagens já feitas.
- M1.6: viewport de 1366 × 768 obtido com quadro de mesma origem na aba, sem janela anônima.
- M1.4: casos MT e BT com bloqueio de requisições por script; casos FC com DevTools Offline e emulação de celular.
