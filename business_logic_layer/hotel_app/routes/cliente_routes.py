@cliente_bp.route('/', methods=['POST'])
def create_cliente():
data = request.get_json()
nombre = data['nombre']
direccion = data.get('direccion', '')
telefono = data.get('telefono', '')
email = data['email']
cursor = db.connection.cursor()
cursor.execute("""
INSERT INTO clientes (nombre, direccion, telefono,
email)
VALUES (%s, %s, %s, %s)
""", (nombre, direccion, telefono, email))
db.connection.commit()
return jsonify({'message': 'Cliente creado exitosamente'}),
201
from pymysql.err import IntegrityError
 @cliente_bp.route('/', methods=['POST'])
 def create_cliente():
 try:
 email)
 cursor.execute("""
 INSERT INTO clientes (nombre, direccion, telefono,
 VALUES (%s, %s, %s, %s)
 """, (nombre, direccion, telefono, email))
 db.connection.commit()
 except IntegrityError:
 return jsonify({'message': 'El email ya está
 registrado'}), 400
