from flask import Blueprint, jsonify, request
from pymysql.err import IntegrityError
from models import db

cliente_bp = Blueprint('clientes', __name__)

# Endpoint para crear un cliente
@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    try:
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()
        nombre = data['nombre']
        direccion = data.get('direccion', '')
        telefono = data.get('telefono', '')
        email = data['email']

        # Crear cursor para interactuar con la base de datos
        cursor = db.connection.cursor()

        # Insertar datos en la tabla `clientes`
        cursor.execute("""
            INSERT INTO clientes (nombre, direccion, telefono, email)
            VALUES (%s, %s, %s, %s)
        """, (nombre, direccion, telefono, email))

        # Confirmar cambios
        db.connection.commit()

        # Respuesta exitosa
        return jsonify({'message': 'Cliente creado exitosamente'}), 201

    except IntegrityError:
        # Manejar error si el email ya está registrado
        return jsonify({'message': 'El email ya está registrado'}), 400

    except Exception as e:
        # Manejar errores generales
        return jsonify({'error': str(e)}), 500
