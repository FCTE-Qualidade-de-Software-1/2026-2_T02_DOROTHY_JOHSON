# Formulários de coleta de capacidade de interação (G1)

Copie as tabelas ou os cabeçalhos CSV para a planilha de trabalho. Use os IDs dos casos, das tarefas e das páginas para vincular os registros às evidências. O [método de G1](metodo-interacao.md) define a ordem de execução e a codificação.

## Ambiente e participantes

Uma linha por ambiente usado na rodada. Campos de local e rede devem descrever a condição de teste sem identificar participantes.

```csv
rodada,data_hora_fuso,atividade,avaliadores,dispositivo,so_versao,navegador_versao,viewport,zoom,rede,local,gravador,axe_versao,observacoes
```

Uma linha por pessoa. Registre o consentimento no controle de acesso restrito.

```csv
codigo,publico_representado,familiaridade_digital,primeiro_acesso,consentimento_confirmado,rodada,observacoes
```

## Observação das tarefas

Preencha o caminho de referência após o piloto. Os valores servem a todos os participantes da rodada.

| Tarefa | Sequência confirmada no celular | Total mínimo | Evidência do piloto |
|---|---|---:|---|
| T1 | | | |
| T2 | | | |
| T3 | | | |

Preencha uma linha por tentativa. Use `sucesso`, `desistência`, `tempo`, `ajuda`, `falha do portal` ou `interrompida` em status. Identifique a evidência por código do arquivo e intervalo na gravação.

```csv
rodada,codigo,tarefa,tentativa,inicio_fuso,duracao_s,primeira_acao,primeiro_destino,acerto_primeiro_destino,status,evidencia_resultado,ajuda_ou_incidente,sequencia_passos,passos_avaliador_1,passos_avaliador_2,passos_consenso,passos_minimos,razao,evidencia_gravacao
```

## Questionário

**Código:** ______ · **Rodada:** ______

Para cada afirmação, assinale um número de 1 a 5. Pense no portal que você acabou de usar.

**1** Discordo totalmente · **2** Discordo · **3** Nem concordo nem discordo · **4** Concordo · **5** Concordo totalmente

| Item | Afirmação | Resposta |
|---|---|---|
| 1 | Acho que gostaria de usar este portal com frequência. | |
| 2 | Achei o portal desnecessariamente complexo. | |
| 3 | Achei o portal fácil de usar. | |
| 4 | Acho que precisaria da ajuda de alguém com conhecimento técnico para usar este portal. | |
| 5 | Achei que as diferentes funções do portal estavam bem integradas. | |
| 6 | Achei que havia muitas inconsistências no portal. | |
| 7 | Imagino que a maioria das pessoas aprenderia a usar este portal rapidamente. | |
| 8 | Achei o portal trabalhoso de usar. | |
| 9 | Senti confiança ao usar o portal. | |
| 10 | Precisei aprender muitas coisas antes de conseguir usar o portal. | |
| 11 | A aparência das páginas é agradável e organizada. | |

Os itens 1 a 10 são uma tradução de trabalho do SUS para o contexto do portal. A aparência é calculada separadamente. [Brooke (1996)](../referencias.md)

```csv
rodada,codigo,sus_1,sus_2,sus_3,sus_4,sus_5,sus_6,sus_7,sus_8,sus_9,sus_10,sus_0_a_100,aparencia_1_a_5
```

## Autodescrição

Use uma linha por seção. Registre URL, texto visível, captura e decisões independentes antes do consenso.

| Seção | URL | Texto visível | Captura | Avaliador 1 | Avaliador 2 | Consenso e justificativa |
|---|---|---|---|---|---|---|
| Início | | | | | | |
| Meu Território | | | | | | |
| SITGeo | | | | | | |
| Biblioteca Territorial | | | | | | |
| Homologações de Territórios | | | | | | |
| Território em Foco | | | | | | |
| Fale Conosco | | | | | | |
| Sobre | | | | | | |
| Espaço do Colegiado (entrada pública) | | | | | | |

## Entradas inválidas

Para Fale Conosco, use como referência **Nome** “Pessoa Teste”, **E-mail** `teste@example.com`, **Telefone** `61912345678`, **Assunto** “Teste de avaliação” (se for uma lista, primeira opção selecionável, registrada no caso) e **Mensagem** “Coleta de avaliação da interface”. Altere somente os campos indicados. Execute a ação de submissão com a rede offline.

| Caso | Página | Entrada inválida e ação |
|---|---|---|
| FC-01 | Fale Conosco | Deixe tudo vazio e tente enviar. |
| FC-02 | Fale Conosco | Troque apenas o e-mail por `teste.example.com` e tente enviar. |
| FC-03 | Fale Conosco | Troque apenas o telefone por `abcdefghijk` e tente enviar se o controle aceitar a entrada. Registre se as letras forem rejeitadas durante a digitação. |
| FC-04 | Fale Conosco | Apague apenas a mensagem e tente enviar. |
| BT-01 | Biblioteca Territorial | Na seção PTDRS, com o programa padrão, mantenha a UF sem seleção e tente Buscar PTDRS. |
| MT-01 | Meu Território | Deixe UF e território sem seleção e tente Selecionar. |
| MT-02 | Meu Território | Escolha GO, deixe território sem seleção e tente Selecionar. |

Copie uma linha por caso. Em M1.4.2, registre a decisão de cada avaliador antes do consenso.

```csv
rodada,caso,data_hora_fuso,url,executado,desvio_ou_motivo,valor_aceito,estado_controle,tentativa_requisicao,protegido,mensagem_literal,campo_indicado,correcao_indicada,avaliador_1,avaliador_2,consenso,justificativa,captura_interface,captura_network
```

## Acessibilidade

Preencha uma linha por página (Início, Meu Território, SITGeo, Biblioteca Territorial e Fale Conosco) e outra tabela com uma linha por elemento distinto crítico ou sério.

```csv
rodada,pagina,url,data_hora_fuso,axe_versao,json,passes,violations,incomplete,inapplicable,proporcao_aprovada,criticos_distintos,serios_distintos,total_afetado,ocorrencias
```

```csv
rodada,pagina,identificador_ancestry_ou_target,regras,maior_impacto,descricao,evidencia
```

## Consolidação

Preencha uma linha por tarefa para M1.1.2, M1.2.1 e M1.3.1, uma por página para M1.6.1 e M1.6.2 e uma para cada métrica restante. Inclua o recorte adicional “média T1–T3” para M1.2.1. Expresse NC e indique a causa no campo de observações.

```csv
rodada,metrica,recorte,numerador,denominador,observacoes_validas,valor,unidade,nivel,evidencia,observacoes
```
