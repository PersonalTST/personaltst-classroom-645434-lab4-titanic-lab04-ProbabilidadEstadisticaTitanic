
import unittest
import pandas as pd
from tarea import *

class TestTarea(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = cargar_datos()

    def test_calcular_probabilidad_total(self):
        prob = calcular_probabilidad_total(self.df, "Sex", "female")
        self.assertAlmostEqual(prob, 0.35241301907968575, places=2)

    def test_calcular_probabilidad_condicional(self):
        prob = calcular_probabilidad_condicional(self.df, "Pclass", 1, "Survived", 1)
        self.assertAlmostEqual(prob, 0.6296296296296297, places=2)

    def test_medidas_tendencia_central(self):
        medidas = calcular_medidas_tendencia_central(self.df, "Age")
        self.assertEqual(medidas["mediana"], 28.0)

    def test_medidas_dispersion(self):
        dispersion = calcular_medidas_dispersion(self.df, "Age")
        self.assertAlmostEqual(dispersion["varianza"], 210.72357975366614, places=1)

    def test_distribucion_por_categoria(self):
        dist = distribucion_por_categoria(self.df, "Pclass")
        self.assertEqual(len(dist), 3)
        self.assertAlmostEqual(dist[dist["Pclass"] == 1]["proporcion"].values[0], 0.242424, places=2)

if __name__ == '__main__':
    unittest.main()
