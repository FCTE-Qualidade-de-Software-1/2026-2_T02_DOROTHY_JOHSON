// Coleta automatizada de M2.2.1 (rolagem horizontal) e M2.2.2 (funções disponíveis no celular)
// do GQM G2, no modo de dispositivo do Chrome (emulação pelo protocolo do DevTools).
// Procedimento: docs/fase-3/metodo-flexibilidade.md (Procedimentos A e B).
//
// Uso: node scripts/fase-4/flexibilidade/telas.js [pasta-de-saida]
// Variáveis opcionais: BASE, CHROME_PATH, EXECUCOES (padrão 2: a segunda confirma a primeira).
// Requer o pacote playwright e o Google Chrome instalado.
//
// Saída (padrão data/fase-4/flexibilidade/):
//   rolagem.csv   uma linha por execução × página × largura
//   funcoes.csv   uma linha por execução × função × largura (1366 e 360 px)
//   capturas/     capturas de tela de cada combinação
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const BASE = process.env.BASE || 'https://territoriosdacidadania.mda.gov.br';
const CHROME_PATH = process.env.CHROME_PATH || '/usr/bin/google-chrome';
const EXECUCOES = Number(process.env.EXECUCOES || 2);

// Larguras da matriz de G2 (docs/fase-3/ambiente.md, seção 3.3). Até 768 px a emulação é de
// aparelho móvel (toque e viewport móvel); acima, de computador.
const LARGURAS = [
  { largura: 360, altura: 800, movel: true },
  { largura: 412, altura: 915, movel: true },
  { largura: 768, altura: 1024, movel: true },
  { largura: 1366, altura: 768, movel: false },
  { largura: 1920, altura: 1080, movel: false },
];
const REFERENCIA = 1366;
const CELULAR = 360;

// Objetos de referência fixados na Fase 3 (docs/fase-3/ambiente.md, seção 2).
const UF = 'GO';
const TERRITORIO = 'Chapada dos Veadeiros - GO';
const CAMADA = 'PRONAF - Valor Total de Crédito Acessado';

// T1 até o resultado da consulta: as funções de Meu Território só aparecem depois dela.
async function prepararMeuTerritorio(page) {
  await page.getByRole('combobox').filter({ hasText: 'Selecione o UF' }).click();
  await page.getByRole('option', { name: UF, exact: true }).click();
  await page.getByRole('combobox').filter({ hasText: 'Selecione o Território' }).click();
  await page.getByRole('option', { name: TERRITORIO, exact: true }).click();
  await page.getByRole('button', { name: 'Selecionar', exact: true }).click();
  await page.getByRole('heading', { name: 'Indicadores Gerais' }).waitFor({ timeout: 120000 });
  await page.waitForTimeout(3000);
}

// T2 até a camada ativa: a legenda da camada só aparece depois dela.
async function prepararSitgeo(page) {
  const card = page.locator('div.relative', { has: page.getByText(CAMADA, { exact: true }) }).first();
  try {
    await card.locator('button').click({ timeout: 10000 });
    return null;
  } catch (e) {
    // Se o clique normal falha (ex.: botão coberto), força o clique para continuar a
    // verificação das demais funções e registra a ocorrência.
    await card.locator('button').click({ force: true, timeout: 10000 });
    return 'ativação da camada só com clique forçado';
  } finally {
    await page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {});
    await page.waitForTimeout(2000);
  }
}

const temas = p => p.locator("xpath=//*[contains(text(),'Qual tema')]/following::button[position()<=5]");
// Botões + e – de um mapa (n-ésimo mapa da página).
const zoom = (p, n) => p.getByRole('button', { name: /^[+–]$/ }).locator(`nth=${2 * n}`).or(p.getByRole('button', { name: /^[+–]$/ }).locator(`nth=${2 * n + 1}`));
const cartaoCamada = (p, nome) => p.locator('div.relative', { has: p.getByText(nome, { exact: true }) }).first().locator('button');

