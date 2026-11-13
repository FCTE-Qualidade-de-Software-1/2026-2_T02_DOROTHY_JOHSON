#!/usr/bin/env python3
"""Calcula os indicadores do plano PSM/CID a partir dos snapshots de data/psm/.

Gera os valores usados no registro semanal (docs/gestao/registro-medicoes.md) e no
Painel PSM do site:
  M1  issues e pontos planejados/concluídos ao fim de cada dia e desvio em relação à linha ideal
  M2  horas por membro nas issues concluídas na semana
  M3  horas por ponto das issues concluídas na semana
  M4  lead time das issues e tempo de revisão dos PRs concluídos na semana

Uso:
  scripts/psm/indicadores.py INICIO FIM PRAZO [MILESTONE ...]
      imprime M1 a M4 da semana INICIO..FIM (AAAA-MM-DD, fuso de Brasília)
  scripts/psm/indicadores.py --json SAIDA INICIO FIM PRAZO [MILESTONE ...]
      grava em SAIDA os dados do painel, com M1 diário e M2 a M4 por semana de INICIO a FIM

  PRAZO      data da entrega, usada na linha ideal do burndown
  MILESTONE  milestones da entrega (padrão: "Fase 1" "Fase 2")

Exemplo: scripts/psm/indicadores.py 2026-10-20 2026-10-26 2026-10-26

Regras de cálculo:
  - A coleta roda de madrugada, então o estado ao fim do dia D vem do primeiro snapshot
    coletado depois das 23:59 de D; uma issue conta como concluída em D se fechou até esse
    instante. O dia corrente fica fora do M1.
  - A coleta descarta o snapshot igual ao anterior. Se não há snapshot nas 36 h seguintes ao
    fim de D, nada mudou desde o último snapshot anterior, que passa a representar D.
  - M2 e M3 usam Estimate e Horas do snapshot mais recente, porque o plano permite o
    preenchimento retroativo desses campos (regra 4 da Seção 5).
  - Em M2, as horas de uma issue com mais de um responsável são divididas igualmente.
  - Issues fechadas como não planejadas ou duplicadas ficam fora de todos os indicadores, em
    todos os dias. A lista vem de data/psm/issues-excluidas.csv, somada às issues que algum
    snapshot registra com motivo_fechamento NOT_PLANNED ou DUPLICATE; os snapshots anteriores a
    essa coluna não dizem o motivo, e uma issue retirada do Project some dos snapshots seguintes.
  - Em M4, o padrão de revisão da equipe é o merge feito por outro membro; a review formal
    do GitHub é contada à parte.

Requisitos: apenas Python 3 (biblioteca padrão).
"""

import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

DADOS = Path(__file__).resolve().parents[2] / "data" / "psm"
EXCLUIDAS = DADOS / "issues-excluidas.csv"
BRASILIA = timezone(timedelta(hours=-3))
LIMITE_M4 = 1.10  # item mais de 10% acima da média é investigado (PSM, 2021b, 8.5)
MILESTONES_PADRAO = ["Fase 1", "Fase 2"]
MOTIVOS_EXCLUIDOS = {"NOT_PLANNED", "DUPLICATE"}
JANELA_COLETA = timedelta(hours=36)  # atraso máximo aceito entre o fim do dia e a coleta


def instante(texto):
    return datetime.fromisoformat(texto.replace("Z", "+00:00")) if texto else None


def dia_brasilia(texto):
    return instante(texto).astimezone(BRASILIA).date()


def fim_do_dia(dia):
    return datetime.combine(dia + timedelta(days=1), time(0), BRASILIA)


def ler(caminho):
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def numero(texto):
    return float(texto) if texto else 0.0


def carregar_snapshots():
    """Lista (coletado_em, caminho) dos snapshots de itens, em ordem de coleta."""
    snapshots = []
    for caminho in DADOS.glob("????-??-??.csv"):
        linhas = ler(caminho)
        if linhas:
            snapshots.append((instante(linhas[0]["coletado_em"]), caminho))
    return sorted(snapshots)


