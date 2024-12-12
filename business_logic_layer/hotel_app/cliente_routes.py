from flask import Blueprint, jsonify, request
from models import db

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/', methods=['GET'])
def get_clientes():
    # Crear un cursor para interactuar con la base de datos
    cursor = db.connection.cursor()

    # Ejecutar la consulta SQL
    cursor.execute("SELECT * FROM clientes")

    # Recuperar todas las filas del resultado
    rows = cursor.fetchall()

    # Construir la lista de clientes
    clientes = []
    for row in rows:
        cliente = {
            'id': row[0],
            'nombre': row[1],
            'direccion': row[2],
            'telefono': row[3],
            'email': row[4],
            'fecha_registro': row[5].strftime('%Y-%m-%d %H:%M:%S')
        }
        clientes.append(cliente)

    # Cerrar el cursor
    cursor.close()

    # Devolver la lista de clientes como JSON
    return jsonify(clientes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