// Lista fixa de funções por página, levantada em 1366 px (método, seção 4.2). "controle" deve
// ser operável (visível, dentro da largura, não coberto e habilitado como em 1366 px);
// "conteudo" deve estar visível, dentro da largura e não coberto.
const PAGINAS = [
  {
    pagina: 'meu-territorio', caminho: '/meu-territorio', preparar: prepararMeuTerritorio,
    funcoes: [
      ['MT-01', 'Seletores de UF e de território', 'controle', p => p.getByRole('combobox')],
      ['MT-02', 'Botão Selecionar (consulta)', 'controle', p => p.getByRole('button', { name: 'Selecionar', exact: true })],
      ['MT-03', 'Indicadores gerais do território', 'conteudo', p => p.getByRole('heading', { name: 'Indicadores Gerais' })],
      ['MT-04', 'Zoom do mapa de abrangência', 'controle', p => zoom(p, 0)],
      ['MT-05', 'Botão Municípios em Dados', 'controle', p => p.getByRole('button', { name: 'Municípios em Dados' })],
      ['MT-06', 'Botão Baixar Mapa', 'controle', p => p.getByRole('button', { name: 'Baixar Mapa' })],
      ['MT-07', 'Abas do Colegiado Territorial', 'controle', p => p.getByRole('tab', { name: /Colegiado/ })],
      ['MT-08', 'Abas de Políticas Públicas (8 programas)', 'controle', p => p.getByRole('tab', { name: /^(Cadastro \(CAF\)|Crédito Rural|Infraestrutura|Crédito Fundiário|GARANTIA SAFRA|Aquisição de Alimentos|Alimentação Escolar|Bolsa Família)/ })],
      ['MT-09', 'Botão Analisar do programa', 'controle', p => p.getByRole('button', { name: /^Analisar/ })],
      ['MT-10', 'Gráficos do programa', 'conteudo', p => p.locator("xpath=//h2[normalize-space(.)='Políticas Públicas']/following::canvas[following::h2[contains(.,'Principais Produtos')]]")],
      ['MT-11', 'Abas de Principais Produtos', 'controle', p => p.getByRole('tab', { name: /^Lavoura/ })],
      ['MT-12', 'Zoom do mapa de produtos', 'controle', p => zoom(p, 1)],
    ],
  },
  {
    pagina: 'plataforma-geoespacial', caminho: '/plataforma-geoespacial', preparar: prepararSitgeo,
    funcoes: [
      ['GEO-01', 'Cartões de tema (5)', 'controle', temas],
      ['GEO-02', 'Grupos de camadas base (5)', 'controle', p => p.getByRole('button', { name: /^(Territórios Rurais|Limites e Camadas Base|Biomas|Hidrografia|Estrutura Viária)$/ })],
      ['GEO-03', 'Ativar e desativar camada do tema', 'controle', p => cartaoCamada(p, CAMADA)],
      ['GEO-04', 'Nome e dados da camada (fonte, unidade)', 'conteudo', p => p.getByText(CAMADA, { exact: true }).first().locator('xpath=..')],
      ['GEO-05', 'Zoom do mapa', 'controle', p => zoom(p, 0)],
      ['GEO-06', 'Legenda da camada ativa', 'conteudo', p => p.locator('img[alt="Legenda"]').first().locator('xpath=..')],
    ],
  },
  {
    pagina: 'downloads', caminho: '/downloads', preparar: null,
    funcoes: [
      ['BIB-01', 'Abas de programa (3)', 'controle', p => p.getByRole('tab', { name: /^(Territórios da Cidadania|PAS Nordeste|PDHC)$/ })],
      ['BIB-02', 'Botões Baixar das listas e shapefiles', 'controle', p => p.getByRole('button', { name: 'Baixar', exact: true })],
      ['BIB-03', 'Links de Legislação', 'controle', p => p.getByRole('link', { name: /^(Resolução Condraf|Portaria MDA)/ })],
      ['BIB-04', 'Links de Documentos de Apoio', 'controle', p => p.getByRole('link', { name: /^(Marco Referencial|Quadro Detalhado|Quadro Síntese)/ })],
      ['BIB-05', 'Setas do carrossel da Mapoteca', 'controle', p => p.getByRole('button', { name: /^(Previous|Next) slide$/ })],
      ['BIB-06', 'Buscador de Mapas (programa, UF, território e botão)', 'controle', p => p.locator("xpath=//*[contains(text(),'Buscador de Mapas')]/following::*[@role='combobox' or self::button][following::*[contains(text(),'(PTDRS)')]]")],
      ['BIB-07', 'Busca do PTDRS (programa, UF e botão)', 'controle', p => p.locator("xpath=//*[contains(text(),'(PTDRS)')]/following::*[(@role='combobox' and following::button[normalize-space(.)='Buscar PTDRS']) or (self::button and normalize-space(.)='Buscar PTDRS')]")],
    ],
  },
];

async function novaPagina(browser, { largura, altura, movel }) {
  const ctx = await browser.newContext({
    viewport: { width: largura, height: altura }, isMobile: movel, hasTouch: movel, deviceScaleFactor: 1,
    locale: 'pt-BR',
  });
  return { ctx, page: await ctx.newPage() };
}

