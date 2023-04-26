# Configuraciones del programa
from flask import Flask
# despues de crear nuestras rutas importamos el blueprint que creamos en routes/contacts.py
from routes.contacts import contacts
# momento de hacer las configs para nuestra base de datos
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Esta configuracion por defecto es True

# al modulo sqlalchemy le pasamos como argumento app
SQLAlchemy(app)
# al terminar con estas configs vamos a utils/db.py

# funcion para anhadir desde flask a blueprint
app.register_blueprint(contacts)
# de momento voy a unificar index y app 
# if __name__ == "main":
#     app.run(debug=True)
