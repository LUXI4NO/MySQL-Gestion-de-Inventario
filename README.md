# Análisis de Datos

Este repositorio contiene códigos para el análisis y visualización de datos, enfocándose en la gestión de inventario, registro de proveedores y productos, así como análisis visual de movimientos de inventario.

## Descripción

Los códigos proporcionados se centran en la gestión de inventario y registro de proveedores y productos, utilizando Streamlit, Plotly Express y una base de datos MySQL. Se incluyen funcionalidades para el registro, visualización y análisis de datos relacionados con el inventario y los movimientos de productos.

## Datos Utilizados

Los datos se almacenan en una base de datos MySQL llamada "Negocio" y se utilizan para registrar proveedores, productos y movimientos de inventario.

## Base de Datos MySQL

El sistema está respaldado por una sólida estructura de Base de Datos MySQL que soporta eficientemente las siguientes funcionalidades clave:

1. **Gestión de Proveedores:**
   - Registro detallado de proveedores, incluyendo información como nombre, ubicación, contacto, correo electrónico y notas adicionales.

2. **Control de Productos:**
   - Almacenamiento y seguimiento de productos con atributos significativos como nombre, descripción, categoría, precios de compra y venta, así como la cantidad disponible en stock.

3. **Seguimiento de Existencias:**
   - Sistema de control de existencias que registra la ubicación en el almacén, la fecha de entrada y la fecha de caducidad (cuando sea aplicable) para una gestión eficiente.

4. **Movimientos de Inventario:**
   - Registro de movimientos de entrada y salida de productos, con detalles como la cantidad afectada, el tipo de movimiento (entrada/salida) y la fecha correspondiente.

La base de datos ha sido diseñada cuidadosamente, aprovechando las relaciones entre las tablas para garantizar la integridad y consistencia de los datos. Esta estructura proporciona una base robusta para la implementación de otras características y facilita el mantenimiento y la expansión del sistema en el futuro.

## Funcionalidades

### Registro de Proveedores y Productos
- Interfaz interactiva para ingresar información de proveedores y productos.
- Validación de entrada para teléfono y correo electrónico.
- Visualización de proveedores y productos registrados en tablas.
- Eliminación de la última fila de proveedores y productos.
![image](https://github.com/LUXI4NO/MySQL-Gestion-de-Inventario/assets/140111840/41725d6a-f283-49ab-b068-185d726bb059)
### Registro Visual del Inventario de Entrada de Productos

- **Inventario Detallado:** Muestra una tabla detallada con información crucial sobre los productos almacenados, incluyendo nombre, stock, precios, categoría, ubicación en el almacén y fechas asociadas.

- **Valor Total del Inventario:** Calcula y muestra el valor total del inventario en función de los productos disponibles y sus precios unitarios.

- **Registro de Salida de Productos:** Permite registrar salidas de productos, como ventas, con la posibilidad de seleccionar el producto, tipo de movimiento y cantidad. La aplicación actualiza automáticamente el stock en consecuencia.

- **Registro Histórico de Salidas:** Ofrece una tabla que presenta el historial de salidas de productos, incluyendo detalles como nombre del producto, ubicación, cantidad, tipo de movimiento, fecha y precio de venta.
![image](https://github.com/LUXI4NO/MySQL-Gestion-de-Inventario/assets/140111840/d09f5d90-361a-4ac1-b52c-b16b94214427)

### Análisis Visual de Movimientos de Salida de Productos

- **Proporción de Movimientos:** Visualiza la proporción de diferentes tipos de movimientos de salida, proporcionando una instantánea clara de las acciones realizadas.

- **Valor Total por Tipo de Movimiento:** Representa gráficamente el valor total generado por cada tipo de movimiento (por ejemplo, ventas), permitiendo una evaluación rápida de la contribución financiera de cada tipo.

- **Cantidad Total por Fecha de Movimiento:** Muestra un gráfico de barras que ilustra la cantidad total de productos que salieron en un día específico, facilitando la identificación de patrones y tendencias.
![image](https://github.com/LUXI4NO/MySQL-Gestion-de-Inventario/assets/140111840/cd26c740-edaf-4584-8718-7a7ff346aa77)

### Análisis Visual de Movimientos del Inventario de Productos
- Gráficos de pastel y de barras para analizar la distribución del stock y el valor total por producto.
- Gráfico adicional para mostrar el stock de productos por ubicación en el almacén.
- Análisis visual de los movimientos de salida de productos con gráficos de pastel y de barras.
![image](https://github.com/LUXI4NO/MySQL-Gestion-de-Inventario/assets/140111840/e006367f-6d08-4578-b8fe-4c05b609a530)


## Librerías Utilizadas
- `streamlit`
- `pandas`
- `mysql.connector`
- `plotly.express`
  
## Instrucciones de Uso

1. Clona el repositorio: `git clone https://github.com/tu_usuario/analisis-de-datos.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación con Streamlit: `streamlit run nombre_del_script.py`

# Autor
### Luciano Ezequiel Alvarez



## Enlaces

- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)
