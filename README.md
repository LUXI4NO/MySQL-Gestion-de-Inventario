# Análisis de Datos

Este repositorio contiene códigos para el análisis y visualización de datos, enfocándose en la gestión de inventario, registro de proveedores y productos, así como análisis visual de movimientos de inventario.

## Descripción

Los códigos proporcionados se centran en la gestión de inventario y registro de proveedores y productos, utilizando Streamlit, Plotly Express y una base de datos MySQL. Se incluyen funcionalidades para el registro, visualización y análisis de datos relacionados con el inventario y los movimientos de productos.

## Tabla de Contenidos

1. **Registro de Proveedores y Productos**
2. **Análisis Visual de Movimientos del Inventario de Productos**
3. **Análisis Visual de Movimientos de Salida de Productos**

## Librerías Utilizadas

- `streamlit`
- `pandas`
- `mysql.connector`
- `plotly.express`

## Datos Utilizados

Los datos se almacenan en una base de datos MySQL llamada "Negocio" y se utilizan para registrar proveedores, productos y movimientos de inventario.

## Funcionalidades

### Registro de Proveedores y Productos
- Interfaz interactiva para ingresar información de proveedores y productos.
- Validación de entrada para teléfono y correo electrónico.
- Visualización de proveedores y productos registrados en tablas.
- Eliminación de la última fila de proveedores y productos.

### Registro Visual del Inventario de Entrada de Productos

- **Inventario Detallado:** Muestra una tabla detallada con información crucial sobre los productos almacenados, incluyendo nombre, stock, precios, categoría, ubicación en el almacén y fechas asociadas.

- **Valor Total del Inventario:** Calcula y muestra el valor total del inventario en función de los productos disponibles y sus precios unitarios.

- **Registro de Salida de Productos:** Permite registrar salidas de productos, como ventas, con la posibilidad de seleccionar el producto, tipo de movimiento y cantidad. La aplicación actualiza automáticamente el stock en consecuencia.

- **Registro Histórico de Salidas:** Ofrece una tabla que presenta el historial de salidas de productos, incluyendo detalles como nombre del producto, ubicación, cantidad, tipo de movimiento, fecha y precio de venta.

### Análisis Visual de Movimientos de Salida de Productos

- **Proporción de Movimientos:** Visualiza la proporción de diferentes tipos de movimientos de salida, proporcionando una instantánea clara de las acciones realizadas.

- **Valor Total por Tipo de Movimiento:** Representa gráficamente el valor total generado por cada tipo de movimiento (por ejemplo, ventas), permitiendo una evaluación rápida de la contribución financiera de cada tipo.

- **Cantidad Total por Fecha de Movimiento:** Muestra un gráfico de barras que ilustra la cantidad total de productos que salieron en un día específico, facilitando la identificación de patrones y tendencias.

### Análisis Visual de Movimientos del Inventario de Productos
- Gráficos de pastel y de barras para analizar la distribución del stock y el valor total por producto.
- Gráfico adicional para mostrar el stock de productos por ubicación en el almacén.
- Análisis visual de los movimientos de salida de productos con gráficos de pastel y de barras.

### Ejemplos de Gráficos Generados

[En desarrollo]

## Uso

[En desarrollo]

## Dependencias

- Streamlit
- Pandas
- MySQL Connector
- Plotly Express

## Instrucciones de Uso

1. Clona el repositorio: `git clone https://github.com/tu_usuario/analisis-de-datos.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación con Streamlit: `streamlit run nombre_del_script.py`

# Autor
### Luciano Ezequiel Alvarez

## Casos de Uso y Aplicaciones Futuras

[En desarrollo]

## Enlaces

- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)



- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)
