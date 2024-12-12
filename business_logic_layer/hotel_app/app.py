from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
from routes.auth_routes import auth_bp
from routes.cliente_routes import cliente_bp
from routes.habitacion_routes import habitacion_bp
from routes.reserva_routes import reserva_bp
from flask_mysqldb import MySQL
from models.usuario import Usuario  # Asegúrate de que este modelo exista

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación
app.config.from_object(Config)

# Configurar la base de datos
db = MySQL(app)
db.init_app(app)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp, url_prefix='/clientes')
app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
app.register_blueprint(reserva_bp, url_prefix='/reservas')

# Función para cargar usuarios en Flask-Login
@login_manager.user_loader
def load_user(user_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    if row:
        return Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
    return None

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
