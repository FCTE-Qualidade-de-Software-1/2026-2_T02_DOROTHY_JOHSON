#!/usr/bin/env python3
"""Calcula os indicadores semanais do plano PSM/CID a partir dos snapshots de data/psm/.

Gera os valores usados no registro semanal (docs/gestao/registro-medicoes.md):
  M1  pontos e issues planejados/concluídos por dia e desvio em relação à linha ideal
  M2  horas por membro nas issues concluídas na semana
  M3  horas por ponto das issues concluídas na semana
  M4  lead time das issues e tempo de revisão dos PRs concluídos na semana

Uso: scripts/psm/indicadores.py INICIO FIM PRAZO [MILESTONE ...]
  INICIO, FIM  semana analisada (AAAA-MM-DD, fuso de Brasília)
  PRAZO        data da entrega, usada na linha ideal do burndown
  MILESTONE    milestones da entrega (padrão: "Fase 1" "Fase 2")

Exemplo: scripts/psm/indicadores.py 2026-10-20 2026-10-26 2026-10-26
Requisitos: apenas Python 3 (biblioteca padrão).
"""

import csv
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

DADOS = Path(__file__).resolve().parents[2] / "data" / "psm"
BRASILIA = timezone(timedelta(hours=-3))
LIMITE_M4 = 1.10  # item mais de 10% acima da média é investigado (PSM, 2021b, 8.5)


def instante(texto):
    return datetime.fromisoformat(texto.replace("Z", "+00:00")) if texto else None


def dia_brasilia(texto):
    return instante(texto).astimezone(BRASILIA).date()


def ler(caminho):
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def numero(texto):
    return float(texto) if texto else 0.0


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    inicio, fim, prazo = (date.fromisoformat(a) for a in sys.argv[1:4])
    milestones = set(sys.argv[4:] or ["Fase 1", "Fase 2"])

    snapshots = sorted(
        p for p in DADOS.glob("????-??-??.csv") if inicio <= date.fromisoformat(p.stem) <= fim
    )
    if not snapshots:
        sys.exit(f"Nenhum snapshot entre {inicio} e {fim} em {DADOS}")

    # M1: burndown por snapshot, em pontos e em número de issues.
    print("## M1: progresso da entrega")
    print("snapshot | issues | concluídas | % | com estimate | pontos | pontos concluídos | %")
    primeiro = None
    for caminho in snapshots:
        itens = [
            r for r in ler(caminho) if r["tipo"] == "ISSUE" and r["milestone"] in milestones
        ]
        feitos = [r for r in itens if r["status"] == "Done"]
        estimados = [r for r in itens if r["estimate"]]
        pontos = sum(numero(r["estimate"]) for r in estimados)
        pontos_feitos = sum(numero(r["estimate"]) for r in estimados if r["status"] == "Done")
        print(
            f"{caminho.stem} | {len(itens)} | {len(feitos)} | {100 * len(feitos) / len(itens):.0f}"
            f" | {len(estimados)} | {pontos:g} | {pontos_feitos:g}"
            f" | {100 * pontos_feitos / pontos if pontos else 0:.0f}"
        )
        primeiro = primeiro or (date.fromisoformat(caminho.stem), len(itens), pontos)

    # Desvio no último snapshot: (restante real − restante ideal) / planejado.
    dia0, issues0, pontos0 = primeiro
    dia_final = date.fromisoformat(snapshots[-1].stem)
    fracao_ideal = max(0.0, (prazo - dia_final).days / max(1, (prazo - dia0).days))
    restantes_issues = len(itens) - len(feitos)
    restantes_pontos = pontos - pontos_feitos
    print(f"linha ideal em {dia_final}: {100 * fracao_ideal:.0f}% do planejado ainda aberto")
    print(
        f"desvio em issues: {100 * (restantes_issues / len(itens) - fracao_ideal):.0f} p.p.;"
        f" desvio em pontos: {100 * (restantes_pontos / pontos - fracao_ideal) if pontos else 0:.0f} p.p."
    )
    print(f"cobertura do campo Estimate: {len(estimados)} de {len(itens)} issues")

    ultimo = ler(snapshots[-1])
    issues_semana = [
        r
        for r in ultimo
        if r["tipo"] == "ISSUE" and r["fechado_em"] and inicio <= dia_brasilia(r["fechado_em"]) <= fim
    ]

    # M2 e M3: horas e pontos das issues concluídas na semana.
    print("\n## M2 e M3: esforço e horas por ponto (issues concluídas na semana)")
    horas_membro = defaultdict(float)
    horas_m3 = pontos_m3 = 0.0
    for r in issues_semana:
        if r["horas"]:
            horas_membro[r["responsaveis"] or "(sem responsável)"] += numero(r["horas"])
            if r["estimate"]:
                horas_m3 += numero(r["horas"])
                pontos_m3 += numero(r["estimate"])
    sem_horas = [r["numero"] for r in issues_semana if not r["horas"]]
    for membro, horas in sorted(horas_membro.items()):
        print(f"{membro}: {horas:g} h")
    print(f"total: {sum(horas_membro.values()):g} h")
    print(f"issues concluídas sem Horas: {len(sem_horas)} de {len(issues_semana)} ({', '.join(sem_horas)})")
    if pontos_m3:
        print(f"horas por ponto: {horas_m3:g} h / {pontos_m3:g} pontos = {horas_m3 / pontos_m3:.2f} h/ponto")

    # M4: lead time das issues e tempo de revisão dos PRs.
    print("\n## M4: lead time (dias) das issues concluídas na semana")
    lead = [
        (r["numero"], (instante(r["fechado_em"]) - instante(r["criado_em"])).total_seconds() / 86400)
        for r in issues_semana
    ]
    media = sum(d for _, d in lead) / len(lead)
    print(f"média: {media:.1f} dias; limite de investigação: {media * LIMITE_M4:.1f} dias")
    for num, dias in sorted(lead, key=lambda x: -x[1]):
        print(f"#{num}: {dias:.1f}{'  ACIMA DO LIMITE' if dias > media * LIMITE_M4 else ''}")

    print("\n## M4: tempo de revisão (horas) dos PRs mergeados na semana")
    prs = [
        r
        for r in ler(DADOS / f"prs-{snapshots[-1].stem}.csv")
        if r["mergeado_em"] and inicio <= dia_brasilia(r["mergeado_em"]) <= fim
    ]
    revisao = [
        (r["numero"], (instante(r["mergeado_em"]) - instante(r["criado_em"])).total_seconds() / 3600, r)
        for r in prs
    ]
    media = sum(h for _, h, _ in revisao) / len(revisao)
    print(f"média: {media:.1f} h; limite de investigação: {media * LIMITE_M4:.1f} h")
    for num, horas, r in revisao:
        marca = "  ACIMA DO LIMITE" if horas > media * LIMITE_M4 else ""
        review = "com review" if r["primeira_review_em"] else "sem review"
        print(f"#{num} ({r['autor']}, {review}): {horas:.1f}{marca}")
    sem_review = sum(1 for _, _, r in revisao if not r["primeira_review_em"])
    print(f"PRs mergeados sem review registrada: {sem_review} de {len(revisao)}")


if __name__ == "__main__":
    main()
