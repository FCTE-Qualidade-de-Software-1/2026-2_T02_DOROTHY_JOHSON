# Análise e respostas GQM: flexibilidade

Esta página responde às questões Q2.1 a Q2.3 e ao objetivo G2 com os dados coletados conforme o
[método de flexibilidade](../fase-3/metodo-flexibilidade.md). Cada recorte foi pontuado pelos
[níveis de G2](../fase-2/niveis-pontuacao.md#3-g2-flexibilidade), de 0 (Insatisfatório) a 3
(Excelente), e consolidado pelos
[critérios de julgamento](../fase-2/niveis-pontuacao.md#5-criterios-de-julgamento-por-caracteristica).

!!! warning "Resultado parcial"
    Os Procedimentos A e B (larguras de tela, M2.2.1 e M2.2.2) foram executados em 15/11/2026.
    A matriz de navegadores e sistemas (Procedimento C, M2.1.1) ainda não foi executada, e
    M2.3.1 depende dela. Por isso, **Q2.1 e Q2.3 ainda não têm resposta completa e o juízo do
    G2 está pendente**, como manda a regra de cobertura insuficiente
    ([seção 5.2](../fase-2/niveis-pontuacao.md#52-regras-de-gravidade-e-excecoes)). Esta
    página é atualizada quando `execucoes.csv` for preenchido; o cálculo é refeito com
    `scripts/fase-4/flexibilidade/pontuar.py`.

## 1. Coleta

| Item | Valor |
|---|---|
| Data e horário | 15/11/2026, das 20:24 às 20:38 (horário de Brasília) |
| Ambiente | Chrome 151 em modo de dispositivo, larguras de 360 a 1920 px ([ambiente, seção 3.3](../fase-3/ambiente.md#33-flexibilidade-g2)) |
| Execuções | 2 de cada combinação e de cada função; as duas deram o mesmo resultado |
| Dados brutos | [`data/fase-4/flexibilidade/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/fase-4/flexibilidade) (`rolagem.csv`, `funcoes.csv`, `falhas.csv` e 42 capturas de tela) |
| Pontuação | `data/fase-4/flexibilidade/pontuacao.csv`, gerado por `scripts/fase-4/flexibilidade/pontuar.py` |
| Desvios do plano | Matriz de ambientes (M2.1.1) pendente; falhas F01 a F03 vistas em emulação, ainda sem confirmação no celular de referência |

## 2. Resultados por questão

### Q2.1 As tarefas T1, T2 e T3 podem ser concluídas nos navegadores e sistemas operacionais mais usados pelo público?

**Pendente.** M2.1.1 depende da execução manual das três tarefas nos seis ambientes da
[matriz](../fase-3/metodo-flexibilidade.md#51-matriz-de-ambientes), que ainda não foi feita.

**Indício (não pontuado):** no Procedimento B, o script executou T1 e T2 no Chrome em emulação
de celular (360 px) e de computador (1366 px), nas 2 execuções, sem precisar de clique
forçado. As duas tarefas, portanto, funcionam no motor do Chrome nas duas larguras. Isso não
substitui a matriz, que testa outros navegadores e aparelhos reais.

### Q2.2 As páginas se adaptam às telas de celular, tablet e computador sem perder conteúdo nem funções?

**M2.2.1, rolagem horizontal:**

| Página | 360 px | 412 px | 768 px | 1366 px | 1920 px |
|---|:---:|:---:|:---:|:---:|:---:|
| Meu Território | Sem rolagem | Sem rolagem | Sem rolagem | Sem rolagem | Sem rolagem |
| SITGeo | Sem rolagem | Sem rolagem | Sem rolagem | Sem rolagem | Sem rolagem |
| Biblioteca Territorial | **Com rolagem** | **Com rolagem** | Sem rolagem | Sem rolagem | Sem rolagem |

*Tabela 1: Rolagem horizontal por página e largura (igual nas 2 execuções).*

São **13 de 15 combinações sem rolagem (86,7%): Aceitável (1)**. A rolagem da Biblioteca
Territorial nas duas larguras de celular vem das setas do carrossel da Mapoteca, que ficam
fora da tela (a borda direita chega a 377 px em uma tela de 360 px). Nenhuma combinação
precisou da exceção do mapa.

**M2.2.2, funções preservadas em 360 px:**

| Página | Preservadas | X | Nível | Funções perdidas |
|---|---:|---:|---|---|
| Meu Território | 12/12 | 100,0% | Excelente (3) | — |
| SITGeo | 4/6 | 66,7% | Aceitável (1) | Nome e dados das camadas (GEO-04); zoom do mapa (GEO-05) |
| Biblioteca Territorial | 6/7 | 85,7% | Bom (2) | Setas do carrossel da Mapoteca (BIB-05) |

*Tabela 2: Funções disponíveis em 1366 px que continuam operáveis em 360 px. M2.2.2 = 2,00
(média das três páginas).*

<div class="grid" markdown>

![SITGeo em 360 px: painel de camadas estreito, com os cartões cobertos, e a caixa da legenda sobre o zoom do mapa](flexibilidade/sitgeo-360.jpg)

![Biblioteca Territorial em 360 px: as setas do carrossel da Mapoteca ficam além da borda direita da tela](flexibilidade/mapoteca-360.jpg)

</div>

*Figura 1: SITGeo (esquerda) e Mapoteca da Biblioteca Territorial (direita) em 360 px. Na
Biblioteca, a captura da página inteira tem 392 px de largura: as setas ficam na faixa além
dos 360 px da tela.*

No SITGeo, a página mantém no celular a mesma grade de 5 colunas do computador: o painel de
camadas fica com cerca de 1/5 da tela (cerca de 65 px), e o mapa, com os outros 4/5. Com isso:

- o cabeçalho do tema, mais largo que a coluna, cobre os cartões das camadas, e o nome, a
  fonte e a unidade de cada camada ficam cortados ou cobertos (GEO-04);
- a caixa com o nome e a legenda da camada ativa ocupa quase toda a largura do mapa e cobre os
  botões + e – (GEO-05).

O botão de ativar a camada continua acessível, por isso T2 ainda pode ser concluída, mas é
difícil saber qual camada está sendo ativada.

**Resposta:** as páginas se adaptam bem a tablet e computador, sem rolagem e sem perda de
funções. No celular, Meu Território se adapta por completo, mas o SITGeo perde duas de suas
seis funções e a Biblioteca Territorial exige rolagem horizontal para usar o carrossel da
Mapoteca. **Pontos de Q2.2: 1,50** (M2.2.1 = 1,00; M2.2.2 = 2,00).

### Q2.3 Quais ambientes concentram as falhas e, por isso, devem ter prioridade na matriz de testes do fornecedor?

**Parcial.** M2.3.1 é calculada por ambiente da matriz e depende do Procedimento C. Até agora,
as três falhas registradas foram vistas em emulação de celular e foram reproduzidas na
segunda execução:

| ID | Página | Largura | Gravidade | Falha |
|---|---|---|---|---|
| F01 | Biblioteca Territorial | 360 e 412 px | Grave | Setas do carrossel da Mapoteca fora da tela, com rolagem horizontal |
| F02 | SITGeo | 360 px | Grave | Botões de zoom cobertos pela caixa da legenda; contorno: gesto de pinça |
| F03 | SITGeo | 360 px | Grave | Nome, fonte e unidade das camadas cobertos; dificulta T2 |

*Tabela 3: Falhas dependentes de largura, pré-registradas para M2.3.1.*

Nenhuma ocorre em 1366 px, nenhuma é bloqueante e todas estão nas larguras de celular. Se as
três forem confirmadas no celular de referência, cada ambiente móvel em que se repetirem terá
3 falhas graves e ficará **Insatisfatório (0)** em M2.3.1 (regra "≥ 3 graves").

**Resposta parcial:** as falhas encontradas até agora se concentram nas **telas de celular**
e, entre as páginas, no **SITGeo**. Para o fornecedor, isso já indica que a matriz de testes
deve incluir pelo menos uma largura de celular (360 px) para o SITGeo e a Biblioteca
Territorial. A comparação entre navegadores (Safari/iOS, Samsung Internet, Firefox e Edge)
depende da matriz manual.

## 3. Julgamento do G2

| Questão | Métricas | Pontos |
|---|---|---:|
| Q2.1 | M2.1.1 = NC | NC |
| Q2.2 | M2.2.1 = 1,00; M2.2.2 = 2,00 | 1,50 |
| Q2.3 | M2.3.1 = NC | NC |
| **G2** | Média das três questões | **pendente** |

*Tabela 4: Consolidação da pontuação do G2.*

- **Juízo:** **pendente**, porque M2.1.1 e M2.3.1 ainda não têm resultado válido.
- **Limitador (seção 5.2):** até agora não há falha bloqueante; se a matriz revelar uma, o
  juízo final será Insatisfatório, qualquer que seja a média.
- **Onde a qualidade já está comprometida:** o layout do SITGeo no celular (F02 e F03) e o
  carrossel da Mapoteca (F01). As três falhas têm a mesma origem provável, um layout que não
  muda de estrutura nas telas estreitas, e podem ser tratadas juntas.

## 4. Hipóteses

| Hipótese | Resultado | Evidência |
|---|---|---|
| H2.1: tarefas concluídas em todos os navegadores Chromium; falha em pelo menos uma execução no Safari/iOS e no Firefox, mais provável em T2 | **Pendente** | Depende de M2.1.1. Indício: T1 e T2 funcionam no Chrome em 360 e 1366 px |
| H2.2: sem rolagem a partir de 768 px e com rolagem em 360 px em pelo menos uma página; perda de funções no celular só no SITGeo | **Parcialmente confirmada** | Rolagem só na Biblioteca, em 360 e 412 px, e nenhuma a partir de 768 px (confirmada). O SITGeo perde funções (confirmada), mas a Biblioteca também perde uma (refutado o "só no SITGeo") |
| H2.3: falhas concentradas no SITGeo, nas larguras de celular e no Safari/iOS; sem falha bloqueante no Chrome/Android | **Parcialmente confirmada** | As 3 falhas estão em larguras de celular e 2 delas no SITGeo; nenhuma é bloqueante. A parte sobre Safari/iOS e Chrome/Android depende da matriz |

*Tabela 5: Situação das hipóteses de G2.*

## 5. Outros achados e limitações

**Defeito geral, fora de M2.3.1.** A imagem da legenda da camada ativa no SITGeo não carrega
(o servidor de mapas devolve uma imagem vazia, e aparece só o texto alternativo "Legenda"), em
360 e em 1366 px. Como também ocorre no ambiente de referência, é um defeito do produto, e não
uma falha de ambiente, e fica registrado separadamente, como manda a
[seção 3 dos níveis](../fase-2/niveis-pontuacao.md#justificativas-e-particularidades-de-g2).

**Limitações:**

- **Emulação:** M2.2.1 e M2.2.2 foram medidas no modo de dispositivo do Chrome, que simula a
  largura, o toque e o *viewport* de celular, mas não um aparelho específico. As perdas de
  função ainda precisam ser confirmadas no celular de referência
  ([método, seção 4.4](../fase-3/metodo-flexibilidade.md#44-confirmacao-no-celular-de-referencia)).
- **Critério automático de função:** o script considera perdida uma função coberta, fora da
  largura ou desabilitada. Ele não avalia se o texto fica legível; por isso uma função
  "preservada" pode ainda ser difícil de usar.
- **Produto em produção:** a coleta reflete o portal em 15/11/2026; mudanças no layout até a
  execução da matriz manual podem alterar o resultado.
