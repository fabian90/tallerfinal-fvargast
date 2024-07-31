from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def obtener_nombre(self):
        pass

    @abstractmethod
    def obtener_edad(self):
        pass

    @abstractmethod
    def obtener_peso(self):
        pass