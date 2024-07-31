from Implementation.Animal_Exotico import Animal_Exotico
from Implementation.Boa_Constrictor import Boa_Constrictor
from Implementation.Huron import Huron

def prueba() -> None:
    # Probando la clase Animal_Exotico
    animal_exotico = Animal_Exotico("Tigre", 5, 300.0, "India", 0.15)
    print(f"Nombre: {animal_exotico.obtener_nombre()}, Edad: {animal_exotico.obtener_edad()}, Peso: {animal_exotico.obtener_peso()}, País de Origen: {animal_exotico.pais_origen}, Impuestos: {animal_exotico.impuestos}")
    print(animal_exotico.calcular_flete())  # Debe devolver 45.0

    # Probando la clase Boa_Constrictor
    boa = Boa_Constrictor("Boa", 2, 30.0, "Brasil", 0.10)
    print(f"Nombre: {boa.obtener_nombre()}, Edad: {boa.obtener_edad()}, Peso: {boa.obtener_peso()}, País de Origen: {boa.pais_origen}, Impuestos: {boa.impuestos}")
    print(boa.hacer_sonido())  # Debe devolver "¡Tsss!"
    boa.agregar_raton() # raton No 1
    boa.agregar_raton()# raton No 2
    print(f"Ratones Comidos: {boa.ratones_comidos}")  # Debe devolver 1

    # Probando la clase Huron
    huron = Huron("Hurón", 3, 5.0, "Estados Unidos", 0.08)
    print(f"Nombre: {huron.obtener_nombre()}, Edad: {huron.obtener_edad()}, Peso: {huron.obtener_peso()}, País de Origen: {huron.pais_origen}, Impuestos: {huron.impuestos}")
    print(huron.hacer_sonido())  # Debe devolver "¡Eek Eek!"

if __name__ == "__main__":
    prueba()