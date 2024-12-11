--Crear la tabla clientes
CREATE TABLA clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	direccion VARCHAR(255),
	telefono VARCHAR(20),
	email VARCHAR(100) NOT NULL UNIQUE,
	fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

--Crear la tabla habitaciones
CREATE TABLE habitaciones (
	id INT AUTO_INCREMENT PRIMARY KEY,
	numero_habitacion VARCHAR(10) NOT NULL UNIQUE,
	tipo VARCHAR(50),
	descripcion TEXT,
	precio DECIMAL(10,2) NOT NULL,
	estado VARCHAR(20) DEFAULT 'Disponible',
	imagen VARCHAR(255)
);

--Crear la tabla reservas
CREATE TABLE reservas (
	id INT AUTO_INCREMENT PRIMARY KEY,
	cliente_id INT NOT NULL,
	habitacion_id INT NOT NULL,
	fecha_inicio DATE NOT NULL,
	fecha_fin DATE NOT NULL,
	estado VARCHAR(20) DEFAULT 'Activa',
	fecha_reserva DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (cliente_id) REFERENCES clientes(id),
	FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id)
);

