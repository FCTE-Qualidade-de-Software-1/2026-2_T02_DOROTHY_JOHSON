# Dados da ação de melhoria (imagens do SITGeo)

Evidências e resultados da ação de melhoria da Fase 4 (issues #82 e #83), documentada em
[`docs/fase-4/acao-melhoria.md`](../../../docs/fase-4/acao-melhoria.md).

| Arquivo | Conteúdo | Gerado por |
|---|---|---|
| `diagnostico.csv` | Por execução do Lighthouse no SITGeo: LCP, elemento do LCP, fases do LCP, peso da página e das imagens e economia estimada | `scripts/fase-4/melhoria/diagnostico.py` |
| `imagens-pagina.csv` | Transferência mediana de cada imagem do portal carregada pelo SITGeo | `scripts/fase-4/melhoria/diagnostico.py` |
| `imagens.csv` | Inventário das imagens originais e otimizadas: formato, dimensões, bytes e SHA-256 | `scripts/fase-4/melhoria/otimizar.py` |
| `medicao.json` | LCP e peso da página por execução, nas condições "antes" e "depois" | `scripts/fase-4/melhoria/medir.js` |
| `resumo.csv` | Mediana, mínimo e máximo de cada medida por condição | `scripts/fase-4/melhoria/medir.js` |

`diagnostico.csv` e `imagens-pagina.csv` derivam dos relatórios da coleta de 08/11/2026
(`data/fase-4/eficiencia/lighthouse/`). Os demais arquivos são criados ao executar os scripts.

As imagens originais ficam em `originais/`, fora do versionamento (`.gitignore`): pertencem ao
portal do MDA e são identificadas em `imagens.csv` pelo endereço, pelo tamanho e pelo hash. As
versões otimizadas ficam em `docs/fase-4/melhoria/img/`.

## Sessão de medição

| Item | Valor |
|---|---|
| Data e horário | 14/11/2026, das 18:34 às 18:36 (horário de Brasília) |
| Avaliador | Artur Henrique Holz Bartz |
| Máquina e sistema | Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz, 8GB RAM e Microsoft Windows 10 Pro |
| Conexão | cabo |
| Chrome | 157.0.8103.51 (modo *headless* novo) |
| Node.js e Playwright | 26.13.1 e 1.48.2 |
| Python e Pillow (geração das imagens) | 3.15.2 e 13.0.0 |
| Modo da troca | `local`, com as versões de 960 px |
| Execuções | 5 por condição, alternadas; nenhuma falhou nem foi repetida |

## Desvios em relação ao procedimento

- A medição foi feita em uma máquina com Windows, e não no notebook com Ubuntu do
  [ambiente da Fase 3](../../../docs/fase-3/ambiente.md), com Chrome 157 e Node.js 26 no
  lugar de Chrome 138 e Node.js 24. As duas condições foram medidas na mesma sessão e na
  mesma máquina.
- Foi usado o modo `local`, porque as imagens otimizadas ainda não estavam publicadas na
  GitPage. A medição pela rede fica pendente.
