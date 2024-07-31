# app.py
from flask import Flask, render_template
from controllers.animal_controller import animal_bp

app = Flask(__name__)

# Registrar el Blueprint del controlador de animales
app.register_blueprint(animal_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)