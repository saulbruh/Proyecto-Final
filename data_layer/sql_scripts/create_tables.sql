--Crear la tabla clientes
CREATE TABLA clientes (
	id INT AUTO_INCREMENT PRIMARY KEY, --Identificador unico para cada cliente
	nombre VARCHAR(100) NOT NULL, --Nombre completo del cliente, obligatorio
	direccion VARCHAR(255), --direccion del cliente
	telefono VARCHAR(20), --numero de telefono del cliente
	email VARCHAR(100) NOT NULL UNIQUE, --correo electronico del cliente, obligatorio
	fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP --Fecha de registro, se registra automaticamente
);

--Crear la tabla habitaciones
CREATE TABLE habitaciones (
	id INT AUTO_INCREMENT PRIMARY KEY, --Identificador unica para cada habitacion
	numero_habitacion VARCHAR(10) NOT NULL UNIQUE, --Numero de habitacion, obligatorio 
	tipo VARCHAR(50), --tipo de habitacion
	descripcion TEXT, --descripcion de la habitacion
	precio DECIMAL(10,2) NOT NULL, --Precio de la habitacion por noche, obligatorio
	estado VARCHAR(20) DEFAULT 'Disponible', --Estado de la habitacion
	imagen VARCHAR(255) --Imagenes de la habitacion
);

--Crear la tabla reservas
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único de la reserva.
    cliente_id INT NOT NULL, -- ID del cliente que realiza la reserva.
    habitacion_id INT NOT NULL -- ID de la habitación reservada.
    fecha_inicio DATE NOT NULL -- Fecha de inicio de la reserva.
    fecha_fin DATE NOT NULL -- Fecha de fin de la reserva.
    estado VARCHAR(20) DEFAULT 'Activa', -- Estado de la reserva (por defecto 'Activa').
    fecha_reserva DATETIME DEFAULT CURRENT_TIMESTAMP, -- Fecha de creación de la reserva.

    -- Llaves foráneas para relaciones:
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id)
);

