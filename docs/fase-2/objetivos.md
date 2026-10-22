# Objetivos de Medição

*Nível conceitual.*

Cada característica selecionada na [Fase 1](../fase-1/index.md) gera um objetivo de medição,
descrito com o *template* do GQM (BASILI; CALDIERA; ROMBACH, 1994; RAMOS, 2026a).

| ID | Característica (ISO/IEC 25010:2023) | Issue |
|---|---|---|
| G1 | Capacidade de interação | #24 |
| G2 | Flexibilidade | #25 |
| G3 | Eficiência de desempenho | #26 |

---

## G1: Capacidade de interação

| Campo | Descrição |
|---|---|
| **Analisar** | a área pública do SIT: as páginas Início, Meu Território, SITGeo, Biblioteca Territorial e Fale Conosco, e as tarefas T1, T2 e T3 (abaixo) |
| **Com o propósito de** | avaliar |
| **Com respeito a** | capacidade de interação: reconhecibilidade de adequação, apreensibilidade, operabilidade, proteção contra erros do usuário, engajamento do usuário e assistência ao usuário |
| **Do ponto de vista de** | usuários do portal: colegiados e agentes territoriais, agricultores familiares e cidadãos |
| **No contexto de** | uso do portal no interior do país, na casa do agricultor familiar ou na sede do colegiado territorial, pelo celular do próprio usuário, por pessoas que acessam o portal pela primeira vez, sem treinamento e sem ninguém por perto para ajudar. Nos testes, esse contexto é reproduzido com participantes que nunca usaram o portal, em um celular, sem ajuda do moderador |

**Tarefas dos testes com usuários:**

- **T1, consultar um território:** a partir da página Início, chegar a Meu Território, selecionar a
  UF e o território e acionar "Selecionar" até os dados do território serem exibidos (mesma
  tarefa de G3).
- **T2, ativar uma camada no mapa:** a partir da página Início, chegar ao SITGeo, escolher um tema
  e ativar uma camada até ela ser exibida no mapa (mesma tarefa de G3).
- **T3, baixar um documento do território:** a partir da página Início, chegar à Biblioteca
  Territorial, selecionar a UF e o território e baixar o PTDRS.

O território, a camada e o documento de referência são fixados na Fase 3, os mesmos usados em G3.

### Ligação com a Fase 1

| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (seis subcaracterísticas de capacidade de interação) | Subcaracterísticas mantidas na seção 4.2; inclusividade e autodescritividade tratadas na seção 5.1 |
| Páginas medidas | Seções prioritárias da seção 3.5, mais o Fale Conosco, onde a seção 4.2 localiza a proteção contra erros |
| Ponto de vista | Stakeholders "colegiados e agentes territoriais" e "agricultores familiares e cidadãos" (seção 2), para quem a capacidade de interação é a característica de ênfase 5 (seção 1.3) |
| Contexto (interior do país, celular próprio, primeiro uso sem ajuda) | Ambiente de uso (seção 3.3), critério de sucesso "uso sem ajuda" do público final (seção 2) e conhecimento de informática básico exigido (seção 3.3) |
| Propósito (avaliar) | Decisão 1 do requisitante: quais telas e fluxos redesenhar (seção 1.2) |
| Envio real pelo Fale Conosco fora do escopo | Corte da seção 5.1: a proteção contra erros é avaliada antes do envio |

### Abstraction sheet

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Área pública do SIT (5 páginas e 3 tarefas) | Avaliar | Capacidade de interação (seis subcaracterísticas) | Usuários do portal |

<div class="grid" markdown>

<div markdown>

**Foco de qualidade**

- Clareza da finalidade de cada seção para quem chega ao portal
- Conclusão das tarefas por usuários de primeira vez, sem ajuda
- Esforço de navegação para concluir as tarefas
- Bloqueio e sinalização de entradas inválidas nos formulários
- Satisfação dos usuários com o uso e com a aparência das páginas
- Conformidade das páginas com critérios de acessibilidade

</div>

<div markdown>

**Fatores de variação**

- Familiaridade digital e experiência prévia dos participantes com portais de governo
- Conhecimento do domínio (política territorial) dos participantes
- Dispositivo e tamanho de tela usados no teste
- Território, camada e documento escolhidos
- Presença e postura do moderador durante o teste
- Mudanças no portal durante o período de coleta

</div>

<div markdown>

**Hipóteses de baseline**

- As seções com nome descritivo são reconhecidas; o SITGeo, cujo nome é uma sigla, não (H1.1)
- T1 e T3 são concluídas sem ajuda pela maioria; T2 não (H1.2 e H1.3)
- Campos vazios são bloqueados, mas as mensagens de erro não explicam como corrigir (H1.4)
- A percepção de usabilidade fica abaixo da média de referência do SUS (H1.5)
- O mapa do SITGeo concentra as violações graves de acessibilidade (H1.6)

</div>

<div markdown>

**Impacto dos fatores nas hipóteses**

