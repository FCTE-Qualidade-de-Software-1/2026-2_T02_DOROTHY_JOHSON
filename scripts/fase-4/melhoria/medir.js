// Mede o efeito da ação de melhoria (imagens do SITGeo otimizadas): LCP e peso da
// página, antes × depois, com a mesma limitação do perfil móvel usada em
// scripts/fase-4/eficiencia/tarefas.js (RTT 150 ms, 1638,4 kbps, CPU 4x, cache vazio).
//
//   antes:  a página do portal como está em produção;
//   depois: a mesma página, com as duas imagens trocadas pelas versões otimizadas no momento
//           da requisição. O portal não é alterado.
//
// As execuções são alternadas (antes, depois, antes, ...) para que a variação do servidor
// afete as duas condições do mesmo modo.
// Procedimento: docs/fase-4/acao-melhoria.md (seção "Como o efeito é medido").
//
// Uso: node scripts/fase-4/melhoria/medir.js [saida.json]
// Variáveis opcionais:
//   OTIMIZADAS  endereço https da pasta com as imagens otimizadas (padrão: GitPage da equipe)
//               ou pasta local (ex.: docs/fase-4/melhoria/img). Com pasta local, o tempo de
//               transferência é simulado pelo tamanho do arquivo, porque a resposta não
//               passa pela rede limitada.
//   LARGURA     versão usada na troca (padrão 960, a maior e, portanto, a mais desfavorável)
//   BASE, PAGINA, EXECUCOES, CHROME_PATH
// Requer o pacote playwright e o Google Chrome instalado.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const BASE = process.env.BASE || 'https://territoriosdacidadania.mda.gov.br';
const PAGINA = process.env.PAGINA || '/plataforma-geoespacial';
const CHROME_PATH = process.env.CHROME_PATH || '/usr/bin/google-chrome';
const EXECUCOES = Number(process.env.EXECUCOES || 5);
const LARGURA = process.env.LARGURA || '960';
const OTIMIZADAS = (process.env.OTIMIZADAS ||
  'https://fcte-qualidade-de-software-1.github.io/2026-2_T02_DOROTHY_JOHSON/fase-4/melhoria/img').replace(/\/$/, '');
const MODO = /^https?:\/\//.test(OTIMIZADAS) ? 'rede' : 'local';

// Imagem original (caminho no portal) -> arquivo otimizado.
const TROCAS = {
  '/img/capa_inicio.jpg': `capa_inicio-${LARGURA}.webp`,
  '/img/indicadores.png': `indicadores-${LARGURA}.webp`,
};

const LATENCIA_MS = 150;
const DOWNLOAD_BPS = (1638.4 * 1024) / 8; // bytes por segundo
const UPLOAD_BPS = (675 * 1024) / 8;

async function novaPagina(browser) {
  const ctx = await browser.newContext({ viewport: { width: 412, height: 823 }, isMobile: true });
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', {
    offline: false, latency: LATENCIA_MS, downloadThroughput: DOWNLOAD_BPS, uploadThroughput: UPLOAD_BPS,
  });
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  return { ctx, page, cdp };
}

// Troca as imagens no momento da requisição. Devolve um contador de trocas feitas.
async function trocarImagens(page, estado) {
  let fila = Promise.resolve(); // no modo local, as respostas simuladas compartilham o enlace
  for (const [original, otimizada] of Object.entries(TROCAS)) {
    await page.route(u => u.pathname === original, async route => {
      estado.trocas++;
      // Redireciona para a versão otimizada: o navegador a baixa pela rede limitada.
      if (MODO === 'rede') {
        return route.fulfill({ status: 302, headers: { location: `${OTIMIZADAS}/${otimizada}` } });
      }
      const arquivo = path.join(OTIMIZADAS, otimizada);
      const bytes = fs.statSync(arquivo).size;
      const espera = LATENCIA_MS + (bytes / DOWNLOAD_BPS) * 1000;
      fila = fila.then(() => new Promise(r => setTimeout(r, espera)));
      await fila;
      return route.fulfill({ path: arquivo, contentType: 'image/webp' });
    });
  }
}

