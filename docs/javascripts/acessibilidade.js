// Ajustes de acessibilidade que o tema não faz sozinho (issue #95, critério AG-C4).
// Roda a cada página, inclusive na navegação instantânea do Material (document$).
(function () {
  "use strict";

  // A janela de busca do tema é um role="dialog" sem nome acessível.
  function nomearBusca() {
    var busca = document.querySelector(".md-search[role='dialog']");
    if (busca && !busca.hasAttribute("aria-label")) {
      busca.setAttribute("aria-label", "Busca no site");
    }
  }

  // Blocos de código e tabelas largas rolam na horizontal; sem foco, quem usa só o teclado
  // não consegue rolar até o fim (WCAG 2.1.1).
  function tornarRolagemAcessivel() {
    var alvos = document.querySelectorAll(".md-typeset pre > code, .md-typeset__scrollwrap");
    var codigos = 0;
    var tabelas = 0;
    alvos.forEach(function (el) {
      if (el.scrollWidth <= el.clientWidth || el.hasAttribute("tabindex")) {
        return;
      }
      // Cada região precisa de um nome único para ser distinguida pelo leitor de tela.
      var nome = el.matches("code")
        ? "Bloco de código " + ++codigos + ", com rolagem horizontal"
        : "Tabela " + ++tabelas + ", com rolagem horizontal";
      el.setAttribute("tabindex", "0");
      el.setAttribute("role", "region");
      el.setAttribute("aria-label", nome);
    });
  }

  function iniciar() {
    nomearBusca();
    tornarRolagemAcessivel();
  }

  if (window.document$) {
    window.document$.subscribe(iniciar);
  } else {
    document.addEventListener("DOMContentLoaded", iniciar);
  }
})();
