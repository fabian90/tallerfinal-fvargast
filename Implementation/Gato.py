from Implementation.Animal import Animal
class Gato(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)

    def hacer_sonido(self) -> str:
        return "¡Miau!"