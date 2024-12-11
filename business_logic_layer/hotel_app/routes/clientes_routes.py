from flask import Blueprint, jsonify, request
from models import db
cliente_bp = Blueprint('clientes', __name__)
@cliente_bp.route('/', methods=['GET'])
def get_clientes():
# Obtener todos los clientes
pass
@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente(id):
# Obtener un cliente por ID
pass
@cliente_bp.route('/', methods=['POST'])
def create_cliente():
# Crear un nuevo cliente
pass
@cliente_bp.route('/<int:id>', methods=['PUT'])
def update_cliente(id):
7
# Actualizar un cliente existente
pass
@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete_cliente(id):
# Eliminar un cliente
pass
