# Ação de melhoria: imagens do SITGeo

O enunciado exige que a equipe execute ao menos uma ação de melhoria, justificada pelas
evidências da avaliação (seção 3.2, item 2). Esta página registra a escolha da ação, a
justificativa, a entrega técnica e a forma de medir o efeito. Ela parte da
[análise de eficiência de desempenho](eficiencia.md) e atende à decisão 2 do requisitante
([Fase 1, seção 1.2](../fase-1/index.md#12-requisitante-e-objetivo)): saber se é preciso
otimizar páginas e mapas para conexões móveis, e por onde começar.

| Item | Valor |
|---|---|
| Ação | Redimensionar e converter as duas imagens que dominam o carregamento do SITGeo |
| Tipo (enunciado, seção 3.2) | Modificação técnica para um problema objetivo (tempo de resposta) |
| Métrica que motiva | M3.1.2, LCP do SITGeo: 23,45 s, nível Insatisfatório (0) |
| Entrega técnica | Imagens otimizadas, alteração proposta no código e scripts de geração e de medição |
| Situação | Entrega produzida e efeito medido em 14/11/2026 (seção 5); a implantação no portal depende do MDA |

## 1. Escolha da ação

A [análise do G3](eficiencia.md#3-classificacao-do-g3) lista três recortes com nível
Insatisfatório, na ordem de prioridade dos
[critérios de classificação](../fase-2/niveis-pontuacao.md#53-da-pontuacao-a-decisao-de-qualidade).
A equipe comparou os três por dois critérios: se a causa pode ser identificada em uma
avaliação caixa-preta e se a correção pode ser produzida sem acesso ao código do portal.

| Prioridade | Problema (métrica) | Causa identificada | Correção executável pela equipe | Decisão |
|:---:|---|---|---|---|
| 1 | T1 leva 20,39 s (M3.2.1) | Não. O atraso ocorre nas requisições disparadas pelo clique em "Selecionar", e a origem (consulta, volume de dados ou servidor) não é observável de fora | Não | Recomendada ao MDA como investigação (seção 6) |
| 2 | LCP do SITGeo de 23,45 s (M3.1.2) | Sim. O elemento do LCP é uma imagem de 2,55 MB exibida em 343 × 264 px | Sim | **Escolhida** |
| 3 | LCP de Meu Território de 8,27 s (M3.1.2) | Em parte. O conteúdo principal só aparece depois da execução do JavaScript (atraso de renderização de 7,3 s; 489 KiB de JavaScript não usado) | Não. Exige dividir o código-fonte | Recomendada ao MDA (seção 6) |

*Tabela 1: Candidatas à ação de melhoria, a partir dos recortes Insatisfatórios do G3.*

A ação escolhida é a de maior prioridade entre as que a equipe consegue executar e medir. As
características G1 e G2 não entraram na comparação porque suas coletas ainda não estavam
concluídas na data da escolha; o enunciado pede ao menos uma ação, e as oportunidades de G1 e
G2 entram na lista de melhorias da Fase 4.

## 2. Justificativa: o que as medidas mostram

Os dados vêm dos 5 relatórios do Lighthouse da coleta de 08/11/2026
(`data/fase-4/eficiencia/lighthouse/plataforma-geoespacial-<n>.json`), resumidos por
`scripts/fase-4/melhoria/diagnostico.py` em `data/fase-4/melhoria/diagnostico.csv`.

| Evidência | Mediana (mín.–máx.) |
|---|---|
| LCP do SITGeo (M3.1.2) | 23,45 s (17,21–23,95) |
| Elemento do LCP, nas 5 execuções | `<img src="/img/capa_inicio.jpg">`, exibido em 343 × 264 px |
| Fase do LCP gasta baixando essa imagem | 18,66 s (12,74–19,36) |
| Peso total da página | 5,34 MB |
| Peso das imagens `capa_inicio.jpg` e `indicadores.png` | 4,48 MB, ou 84% da página |
| Economia de tempo estimada pelo Lighthouse com imagens no tamanho de exibição | 12,25 s (12,02–12,47) |

*Tabela 2: Evidências que motivam a ação.*

Três pontos sustentam a escolha:

1. **A causa é localizada.** Das fases do LCP, o download da imagem responde pela maior parte
   do tempo (18,66 s). As outras três fases somam cerca de 4,4 s: resposta do servidor
   (0,95 s), atraso até o início do download (2,75 s) e renderização (0,73 s).
2. **O desperdício é mensurável.** No perfil avaliado, a imagem ocupa 343 × 264 px na tela.
   Mesmo com tela de alta densidade, cerca de 960 px de largura bastam. O Lighthouse classifica
   4,26 MB das imagens da página como bytes que não chegam a ser exibidos (GOOGLE, [s.d.]).
3. **O problema é um desvio, não uma decisão de projeto.** As outras três imagens
   ilustrativas da mesma página têm entre 22 e 67 kB (Tabela 3). Só duas fogem do padrão.

| Imagem | Transferência |
|---|---:|
| `capa_inicio.jpg` | 2 554,0 kB |
| `indicadores.png` | 1 929,2 kB |
| `demografia.jpg` | 67,0 kB |
| `povos_comunidades_tradicionais.png` | 23,5 kB |
| `socioeconomico.jpg` | 22,1 kB |

*Tabela 3: Imagens ilustrativas carregadas pelo SITGeo (`data/fase-4/melhoria/imagens-pagina.csv`).*

Para o público do objetivo G3, que acessa por celular de entrada com rede móvel lenta
([Fase 2, objetivo G3](../fase-2/objetivos.md#g3-eficiencia-de-desempenho)), o efeito é duplo:
espera de mais de 20 s pelo conteúdo principal e consumo de 4,48 MB do plano de dados em duas
imagens ilustrativas, a cada visita sem cache.

## 3. Como o efeito é medido

A equipe não pode alterar o portal. O efeito é medido carregando a página real e trocando
apenas as duas imagens pelas versões otimizadas no momento da requisição.

| Elemento | Definição |
|---|---|
| Indicador principal | LCP do SITGeo (s), a mesma grandeza de M3.1.2 |
| Indicador secundário | Peso da página (kB transferidos) |
| Condição "antes" | Página em produção, sem alteração |
| Condição "depois" | Mesma página, com `capa_inicio.jpg` e `indicadores.png` redirecionadas para as versões WebP de 960 px, hospedadas na GitPage da equipe |
| Ambiente | O da [Fase 3, seção 3.1](../fase-3/ambiente.md#31-eficiencia-de-desempenho-g3): celular simulado de 412 × 823 px, latência de 150 ms, 1,6 Mbit/s, CPU 4 vezes mais lenta e cache vazio |
| Execuções | 5 por condição, alternadas (antes, depois, antes, ...), para que a variação do servidor afete as duas do mesmo modo |
| Valor do indicador | Mediana das 5 execuções, com mínimo e máximo, como nas métricas do G3 |
| Instrumento | `scripts/fase-4/melhoria/medir.js` (Playwright e protocolo do Chrome DevTools) |

**Efeito esperado.** A estimativa do Lighthouse (Tabela 2) indica redução de cerca de metade do
LCP. A equipe espera redução de pelo menos 50% no LCP e de pelo menos 75% no peso da página.
Como as demais fases do LCP somam cerca de 4,4 s, a ação sozinha pode não levar o SITGeo ao
nível Aceitável (LCP de até 4,0 s): ela remove a maior parcela do atraso, e o restante depende
das recomendações da seção 6.

**Comparação com M3.1.2.** O script aplica a limitação de rede no próprio navegador, enquanto
o Lighthouse a aplica por simulação
([Fase 3, riscos do ambiente](../fase-3/ambiente.md#5-riscos-do-ambiente)). Por isso o "antes"
é medido de novo com o mesmo script, e a comparação válida é entre as duas condições desta
medição, não entre o "depois" e os 23,45 s da coleta do G3.

## 4. Entrega técnica

### 4.1 Problema original e solução proposta

| Aspecto | Problema original | Solução proposta |
|---|---|---|
| Arquivos | `capa_inicio.jpg` (JPEG, 2 554 kB) e `indicadores.png` (PNG, 1 929 kB), servidos no tamanho original para qualquer tela | Versões WebP de 480 e 960 px de largura para cada imagem |
| Marcação | `<img src="/img/capa_inicio.jpg">`, sem `srcset` | `srcset` e `sizes`, para o navegador escolher a menor versão suficiente |
| Prioridade de carga | A imagem do LCP começa a ser baixada 2,75 s depois da resposta do servidor | `fetchpriority="high"` na imagem do LCP |
| Prevenção | Nenhum controle do peso das imagens publicadas | Limite de peso por imagem verificado antes da publicação (seção 6) |

*Tabela 4: Problema original e solução proposta.*

### 4.2 Arquivos da entrega

| Arquivo | Conteúdo |
|---|---|
| `scripts/fase-4/melhoria/diagnostico.py` | Extrai as evidências da Tabela 2 dos relatórios do Lighthouse |
| `scripts/fase-4/melhoria/otimizar.py` | Baixa as duas imagens, redimensiona, converte para WebP e grava o inventário |
| `docs/fase-4/melhoria/img/` | Imagens otimizadas: `capa_inicio-480.webp`, `capa_inicio-960.webp`, `indicadores-480.webp` e `indicadores-960.webp` |
| `scripts/fase-4/melhoria/medir.js` | Mede o LCP e o peso da página, antes × depois |
| `data/fase-4/melhoria/` | Evidências e resultados: `diagnostico.csv`, `imagens-pagina.csv`, `imagens.csv`, `medicao.json` e `resumo.csv` |

As imagens originais pertencem ao portal do MDA. As versões otimizadas são derivadas delas e
estão no repositório apenas como demonstração da correção.

### 4.3 Alteração proposta no código

O portal é uma aplicação Next.js (os recursos são servidos em `/_next/static/`). A correção
pode ser feita de duas formas equivalentes.

Com as imagens geradas por esta entrega, em HTML:

```html
<img
  src="/img/capa_inicio-960.webp"
  srcset="/img/capa_inicio-480.webp 480w, /img/capa_inicio-960.webp 960w"
  sizes="(max-width: 768px) 90vw, 320px"
  width="320" height="240"
  alt="Políticas Públicas"
  fetchpriority="high">
```

Com o componente de imagem do próprio Next.js, que gera as versões e o `srcset` no servidor:

```jsx
import Image from "next/image";

<Image
  src="/img/capa_inicio.jpg"
  alt="Políticas Públicas"
  width={320}
  height={240}
  sizes="(max-width: 768px) 90vw, 320px"
  priority
/>
```

A mesma alteração vale para `indicadores.png`, sem `fetchpriority` nem `priority`, porque essa
imagem não é o elemento do LCP. O valor de `sizes` supõe o cartão de 320 px observado no
portal; a equipe do MDA deve ajustá-lo ao leiaute real em telas maiores.

### 4.4 Como reproduzir

Na raiz do repositório, com o ambiente da
[Fase 3](../fase-3/metodo-eficiencia.md#2-preparacao) e o Pillow instalado
(`pip install pillow`):

```bash
scripts/fase-4/melhoria/diagnostico.py   # evidências (não acessa o portal)
scripts/fase-4/melhoria/otimizar.py      # gera as imagens e data/fase-4/melhoria/imagens.csv
node scripts/fase-4/melhoria/medir.js    # mede antes × depois (cerca de 10 minutos)
```

O `medir.js` carrega as imagens otimizadas da GitPage, portanto elas precisam estar publicadas
antes da medição. Para medir antes de publicar, usar
`OTIMIZADAS=docs/fase-4/melhoria/img node scripts/fase-4/melhoria/medir.js`; nesse modo o tempo
de transferência das duas imagens é simulado a partir do tamanho dos arquivos, e o modo usado
fica registrado em `medicao.json`.

## 5. Resultado

### 5.1 Imagens geradas

| Arquivo | Tipo | Formato | Dimensões (px) | Tamanho (kB) |
|---|---|---|---|---:|
| `capa_inicio.jpg` | original | JPEG | 5568 × 3132 | 2553,7 |
| `capa_inicio-480.webp` | otimizada | WEBP | 480 × 270 | 47,8 |
| `capa_inicio-960.webp` | otimizada | WEBP | 960 × 540 | 151,7 |
| `indicadores.png` | original | PNG | 1999 × 1142 | 1928,9 |
| `indicadores-480.webp` | otimizada | WEBP | 480 × 274 | 12,2 |
| `indicadores-960.webp` | otimizada | WEBP | 960 × 548 | 26,0 |

*Tabela 5: Imagens originais e otimizadas (`data/fase-4/melhoria/imagens.csv`), geradas em 14/11/2026.*

As duas imagens passam de 4 482,5 kB para 177,7 kB nas versões de 960 px, uma redução de
96,0%. A original `capa_inicio.jpg` tem 5568 × 3132 px e é exibida em 343 × 264 px.

### 5.2 Efeito medido

| Medida | Antes (mín.–máx.) | Depois (mín.–máx.) | Variação |
|---|---|---|---:|
| LCP (s) | 26,45 (26,42–26,63) | 1,87 (1,64–2,07) | −92,9% |
| Peso da página (kB) | 5338 (5338–5339) | 1033 (1033–1033) | −80,7% |

*Tabela 6: LCP e peso do SITGeo antes e depois da troca das imagens; mediana de 5 execuções
por condição (`data/fase-4/melhoria/medicao.json` e `resumo.csv`).*

| Item | Valor |
|---|---|
| Data e horário | 14/11/2026, das 18:34 às 18:36 (horário de Brasília) |
| Avaliador | Artur Henrique Holz Bartz |
| Modo da troca | `local`: imagens otimizadas lidas do repositório, com o tempo de transferência simulado pelo tamanho do arquivo |
| Versão otimizada usada | 960 px |
| Navegador | Google Chrome 157.0.8103.51, em modo *headless* |
| Elemento do LCP | `capa_inicio.jpg` nas duas condições, em todas as execuções |
| Execuções com falha | Nenhuma |

**Interpretação.** O efeito esperado da seção 3 foi atingido: o LCP caiu 92,9% (esperado: pelo
menos 50%) e o peso da página caiu 80,7% (esperado: pelo menos 75%). A variação entre
execuções é pequena nas duas condições, e o elemento do LCP continua sendo a mesma imagem, o
que indica que a redução vem da troca dos arquivos, e não de outra mudança na página.

**Cuidados ao ler o resultado:**

- **O "depois" é otimista.** No modo `local`, as duas imagens não disputam a banda limitada
  com os demais recursos da página (cerca de 855 kB de scripts, fontes, estilos e blocos do
  mapa). Com as imagens servidas pela rede, o LCP do "depois" tende a ser maior que 1,87 s. A
  medição pela rede (`medir.js` sem `OTIMIZADAS`) deve ser repetida depois que as imagens
  estiverem publicadas na GitPage.
- **Não é uma nova medida de M3.1.2.** O valor de 1,87 s cairia na faixa Bom de M3.1.2 (de 1,5
  a 2,5 s), mas foi obtido com outro instrumento e outra máquina. A classificação do G3 continua
  sendo a da [análise de eficiência](eficiencia.md#3-classificacao-do-g3). A previsão da seção 3
  de que restariam cerca de 4,4 s vinha das fases do LCP estimadas pelo Lighthouse, que simula
  a rede de outra forma; os dois números não são comparáveis diretamente.
- **Ambiente diferente do da Fase 3.** A medição foi feita em outra máquina, com Windows, e
  com versões mais novas do Chrome e do Node.js
  (`data/fase-4/melhoria/README.md`). Como "antes" e "depois" foram medidos na mesma sessão
  e na mesma máquina, a comparação entre as duas condições não é afetada.

## 6. Recomendações ao requisitante

Em ordem de prioridade para o backlog do MDA:

1. **Implantar a correção das duas imagens** (seção 4.3) e repetir a coleta do G3
   ([método de eficiência](../fase-3/metodo-eficiencia.md)) para confirmar o efeito em produção.
2. **Investigar a T1** (20,39 s após o clique em "Selecionar"): medir no servidor o tempo e o
   tamanho das respostas da consulta de território, que a avaliação caixa-preta não alcança.
3. **Reduzir o JavaScript de Meu Território** (489 KiB não usados no carregamento), que atrasa
   a exibição do conteúdo principal em 7,3 s.
4. **Prevenir a reincidência:** definir um limite de peso por imagem (por exemplo, 200 kB) e
   verificá-lo antes de cada publicação, com uma checagem automática na integração contínua.
   As três imagens que já seguem o padrão mostram que o limite é viável.

## 7. Limitações

- **Simulação, não implantação:** a troca das imagens ocorre no navegador de teste, e o portal
  não foi alterado. No modo `local` usado na medição, o tempo de transferência das imagens
  otimizadas é calculado pelo tamanho do arquivo, sem concorrência com os outros recursos, o
  que favorece o "depois" (seção 5.2).
- **Uma página e um perfil:** o efeito foi medido só no SITGeo e no perfil móvel do G3. A
  ação não trata a T1 nem Meu Território.
- **Largura das imagens:** as versões de 480 e 960 px cobrem o cartão observado no celular. O
  tamanho exibido em telas maiores não foi levantado.
- **Outras métricas:** o efeito sobre o tempo de CPU do SITGeo (M3.3.1) e sobre a T2 não foi
  medido.

## Referências

GOOGLE. **Properly size images**. [S.l.]: Google, [s.d.]. Disponível em: <https://developer.chrome.com/docs/lighthouse/performance/uses-responsive-images>. Acesso em: 13 nov. 2026.
