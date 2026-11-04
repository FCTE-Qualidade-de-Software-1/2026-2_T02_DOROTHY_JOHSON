# Painel PSM

Visão rápida dos indicadores do [Plano de Medição](plano-medicao.md), calculados a partir dos
snapshots diários em
[`data/psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_DOROTHY_JOHSON/tree/main/data/psm)
pelo script `scripts/psm/indicadores.py`. O painel é recalculado a cada publicação do site, e o
site é publicado logo depois de cada coleta diária. A interpretação de cada semana e as decisões
tomadas ficam no [Registro Semanal](registro-medicoes.md).

<div id="painel-psm-dados" class="painel-psm" data-fonte="../../assets/psm/painel.json">
  <p class="painel-psm__estado" role="status">Carregando os dados do painel…</p>
  <div class="painel-psm__kpis" data-kpis></div>

  <section class="painel-psm__bloco" aria-labelledby="painel-m1">
    <h2 id="painel-m1">M1: trabalho restante da entrega</h2>
    <p class="painel-psm__nota">Percentual do planejado ainda aberto ao fim de cada dia, em issues e em pontos, comparado com a linha ideal até o prazo.</p>
    <div class="painel-psm__grafico painel-psm__grafico--alto"><canvas data-grafico="m1" role="img" aria-label="Linhas do trabalho restante em issues e em pontos, com a linha ideal"></canvas></div>
    <details class="painel-psm__tabela"><summary>Ver os dados do M1 em tabela</summary><div data-tabela="m1"></div></details>
  </section>

  <div class="painel-psm__filtro">
    <label for="painel-semana">Semana de M2 a M4</label>
    <select id="painel-semana" data-semana></select>
  </div>

  <div class="painel-psm__grade">
    <section class="painel-psm__bloco" aria-labelledby="painel-m2">
      <h2 id="painel-m2">M2: horas por membro</h2>
      <p class="painel-psm__nota" data-nota="m2"></p>
      <div class="painel-psm__grafico"><canvas data-grafico="m2" role="img" aria-label="Barras de horas por membro na semana"></canvas></div>
    </section>

    <section class="painel-psm__bloco" aria-labelledby="painel-m3">
      <h2 id="painel-m3">M3: horas por ponto</h2>
      <p class="painel-psm__nota" data-nota="m3"></p>
      <div class="painel-psm__grafico"><canvas data-grafico="m3" role="img" aria-label="Barras de horas por ponto em cada semana"></canvas></div>
    </section>
  </div>

  <section class="painel-psm__bloco" aria-labelledby="painel-m4">
    <h2 id="painel-m4">M4: lead time das issues</h2>
    <p class="painel-psm__nota" data-nota="m4-issues"></p>
    <div class="painel-psm__grafico painel-psm__grafico--variavel" data-altura="m4-issues"><canvas data-grafico="m4-issues" role="img" aria-label="Barras do lead time de cada issue concluída na semana"></canvas></div>
  </section>

  <section class="painel-psm__bloco" aria-labelledby="painel-m4-prs">
    <h2 id="painel-m4-prs">M4: tempo até o merge dos PRs</h2>
    <p class="painel-psm__nota" data-nota="m4-prs"></p>
    <div class="painel-psm__grafico painel-psm__grafico--variavel" data-altura="m4-prs"><canvas data-grafico="m4-prs" role="img" aria-label="Barras do tempo entre abertura e merge de cada PR da semana"></canvas></div>
  </section>

  <details class="painel-psm__tabela"><summary>Ver os dados de M2 a M4 da semana em tabela</summary><div data-tabela="semana"></div></details>
  <p class="painel-psm__rodape" data-rodape></p>
</div>

!!! note "Como ler"
    - **M1:** a linha ideal cai até zero no prazo da entrega. Linhas acima dela indicam atraso;
      pelo plano, um desvio maior que 10 pontos percentuais leva a considerar o replanejamento.
    - **M2 e M3:** usam `Estimate` e `Horas` atuais das issues concluídas na semana. Parte dos
      valores da Entrega 1 foi preenchida retroativamente (ver o
      [Registro Semanal](registro-medicoes.md#semana-2-2710-a-02112026)).
    - **M4:** barras marcadas com "acima do limite" passam de 10% sobre a média da semana e
      devem ser investigadas no registro semanal. O padrão de revisão da equipe é o merge feito
      por outro membro; PRs mergeados pelo próprio autor aparecem como "merge do autor".
    - **Cobertura de Estimate e Horas:** conta só as issues da entrega que não foram fechadas
      como não planejadas.
