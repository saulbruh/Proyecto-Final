from flask import Blueprint, jsonify
from models import db

habitacion_bp = Blueprint('habitaciones', __name__)

@habitacion_bp.route('/disponibles', methods=['GET'])
def get_habitaciones_disponibles():
    try:
        # Crear un cursor para interactuar con la base de datos
        cursor = db.connection.cursor()

        # Ejecutar la consulta SQL para obtener habitaciones disponibles
        cursor.execute("SELECT * FROM habitaciones WHERE estado = 'Disponible'")
        rows = cursor.fetchall()

        # Convertir los resultados en una lista de objetos JSON
        habitaciones = []
        for row in rows:
            habitacion = {
                'id': row[0],
                'numero_habitacion': row[1],
                'tipo': row[2],
                'descripcion': row[3],
                'precio': float(row[4]),
                'estado': row[5],
                'imagen': row[6]
            }
            habitaciones.append(habitacion)

        # Cerrar el cursor
        cursor.close()

        # Retornar las habitaciones en formato JSON
        return jsonify(habitaciones), 200

    except Exception as e:
        # Manejar errores y devolver un mensaje en formato JSON
        return jsonify({'error': str(e)}), 500
