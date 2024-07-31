# En el archivo Animal.py
from Interface.IAnimal import IAnimal
from Interface.IAnimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def hacer_sonido(self):
        pass

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_peso(self):
        return self.peso