def snapshot_do_dia(dia, snapshots):
    """Snapshot que representa o estado ao fim do dia."""
    fim = fim_do_dia(dia)
    depois = next(((c, p) for c, p in snapshots if c >= fim), None)
    if depois and depois[0] <= fim + JANELA_COLETA:
        return depois[1]
    antes = [p for c, p in snapshots if c < fim]
    return antes[-1] if antes else None


def nao_planejadas(snapshots):
    """Números das issues fora dos indicadores: lista fixa e motivos excluídos nos snapshots."""
    fixas = {r["numero"] for r in ler(EXCLUIDAS)} if EXCLUIDAS.exists() else set()
    return fixas | {
        r["numero"]
        for _, caminho in snapshots
        for r in ler(caminho)
        if r.get("motivo_fechamento") in MOTIVOS_EXCLUIDOS
    }


def issues_da_entrega(linhas, milestones, excluidas):
    return [
        r
        for r in linhas
        if r["tipo"] == "ISSUE" and r["milestone"] in milestones and r["numero"] not in excluidas
    ]


def progresso(dia, snapshots, milestones, excluidas):
    """M1 ao fim do dia: (issues, concluídas, com Estimate, pontos, pontos concluídos)."""
    fim = fim_do_dia(dia)
    caminho = snapshot_do_dia(dia, snapshots)
    if caminho is None or dia >= datetime.now(BRASILIA).date():
        return None
    itens = [
        r for r in issues_da_entrega(ler(caminho), milestones, excluidas) if instante(r["criado_em"]) < fim
    ]
    if not itens:
        return None
    feitos = [r for r in itens if r["fechado_em"] and instante(r["fechado_em"]) < fim]
    estimados = [r for r in itens if r["estimate"]]
    return {
        "dia": dia.isoformat(),
        "snapshot": caminho.name,
        "issues": len(itens),
        "concluidas": len(feitos),
        "com_estimate": len(estimados),
        "pontos": sum(numero(r["estimate"]) for r in estimados),
        "pontos_concluidos": sum(numero(r["estimate"]) for r in feitos if r["estimate"]),
    }


def fracao_ideal(dia, inicio, prazo):
    return max(0.0, (prazo - dia).days / max(1, (prazo - inicio).days))


def media_e_limite(valores):
    if not valores:
        return None, None
    media = sum(valores) / len(valores)
    return media, media * LIMITE_M4


def semana(inicio, fim, snapshots, excluidas):
    """M2 a M4 das issues fechadas e dos PRs mergeados entre inicio e fim."""
    ultimo = ler(snapshots[-1][1])
    issues = [
        r
        for r in ultimo
        if r["tipo"] == "ISSUE"
        and r["numero"] not in excluidas
        and r["fechado_em"]
        and inicio <= dia_brasilia(r["fechado_em"]) <= fim
    ]

    horas_membro = defaultdict(float)
    horas_m3 = pontos_m3 = 0.0
    for r in issues:
        if not r["horas"]:
            continue
        responsaveis = r["responsaveis"].split(";") if r["responsaveis"] else ["(sem responsável)"]
        for membro in responsaveis:
            horas_membro[membro] += numero(r["horas"]) / len(responsaveis)
        if r["estimate"]:
            horas_m3 += numero(r["horas"])
            pontos_m3 += numero(r["estimate"])

    lead = [
        {
            "numero": int(r["numero"]),
            "titulo": r["titulo"],
            "dias": (instante(r["fechado_em"]) - instante(r["criado_em"])).total_seconds() / 86400,
        }
        for r in issues
    ]
    media_lead, limite_lead = media_e_limite([i["dias"] for i in lead])
    for i in lead:
        i["acima"] = i["dias"] > limite_lead

    arquivos_prs = sorted(DADOS.glob("prs-????-??-??.csv"))
    prs = [
        r
        for r in (ler(arquivos_prs[-1]) if arquivos_prs else [])
        if r["mergeado_em"] and inicio <= dia_brasilia(r["mergeado_em"]) <= fim
    ]
    revisao = [
        {
            "numero": int(r["numero"]),
            "titulo": r["titulo"],
            "autor": r["autor"],
            "horas": (instante(r["mergeado_em"]) - instante(r["criado_em"])).total_seconds() / 3600,
            "com_review": bool(r["primeira_review_em"]),
            "mergeado_por": r.get("mergeado_por") or None,
            "por_outra_pessoa": bool(r.get("mergeado_por")) and r.get("mergeado_por") != r["autor"],
        }
        for r in prs
    ]
    media_rev, limite_rev = media_e_limite([p["horas"] for p in revisao])
    for p in revisao:
        p["acima"] = p["horas"] > limite_rev

    return {
        "inicio": inicio.isoformat(),
        "fim": fim.isoformat(),
        "issues_concluidas": len(issues),
        "m2": dict(sorted(horas_membro.items())),
        "issues_sem_horas": [int(r["numero"]) for r in issues if not r["horas"]],
        "m3": {
            "horas": horas_m3,
            "pontos": pontos_m3,
            "horas_por_ponto": horas_m3 / pontos_m3 if pontos_m3 else None,
        },
        "m4_issues": {"media": media_lead, "limite": limite_lead, "itens": lead},
        "m4_prs": {
            "media": media_rev,
            "limite": limite_rev,
            "itens": revisao,
            "sem_review": sum(1 for p in revisao if not p["com_review"]),
            "por_outra_pessoa": sum(1 for p in revisao if p["por_outra_pessoa"]),
        },
    }


