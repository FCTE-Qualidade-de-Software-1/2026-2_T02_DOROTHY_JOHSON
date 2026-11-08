// Coleta de M3.2.1 (tempo das tarefas T1 e T2) e M3.4.1 (JS heap) do GQM G3.
// Limitação equivalente ao perfil móvel do Lighthouse: RTT 150 ms, 1638,4 kbps, CPU 4x.
// Procedimento: docs/fase-3/metodo-eficiencia.md (seção "Procedimento B").
//
// Uso: node scripts/fase-4/eficiencia/tarefas.js [saida.json]
// Requer o pacote playwright e o Google Chrome instalado (CHROME_PATH).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const BASE = process.env.BASE || 'https://territoriosdacidadania.mda.gov.br';
const CHROME_PATH = process.env.CHROME_PATH || '/usr/bin/google-chrome';
const EXECUCOES = Number(process.env.EXECUCOES || 5);

// Objetos de referência fixados na Fase 3 (docs/fase-3/ambiente.md).
const UF = 'GO';
const TERRITORIO = 'Chapada dos Veadeiros - GO';
const CAMADA = 'PRONAF - Valor Total de Crédito Acessado';

async function novaPagina(browser) {
  const ctx = await browser.newContext({ viewport: { width: 412, height: 823 }, isMobile: true });
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', {
    offline: false, latency: 150, downloadThroughput: (1638.4 * 1024) / 8, uploadThroughput: (675 * 1024) / 8,
  });
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  await cdp.send('Performance.enable');
  await cdp.send('HeapProfiler.enable');
  return { ctx, page, cdp };
}

// JS heap usado, em MB, após forçar a coleta de lixo.
async function heapMB(cdp) {
  await cdp.send('HeapProfiler.collectGarbage');
  const { metrics } = await cdp.send('Performance.getMetrics');
  return metrics.find(m => m.name === 'JSHeapUsedSize').value / 1048576;
}

// Fim da tarefa: a última requisição disparada após o clique termina e a rede fica ociosa
// por 1 s; o tempo vai do clique até o fim dessa última requisição.
async function cronometrar(page, acao) {
  let pendentes = 0, ultimo = 0, houve = false;
  const ini = () => { pendentes++; houve = true; };
  const fim = () => { pendentes = Math.max(0, pendentes - 1); ultimo = Date.now(); };
  page.on('request', ini); page.on('requestfinished', fim); page.on('requestfailed', fim);
  const t0 = Date.now();
  await acao();
  const limite = t0 + 60000;
  let ociosoDesde = Date.now();
  while (Date.now() < limite) {
    await page.waitForTimeout(100);
    if (pendentes > 0) { ociosoDesde = Date.now(); continue; }
    if (Date.now() - ociosoDesde >= 1000) break;
  }
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  const tFim = houve ? ultimo : Date.now();
  page.off('request', ini); page.off('requestfinished', fim); page.off('requestfailed', fim);
  return { tempo_s: (tFim - t0) / 1000, houve_requisicoes: houve };
}

async function t1(browser) {
  const { ctx, page, cdp } = await novaPagina(browser);
  await page.goto(`${BASE}/meu-territorio`, { waitUntil: 'networkidle', timeout: 90000 });
  const heap_carga_mb = await heapMB(cdp);
  await page.getByRole('combobox').filter({ hasText: 'Selecione o UF' }).click();
  await page.getByRole('option', { name: UF, exact: true }).click();
  await page.getByRole('combobox').filter({ hasText: 'Selecione o Território' }).click();
  await page.getByRole('option', { name: TERRITORIO, exact: true }).click();
  const r = await cronometrar(page, () => page.getByRole('button', { name: 'Selecionar', exact: true }).click());
  const heap_tarefa_mb = await heapMB(cdp);
  await ctx.close();
  return { tarefa: 'T1', objeto: 'meu-territorio', referencia: TERRITORIO, ...r, heap_carga_mb, heap_tarefa_mb };
}

async function t2(browser) {
  const { ctx, page, cdp } = await novaPagina(browser);
  await page.goto(`${BASE}/plataforma-geoespacial`, { waitUntil: 'networkidle', timeout: 90000 });
  const heap_carga_mb = await heapMB(cdp);
  const card = page.locator('div.relative', { has: page.getByText(CAMADA, { exact: true }) }).first();
  const r = await cronometrar(page, () => card.locator('button').click());
  const heap_tarefa_mb = await heapMB(cdp);
  await ctx.close();
  return { tarefa: 'T2', objeto: 'plataforma-geoespacial', referencia: CAMADA, ...r, heap_carga_mb, heap_tarefa_mb };
}

// A Biblioteca Territorial não tem tarefa no G3; mede-se só o JS heap após o carregamento.
async function carregamentoBiblioteca(browser) {
  const { ctx, page, cdp } = await novaPagina(browser);
  await page.goto(`${BASE}/downloads`, { waitUntil: 'networkidle', timeout: 90000 });
  const heap_carga_mb = await heapMB(cdp);
  await ctx.close();
  return { tarefa: null, objeto: 'downloads', heap_carga_mb };
}

(async () => {
  const saida = process.argv[2] || 'data/fase-4/eficiencia/tarefas.json';
  fs.mkdirSync(path.dirname(saida), { recursive: true });
  // O Chrome removeu o headless antigo; o novo é pedido por argumento, independente da versão
  // do Playwright.
  const browser = await chromium.launch({ executablePath: CHROME_PATH, headless: false, args: ['--headless=new'] });
  const navegador = browser.version();
  const resultados = [];
  for (const fn of [t1, t2, carregamentoBiblioteca]) {
    for (let i = 1, tentativas = 0; i <= EXECUCOES && tentativas < EXECUCOES * 2; tentativas++) {
      try {
        const r = await fn(browser);
        resultados.push({ ...r, execucao: i, navegador, coletado_em: new Date().toISOString() });
        console.log(JSON.stringify(resultados[resultados.length - 1]));
        i++;
      } catch (e) {
        console.error(`falha em ${fn.name}, execução ${i}: ${String(e).split('\n')[0]}`);
      }
    }
  }
  await browser.close();
  fs.writeFileSync(saida, JSON.stringify(resultados, null, 2) + '\n');
})();