- Mais familiaridade digital ou com o domínio aumenta a conclusão e o SUS: o recrutamento mistura
  perfis, que são registrados (sem identificar o participante) para a análise.
- Telas pequenas dificultam o SITGeo: todos os participantes usam o mesmo tipo de dispositivo,
  definido na Fase 3; a variação entre telas é tratada em G2.
- Territórios com mais dados podem confundir a leitura: a Fase 3 fixa o território, a camada e o
  documento de referência.
- Ajuda do moderador invalida a medida de conclusão sem ajuda: o roteiro do teste proíbe dicas e
  registra qualquer intervenção como falha.
- Mudanças no portal invalidam a comparação entre participantes: são registradas como ameaça à
  validade (Fase 1, seção 5.2).

</div>

</div>

---

## G2: Flexibilidade

| Campo | Descrição |
|---|---|
| **Analisar** | a área pública do SIT: as páginas Meu Território, SITGeo e Biblioteca Territorial, e as tarefas T1, T2 e T3 (descritas em [G1](#g1-capacidade-de-interacao)) |
| **Com o propósito de** | avaliar |
| **Com respeito a** | flexibilidade: adaptabilidade a diferentes navegadores, sistemas operacionais e tamanhos de tela |
| **Do ponto de vista de** | equipe de desenvolvimento e TI do SIT (fornecedor) |
| **No contexto de** | uso do portal em lugares e aparelhos diferentes: no campo e em casa, em municípios do interior, por celulares Android e iPhone de vários tamanhos; e em escritórios de prefeituras, sindicatos e órgãos públicos, por computadores com Windows. Nos testes, esse contexto é reproduzido pela matriz de ambientes abaixo, com aparelhos reais para os celulares de maior participação |

**Ambientes de referência:** a combinação de navegador, sistema operacional e largura de tela
é fixada na Fase 3 a partir de dados de participação de mercado no Brasil (STATCOUNTER, 2026).
A matriz inicial proposta é:

| Dimensão | Valores |
|---|---|
| Navegador e sistema operacional | Chrome/Android, Samsung Internet/Android, Safari/iOS, Chrome/Windows, Edge/Windows, Firefox/Windows |
| Largura da janela (px) | 360 e 412 (celular), 768 (tablet), 1366 e 1920 (computador) |

### Ligação com a Fase 1

| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (adaptabilidade) | Única subcaracterística de flexibilidade mantida na seção 4.2; escalabilidade, instalabilidade e substituibilidade ficaram fora (seção 5.1) |
| Navegadores, sistemas e telas | Nota "Compatibilidade × flexibilidade" da seção 1.3 |
| Ponto de vista | Stakeholder "equipe de desenvolvimento e TI do SIT", cujo critério de sucesso é ter defeitos reproduzíveis, com ambiente e passos (seção 2) |
| Contexto (campo e escritório, celular e computador) | Ambiente de uso (seção 3.3) e justificativa da ênfase 4 (seção 1.3): acesso predominante por celular |
| Propósito (avaliar) | Decisão 3 do requisitante: quais ambientes entram na matriz de testes do fornecedor (seção 1.2) |

### Abstraction sheet

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Área pública do SIT (3 páginas e 3 tarefas) | Avaliar | Adaptabilidade | Equipe de desenvolvimento e TI do SIT |

<div class="grid" markdown>

<div markdown>

**Foco de qualidade**

- Conclusão das tarefas em cada navegador e sistema operacional
- Adaptação do layout às larguras de tela, sem rolagem horizontal
- Disponibilidade, no celular, das funções oferecidas no computador
- Falhas que só ocorrem em um ambiente e sua gravidade

</div>

<div markdown>

**Fatores de variação**

- Versão do navegador e do sistema operacional
- Dispositivo real ou emulado
- Densidade de pixels e nível de zoom
- Orientação da tela (retrato ou paisagem)
- Velocidade da conexão
- Mudanças no portal durante o período de coleta

</div>

<div markdown>

**Hipóteses de baseline**

- As tarefas funcionam nos navegadores baseados em Chromium; as falhas aparecem no Safari/iOS e no Firefox (H2.1)
- Acima de 768 px não há rolagem horizontal; em 360 px há pelo menos uma página com problema (H2.2)
- O SITGeo perde funções no celular (H2.2)
- As falhas se concentram no SITGeo em telas pequenas (H2.3)

</div>

<div markdown>

**Impacto dos fatores nas hipóteses**

- Versões diferentes do mesmo navegador podem mudar o resultado: cada execução registra a versão
  exata, e a Fase 3 fixa versões estáveis atuais.
- A emulação no computador não reproduz todos os comportamentos do celular: os ambientes móveis
  com maior participação são testados em aparelho real, e os demais podem ser emulados, com o
  tipo registrado.
- Zoom e orientação mudam a largura útil: os testes usam zoom de 100% e orientação retrato,
  salvo nos casos previstos na Fase 3.
- Conexões lentas podem parecer falhas de ambiente: as execuções usam a mesma rede, e uma
  falha só é atribuída ao ambiente se for reproduzida.
- Mudanças no portal invalidam a comparação entre ambientes: são registradas como ameaça à
  validade (Fase 1, seção 5.2).

</div>

</div>

---

## G3: Eficiência de desempenho

| Campo | Descrição |
|---|---|
| **Analisar** | a área pública do SIT: as páginas Meu Território, SITGeo e Biblioteca Territorial, e as tarefas T1 e T2 (abaixo) |
| **Com o propósito de** | entender |
| **Com respeito a** | eficiência de desempenho: comportamento temporal e utilização de recursos |
| **Do ponto de vista de** | requisitante (MDA, simulado) |
| **No contexto de** | uso do portal em área rural, por um usuário de cada vez, em um celular de entrada (pouca memória e processador modesto) conectado a uma rede móvel 3G/4G com sinal fraco ou instável. Nos testes, esse contexto é reproduzido pelo perfil móvel do Lighthouse, que limita a velocidade da rede e do processador |

**Tarefas medidas:**

- **T1, consultar um território:** em Meu Território, selecionar a UF, selecionar o território e
  acionar "Selecionar" até os dados do território serem exibidos.
- **T2, ativar uma camada no mapa:** no SITGeo, escolher um tema e ativar uma camada até ela ser
  exibida no mapa.

### Ligação com a Fase 1

| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (comportamento temporal e utilização de recursos) | Subcaracterísticas mantidas na seção 4.2; capacidade ficou fora (seção 5.1) |
| Páginas medidas | Seções prioritárias definidas na seção 3.5 |
| Ponto de vista | Requisitante definido na seção 1.2 |
| Contexto (área rural, celular de entrada, rede móvel fraca) | Ambiente de uso (seção 3.3), decisão 2 do requisitante (seção 1.2) e stakeholders "agricultores familiares e cidadãos" e "equipe de desenvolvimento e TI" (seção 2) |
| Acesso individual | Corte da capacidade: os resultados não valem para picos de uso (seção 5.1) |

### Abstraction sheet

O *abstraction sheet* registra o que a equipe sabe e espera sobre o objeto antes da medição
(RAMOS, 2026a). As hipóteses de baseline estão detalhadas na página de
[hipóteses](hipoteses.md).

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Área pública do SIT (3 páginas e 2 tarefas) | Entender | Comportamento temporal e utilização de recursos | Requisitante (MDA, simulado) |

<div class="grid" markdown>

<div markdown>

**Foco de qualidade**

- Tempo até a primeira resposta visível de cada página
- Tempo até a exibição do conteúdo principal de cada página
- Tempo de execução das tarefas T1 e T2
- Tempo de CPU gasto no carregamento de cada página
- Memória ocupada por cada página e tarefa

</div>

<div markdown>

**Fatores de variação**

- Velocidade e latência da rede
- Capacidade de processamento do aparelho (ou da máquina que simula o aparelho)
- Estado do cache do navegador (vazio ou preenchido)
- Horário e carga do servidor
- Território e camada escolhidos (o volume de dados varia)
- Mudanças no portal durante o período de coleta
- Outros processos executando na máquina durante a medição

</div>

<div markdown>

**Hipóteses de baseline**

- A primeira resposta das páginas é rápida, mas o conteúdo principal demora (H3.1)
- O SITGeo é a página mais lenta e a que mais exige processamento (H3.1 e H3.3)
- T2 interrompe o fluxo de pensamento do usuário, e T1 chega a ameaçar a atenção dele (H3.2)
- As tarefas aumentam a memória ocupada, mais em T1 que em T2 (H3.4)

</div>

<div markdown>

**Impacto dos fatores nas hipóteses**

- Rede e aparelho mais lentos aumentam todos os tempos: a medição usa sempre o mesmo perfil
  móvel simulado.
- Cache preenchido reduz os tempos: a medição parte sempre de cache vazio.
- Territórios e camadas com mais dados aumentam o tempo de T1 e T2 e a memória: a Fase 3 fixa
  um território e uma camada de referência.
- Horário, carga do servidor e processos concorrentes aumentam a variação entre execuções: cada
  medição é repetida e registra data e hora, e as execuções nunca são simultâneas.
- Mudanças no portal invalidam a comparação entre medições: são registradas como ameaça à
  validade (Fase 1, seção 5.2).

</div>

</div>

---

## Referências

BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The goal question metric approach. In: MARCINIAK, J. J. (ed.). **Encyclopedia of software engineering**. New York: Wiley, 1994. p. 528-532.

RAMOS, C. S. **Medição baseada em objetivos**: determinando o que medir. Notas de aula da disciplina Qualidade de Software 1. Brasília: FCTE/UnB, 2026a.

STATCOUNTER. **Browser market share Brazil**. [S.l.]: StatCounter Global Stats, 2026. Disponível em: <https://gs.statcounter.com/browser-market-share/all/brazil>. Acesso em: 20 out. 2026.