def imprimir(inicio, fim, prazo, milestones, snapshots):
    excluidas = nao_planejadas(snapshots)
    dias = [inicio + timedelta(days=n) for n in range((fim - inicio).days + 1)]
    m1 = [p for p in (progresso(d, snapshots, milestones, excluidas) for d in dias) if p]
    if not m1:
        sys.exit(f"Nenhum snapshot coletado depois do fim de {inicio} em {DADOS}")

    print("## M1: progresso da entrega (fim de cada dia)")
    print("dia | snapshot | issues | concluídas | % | com estimate | pontos | pontos concluídos | %")
    for p in m1:
        print(
            f"{p['dia']} | {p['snapshot']} | {p['issues']} | {p['concluidas']}"
            f" | {100 * p['concluidas'] / p['issues']:.0f} | {p['com_estimate']} | {p['pontos']:g}"
            f" | {p['pontos_concluidos']:g}"
            f" | {100 * p['pontos_concluidos'] / p['pontos'] if p['pontos'] else 0:.0f}"
        )
    p = m1[-1]
    ideal = fracao_ideal(date.fromisoformat(p["dia"]), inicio, prazo)
    restante_issues = (p["issues"] - p["concluidas"]) / p["issues"]
    restante_pontos = (p["pontos"] - p["pontos_concluidos"]) / p["pontos"] if p["pontos"] else 0
    print(f"linha ideal em {p['dia']}: {100 * ideal:.0f}% do planejado ainda aberto")
    print(
        f"desvio em issues: {100 * (restante_issues - ideal):.0f} p.p.;"
        f" desvio em pontos: {100 * (restante_pontos - ideal) if p['pontos'] else 0:.0f} p.p."
    )
    print(f"cobertura do campo Estimate: {p['com_estimate']} de {p['issues']} issues")

    s = semana(inicio, fim, snapshots, excluidas)
    print("\n## M2 e M3: esforço e horas por ponto (issues concluídas na semana)")
    for membro, horas in s["m2"].items():
        print(f"{membro}: {horas:g} h")
    print(f"total: {sum(s['m2'].values()):g} h")
    sem_horas = ", ".join(map(str, s["issues_sem_horas"]))
    print(f"issues concluídas sem Horas: {len(s['issues_sem_horas'])} de {s['issues_concluidas']} ({sem_horas})")
    m3 = s["m3"]
    if m3["horas_por_ponto"] is not None:
        print(f"horas por ponto: {m3['horas']:g} h / {m3['pontos']:g} pontos = {m3['horas_por_ponto']:.2f} h/ponto")

    print("\n## M4: lead time (dias) das issues concluídas na semana")
    m4 = s["m4_issues"]
    if not m4["itens"]:
        print("nenhuma issue concluída na semana")
    else:
        print(f"média: {m4['media']:.1f} dias; limite de investigação: {m4['limite']:.1f} dias")
        for i in sorted(m4["itens"], key=lambda x: -x["dias"]):
            print(f"#{i['numero']}: {i['dias']:.1f}{'  ACIMA DO LIMITE' if i['acima'] else ''}")

    print("\n## M4: tempo de revisão (horas) dos PRs mergeados na semana")
    m4 = s["m4_prs"]
    if not m4["itens"]:
        print("nenhum PR mergeado na semana")
    else:
        print(f"média: {m4['media']:.1f} h; limite de investigação: {m4['limite']:.1f} h")
        for pr in m4["itens"]:
            merge = f"merge de {pr['mergeado_por']}" if pr["mergeado_por"] else "merge sem registro"
            review = ", com review" if pr["com_review"] else ""
            marca = "  ACIMA DO LIMITE" if pr["acima"] else ""
            print(f"#{pr['numero']} ({pr['autor']}, {merge}{review}): {pr['horas']:.1f}{marca}")
        total = len(m4["itens"])
        print(f"PRs mergeados por outra pessoa: {m4['por_outra_pessoa']} de {total}")
        print(f"PRs com review formal do GitHub: {total - m4['sem_review']} de {total}")


