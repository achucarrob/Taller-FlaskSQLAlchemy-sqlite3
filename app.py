# Configuraciones del programa
from flask import Flask
# despues de crear nuestras rutas importamos el blueprint que creamos en routes/contacts.py
from routes.contacts import contacts
# momento de hacer las configs para nuestra base de datos
from flask_sqlalchemy import SQLAlchemy

from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Esta configuracion por defecto es True
db.init_app(app)
# al modulo sqlalchemy le pasamos como argumento app
# SQLAlchemy(app)
# al terminar con estas configs vamos a utils/db.py

# funcion para anhadir desde flask a blueprint
app.register_blueprint(contacts)

