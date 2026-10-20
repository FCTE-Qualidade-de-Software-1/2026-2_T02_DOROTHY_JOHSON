# Piloto do GQM G3 (eficiência de desempenho)

Medição piloto de 20/10/2026, usada para formular as hipóteses H3.1 a H3.4
(`docs/fase-2/hipoteses.md`). Não substitui a coleta da Fase 4.

| Arquivo | Conteúdo | Gerado por |
|---|---|---|
| `lighthouse/<pagina>-<n>.json` | Relatório completo do Lighthouse 12.8.2, perfil móvel padrão, 5 execuções por página | `scripts/fase-2/piloto-lighthouse.sh` |
| `tarefas.json` | Tempo das tarefas T1 e T2 e JS heap após o carregamento e após a tarefa, 5 execuções cada | `scripts/fase-2/piloto-tarefas.js` |
| `resumo.csv` | Mediana de cada métrica | `scripts/fase-2/resumo-piloto.sh` |

Páginas: `meu-territorio` (Meu Território), `plataforma-geoespacial` (SITGeo) e
`downloads` (Biblioteca Territorial).

## Como reproduzir

Requisitos: Node.js, Google Chrome, `jq` e o pacote `playwright` (só para as tarefas).

```bash
./scripts/fase-2/piloto-lighthouse.sh
node scripts/fase-2/piloto-tarefas.js data/fase-2/piloto/tarefas.json
./scripts/fase-2/resumo-piloto.sh
```

As execuções devem ser sequenciais, sem outros programas pesados abertos na máquina.
