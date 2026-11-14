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

Preencher ao executar `medir.js`:

| Item | Valor |
|---|---|
| Data e horário | |
| Avaliador | |
| Conexão | |
| Chrome, Node.js e Playwright | |
| Modo da troca (`rede` ou `local`) | |
| Desvios em relação ao procedimento | |
