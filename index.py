# Archivo que corre el programa
from app import app # import app o no funciona el app.run
# importar db
from utils.db import db

# Crea las tablas
with app.app_context():
    db.create_all()

# inicializa la app
if __name__ == "main":
    app.run(debug=True)