def painel(inicio, fim, prazo, milestones, snapshots):
    excluidas = nao_planejadas(snapshots)
    dias = [inicio + timedelta(days=n) for n in range((fim - inicio).days + 1)]
    m1 = [p for p in (progresso(d, snapshots, milestones, excluidas) for d in dias) if p]
    for p in m1:
        dia = date.fromisoformat(p["dia"])
        p["ideal_pct"] = 100 * fracao_ideal(dia, inicio, prazo)
        p["restante_issues_pct"] = 100 * (p["issues"] - p["concluidas"]) / p["issues"]
        p["restante_pontos_pct"] = (
            100 * (p["pontos"] - p["pontos_concluidos"]) / p["pontos"] if p["pontos"] else None
        )

    ultimo = issues_da_entrega(ler(snapshots[-1][1]), milestones, excluidas)
    semanas = []
    comeco = inicio
    while comeco <= fim:
        semanas.append(semana(comeco, min(comeco + timedelta(days=6), fim), snapshots, excluidas))
        comeco += timedelta(days=7)

    return {
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "inicio": inicio.isoformat(),
        "prazo": prazo.isoformat(),
        "milestones": sorted(milestones),
        "nao_planejadas": sorted(int(n) for n in excluidas),
        "ultimo_snapshot": {
            "arquivo": snapshots[-1][1].name,
            "coletado_em": snapshots[-1][0].isoformat(),
        },
        "cobertura": {
            "issues": len(ultimo),
            "com_estimate": sum(1 for r in ultimo if r["estimate"]),
            "com_horas": sum(1 for r in ultimo if r["horas"]),
        },
        "m1": m1,
        "semanas": semanas,
    }


def main(argumentos):
    saida = None
    if argumentos[:1] == ["--json"]:
        if len(argumentos) < 2:
            sys.exit(__doc__)
        saida, argumentos = Path(argumentos[1]), argumentos[2:]
    if len(argumentos) < 3:
        sys.exit(__doc__)
    inicio, fim, prazo = (date.fromisoformat(a) for a in argumentos[:3])
    milestones = set(argumentos[3:] or MILESTONES_PADRAO)

    snapshots = carregar_snapshots()
    if not snapshots:
        sys.exit(f"Nenhum snapshot em {DADOS}")

    if saida is None:
        imprimir(inicio, fim, prazo, milestones, snapshots)
        return
    saida.parent.mkdir(parents=True, exist_ok=True)
    dados = painel(inicio, fim, prazo, milestones, snapshots)
    saida.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
