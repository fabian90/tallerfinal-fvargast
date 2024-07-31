# controllers/animal_controller.py
from flask import Blueprint, jsonify
from Implementation.Gato import Gato
from Implementation.Perro import Perro
from Implementation.Huron import Huron
from Implementation.Boa_Constrictor import Boa_Constrictor

animal_bp = Blueprint('animal', __name__)

# Crear instancias de los animales
gato = Gato("Gato", 3, 5)
perro = Perro("Perro", 4, 20)
huron = Huron("Hurón", 2, 2, "USA", 50)
boa_constrictor = Boa_Constrictor("Boa Constrictor", 5, 50, "Brasil", 200)

@animal_bp.route('/animal/<string:animal_name>', methods=['GET'])
def get_animal_sound(animal_name):
    if animal_name.lower() == "gato":
        return jsonify({"animal": "Gato", "sonido": gato.hacer_sonido()})
    elif animal_name.lower() == "perro":
        return jsonify({"animal": "Perro", "sonido": perro.hacer_sonido()})
    elif animal_name.lower() == "huron":
        return jsonify({"animal": "Hurón", "sonido": huron.hacer_sonido()})
    elif animal_name.lower() == "boa":
        return jsonify({"animal": "Boa Constrictor", "sonido": boa_constrictor.hacer_sonido()})
    else:
        return jsonify({"error": "Animal no encontrado"}), 404