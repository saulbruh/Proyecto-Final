--Insertar datos a la tabla habitaciones
INSERT INTO habitaciones (numero_habitacion, tipo, descripcion,
precio, estado, imagen) --Campos a llenar
VALUES
('101', 'Sencilla', 'Habitación sencilla con cama individual',
50.00, 'Disponible', '../../presentation_layer/img/habitacion01.jpg'), --Datos de la habitacion 101
('102', 'Doble', 'Habitación doble con dos camas individuales',
75.00, 'Disponible', '../../presentation_layer/img/habitacion02.jpeg'), --Datos de la habitacion 102
('201', 'Matrimonial', 'Habitación matrimonial con cama king size', 100.00, 'Disponible',
 '../../presentation_layer/img/habitacion03.jpeg'), --Datos de la habitacion 201
('202', 'Suite', 'Suite de lujo con vista al mar', 
'Disponible', '../../presentation_layer/img/habitacion04.jpg'), --Datos de la habitacion 202
('301', 'Presidencial', 'Habitación presidencial con todas las comodidades', 
250.00, 'Disponible', '../../presentation_layer/img/habitacion05.jpeg'); --Datos de la habitacion 301
