# Objetivos de Medição

*Nível conceitual.*

Cada característica selecionada na [Fase 1](../fase-1/index.md) gera um objetivo de medição,
descrito com o *template* do GQM (BASILI; CALDIERA; ROMBACH, 1994; RAMOS, 2026a).

| ID | Característica (ISO/IEC 25010:2011) | Issue |
|---|---|---|
| G1 | Usabilidade | #24 |
| G2 | Portabilidade | #25 |
| G3 | Eficiência de desempenho | #26 |

---

## G1: Usabilidade

!!! info "Em construção"
    Seção da issue #24.

---

## G2: Portabilidade

!!! info "Em construção"
    Seção da issue #25.

---

## G3: Eficiência de desempenho

| Campo | Descrição |
|---|---|
| **Analisar** | a área pública do SIT: as páginas Meu Território, SITGeo e Biblioteca Territorial, e as tarefas T1 e T2 (abaixo) |
| **Com o propósito de** | entender |
| **Com respeito a** | eficiência de desempenho: comportamento temporal e utilização de recursos |
| **Do ponto de vista de** | requisitante (MDA, simulado) |
| **No contexto de** | acesso individual por navegador em celular, com conexão móvel limitada, típico dos usuários em áreas rurais |

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
| Contexto (celular, conexão limitada) | Decisão 2 do requisitante (seção 1.2) e stakeholders "agricultores familiares e cidadãos" e "equipe de desenvolvimento e TI" (seção 2) |
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
