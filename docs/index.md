---
hide:
  - navigation
  - toc
---

<div class="dj-hero" markdown>
<span class="dj-kicker">Qualidade de Software · 2026/2 · FCTE/UnB</span>

# Dorothy Johnson

Avaliação independente da qualidade da **Plataforma Territórios da Cidadania (SIT)**, o portal
público do Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA) que reúne dados,
mapas e documentos dos territórios rurais. Esta página reúne o método, os dados e os
resultados da avaliação, feita pela equipe Dorothy Johnson na disciplina de Qualidade de Software.

[Ver os resultados :material-arrow-right:](fase-4/index.md){ .md-button .md-button--primary }
[Começar pela Fase 1](fase-1/index.md){ .md-button }
[Rastrear um resultado](rastreabilidade.md){ .md-button }
</div>

## O que avaliamos e por quê

O SIT atende colegiados e agentes territoriais, gestores públicos, agricultores familiares e
cidadãos, muitos deles em áreas rurais, com pouca familiaridade digital e acesso por celular. A avaliação simula um pedido do MDA,
como gestor do portal, e responde a uma pergunta de gestão: **quais problemas de qualidade mais
dificultam o acesso às informações territoriais e devem ser tratados primeiro?**

Para isso, a equipe escolheu três características do modelo de qualidade da
ISO/IEC 25010:2023, cada uma ligada a uma decisão do requisitante:

| Característica | Pergunta que ela responde |
|---|---|
| **Capacidade de interação** | Quais telas e tarefas precisam ser redesenhadas para quem tem pouca familiaridade digital? |
| **Flexibilidade** | Quais combinações de navegador, sistema e tamanho de tela devem entrar nos testes do portal? |
| **Eficiência de desempenho** | É preciso otimizar o carregamento das páginas e dos mapas em conexões móveis? |

*Tabela 1: Características avaliadas. A justificativa da escolha está na
[Fase 1](fase-1/index.md#13-enfase-por-caracteristica).*

## Como a avaliação foi feita

O trabalho segue o processo de avaliação de produto da ISO/IEC 25040, em quatro fases. As
métricas foram definidas com o método GQM (*Goal–Question–Metric*): cada objetivo de medição
se desdobra em questões, e cada questão em métricas com níveis de pontuação definidos antes
da coleta.

<div class="grid cards" markdown>

-   :material-numeric-1-circle-outline:{ .lg .middle } **Fase 1 — Requisitos**

    ---

    Propósito da avaliação, partes interessadas, escopo e priorização das características.

    [:octicons-arrow-right-24: Abrir a Fase 1](fase-1/index.md)

-   :material-numeric-2-circle-outline:{ .lg .middle } **Fase 2 — Especificação (GQM)**

    ---

    Objetivos, questões, hipóteses, as 19 métricas, os níveis de pontuação e o gráfico GQM.

    [:octicons-arrow-right-24: Abrir a Fase 2](fase-2/index.md)

-   :material-numeric-3-circle-outline:{ .lg .middle } **Fase 3 — Projeto**

    ---

    Como cada medida é coletada: ambiente, ferramentas, participantes e protocolos.

    [:octicons-arrow-right-24: Abrir a Fase 3](fase-3/index.md)

-   :material-numeric-4-circle-outline:{ .lg .middle } **Fase 4 — Execução**

    ---

    Coleta, análise de cada característica, classificação final e oportunidades de melhoria.

    [:octicons-arrow-right-24: Abrir a Fase 4](fase-4/index.md)

-   :material-chart-line:{ .lg .middle } **Gestão do projeto**

    ---

    Plano de medição PSM/CID, registro semanal das medições e painel com os indicadores.

    [:octicons-arrow-right-24: Abrir a Gestão](gestao/index.md)

-   :material-file-document-outline:{ .lg .middle } **Artigo**

    ---

    Versão em texto do artigo da equipe: introdução, referencial teórico e metodologia.

    [:octicons-arrow-right-24: Abrir o Artigo](artigo/introducao.md)

</div>

## Principais resultados

Cada característica recebe uma classificação própria; não se calcula uma nota única para o SIT.

| Característica | Classificação | Em resumo |
|---|---|---|
| **Capacidade de interação** | **NC** (não calculável), com ressalvas | SUS médio de 50/100 e barreiras críticas de acessibilidade nas cinco páginas avaliadas; parte das tarefas ficou sem observação válida |
| **Flexibilidade** | **Bom** (2,21 de 3) | As 18 tarefas foram concluídas nos seis ambientes; em celulares há rolagem horizontal e falhas graves, mas nenhuma bloqueante |
| **Eficiência de desempenho** | **Aceitável** (1,35 de 3) | O conteúdo principal do SITGeo leva 23,45 s para aparecer, e a consulta da tarefa T1, 20,39 s |

*Tabela 2: Resultado por característica. O cálculo, os limitadores e a ligação com o
propósito estão na [classificação final](fase-4/classificacao-final.md).*

Como ação de melhoria, a equipe otimizou duas imagens do SITGeo e mediu a página antes e
depois, em ambiente local: o tempo até exibir o conteúdo principal caiu de 26,45 s para 1,87 s
([ação de melhoria](fase-4/acao-melhoria.md)). A mudança não foi implantada no portal.

## Como conferir os dados

Todos os números do site podem ser refeitos a partir dos arquivos do repositório.

- [Repositório no GitHub](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON):
  código do site, scripts de coleta e de cálculo.
- [Release mais recente](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/releases/latest):
  versão publicada do repositório, com a descrição do que foi entregue.
- [Dados brutos](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data)
  e o [mapa dos dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/blob/main/data/README.md),
  que liga cada arquivo à sua métrica e à sua questão.
- [Consolidação e cálculo](fase-4/consolidacao.md): o passo a passo para recalcular os resultados.

## Siglas usadas no site

GQM
:   *Goal–Question–Metric*, método que deriva as métricas de objetivos e questões.

LCP
:   *Largest Contentful Paint*, tempo até a página exibir seu maior elemento visível.

NC
:   Não calculável: faltam dados válidos para classificar o recorte ou a característica.

PSM/CID
:   *Practical Software and Systems Measurement*, usado aqui para medir a gestão do projeto.

SUS
:   *System Usability Scale*, questionário de usabilidade com nota de 0 a 100.

## Equipe

<div class="dj-team">
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">AL</div><strong>Ana Luíza Fernandes</strong></div>
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">AR</div><strong>Artur Henrique Holz Bartz</strong></div>
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">CA</div><strong>Cayo Felipe Alencar Câmara</strong></div>
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">FE</div><strong>Felipe Rodrigues</strong></div>
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">GA</div><strong>Gabriel Augusto V. V. Rocha</strong></div>
  <div class="dj-member"><div class="dj-avatar" aria-hidden="true">TA</div><strong>Tales Rodrigues Gonçalves</strong></div>
</div>

[Veja a tabela de contribuição :octicons-arrow-right-24:](contribuicao.md) ·
[Declaração de uso de IA :octicons-arrow-right-24:](uso-de-ia.md)

## Entregas

<div class="dj-timeline">
  <div class="dj-step done"><strong>Entrega 1 — Fases 1 e 2</strong><span>Prazo: 26/10/2026 · concluída</span></div>
  <div class="dj-step done"><strong>Ponto de controle 2 — release v2.0.0</strong><span>Publicado em 15/11/2026</span></div>
  <div class="dj-step current"><strong>Entrega 2 — Fases 3 e 4</strong><span>Prazo: 24/11/2026</span></div>
</div>