// M2.2.1: rolagem horizontal = scrollWidth > clientWidth. Também identifica os elementos que
// transbordam sem estar recortados por um contêiner; os que ficam dentro do mapa
// (.leaflet-container) são exceção do critério 1.4.10 da WCAG.
async function medirRolagem(page) {
  return page.evaluate(() => {
    const doc = document.documentElement;
    const cw = doc.clientWidth;
    const recortado = e => {
      for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
        const s = getComputedStyle(a);
        if (s.overflowX !== 'visible' || s.position === 'fixed') return true;
      }
      return false;
    };
    const culpados = [];
    for (const e of document.querySelectorAll('body *')) {
      const r = e.getBoundingClientRect();
      if (r.width === 0 || r.right <= cw + 1 || getComputedStyle(e).position === 'fixed' || recortado(e)) continue;
      if ([...e.children].some(c => c.getBoundingClientRect().right > cw + 1)) continue;
      const nome = (e.getAttribute('aria-label') || e.innerText || e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);
      culpados.push({ desc: `${e.tagName.toLowerCase()} "${nome}" (direita em ${Math.round(r.right)} px)`, mapa: !!e.closest('.leaflet-container') });
    }
    return { scroll_width: doc.scrollWidth, client_width: cw, culpados };
  });
}

// M2.2.2: situação de um elemento da função. Rola até ele (inclusive dentro de contêineres
// roláveis, como listas de abas) e verifica visibilidade, posição, cobertura e habilitação.
async function situacaoElemento(el, tipo) {
  // Centraliza o elemento na tela (também dentro de contêineres roláveis), para que o
  // cabeçalho fixo não o cubra no teste de cobertura.
  await el.evaluate(e => e.scrollIntoView({ block: 'center', inline: 'nearest' }), null, { timeout: 5000 }).catch(() => {});
  await el.page().waitForTimeout(300);
  const info = await el.evaluate(e => {
    const s = getComputedStyle(e);
    const r = e.getBoundingClientRect();
    const cw = document.documentElement.clientWidth;
    const visivel = s.display !== 'none' && s.visibility !== 'hidden' && Number(s.opacity) > 0 && r.width > 0 && r.height > 0;
    const dentro = r.left >= -1 && r.right <= cw + 1;
    let livre = false;
    if (visivel) {
      const x = Math.min(Math.max(r.left + r.width / 2, 1), cw - 1);
      const y = Math.min(Math.max(r.top + Math.min(r.height / 2, 20), 1), innerHeight - 1);
      const topo = document.elementFromPoint(x, y);
      livre = !!topo && (topo === e || e.contains(topo) || topo.contains(e));
    }
    return { visivel, dentro, livre, habilitado: !e.disabled && e.getAttribute('aria-disabled') !== 'true', largura: Math.round(r.width) };
  }).catch(() => ({ visivel: false, dentro: false, livre: false, habilitado: false, largura: 0 }));
  if (tipo === 'controle' && info.visivel && info.habilitado) {
    info.clicavel = await el.click({ trial: true, timeout: 3000 }).then(() => true, () => false);
  }
  return info;
}

function motivo(info, ref, tipo) {
  if (!info) return 'ausente';
  if (!info.visivel) return 'invisível';
  if (!info.dentro) return 'fora da largura da tela';
  if (!info.livre) return 'coberto por outro elemento';
  if (tipo === 'controle' && ref && ref.habilitado && !info.habilitado) return 'desabilitado';
  if (tipo === 'controle' && info.habilitado && info.clicavel === false) return 'não recebe o clique';
  return '';
}

async function verificarFuncoes(page, def) {
  const linhas = [];
  for (const [id, nome, tipo, loc] of def.funcoes) {
    const lista = loc(page);
    const n = await lista.count();
    const elementos = [];
    for (let i = 0; i < n; i++) elementos.push(await situacaoElemento(lista.nth(i), tipo));
    linhas.push({ id, nome, tipo, elementos });
  }
  return linhas;
}

const csv = v => {
  const s = v === null || v === undefined ? '' : String(v);
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
};
const linhaCsv = (cols, o) => cols.map(c => csv(o[c])).join(',');

