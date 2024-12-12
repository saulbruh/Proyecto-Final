from flask import Blueprint, jsonify, request
from models import db

reserva_bp = Blueprint('reservas', __name__)

@reserva_bp.route('/crear', methods=['POST'])
def create_reserva():
    try:
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()
        cliente_id = data['cliente_id']
        habitacion_id = data['habitacion_id']
        fecha_inicio = data['fecha_inicio']
        fecha_fin = data['fecha_fin']

        # Crear un cursor para interactuar con la base de datos
        cursor = db.connection.cursor()

        # Insertar la reserva en la tabla `reservas`
        cursor.execute("""
            INSERT INTO reservas (cliente_id, habitacion_id, fecha_inicio, fecha_fin)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, habitacion_id, fecha_inicio, fecha_fin))

        # Confirmar cambios
        db.connection.commit()

        # Cerrar el cursor
        cursor.close()

        # Respuesta exitosa
        return jsonify({'message': 'Reserva creada exitosamente'}), 201

    except Exception as e:
        # Manejar errores generales
        return jsonify({'error': str(e)}), 500
