# Gráfico GQM

O gráfico mostra a hierarquia completa da modelagem GQM nos três níveis definidos por Basili,
Caldiera e Rombach (1994): o **conceitual**, com os [objetivos de medição](objetivos.md); o
**operacional**, com as [questões](questoes.md); e o **quantitativo**, com as
[métricas](metricas.md). Cada métrica responde a uma única questão, e cada questão pertence a
um único objetivo, o que mantém a rastreabilidade pelos identificadores (por exemplo,
G3 → Q3.1 → M3.1.1).

```mermaid
flowchart LR
    accTitle: Hierarquia GQM da avaliação do SIT
    accDescr: Três objetivos de medição no nível conceitual, treze questões no nível operacional e dezenove métricas no nível quantitativo. A versão em texto está logo abaixo do gráfico.

    subgraph C["Nível conceitual"]
        direction TB
        G1(["G1 Capacidade de interação<br/>avaliar · usuários do portal"])
        G2(["G2 Flexibilidade<br/>avaliar · equipe de desenvolvimento e TI"])
        G3(["G3 Eficiência de desempenho<br/>entender · requisitante (MDA)"])
    end

    subgraph O["Nível operacional"]
        direction TB
        Q11["Q1.1 Quem chega identifica a seção que precisa?"]
        Q12["Q1.2 Usuários de primeira vez concluem as tarefas sem ajuda?"]
        Q13["Q1.3 Quanto o caminho se afasta do caminho mais curto?"]
        Q14["Q1.4 O portal impede entradas inválidas e explica a correção?"]
        Q15["Q1.5 Como os usuários percebem o uso e a aparência?"]
        Q16["Q1.6 As páginas atendem aos critérios de acessibilidade?"]
        Q21["Q2.1 As tarefas funcionam nos navegadores e sistemas mais usados?"]
        Q22["Q2.2 As páginas se adaptam a celular, tablet e computador?"]
        Q23["Q2.3 Quais ambientes concentram as falhas?"]
        Q31["Q3.1 Quanto tempo até a primeira resposta e o conteúdo principal?"]
        Q32["Q3.2 Quanto tempo para concluir T1 e T2?"]
        Q33["Q3.3 Quanto processamento (CPU) o carregamento exige?"]
        Q34["Q3.4 Quanta memória páginas e tarefas ocupam?"]
    end

    subgraph M["Nível quantitativo"]
        direction TB
        M111[/"M1.1.1 Autodescrição dos pontos de entrada"/]
        M112[/"M1.1.2 Acerto do primeiro clique"/]
        M121[/"M1.2.1 Conclusão de tarefas sem ajuda"/]
        M131[/"M1.3.1 Eficiência do caminho"/]
        M141[/"M1.4.1 Prevenção de erros de operação"/]
        M142[/"M1.4.2 Correção de erros de entrada"/]
        M151[/"M1.5.1 Pontuação SUS"/]
        M152[/"M1.5.2 Nota de aparência"/]
        M161[/"M1.6.1 Conformidade automática de acessibilidade"/]
        M162[/"M1.6.2 Violações críticas e sérias"/]
        M211[/"M2.1.1 Adaptabilidade ao ambiente de software"/]
        M221[/"M2.2.1 Ausência de rolagem horizontal"/]
        M222[/"M2.2.2 Funções disponíveis no celular"/]
        M231[/"M2.3.1 Falhas dependentes de ambiente"/]
        M311[/"M3.1.1 Tempo médio de resposta (FCP)"/]
        M312[/"M3.1.2 Tempo médio de execução do carregamento (LCP)"/]
        M321[/"M3.2.1 Tempo médio de execução da tarefa"/]
        M331[/"M3.3.1 Utilização média de CPU"/]
        M341[/"M3.4.1 Utilização média de memória"/]
    end

    G1 --> Q11 & Q12 & Q13 & Q14 & Q15 & Q16
    G2 --> Q21 & Q22 & Q23
    G3 --> Q31 & Q32 & Q33 & Q34

    Q11 --> M111 & M112
    Q12 --> M121
    Q13 --> M131
    Q14 --> M141 & M142
    Q15 --> M151 & M152
    Q16 --> M161 & M162
    Q21 --> M211
    Q22 --> M221 & M222
    Q23 --> M231
    Q31 --> M311 & M312
    Q32 --> M321
    Q33 --> M331
    Q34 --> M341
```

*Figura 1: Hierarquia GQM da avaliação do SIT. Elaborada pela equipe.*

**Legenda:**

| Forma | Nível GQM | Conteúdo |
|---|---|---|
| Retângulo arredondado | Conceitual | Objetivo de medição, com o propósito (avaliar ou entender) e o ponto de vista |
| Retângulo | Operacional | Questão, resumida; o texto completo está em [Questões](questoes.md) |
| Paralelogramo | Quantitativo | Métrica, com o nome da ficha em [Métricas](metricas.md) |

| Objetivo | Questões | Métricas |
|---|---|---|
| G1 Capacidade de interação | 6 | 10 |
| G2 Flexibilidade | 3 | 4 |
| G3 Eficiência de desempenho | 4 | 5 |
| **Total** | **13** | **19** |

??? info "Versão em texto do gráfico"

    - **G1 Capacidade de interação** (avaliar, do ponto de vista dos usuários do portal)
        - Q1.1 Reconhecibilidade de adequação: M1.1.1 Autodescrição dos pontos de entrada;
          M1.1.2 Acerto do primeiro clique
        - Q1.2 Apreensibilidade: M1.2.1 Conclusão de tarefas sem ajuda
        - Q1.3 Operabilidade: M1.3.1 Eficiência do caminho
        - Q1.4 Proteção contra erros do usuário: M1.4.1 Prevenção de erros de operação;
          M1.4.2 Correção de erros de entrada
        - Q1.5 Engajamento do usuário: M1.5.1 Pontuação SUS; M1.5.2 Nota de aparência
        - Q1.6 Assistência ao usuário: M1.6.1 Conformidade automática de acessibilidade;
          M1.6.2 Violações críticas e sérias
    - **G2 Flexibilidade** (avaliar, do ponto de vista da equipe de desenvolvimento e TI)
        - Q2.1 Adaptabilidade (ambiente de software): M2.1.1 Adaptabilidade ao ambiente de
          software
        - Q2.2 Adaptabilidade (ambiente de hardware): M2.2.1 Ausência de rolagem horizontal;
          M2.2.2 Funções disponíveis no celular
        - Q2.3 Adaptabilidade: M2.3.1 Falhas dependentes de ambiente
    - **G3 Eficiência de desempenho** (entender, do ponto de vista do requisitante)
        - Q3.1 Comportamento temporal: M3.1.1 Tempo médio de resposta (FCP); M3.1.2 Tempo
          médio de execução do carregamento (LCP)
        - Q3.2 Comportamento temporal: M3.2.1 Tempo médio de execução da tarefa
        - Q3.3 Utilização de recursos: M3.3.1 Utilização média de CPU
        - Q3.4 Utilização de recursos: M3.4.1 Utilização média de memória

## Referências

BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The goal question metric approach. In: MARCINIAK, J. J. (ed.). **Encyclopedia of software engineering**. New York: Wiley, 1994. p. 528-532.
