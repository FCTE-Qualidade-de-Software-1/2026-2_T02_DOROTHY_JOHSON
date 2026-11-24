# Uso de Inteligência Artificial

Esta página declara, para cada entrega, qual ferramenta de IA foi usada, em quais tarefas e
como a equipe conferiu e ajustou o resultado (critério AG-C3). A mesma declaração, em versão
resumida, está no artigo.

| Item | Valor |
|---|---|
| Ferramentas | Claude (Anthropic), em conversa por texto; Codex (OpenAI), na análise de flexibilidade da #77 |
| Imagens, ícones ou figuras geradas por IA | Nenhum |
| Atualizado em | 24/11/2026 |

## Entrega 1 (Fases 1 e 2)

| Tarefa com apoio da ferramenta | Como a equipe conferiu e ajustou |
|---|---|
| Conversão das páginas da GitPage (Markdown) para LaTeX e adaptação do documento ao modelo da SBC | Cada trecho foi conferido por um integrante contra a página de origem e ajustado antes de entrar no artigo |
| Redesenho dos diagramas em TikZ | Conferidos contra os diagramas da GitPage |
| Rascunho do resumo, do *abstract* e do referencial teórico, a partir das páginas escritas pela equipe | Conferidos contra as páginas da GitPage e as referências citadas, e ajustados |
| Organização da tabela de contribuição | Conferida contra as *issues* do repositório |

## Entrega 2 (Fases 3 e 4)

| Tarefa com apoio da ferramenta | Como a equipe conferiu e ajustou |
|---|---|
| Redação da visão geral da [Fase 3](fase-3/index.md), com a tabela de rastreabilidade F2 → F3 e o cronograma, a partir das fichas da Fase 2 e das páginas de ambiente e de método | Cada linha da tabela foi comparada com a ficha da métrica correspondente; as datas do cronograma foram validadas pela equipe |
| Seção da Fase 3 no artigo, resumida a partir das páginas da GitPage | Conferida contra as páginas de origem e ajustada às referências e aos rótulos do artigo |
| Leitura dos relatórios do Lighthouse para localizar a causa do LCP do SITGeo e proposta da [ação de melhoria](fase-4/acao-melhoria.md) a partir dessa evidência | Os valores foram recalculados pela equipe com `scripts/fase-4/melhoria/diagnostico.py` e comparados com `data/fase-4/eficiencia/resumo.csv`; a equipe avaliou a proposta e registrou a decisão em ata |
| Escrita dos scripts da ação de melhoria (`scripts/fase-4/melhoria/`) e da página que a documenta | Scripts lidos e executados pela equipe no ambiente da Fase 3; os resultados publicados são os gerados nessa execução, não valores sugeridos pela ferramenta |
| Roteiro dos slides da apresentação final | Conteúdo e divisão das falas revistos pela equipe no ensaio |
| Incorporação do pacote de coleta Windows (#72), análise de flexibilidade (#77), reconciliação da conferência no aparelho em `pontuar.py` e atualização dos CSVs derivados, com Codex | Cálculos confrontados com os CSVs e regras F2/F3 por verificações automatizadas; revisão humana desta alteração pendente. Nenhuma nova medição foi produzida pela ferramenta |
| Síntese da classificação por característica e rastreabilidade com o propósito da F1 (#79), com Codex | Texto comparado às análises G1/G2/G3, aos CSVs consolidados e aos critérios da F2; reprodução dos cálculos e build da documentação verificados. G1 mantido pendente; revisão humana desta síntese pendente |

## Limites do uso

- As medições, os dados brutos e as classificações de qualidade vêm das coletas feitas pela
  equipe e dos critérios definidos na Fase 2. A ferramenta não gerou nem estimou medidas.
- A revisão por ao menos um integrante é necessária antes de incorporar o texto produzido
  com apoio da ferramenta; a situação da #77 está declarada na tabela. As decisões sobre características, métricas, níveis e ação de melhoria
  foram tomadas pela equipe, inclusive quando partiram de uma proposta da ferramenta.
