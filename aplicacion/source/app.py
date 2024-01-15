from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'aplicacion.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    documentacion = db.Column(db.String(20), nullable=False, unique=True)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefono = db.Column(db.String(15), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        documentacion = request.form['Documentacion']
        edad = request.form['Edad']
        genero = request.form['Genero']
        email = request.form['Correo']
        telefono = request.form['Telefono']

        # Crear un nuevo usuario y agregarlo a la base de datos
        nuevo_usuario = Usuario(nombre=nombre, apellidos=apellidos, documentacion=documentacion, edad=edad, genero=genero, email=email, telefono=telefono)
        db.session.add(nuevo_usuario)
        db.session.commit()

    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
