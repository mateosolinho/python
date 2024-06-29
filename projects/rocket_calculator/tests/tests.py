import unittest
from projects.rocket_calculator.src.main import calcular_empuje_cohete

class TestFormulas(unittest.TestCase):
    def test_calcular_empuje(self):
        self.assertAlmostEqual(calcular_empuje_cohete(0.5, 100, 9.81), 490.5, places=1)
        self.assertAlmostEqual(calcular_empuje_cohete(512, 366, 9.81), 1838315.52, places=2) # RS-25 nivel del mar
        self.assertAlmostEqual(calcular_empuje_cohete(699.70, 350, 9.81), 2402419.95, places=2) # Raptor nivel del mar