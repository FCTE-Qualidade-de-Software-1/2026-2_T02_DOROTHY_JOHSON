# Dados da avaliação

Mapa dos dados da avaliação da Plataforma Territórios da Cidadania: onde está cada dado bruto,
qual métrica e qual questão do GQM ele responde e como chegar de um resultado publicado até ele
(issue #74, critério F4-C2 e premissa 5 do enunciado).

## Pastas

| Pasta | Conteúdo | Tipo | Detalhes da coleta |
|---|---|---|---|
| `fase-2/piloto/` | Piloto de G3 de 20/10/2026, usado para formular as hipóteses; não entra na classificação | Bruto e resumo | [README](fase-2/piloto/README.md) |
| `fase-4/eficiencia/` | Coleta de G3 de 08/11/2026 | Bruto e derivado | [README](fase-4/eficiencia/README.md) |
| `fase-4/flexibilidade/` | Coleta de G2 de 15/11/2026 (parcial: falta a matriz manual de ambientes) | Bruto e derivado | [README](fase-4/flexibilidade/README.md) |
| `fase-4/melhoria/` | Evidências e medição da ação de melhoria, de 14/11/2026 | Bruto e derivado | [README](fase-4/melhoria/README.md) |
| `fase-4/consolidado/` | Todas as medidas e as classificações, reunidos por `scripts/fase-4/consolidar.py` | Derivado | [Consolidação e cálculo](../docs/fase-4/consolidacao.md) |
| `psm/` | Indicadores de gestão do projeto (PSM/CID); não são dados da avaliação do produto | Bruto | [Plano de medição](../docs/gestao/plano-medicao.md) |

As issues da Fase 4 citam `dados/brutos/` e `dados/consolidados/`. O repositório usa `data/`
desde a Fase 2, com o bruto e o derivado de cada característica na mesma pasta; a distinção está
na tabela abaixo. A estrutura foi mantida porque as páginas e os scripts já apontam para ela.

## Do resultado ao dado bruto

Para rastrear um resultado do artigo ou da GitPage:

1. identificar a métrica (M*x.y.z*) e o recorte (página, tarefa ou ambiente);
2. localizar a linha em [`fase-4/consolidado/medidas.csv`](fase-4/consolidado/medidas.csv); a
   coluna `dado_bruto` indica o arquivo de origem;
3. abrir o arquivo no campo indicado na tabela a seguir.

Para conferir o cálculo inteiro: `scripts/fase-4/consolidar.py --verificar`.

**Exemplo.** "O LCP do SITGeo é de 23,45 s": métrica M3.1.2, recorte SITGeo; a linha de
`medidas.csv` aponta para `data/fase-4/eficiencia/lighthouse/plataforma-geoespacial-<1 a 5>.json`;
o valor é a mediana de `audits["largest-contentful-paint"].numericValue` nas 5 execuções (17 207,
18 850, 23 453, 23 815 e 23 951 ms).

## Mapa arquivo → métrica → questão

| Questão | Métrica | Dado bruto | Campo | Derivado | Resultado publicado |
|---|---|---|---|---|---|
| Q1.1 a Q1.6 | M1.1.1 a M1.6.2 | **Sem coleta** (#71) | — | NC em `consolidado/` | — |
| Q2.1 | M2.1.1 | `fase-4/flexibilidade/execucoes.csv` (**a preencher**, #72) | `resultado` | `flexibilidade/pontuacao.csv` | [Flexibilidade, Q2.1](../docs/fase-4/flexibilidade.md) |
| Q2.2 | M2.2.1 | `fase-4/flexibilidade/rolagem.csv` e `capturas/rolagem-*.jpg` | `rolagem_horizontal` | `flexibilidade/pontuacao.csv` | [Flexibilidade, Tabela 1](../docs/fase-4/flexibilidade.md) |
| Q2.2 | M2.2.2 | `fase-4/flexibilidade/funcoes.csv` e `capturas/funcoes-*.jpg` | `disponivel` | `flexibilidade/pontuacao.csv` | [Flexibilidade, Tabela 2](../docs/fase-4/flexibilidade.md) |
| Q2.3 | M2.3.1 | `fase-4/flexibilidade/falhas.csv` e as capturas da coluna `evidencia` (**parcial**, depende da #72) | `gravidade`, `reproduzida` | `flexibilidade/pontuacao.csv` | [Flexibilidade, Tabela 3](../docs/fase-4/flexibilidade.md) |
| Q3.1 | M3.1.1 | `fase-4/eficiencia/lighthouse/<pagina>-<n>.json` | `audits["first-contentful-paint"].numericValue` | `eficiencia/resumo.csv` e `pontuacao.csv` | [Eficiência, Tabela 1](../docs/fase-4/eficiencia.md) |
| Q3.1 | M3.1.2 | Os mesmos relatórios | `audits["largest-contentful-paint"].numericValue` | Os mesmos | [Eficiência, Tabela 1](../docs/fase-4/eficiencia.md) |
| Q3.2 | M3.2.1 | `fase-4/eficiencia/tarefas.json` | `tempo_s` | Os mesmos | [Eficiência, Tabela 2](../docs/fase-4/eficiencia.md) |
| Q3.3 | M3.3.1 | Os mesmos relatórios de M3.1.1 | `audits["mainthread-work-breakdown"].numericValue` | Os mesmos | [Eficiência, Tabela 3](../docs/fase-4/eficiencia.md) |
| Q3.4 | M3.4.1 | `fase-4/eficiencia/tarefas.json` | `heap_carga_mb` e `heap_tarefa_mb` | Os mesmos | [Eficiência, Tabela 4](../docs/fase-4/eficiencia.md) |
| Ação de melhoria | LCP e peso da página, antes e depois | `fase-4/melhoria/medicao.json` | `lcp_s` e `peso_pagina_kb` | `melhoria/resumo.csv` | [Ação de melhoria, Tabela 6](../docs/fase-4/acao-melhoria.md) |
| Ação de melhoria | Causa do LCP do SITGeo | `fase-4/eficiencia/lighthouse/plataforma-geoespacial-<n>.json` | `audits["largest-contentful-paint-element"]` | `melhoria/diagnostico.csv` e `imagens-pagina.csv` | [Ação de melhoria, Tabela 2](../docs/fase-4/acao-melhoria.md) |

Os três nomes de página usados nos arquivos são `meu-territorio` (Meu Território),
`plataforma-geoespacial` (SITGeo) e `downloads` (Biblioteca Territorial).

## Nomes dos arquivos

Um arquivo bruto precisa informar característica, métrica, data e execução. As coletas já feitas
informam os quatro itens, parte no caminho e parte no conteúdo, e **não foram renomeadas**:

| Item | Coletas de G2 e G3 | Onde está |
|---|---|---|
| Característica | `fase-4/eficiencia/`, `fase-4/flexibilidade/` | Pasta |
| Métrica | Um arquivo alimenta várias métricas (um relatório do Lighthouse serve a M3.1.1, M3.1.2 e M3.3.1) | Mapa acima |
| Data | `coletado_em` (CSV e JSON) e `fetchTime` (Lighthouse), em UTC | Conteúdo |
| Execução | `-<n>` (Lighthouse), `-e<n>` (capturas) ou coluna/campo `execucao` | Nome ou conteúdo |

As datas em UTC podem cair no dia seguinte: a coleta de G3, feita em 08/11/2026 às 21:24 em
Brasília, aparece como 09/11 às 00:24 nos arquivos.

**Para arquivos novos**, usar `<metrica>_<recorte>_<AAAA-MM-DD>_<execucao>.<ext>` na pasta da
característica, em minúsculas e sem espaços (por exemplo,
`m1.6.1_meu-territorio_2026-11-22_e1.json`). Arquivos com dados de participantes usam o código
no lugar do recorte (`m1.5.1_p1_...`).

## Privacidade e condições de acesso

- **Situação atual:** não há dados de participantes no repositório. As coletas de G2 e G3 são
  técnicas, feitas por integrantes da equipe em páginas públicas, sem login. Em 22/11/2026, os
  arquivos JSON e CSV foram verificados por busca automática e não contêm e-mails, CPFs nem
  caminhos de pastas pessoais, e as capturas não têm metadados EXIF.
- **Pessoas citadas:** os READMEs trazem o nome do integrante que fez cada coleta, e `psm/` traz
  os usuários do GitHub da equipe, que já são públicos no repositório.
- **Participantes de G1:** quando houver sessões, valem as
  [condições comuns da Fase 2](../docs/fase-2/metricas.md#condicoes-comuns-de-coleta):
  identificação apenas por código (P1 a P5), sem publicar o vínculo entre código e nome. O termo
  de consentimento e o acesso às gravações são definidos no protocolo de participantes (#68).
- **Acesso:** todos os arquivos deste diretório são públicos, no repositório. A única exceção são
  as imagens originais do portal (`fase-4/melhoria/originais/`), que pertencem ao MDA e não são
  versionadas; `fase-4/melhoria/imagens.csv` traz o endereço, o tamanho e o SHA-256 de cada uma.
