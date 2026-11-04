// Painel PSM: desenha M1 a M4 a partir de assets/psm/painel.json (gerado por hooks/psm_painel.py).
(function () {
  "use strict";

  const graficos = [];
  let dados = null;
  let observador = null;

  const numero = (valor, casas = 1) =>
    valor == null ? "–" : valor.toLocaleString("pt-BR", { minimumFractionDigits: casas, maximumFractionDigits: casas });
  const diaCurto = (iso) => iso.slice(8, 10) + "/" + iso.slice(5, 7);

  function cores(raiz) {
    const css = getComputedStyle(raiz);
    const ler = (nome) => css.getPropertyValue(nome).trim();
    return {
      serie1: ler("--psm-serie-1"),
      serie2: ler("--psm-serie-2"),
      ideal: ler("--psm-ideal"),
      critico: ler("--psm-critico"),
      texto: ler("--psm-texto"),
      textoSecundario: ler("--psm-texto-2"),
      grade: ler("--psm-grade"),
      eixo: ler("--psm-eixo"),
      superficie: ler("--psm-superficie"),
    };
  }

  // Linhas verticais de referência (média e limite) nos gráficos de M4.
  const referencias = {
    id: "referencias",
    afterDatasetsDraw(chart, _args, opcoes) {
      const { ctx, chartArea, scales } = chart;
      (opcoes.linhas || []).forEach((linha) => {
        if (linha.valor == null) return;
        const x = scales.x.getPixelForValue(linha.valor);
        ctx.save();
        ctx.strokeStyle = linha.cor;
        ctx.lineWidth = 1.5;
        ctx.setLineDash(linha.tracejado ? [4, 4] : []);
        ctx.beginPath();
        ctx.moveTo(x, chartArea.top);
        ctx.lineTo(x, chartArea.bottom);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = opcoes.corTexto;
        ctx.font = "12px system-ui, sans-serif";
        ctx.textAlign = "left";
        ctx.fillText(linha.rotulo, x + 4, chartArea.top + 12 + (linha.deslocamento || 0));
        ctx.restore();
      });
    },
  };

  function base(c) {
    return {
      responsive: true,
      maintainAspectRatio: false,
      animation: false,
      interaction: { mode: "index", intersect: false },
      plugins: {
        legend: { labels: { color: c.texto, usePointStyle: true, boxHeight: 8 } },
        tooltip: { backgroundColor: c.superficie, titleColor: c.texto, bodyColor: c.texto, borderColor: c.eixo, borderWidth: 1 },
      },
      scales: {
        x: { ticks: { color: c.textoSecundario }, grid: { color: c.grade }, border: { color: c.eixo } },
        y: { ticks: { color: c.textoSecundario }, grid: { color: c.grade }, border: { color: c.eixo } },
      },
    };
  }

  function barras(c, rotulos, valores, cor, rotuloEixo, extra = {}) {
    const opcoes = base(c);
    opcoes.indexAxis = "y";
    opcoes.interaction = { mode: "nearest", axis: "y", intersect: false };
    opcoes.plugins.legend.display = false;
    opcoes.scales.x.beginAtZero = true;
    opcoes.scales.x.title = { display: true, text: rotuloEixo, color: c.textoSecundario };
    opcoes.scales.y.grid = { display: false };
    Object.assign(opcoes.plugins, extra.plugins || {});
    return {
      type: "bar",
      data: { labels: rotulos, datasets: [{ data: valores, backgroundColor: cor, borderRadius: 4, borderSkipped: "start", barPercentage: 0.7, categoryPercentage: 0.9, maxBarThickness: 22 }] },
      options: opcoes,
      plugins: extra.registrar || [],
    };
  }

  function desenhar(raiz, canvasId, config) {
    const canvas = raiz.querySelector(`[data-grafico="${canvasId}"]`);
    graficos.push(new Chart(canvas, config));
  }

  function tabela(cabecalho, linhas) {
    const th = cabecalho.map((t) => `<th>${t}</th>`).join("");
    const tr = linhas.map((l) => `<tr>${l.map((v) => `<td>${v}</td>`).join("")}</tr>`).join("");
    return `<table><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table>`;
  }

  function kpis(raiz) {
    const ultimo = dados.m1[dados.m1.length - 1];
    const horas = dados.semanas.reduce((t, s) => t + Object.values(s.m2).reduce((a, b) => a + b, 0), 0);
    const prs = dados.semanas.flatMap((s) => s.m4_prs.itens);
    const revisados = prs.filter((p) => p.por_outra_pessoa).length;
    const desvio = ultimo.restante_issues_pct - ultimo.ideal_pct;
    const blocos = [
      ["Concluído (issues)", `${numero(100 * ultimo.concluidas / ultimo.issues, 0)}%`, `${ultimo.concluidas} de ${ultimo.issues} em ${diaCurto(ultimo.dia)}`],
      ["Desvio da linha ideal", `${numero(desvio, 0)} p.p.`, desvio > 10 ? "⚠ acima do limite de 10 p.p." : "dentro do limite de 10 p.p."],
      ["Horas registradas", `${numero(horas, 1)} h`, "issues concluídas no período"],
      ["Cobertura de Estimate e Horas", `${dados.cobertura.com_horas} de ${dados.cobertura.issues}`, `com Horas; ${dados.cobertura.com_estimate} com Estimate (sem as não planejadas)`],
      ["PRs mergeados por outra pessoa", `${revisados} de ${prs.length}`, "padrão de revisão da equipe"],
    ];
    raiz.querySelector("[data-kpis]").innerHTML = blocos
      .map(([rotulo, valor, detalhe]) => `<div class="painel-psm__kpi"><span>${rotulo}</span><strong>${valor}</strong><small>${detalhe}</small></div>`)
      .join("");
  }

  function graficoM1(raiz, c) {
    const opcoes = base(c);
    opcoes.scales.y.min = 0;
    opcoes.scales.y.max = 100;
    opcoes.scales.y.title = { display: true, text: "% do planejado ainda aberto", color: c.textoSecundario };
    opcoes.plugins.tooltip.callbacks = { label: (ctx) => `${ctx.dataset.label}: ${numero(ctx.parsed.y, 0)}%` };
    desenhar(raiz, "m1", {
      type: "line",
      data: {
        labels: dados.m1.map((p) => diaCurto(p.dia)),
        datasets: [
          { label: "Issues", data: dados.m1.map((p) => p.restante_issues_pct), borderColor: c.serie1, backgroundColor: c.serie1, borderWidth: 2, pointRadius: 4, pointBorderColor: c.superficie, pointBorderWidth: 2, tension: 0 },
          { label: "Pontos", data: dados.m1.map((p) => p.restante_pontos_pct), borderColor: c.serie2, backgroundColor: c.serie2, borderWidth: 2, pointRadius: 4, pointStyle: "rectRot", pointBorderColor: c.superficie, pointBorderWidth: 2, tension: 0 },
          { label: "Linha ideal", data: dados.m1.map((p) => p.ideal_pct), borderColor: c.ideal, backgroundColor: c.ideal, borderWidth: 2, borderDash: [6, 4], pointRadius: 0, tension: 0 },
        ],
      },
      options: opcoes,
    });
    raiz.querySelector('[data-tabela="m1"]').innerHTML = tabela(
      ["Dia", "Issues", "Concluídas", "Pontos", "Pontos concluídos", "Restante (issues)", "Ideal"],
      dados.m1.map((p) => [diaCurto(p.dia), p.issues, p.concluidas, p.pontos, p.pontos_concluidos, `${numero(p.restante_issues_pct, 0)}%`, `${numero(p.ideal_pct, 0)}%`])
    );
  }

  function graficosSemana(raiz, c, indice) {
    graficos.splice(1).forEach((g) => g.destroy());
    const s = dados.semanas[indice];
    const periodo = `${diaCurto(s.inicio)} a ${diaCurto(s.fim)}`;

    const membros = Object.keys(s.m2);
    raiz.querySelector('[data-nota="m2"]').textContent = membros.length
      ? `Issues concluídas de ${periodo}. Horas de issues com mais de um responsável são divididas igualmente.`
      : `Nenhuma issue com Horas concluída de ${periodo}.`;
    desenhar(raiz, "m2", barras(c, membros, membros.map((m) => s.m2[m]), c.serie1, "horas", {
      plugins: { tooltip: { ...base(c).plugins.tooltip, callbacks: { label: (ctx) => `${numero(ctx.parsed.x, 2)} h` } } },
    }));

    const semanasM3 = dados.semanas.filter((x) => x.m3.horas_por_ponto != null);
    raiz.querySelector('[data-nota="m3"]').textContent = semanasM3.length
      ? "Horas por ponto de cada semana. O plano investiga variação acima de 10% em relação à semana anterior."
      : "Sem issues com Estimate e Horas concluídas no período.";
    const opcoesM3 = base(c);
    opcoesM3.plugins.legend.display = false;
    opcoesM3.scales.y.beginAtZero = true;
    opcoesM3.scales.y.title = { display: true, text: "h/ponto", color: c.textoSecundario };
    opcoesM3.scales.x.grid = { display: false };
    opcoesM3.plugins.tooltip.callbacks = { label: (ctx) => `${numero(ctx.parsed.y, 2)} h/ponto` };
    desenhar(raiz, "m3", {
      type: "bar",
      data: {
        labels: semanasM3.map((x) => `${diaCurto(x.inicio)}–${diaCurto(x.fim)}`),
        datasets: [{ data: semanasM3.map((x) => x.m3.horas_por_ponto), backgroundColor: c.serie1, borderRadius: 4, borderSkipped: "start", maxBarThickness: 48 }],
      },
      options: opcoesM3,
    });

    const m4 = (chave, nota, unidade, rotuloItem) => {
      const bloco = s[chave];
      const itens = [...bloco.itens].sort((a, b) => b[unidade.campo] - a[unidade.campo]);
      raiz.querySelector(`[data-altura="${chave.replace("_", "-")}"]`).style.height = `${Math.max(120, 28 * itens.length + 70)}px`;
      raiz.querySelector(`[data-nota="${chave.replace("_", "-")}"]`).textContent = itens.length
        ? `${nota} de ${periodo}: média de ${numero(bloco.media)} ${unidade.nome}, limite de investigação de ${numero(bloco.limite)} ${unidade.nome}. ${itens.filter((i) => i.acima).length} acima do limite.`
        : `Nenhum item de ${periodo}.`;
      desenhar(raiz, chave.replace("_", "-"), barras(
        c,
        itens.map(rotuloItem),
        itens.map((i) => i[unidade.campo]),
        itens.map((i) => (i.acima ? c.critico : c.serie1)),
        unidade.nome,
        {
          plugins: {
            tooltip: { ...base(c).plugins.tooltip, callbacks: { title: (ctx) => itens[ctx[0].dataIndex].titulo, label: (ctx) => `${numero(ctx.parsed.x)} ${unidade.nome}${itens[ctx.dataIndex].acima ? " (acima do limite)" : ""}` } },
            referencias: {
              corTexto: c.textoSecundario,
              linhas: [
                { valor: bloco.media, rotulo: "média", cor: c.ideal, tracejado: false },
                { valor: bloco.limite, rotulo: "limite", cor: c.critico, tracejado: true, deslocamento: 14 },
              ],
            },
          },
          registrar: [referencias],
        }
      ));
      return itens;
    };
    const issues = m4("m4_issues", "Issues concluídas", { campo: "dias", nome: "dias" }, (i) => `#${i.numero}${i.acima ? " ⚠ acima do limite" : ""}`);
    const prs = m4("m4_prs", "PRs mergeados", { campo: "horas", nome: "h" }, (p) => `#${p.numero}${p.por_outra_pessoa ? "" : " (merge do autor)"}${p.acima ? " ⚠ acima do limite" : ""}`);

    raiz.querySelector('[data-tabela="semana"]').innerHTML =
      tabela(["Membro", "Horas"], membros.map((m) => [m, numero(s.m2[m], 2)])) +
      tabela(["Issue", "Título", "Lead time (dias)", "Situação"], issues.map((i) => [`#${i.numero}`, i.titulo, numero(i.dias), i.acima ? "acima do limite" : "–"])) +
      tabela(["PR", "Autor", "Merge feito por", "Até o merge (h)", "Situação"], prs.map((p) => [`#${p.numero}`, p.autor, p.mergeado_por || "–", numero(p.horas), p.acima ? "acima do limite" : "–"]));
  }

  function renderizar(raiz) {
    graficos.splice(0).forEach((g) => g.destroy());
    const c = cores(raiz);
    kpis(raiz);
    graficoM1(raiz, c);
    const seletor = raiz.querySelector("[data-semana]");
    graficosSemana(raiz, c, Number(seletor.value));
  }

  async function iniciar() {
    const raiz = document.getElementById("painel-psm-dados");
    if (!raiz || typeof Chart === "undefined") return;
    const estado = raiz.querySelector(".painel-psm__estado");
    try {
      const resposta = await fetch(raiz.dataset.fonte, { cache: "no-store" });
      dados = await resposta.json();
    } catch (erro) {
      estado.textContent = "Não foi possível carregar os dados do painel.";
      return;
    }
    estado.hidden = true;

    const seletor = raiz.querySelector("[data-semana]");
    seletor.innerHTML = dados.semanas
      .map((s, i) => `<option value="${i}">${diaCurto(s.inicio)} a ${diaCurto(s.fim)}</option>`)
      .join("");
    const comDados = dados.semanas.map((s, i) => (s.issues_concluidas || s.m4_prs.itens.length ? i : -1)).filter((i) => i >= 0);
    seletor.value = String(comDados.length ? comDados[comDados.length - 1] : dados.semanas.length - 1);
    seletor.addEventListener("change", () => graficosSemana(raiz, cores(raiz), Number(seletor.value)));

    raiz.querySelector("[data-rodape]").textContent =
      `Último snapshot: ${dados.ultimo_snapshot.arquivo}, coletado em ${new Date(dados.ultimo_snapshot.coletado_em).toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo" })}. ` +
      `Milestones: ${dados.milestones.join(", ")}; prazo em ${diaCurto(dados.prazo)}.`;

    renderizar(raiz);
    observador?.disconnect();
    observador = new MutationObserver(() => renderizar(raiz));
    observador.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
  }

  if (window.document$) {
    window.document$.subscribe(iniciar);
  } else {
    document.addEventListener("DOMContentLoaded", iniciar);
  }
})();
