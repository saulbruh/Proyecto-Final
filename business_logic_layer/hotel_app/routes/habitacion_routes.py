@habitacion_bp.route('/disponibles', methods=['GET'])
def get_habitaciones_disponibles():
cursor = db.connection.cursor()
13
cursor.execute("SELECT * FROM habitaciones WHERE estado =
'Disponible'")
rows = cursor.fetchall()
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
return jsonify(habitaciones)
