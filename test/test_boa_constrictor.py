from Implementation.Boa_Constrictor import Boa_Constrictor
import unittest
class test_boa_constrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Boa1", 5, 50, "Brasil", 200)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")
    
    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 10000.0)
    
    def test_agregar_raton(self):
        for _ in range(10):
            self.boa.ratones_comidos =21
            if self.boa.ratones_comidos > 20:
                self.boa.agregar_raton()
        with self.assertRaises(ValueError):
            self.boa.agregar_raton()

if __name__ == '__main__':
    unittest.main()