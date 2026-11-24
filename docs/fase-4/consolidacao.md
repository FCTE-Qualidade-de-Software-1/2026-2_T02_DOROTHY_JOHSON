# Consolidação e cálculo dos resultados

Esta página documenta como os dados brutos viram medidas, pontos e classificação: o comando que
refaz tudo, as fórmulas e o tratamento de valores ausentes e atípicos
([issue #75](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/issues/75)).
Ela não define regras novas: as definições são das [fichas da Fase 2](../fase-2/metricas.md), dos
[níveis de pontuação](../fase-2/niveis-pontuacao.md) e dos métodos da Fase 3.

## 1. Como reproduzir

Na raiz do repositório, com Python 3, bash e `jq` (nenhum script acessa o portal):

```bash
scripts/fase-4/consolidar.py --verificar   # recalcula em pasta temporária e compara; não altera nada
scripts/fase-4/consolidar.py               # recalcula e grava os arquivos que mudaram
```

O comando valida os dados brutos, executa os scripts de cada característica e reúne os
resultados. Com `--verificar`, termina com erro se algum arquivo publicado não puder ser
reproduzido a partir do dado bruto.

| Etapa | Entrada (dado bruto) | Script | Saída |
|---|---|---|---|
| G3, medianas | `eficiencia/lighthouse/*.json` e `eficiencia/tarefas.json` | `eficiencia/resumo.sh` | `eficiencia/resumo.csv` |
| G3, pontos | `eficiencia/resumo.csv` | `eficiencia/pontuar.py` | `eficiencia/pontuacao.csv` |
| G2, pontos | `flexibilidade/rolagem.csv`, `funcoes.csv`, `execucoes.csv` e `falhas.csv` | `flexibilidade/pontuar.py` | `flexibilidade/pontuacao.csv` |
| Melhoria, evidências | `eficiencia/lighthouse/plataforma-geoespacial-*.json` | `melhoria/diagnostico.py` | `melhoria/diagnostico.csv` e `imagens-pagina.csv` |
| Melhoria, efeito | `melhoria/medicao.json` | `melhoria/medir.js` (acessa o portal; aqui só o cálculo é conferido) | `melhoria/resumo.csv` |
| Reunião | As saídas acima | `consolidar.py` | `consolidado/medidas.csv` e `consolidado/classificacao.csv` |

*Tabela 1: Do dado bruto ao resultado. Os dados ficam em `data/fase-4/`, e os scripts, em
`scripts/fase-4/`.*

| Arquivo consolidado | Uma linha por | Conteúdo |
|---|---|---|
| [`medidas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/consolidado/medidas.csv) | Recorte de cada uma das 19 métricas | Valor, mínimo, máximo, execuções, pontos, nível, situação e caminho do dado bruto |
| [`classificacao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/consolidado/classificacao.csv) | Métrica, questão e característica | Pontos, classificação pela média, limitador e classificação final |

*Tabela 2: Arquivos consolidados.*

## 2. Fórmulas

### 2.1 Da coleta ao valor da métrica

| Métrica | Fórmula | Unidade |
|---|---|---|
| M2.1.1 | Por ambiente: tarefas concluídas / 3. Uma falha só conta se a reexecução também falhar | Proporção |
| M2.2.1 | Combinações página × largura sem rolagem / 15. Só conta como rolagem a que aparece nas 2 execuções | Proporção |
| M2.2.2 | Por página: (B − perdidas) / B, com B = funções disponíveis em 1366 px nas 2 execuções e perdidas = indisponíveis em 360 px nas 2 execuções; perdas explicitamente não confirmadas no aparelho voltam a contar como preservadas (F3, seção 4.4) | Proporção |
| M2.3.1 | Por ambiente, sem a referência: contagem de falhas reproduzidas, por gravidade | Falhas |
| M3.1.1, M3.1.2 e M3.3.1 | Por página: mediana de 5 execuções do `numericValue` do Lighthouse / 1000 (FCP, LCP e tempo na thread principal) | s |
| M3.2.1 | Por tarefa: mediana de 5 execuções de `tempo_s` | s |
| M3.4.1 | Por momento: mediana de 5 execuções de `heap_carga_mb` ou `heap_tarefa_mb` | MB |

*Tabela 3: Fórmulas das métricas de G1, G2 e G3. As de G1 estão nas
[fichas da Fase 2](../fase-2/metricas.md#g1-capacidade-de-interacao).*

### 2.2 Do valor à classificação

1. **Recorte:** o valor não arredondado recebe de 0 a 3 pontos pelas faixas da Fase 2.
2. **Métrica:** média dos pontos dos seus recortes.
3. **Questão:** média das suas métricas.
4. **Característica:** média das suas questões, convertida em classificação e submetida aos
   [limitadores](../fase-2/niveis-pontuacao.md#52-regras-de-gravidade-e-excecoes).

O arredondamento ocorre só na apresentação. Exemplo, Q3.1: M3.1.1 = (2 + 2 + 2) / 3 = 2,00;
M3.1.2 = (0 + 0 + 1) / 3 = 0,33; Q3.1 = (2,00 + 0,33) / 2 = 1,17.

## 3. Valores ausentes

| Situação | Tratamento |
|---|---|
| Menos de 5 execuções válidas em um recorte de G3 | Recorte **NC** (não classificável); a mediana parcial é mostrada com o número real de execuções |
| Ambiente da matriz de G2 sem as 3 tarefas, ou com falha sem reexecução | Ambiente **NC** |
| Tarefa G1 iniciada fora de Início, quando a métrica exige esse ponto de partida | Observação não entra no recorte; se não restar observação válida, o recorte fica **NC** |
| Métrica com algum recorte NC | Métrica, questão e característica ficam **pendentes** |
| Linha ou captura que falta em G2, relatório com `runtimeError` ou valor nulo | O cálculo é **interrompido** com a lista dos problemas, para ser corrigido na origem |

*Tabela 4: Tratamento de valores ausentes.*

Nenhum valor ausente é estimado, e NC nunca vira 0 nem 3
([regra 5 da Fase 2](../fase-2/niveis-pontuacao.md#1-escala-comum-e-regras-de-aplicacao)).

**Situação atual:** dos 55 recortes listados em `medidas.csv`, 51 estão classificados (20 de G1,
15 de G2 e todos os 16 de G3) e 4 são NC:

- 4 de G1: M1.1.2/T3, M1.2.1/T3 e M1.3.1/T2–T3. A rodada tem 4 dos 5 participantes previstos;
  os recortes NC também refletem tarefas iniciadas fora de Início
  ([coleta](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/fase-4/capacidade-de-interacao/README.md) e [análise](interacao.md));

G2 tem a matriz completa: 18/18 tarefas concluídas nos seis ambientes, sem recortes NC.
A [análise de flexibilidade](flexibilidade.md) apresenta Q2.1 = 3,00, Q2.2 = 11/6,
Q2.3 = 1,80 e G2 = 199/90 ≈ 2,21, classificação final Bom, sem limitador acionado.

Em G2, `falhas.csv` também é fonte de M2.2.2: F02/F03 não foram confirmadas no aparelho,
reintegrando GEO-04/GEO-05. O SITGeo recebe 3 pontos (6/6), M2.2.2 = 8/3 e Q2.2 = 11/6
(1,83 na apresentação). A emulação original permanece em `funcoes.csv`.

## 4. Valores atípicos

Nenhuma execução válida é descartada, e nenhum teste de exclusão é aplicado: com 5 execuções,
uma regra de corte teria pouca base. Em vez disso:

- **G3:** a mediana reduz o peso de uma execução isolada
  ([método, seção 5](../fase-3/metodo-eficiencia.md#5-consolidacao)), e o mínimo e o máximo são
  sempre publicados;
- **G2:** o resultado só conta quando se repete na segunda execução
  ([método, seções 3 e 4](../fase-3/metodo-flexibilidade.md#3-procedimento-a-rolagem-horizontal-m221)).

**Análise de sensibilidade.** As colunas `pontos_no_minimo` e `pontos_no_maximo` mostram o nível
que cada recorte de G3 teria com a menor e com a maior das 5 execuções. Só dois dos 16 recortes
mudam de nível:

| Recorte | Mínimo | Mediana (usada) | Máximo |
|---|---|---|---|
| M3.1.2, LCP da Biblioteca Territorial | 3,89 s: Aceitável (1) | 3,91 s: Aceitável (1) | 4,43 s: Insatisfatório (0) |
| M3.3.1, CPU da Biblioteca Territorial | 1,62 s: Excelente (3) | 2,23 s: Bom (2) | 4,60 s: Insatisfatório (0) |

*Tabela 5: Recortes de G3 cujo nível depende da execução.*

Com os dois recortes no pior nível, o G3 cairia de 1,35 para 1,14; no melhor, subiria para 1,43.
Nos dois casos **a classificação continua Aceitável**, então a dispersão não a altera. Ela
indica apenas que os níveis da Biblioteca Territorial devem ser lidos com cautela.
