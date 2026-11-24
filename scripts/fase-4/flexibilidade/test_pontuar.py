"""Regressões da análise #77: conferência no aparelho e limites da coleta.

Executar: python3 -m unittest discover -s scripts/fase-4/flexibilidade -p 'test_*.py'
"""

import copy
import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pontuar


RAIZ = Path(__file__).resolve().parents[3]
DADOS = RAIZ / "data/fase-4/flexibilidade"


class AnaliseFlexibilidadeTest(unittest.TestCase):
    def setUp(self):
        self.funcoes = pontuar.ler(DADOS / "funcoes.csv")
        self.falhas = pontuar.ler(DADOS / "falhas.csv")

    def test_conferencia_reintegra_sitgeo_e_mantem_perda_confirmada(self):
        original = copy.deepcopy(self.funcoes)
        paginas = pontuar.m222(self.funcoes, self.falhas)
        self.assertEqual((paginas["plataforma-geoespacial"]["a"],
                          paginas["plataforma-geoespacial"]["b"]), (6, 6))
        self.assertEqual((paginas["downloads"]["a"], paginas["downloads"]["b"]), (6, 7))
        self.assertEqual(self.funcoes, original)
        self.assertEqual(pontuar.m222(self.funcoes)["plataforma-geoespacial"]["a"], 4)

    def test_confirmacao_ausente_ou_positiva_nao_reintegra(self):
        for valor in ("", "sim"):
            with self.subTest(confirmacao=valor):
                falhas = copy.deepcopy(self.falhas)
                for f in falhas:
                    if f["id"] in ("F02", "F03"):
                        f["confirmada_no_aparelho"] = valor
                self.assertEqual(pontuar.m222(self.funcoes, falhas)
                                 ["plataforma-geoespacial"]["a"], 4)

    def test_confirmacao_conflitante_nao_reintegra_a_funcao(self):
        outra = next(f.copy() for f in self.falhas if f["id"] == "F02")
        outra["confirmada_no_aparelho"] = "sim"
        paginas = pontuar.m222(self.funcoes, self.falhas + [outra])
        self.assertEqual(paginas["plataforma-geoespacial"]["a"], 5)

    def test_falhas_sem_reproducao_e_emulacao_nao_inflam_contagem(self):
        ambientes = pontuar.m211(pontuar.ler(DADOS / "execucoes.csv"))
        contagem = pontuar.m231(self.falhas + self.falhas, ambientes)
        self.assertEqual(set(contagem), {"AND-CHROME", "AND-SAMSUNG", "IOS-SAFARI", "WIN-EDGE", "WIN-FIREFOX"})
        self.assertEqual([contagem[a]["grave"] for a in contagem], [2, 1, 1, 0, 0])
        self.assertTrue(all(c["cosmetica"] == c["bloqueante"] == 0 for c in contagem.values()))

    def calcular_saida(self, parcial=False):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            for nome in ("rolagem.csv", "funcoes.csv", "execucoes.csv", "falhas.csv"):
                (pasta / nome).write_bytes((DADOS / nome).read_bytes())
            if parcial:
                linhas = pontuar.ler(pasta / "execucoes.csv")
                for linha in linhas:
                    if linha["ambiente"].startswith("WIN-"):
                        linha["resultado"] = ""
                with (pasta / "execucoes.csv").open("w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=list(linhas[0]))
                    writer.writeheader()
                    writer.writerows(linhas)
            subprocess.run([sys.executable, str(Path(pontuar.__file__)), tmp],
                           check=True, capture_output=True, text=True)
            with (pasta / "pontuacao.csv").open(encoding="utf-8", newline="") as f:
                linhas = list(csv.DictReader(f))
        return linhas

    def test_saida_mantem_nc_quando_faltam_ambientes(self):
        linhas = self.calcular_saida(parcial=True)
        por_item = {l["item"]: l for l in linhas}
        self.assertEqual(por_item["Q2.2"]["pontos"], "1.8333")
        for item in ("Q2.1", "Q2.3", "G2"):
            self.assertEqual(por_item[item]["pontos"], "")
        self.assertEqual(por_item["G2"]["nivel"], "pendente")
        self.assertEqual(sum(l["item"] == "M2.1.1" for l in linhas), 3)

    def test_matriz_completa_classifica_g2_com_conferencia_no_aparelho(self):
        linhas = self.calcular_saida()
        por_item = {l["item"]: l for l in linhas}
        self.assertEqual(por_item["Q2.1"]["pontos"], "3.0000")
        self.assertEqual(por_item["Q2.2"]["pontos"], "1.8333")
        self.assertEqual(por_item["Q2.3"]["pontos"], "1.8000")
        self.assertEqual(por_item["G2"]["pontos"], "2.2111")
        self.assertEqual(por_item["G2"]["nivel"], "Bom")


if __name__ == "__main__":
    unittest.main()
