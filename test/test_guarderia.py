
from Implementation.Guarderia import Guarderia
import unittest
class test_guarderia(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de prueba con una instancia de Guarderia"""
        self.guarderia = Guarderia()

    def test_alimentar_boa_exito(self):
        """Prueba alimentar una boa correctamente"""
        resultado = self.guarderia.alimentar_boa(self.guarderia.boas[0])
        self.assertEqual(resultado, "Éxito")

    def test_alimentar_boa_llena(self):
        """Prueba alimentar una boa que ya está llena"""
        boa = self.guarderia.boas[0]
        # Alimentamos la boa hasta llenarla
        while True:
            try:
                boa.agregar_raton()
            except ValueError:
                break
        resultado = self.guarderia.alimentar_boa(boa)
        self.assertEqual(resultado, "La boa está llena")

    def test_alimentar_boa_inexistente(self):
        """Prueba alimentar una boa inexistente"""
        resultado = self.guarderia.alimentar_boa(None)
        self.assertEqual(resultado, "Esta Boa no existe!")

if __name__ == '__main__':
    unittest.main()