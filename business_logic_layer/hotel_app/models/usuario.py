from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, email, password, nombre, rol):
        self.id = id
        self.email = email
        self.password = password
        self.nombre = nombre
        self.rol = rol  # Ejemplo: 'admin' o 'cliente'

    def __repr__(self):
        return f"<Usuario {self.email}>"