async function medir(browser, condicao) {
  const { ctx, page, cdp } = await novaPagina(browser);
  const estado = { trocas: 0, bytesRede: 0 };
  cdp.on('Network.loadingFinished', e => { estado.bytesRede += e.encodedDataLength || 0; });
  await page.addInitScript(() => {
    window.__lcp = null;
    new PerformanceObserver(lista => {
      const e = lista.getEntries().pop();
      window.__lcp = { t: e.startTime, url: e.url || '', tag: e.element ? e.element.tagName : '', area: e.size };
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  });
  if (condicao === 'depois') await trocarImagens(page, estado);
  await page.goto(`${BASE}${PAGINA}`, { waitUntil: 'networkidle', timeout: 120000 });
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  const lcp = await page.evaluate(() => window.__lcp);
  // Imagens trocadas que estão na página mas não foram exibidas (falha na troca).
  const quebradas = await page.evaluate(caminhos => [...document.images]
    .filter(i => caminhos.includes(new URL(i.src, location.href).pathname) && i.naturalWidth === 0)
    .map(i => i.src), Object.keys(TROCAS));
  await ctx.close();
  if (!lcp) throw new Error('LCP não registrado');
  if (condicao === 'depois' && quebradas.length) {
    throw new Error(`imagem otimizada não carregou: ${quebradas.join(', ')}`);
  }
  if (condicao === 'depois' && estado.trocas < Object.keys(TROCAS).length) {
    throw new Error(`só ${estado.trocas} de ${Object.keys(TROCAS).length} imagens foram trocadas`);
  }
  return {
    condicao,
    lcp_s: lcp.t / 1000,
    lcp_elemento: lcp.tag,
    lcp_url: lcp.url,
    peso_pagina_kb: estado.bytesRede / 1000,
    imagens_trocadas: estado.trocas,
  };
}

function estat(valores) {
  const v = [...valores].sort((a, b) => a - b);
  const n = v.length;
  const mediana = n % 2 ? v[(n - 1) / 2] : (v[n / 2 - 1] + v[n / 2]) / 2;
  return { mediana, minimo: v[0], maximo: v[n - 1], n };
}

const br = (x, casas = 2) => x.toFixed(casas).replace('.', ',');

(async () => {
  const saida = process.argv[2] || 'data/fase-4/melhoria/medicao.json';
  fs.mkdirSync(path.dirname(saida), { recursive: true });
  const browser = await chromium.launch({
    executablePath: CHROME_PATH, headless: false,
    args: ['--headless=new', ...(process.env.CHROME_ARGS ? process.env.CHROME_ARGS.split(' ') : [])],
  });
  const navegador = browser.version();
  const resultados = [];
  for (let i = 1; i <= EXECUCOES; i++) {
    for (const condicao of ['antes', 'depois']) {
      let r = null;
      for (let tentativa = 1; tentativa <= 3 && !r; tentativa++) {
        try {
          r = await medir(browser, condicao);
        } catch (e) {
          console.error(`falha em ${condicao}, execução ${i}, tentativa ${tentativa}: ${String(e).split('\n')[0]}`);
        }
      }
      if (!r) continue;
      resultados.push({
        ...r, execucao: i, modo_troca: condicao === 'depois' ? MODO : null,
        largura_otimizada: condicao === 'depois' ? Number(LARGURA) : null,
        navegador, coletado_em: new Date().toISOString(),
      });
      console.log(JSON.stringify(resultados[resultados.length - 1]));
    }
  }
  await browser.close();
  fs.writeFileSync(saida, JSON.stringify(resultados, null, 2) + '\n');

  // Consolidação: mediana, mínimo e máximo por condição (resumo.csv) e tabela em Markdown.
  const medidas = [['LCP (s)', 'lcp_s'], ['Peso da página (kB)', 'peso_pagina_kb']];
  const linhas = ['"condicao","medida","mediana","minimo","maximo","execucoes"'];
  const e = {};
  for (const condicao of ['antes', 'depois']) {
    for (const [nome, campo] of medidas) {
      const valores = resultados.filter(r => r.condicao === condicao).map(r => r[campo]);
      if (!valores.length) continue;
      e[`${condicao}:${campo}`] = estat(valores);
      const s = e[`${condicao}:${campo}`];
      linhas.push(`"${condicao}","${nome}",${s.mediana},${s.minimo},${s.maximo},${s.n}`);
    }
  }
  fs.writeFileSync(path.join(path.dirname(saida), 'resumo.csv'), linhas.join('\n') + '\n');

  console.log(`\nModo da troca: ${MODO} | versão otimizada: ${LARGURA} px | navegador: ${navegador}\n`);
  console.log('| Medida | Antes (mín.–máx.) | Depois (mín.–máx.) | Variação |');
  console.log('|---|---|---|---:|');
  for (const [nome, campo] of medidas) {
    const a = e[`antes:${campo}`], d = e[`depois:${campo}`];
    if (!a || !d) continue;
    const casas = campo === 'lcp_s' ? 2 : 0;
    const variacao = (100 * (d.mediana - a.mediana)) / a.mediana;
    console.log(`| ${nome} | ${br(a.mediana, casas)} (${br(a.minimo, casas)}–${br(a.maximo, casas)}) | ` +
      `${br(d.mediana, casas)} (${br(d.minimo, casas)}–${br(d.maximo, casas)}) | ${variacao > 0 ? '+' : ''}${br(variacao, 1)}% |`);
  }
  const elementos = c => [...new Set(resultados.filter(r => r.condicao === c).map(r => r.lcp_url || r.lcp_elemento))];
  console.log(`\nElemento do LCP antes: ${elementos('antes').join(', ')}`);
  console.log(`Elemento do LCP depois: ${elementos('depois').join(', ')}`);
})();
