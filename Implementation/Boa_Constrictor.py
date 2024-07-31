
from Implementation.Animal_Exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def agregar_raton(self) -> None:
        if self.ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1