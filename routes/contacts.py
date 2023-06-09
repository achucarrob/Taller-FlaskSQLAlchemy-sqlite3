# importar Blueprint
from flask import Blueprint, render_template, request, url_for, redirect

# importar la base de datos para traer los datos cuando se complete el form
from models.contact import Contact # Import el modelo de base de datos
from utils.db import db # Import de coneccion a la base de datos

# Crear una ruta con Blueprint
contacts = Blueprint("contacts", __name__)

# En vez de referirnos a app nos referimos a contacts

@contacts.route("/")
def index():
    mi_libreta = Contact.query.all()
    return render_template('index.html', libreta=mi_libreta)

# Trae los datos desde el form que esta en index.html
@contacts.route("/create", methods=['POST'])
def nuevo_contacto():
    fullname = request.form['fullname']
    phone = request.form['phone']

# new_contact devuelve un obj
    new_contact = Contact(fullname, phone)

# para guardar en la base de datos
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))

@contacts.route("/update/<id>", methods=['GET' , 'POST'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.phone = request.form['phone']

        db.session.commit()
        return redirect(url_for('contacts.index'))
        
    return render_template('update.html', update=contact)

@contacts.route("/delete/<id>")
def delete(id):
    del_contact = Contact.query.get(id)
    db.session.delete(del_contact)
    db.session.commit()
    return redirect(url_for('contacts.index'))

# Exportar blueprint al archivo de configuracion app.py