# importar Blueprint
from flask import Blueprint, render_template

contacts = Blueprint("contacts", __name__)

# En vez de referirnos a app nos referimos a contacts
@contacts.route("/")
def libreta():
    return render_template('index.html')

@contacts.route("/create")
def nuevo_contacto():
    return "nuevo contacto"

@contacts.route("/update")
def update():
    return "actualiza un contacto"

@contacts.route("/delete")
def delete():
    return "elimina un contacto"

# Exportar blueprint al archivo de configuracion app.py