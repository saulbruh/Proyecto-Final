from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    url_for, 
    request, 
    flash
)
from flask_login import login_user, logout_user, login_required
from models import db
from models.cliente import Cliente  # Asegúrate de que este modelo esté bien definido

auth_bp = Blueprint('auth', __name__)

# Ruta para iniciar sesión
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos del formulario
        email = request.form.get('email')
        password = request.form.get('password')

        # Buscar al usuario en la base de datos
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM clientes WHERE email = %s", (email,))
        row = cursor.fetchone()

        if row and row[2] == password:  # Cambia esto para usar hash si es necesario
            user = Cliente(id=row[0], nombre=row[1], email=row[2])  # Actualiza según tu modelo
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas', 'danger')

    return render_template('login.html')

# Ruta para cerrar sesión
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('auth.login'))
