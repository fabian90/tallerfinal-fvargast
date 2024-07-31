from .Boa_Constrictor import Boa_Constrictor
from .Huron import Huron
class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1", 5, 50, "Brasil", 200), Boa_Constrictor("Boa2", 4, 45, "Argentina", 180)]
        self.hurones = [Huron("Huron1", 2, 2, "USA", 50), Huron("Huron2", 3, 3, "Canada", 55)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.agregar_raton()
            return "Éxito"
        except ValueError:
            return "La boa está llena"