(async () => {
  const saida = process.argv[2] || 'data/fase-4/flexibilidade';
  const capturas = path.join(saida, 'capturas');
  fs.mkdirSync(capturas, { recursive: true });
  const browser = await chromium.launch({ executablePath: CHROME_PATH, headless: false, args: ['--headless=new'] });
  const navegador = `Chrome ${browser.version()}`;
  const rolagem = [];
  const funcoes = [];

  for (let execucao = 1; execucao <= EXECUCOES; execucao++) {
    // Procedimento A: M2.2.1, 3 páginas × 5 larguras, página recém-carregada.
    // PROC=B pula este procedimento (útil para testar só o Procedimento B).
    if (process.env.PROC !== 'B') for (const def of PAGINAS) {
      for (const tela of LARGURAS) {
        const { ctx, page } = await novaPagina(browser, tela);
        try {
          await page.goto(BASE + def.caminho, { waitUntil: 'networkidle', timeout: 90000 });
          await page.waitForTimeout(2000);
          const r = await medirRolagem(page);
          const foraDoMapa = r.culpados.filter(c => !c.mapa);
          const captura = `rolagem-${def.pagina}-${tela.largura}-e${execucao}.jpg`;
          await page.screenshot({ path: path.join(capturas, captura), type: 'jpeg', quality: 60 });
          const linha = {
            execucao, pagina: def.pagina, largura: tela.largura, emulacao: tela.movel ? 'móvel' : 'computador',
            scroll_width: r.scroll_width, client_width: r.client_width,
            rolagem_horizontal: r.scroll_width > r.client_width && foraDoMapa.length > 0 ? 'sim' : 'não',
            excecao_mapa: r.scroll_width > r.client_width && foraDoMapa.length === 0 ? 'sim' : 'não',
            elementos: foraDoMapa.slice(0, 3).map(c => c.desc).join('; '),
            captura, navegador, coletado_em: new Date().toISOString(),
          };
          rolagem.push(linha);
          console.log(`A e${execucao} ${def.pagina} ${tela.largura}px: rolagem=${linha.rolagem_horizontal} ${linha.elementos}`);
        } catch (e) {
          console.error(`falha em A ${def.pagina} ${tela.largura}px, execução ${execucao}: ${String(e).split('\n')[0]}`);
        }
        await ctx.close();
      }
    }

    // Procedimento B: M2.2.2, funções levantadas em 1366 px, verificadas em 360 px.
    for (const def of PAGINAS) {
      const porLargura = {};
      for (const largura of [REFERENCIA, CELULAR]) {
        const tela = LARGURAS.find(t => t.largura === largura);
        const { ctx, page } = await novaPagina(browser, tela);
        let obs = '';
        try {
          await page.goto(BASE + def.caminho, { waitUntil: 'networkidle', timeout: 90000 });
          if (def.preparar) obs = (await def.preparar(page)) || '';
          porLargura[largura] = { linhas: await verificarFuncoes(page, def), obs };
          await page.evaluate(() => window.scrollTo(0, 0));
          await page.screenshot({
            path: path.join(capturas, `funcoes-${def.pagina}-${largura}-e${execucao}.jpg`), type: 'jpeg', quality: 50, fullPage: true,
          });
        } catch (e) {
          console.error(`falha em B ${def.pagina} ${largura}px, execução ${execucao}: ${String(e).split('\n')[0]}`);
        }
        await ctx.close();
      }
      const ref = porLargura[REFERENCIA];
      const cel = porLargura[CELULAR];
      if (!ref || !cel) continue;
      ref.linhas.forEach((f, k) => {
        const g = cel.linhas[k];
        for (const [largura, dados, base] of [[REFERENCIA, f, null], [CELULAR, g, f]]) {
          const problemas = dados.elementos.map((el, i) => motivo(el, base && base.elementos[i], f.tipo)).filter(Boolean);
          const faltando = base && dados.elementos.length < base.elementos.length ? base.elementos.length - dados.elementos.length : 0;
          const ok = dados.elementos.length > 0 && problemas.length === 0 && faltando === 0;
          const obsTela = (largura === REFERENCIA ? ref.obs : cel.obs);
          funcoes.push({
            execucao, pagina: def.pagina, funcao: f.id, nome: f.nome, tipo: f.tipo, largura,
            elementos: dados.elementos.length, com_problema: problemas.length + faltando,
            disponivel: ok ? 'sim' : 'não',
            motivo: [...new Set(problemas.concat(faltando ? [`${faltando} ausente(s)`] : []))].join('; ') || (dados.elementos.length ? '' : 'ausente'),
            observacao: obsTela, navegador, coletado_em: new Date().toISOString(),
          });
          const u = funcoes[funcoes.length - 1];
          console.log(`B e${execucao} ${u.funcao} ${largura}px: ${u.disponivel} ${u.motivo}`);
        }
      });
    }
  }
  await browser.close();

  const colsA = ['execucao', 'pagina', 'largura', 'emulacao', 'scroll_width', 'client_width', 'rolagem_horizontal', 'excecao_mapa', 'elementos', 'captura', 'navegador', 'coletado_em'];
  const colsB = ['execucao', 'pagina', 'funcao', 'nome', 'tipo', 'largura', 'elementos', 'com_problema', 'disponivel', 'motivo', 'observacao', 'navegador', 'coletado_em'];
  fs.writeFileSync(path.join(saida, 'rolagem.csv'), [colsA.join(','), ...rolagem.map(o => linhaCsv(colsA, o))].join('\n') + '\n');
  fs.writeFileSync(path.join(saida, 'funcoes.csv'), [colsB.join(','), ...funcoes.map(o => linhaCsv(colsB, o))].join('\n') + '\n');
})();
