@reserva_bp.route('/', methods=['POST'])
@login_required
def create_reserva():
data = request.get_json()
habitacion_id = data['habitacion_id']
fecha_inicio = data['fecha_inicio']
fecha_fin = data['fecha_fin']
cliente_id = current_user.id
cursor = db.connection.cursor()
cursor.execute("""
INSERT INTO reservas (cliente_id, habitacion_id,
fecha_inicio, fecha_fin)
VALUES (%s, %s, %s, %s)
""", (cliente_id, habitacion_id, fecha_inicio, fecha_fin))
14
db.connection.commit()
return jsonify({'message': 'Reserva creada exitosamente'}),
201
