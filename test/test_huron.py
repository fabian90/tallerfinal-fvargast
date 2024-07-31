from Implementation.Huron import Huron
import unittest
import os
class test_huron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Huron1", 2, 2, "USA", 50)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")
    
    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 100.0)
if __name__ == '__main__':
    unittest.main()