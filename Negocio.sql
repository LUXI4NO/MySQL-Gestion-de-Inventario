CREATE DATABASE Negocio;
USE Negocio;

 CREATE TABLE Proveedores (
    Proveedor_ID INT NOT NULL AUTO_INCREMENT,
    NombreProveedor VARCHAR(255) NOT NULL,
    Ubicacion VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(100),
    Notas TEXT,
    PRIMARY KEY( Proveedor_ID)
);


CREATE TABLE Productos (

    ID_Productos INT NOT NULL AUTO_INCREMENT,
    Proveedor_ID INT,
    Nombre VARCHAR(255),
    Descripcion TEXT,
    Categoria VARCHAR(255),
    PrecioCompra  DECIMAL(10,2),
    PrecioVenta DECIMAL(10,2),
    Stock INT,
    PRIMARY KEY(ID_Productos),
    FOREIGN KEY (Proveedor_ID) REFERENCES Proveedores(Proveedor_ID)
);

CREATE TABLE Existencias (
    ID_Existencia INT AUTO_INCREMENT PRIMARY KEY,
    ID_Productos INT,
    UbicacionAlmacen VARCHAR(100),
    FechaEntrada DATE,
    FechaCaducidad DATE,
    FOREIGN KEY (ID_Productos) REFERENCES Productos(ID_Productos)
);

-- Crear la tabla de Movimientos de Inventario
CREATE TABLE MovimientosInventario (
    ID_Movimiento INT AUTO_INCREMENT PRIMARY KEY,
    ID_Productos INT,
    TipoMovimiento ENUM('Entrada', 'Salida'),
    Cantidad INT,
    FechaMovimiento DATE,
    FOREIGN KEY (ID_Productos) REFERENCES Productos(ID_Productos)
);


