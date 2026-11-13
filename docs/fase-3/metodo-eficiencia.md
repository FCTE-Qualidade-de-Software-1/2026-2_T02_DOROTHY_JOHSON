# Método e instruções de medição: eficiência de desempenho

Esta página descreve como obter as cinco métricas do objetivo G3
([Fase 2](../fase-2/metricas.md#g3-eficiencia-de-desempenho)) de forma repetível: outra pessoa
da equipe deve conseguir executar a coleta só lendo estas instruções (critério F3-C1). O
ambiente está em [Recursos e ambiente](ambiente.md#31-eficiencia-de-desempenho-g3).

## 1. Visão geral

| Métrica | O que mede | Método | Instrumento | Dado bruto |
|---|---|---|---|---|
| M3.1.1 | Primeira resposta da página (FCP) | Procedimento A | Lighthouse 12.8.2 | `lighthouse/<pagina>-<n>.json` |
| M3.1.2 | Exibição do conteúdo principal (LCP) | Procedimento A | Lighthouse 12.8.2 | `lighthouse/<pagina>-<n>.json` |
| M3.3.1 | Tempo de CPU na thread principal | Procedimento A | Lighthouse 12.8.2 | `lighthouse/<pagina>-<n>.json` |
| M3.2.1 | Tempo de execução de T1 e T2 | Procedimento B | Script com Playwright e protocolo do Chrome DevTools | `tarefas.json` |
| M3.4.1 | Memória do JavaScript (*JS heap*) | Procedimento B | Script com Playwright e protocolo do Chrome DevTools | `tarefas.json` |

Os dados brutos ficam em `data/fase-4/eficiencia/`. Cada página ou tarefa é medida **5 vezes**,
e o valor da métrica é a **mediana** das 5 execuções.

| Página | Endereço | Procedimento A | Procedimento B |
|---|---|---|---|
| Meu Território | `/meu-territorio` | Carregamento | Carregamento e T1 |
| SITGeo | `/plataforma-geoespacial` | Carregamento | Carregamento e T2 |
| Biblioteca Territorial | `/downloads` | Carregamento | Carregamento |

## 2. Preparação

1. Usar a máquina e as versões descritas no [ambiente](ambiente.md#31-eficiencia-de-desempenho-g3).
   Se alguma versão for diferente, registrar a diferença no README da coleta (passo 5).
2. Instalar as dependências, sem baixar navegadores do Playwright (é usado o Chrome instalado):

    ```bash
    PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install --no-save playwright@1.48.2
    ```

3. Fechar navegadores, editores pesados, sincronizações e downloads. Manter o notebook ligado à
   tomada.
4. Conferir no navegador que o portal abre e que o território e a camada de referência existem
   ([objetos de referência](ambiente.md#2-paginas-tarefas-e-objetos-de-referencia)).
5. Criar `data/fase-4/eficiencia/README.md` com: data, hora de início, avaliador, tipo de
   conexão (cabo ou Wi-Fi) e versões do Chrome e do Node.js.

## 3. Procedimento A: carregamento das páginas (M3.1.1, M3.1.2 e M3.3.1)

Na raiz do repositório:

```bash
scripts/fase-4/eficiencia/lighthouse.sh
```

O script executa o Lighthouse 5 vezes em cada página, uma de cada vez, com:

- categoria desempenho e o perfil móvel padrão (celular de 412 × 823 px, latência de 150 ms,
  1,6 Mbit/s de download e CPU 4 vezes mais lenta);
- um perfil de navegador novo a cada execução, portanto com cache vazio;
- saída em `data/fase-4/eficiencia/lighthouse/<pagina>-<n>.json`.

Cada relatório fornece as três métricas:

| Métrica | Campo do relatório JSON |
|---|---|
| M3.1.1 | `audits["first-contentful-paint"].numericValue` (ms) |
| M3.1.2 | `audits["largest-contentful-paint"].numericValue` (ms) |
| M3.3.1 | `audits["mainthread-work-breakdown"].numericValue` (ms) |

**Conferência:** abrir um relatório de cada página e verificar que não há `runtimeError`. Se uma
execução falhar, apagar o arquivo e repetir só essa execução com o mesmo número, anotando a
repetição no README da coleta.

## 4. Procedimento B: tarefas e memória (M3.2.1 e M3.4.1)

```bash
node scripts/fase-4/eficiencia/tarefas.js
```

O script aplica a mesma limitação do perfil móvel no próprio navegador e, para cada execução,
abre um contexto novo (cache vazio):

1. **T1:** carrega Meu Território e espera a rede ficar ociosa; força a coleta de lixo e
   registra o *JS heap* (memória após o carregamento); seleciona a UF **GO** e o território
   **Chapada dos Veadeiros - GO**; clica em **Selecionar** e cronometra a tarefa; força a
   coleta de lixo e registra o *JS heap* (memória após a tarefa).
2. **T2:** carrega o SITGeo, registra a memória após o carregamento, clica para ativar a camada
   **PRONAF - Valor Total de Crédito Acessado**, cronometra e registra a memória após a tarefa.
3. **Biblioteca Territorial:** carrega a página e registra só a memória após o carregamento,
   porque o G3 não tem tarefa nela.

**Fim da tarefa.** O tempo vai do clique até o fim da última requisição de rede disparada pela
ação, considerando a tarefa concluída quando a rede fica 1 s sem requisições pendentes (limite
de 60 s). O critério é o mesmo do piloto, o que mantém a comparação com ele.

O resultado vai para `data/fase-4/eficiencia/tarefas.json`, uma linha por execução, com o tempo
em segundos, a memória em MB, a versão do navegador e o instante da coleta. Uma execução que
falha é repetida automaticamente (até 10 tentativas por tarefa), e a falha aparece no terminal;
copiar essas mensagens para o README da coleta.

## 5. Consolidação

```bash
scripts/fase-4/eficiencia/resumo.sh
```

Gera `data/fase-4/eficiencia/resumo.csv` com, para cada página ou tarefa e métrica, a
**mediana**, o **mínimo**, o **máximo** e o número de execuções.

- **Mediana como valor da métrica:** a documentação do Lighthouse recomenda valores agregados,
  como a mediana de 5 execuções, por serem mais estáveis que uma execução isolada
  (GOOGLE, 2023). A mediana também reduz o efeito de uma execução atípica sem exigir um
  critério de descarte.
- **Mínimo e máximo:** mostram a dispersão das 5 execuções e entram nas tabelas de resultado da
  Fase 4. Nenhuma execução válida é descartada.
- **Valores ausentes:** uma métrica só é consolidada com 5 execuções válidas. Se não for
  possível obtê-las, o resumo mostra o número real de execuções, e a lacuna é registrada como
  limitação na Fase 4.

A pontuação de cada recorte, de 0 (Insatisfatório) a 3 (Excelente), e o julgamento do G3 seguem os
[níveis de pontuação de G3](../fase-2/niveis-pontuacao.md#4-g3-eficiencia-de-desempenho).

## 6. Diferença em relação à Fase 2

As fichas de M3.2.1 e M3.4.1 previam a gravação manual no painel Performance do Chrome
DevTools. A coleta passa a usar o script do Procedimento B, que lê as mesmas grandezas pelo
protocolo do DevTools (instante do clique, requisições de rede e *JS heap* após a coleta de
lixo). A troca evita a marcação manual do início e do fim em 30 gravações e torna a medição
repetível por qualquer membro da equipe. As fichas da Fase 2 foram atualizadas, e a decisão
entra na rastreabilidade F2 → F3 (#69).

## 7. Tempo estimado

A coleta completa (Procedimentos A e B) leva cerca de 15 a 20 minutos, a ordem de grandeza do
piloto de 20/10/2026, que durou 12 minutos.

## Referências

GOOGLE. **Lighthouse variability**. [S.l.]: Google, 2023. Disponível em: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md>. Acesso em: 08 nov. 2026.
