import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(page_title="Gestion De Inventario", page_icon="⭕", layout="wide")
st.sidebar.info("### Sistema de Gestion de Inventario")
# Función para conectar a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='Negocio'
    )

def mostrar_inventario():
    st.markdown("<h1 style='text-align: center;'>Inventario</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>En esta sección, podrás ingresar la información necesaria para la gestión de Inventario. A continuación, se te guiará para registrar los datos pertinentes.</h6>", unsafe_allow_html=True)

    # Conectar a la base de datos y recuperar los datos del inventario
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query_inventario = """
    SELECT p.Nombre AS Nombre_Producto, p.Stock, p.PrecioCompra, p.PrecioVenta, p.Categoria, e.UbicacionAlmacen, e.FechaEntrada, e.FechaCaducidad
    FROM Existencias e
    INNER JOIN Productos p ON e.ID_Productos = p.ID_Productos
    WHERE p.Stock > 0
    """

    cursor.execute(query_inventario)
    datos_inventario = cursor.fetchall()
    cursor.close()
    conexion.close()

    # Inicializar tabla_inventario como None
    tabla_inventario = None

    if datos_inventario:
        tabla_inventario = pd.DataFrame(datos_inventario, columns=["Producto", "Stock", "Precio Unitario", "Precio de Venta", "Categoría", "Ubicación en Almacén", "Fecha de Entrada", "Fecha de Caducidad"])

        st.table(tabla_inventario)

        tabla_inventario["Valor Total"] = tabla_inventario['Stock'] * tabla_inventario['Precio Unitario']
        valor_total = tabla_inventario["Valor Total"].sum()

        st.info(f"Valor total del inventario: ${valor_total:,.0f}")
    else:
        st.warning("No se encontraron registros en el inventario.")

    st.write("---")

    st.markdown("<h1 style='text-align: center;'>Salida de Productos</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>En esta sección, podrás ingresar la información necesaria para la gestión de Inventario. A continuación, se te guiará para registrar los datos pertinentes.</h6>", unsafe_allow_html=True)

    with st.container():
        column1, column2 = st.columns(2)

        with column1:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            query_productos = "SELECT ID_Productos, Nombre FROM Productos"
            cursor.execute(query_productos)
            productos = cursor.fetchall()
            producto_dict = {str(producto[0]): producto[1] for producto in productos}
            selected_product_id = st.selectbox("Selecciona un Producto:", options=list(producto_dict.keys()))
            selected_product_name = producto_dict.get(selected_product_id, None)

            if selected_product_id is not None:
                query_cantidad_disponible = "SELECT Stock FROM Productos WHERE ID_Productos = %s"
                cursor.execute(query_cantidad_disponible, (int(selected_product_id),))
                cantidad_disponible = cursor.fetchone()[0]
            else:
                cantidad_disponible = None

            fecha_movimiento = st.date_input("Fecha de Movimiento del Producto:")

        with column2:
            movimiento = {"Salida por venta": "Venta",}
            tipo_movimiento = st.selectbox("Seleccione el Tipo de Movimiento:", list(movimiento.keys()))

            if cantidad_disponible is not None and cantidad_disponible >= 1 and tipo_movimiento == "Salida por venta":
                cantidad = st.number_input("Cantidad de Salida:", min_value=1, max_value=cantidad_disponible)


        if st.button("Registrar Salida", key="registrar_salida"):
            conexion = conectar_bd()
            cursor = conexion.cursor()
            consulta = "INSERT INTO MovimientosInventario (ID_Productos, TipoMovimiento, Cantidad, FechaMovimiento) VALUES (%s, %s, %s, %s)"
            datos = (int(selected_product_id), "Salida", cantidad, fecha_movimiento)

            try:
                cursor.execute(consulta, datos)

                if tipo_movimiento == "Salida por venta":
                    nueva_cantidad = cantidad_disponible - cantidad
                    query_actualizar_stock = "UPDATE Productos SET Stock = %s WHERE ID_Productos = %s"
                    cursor.execute(query_actualizar_stock, (nueva_cantidad, int(selected_product_id)))

                conexion.commit()
                st.success("Los datos de la salida se han registrado exitosamente.")
            except mysql.connector.Error as e:
                st.error("Hubo un error al registrar la salida.")
            finally:
                cursor.close()
                conexion.close()

    with st.container():
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query_salida = """
        SELECT m.ID_Movimiento, p.Nombre AS Nombre_Producto, e.UbicacionAlmacen AS Ubicacion_Producto, m.Cantidad, m.TipoMovimiento, m.FechaMovimiento, p.PrecioVenta
        FROM MovimientosInventario m
        INNER JOIN Productos p ON m.ID_Productos = p.ID_Productos
        INNER JOIN Existencias e ON m.ID_Productos = e.ID_Productos
        WHERE m.TipoMovimiento = 'Salida'
        ORDER BY m.FechaMovimiento DESC
        """

        cursor.execute(query_salida)
        salida_data = cursor.fetchall()
        cursor.close()
        conexion.close()

        if salida_data:
            df_salida = pd.DataFrame(salida_data, columns=["ID Movimiento", "Nombre Producto", "Ubicación Producto", "Cantidad", "Tipo de Movimiento", "Fecha de Movimiento", "Precio de Venta"])
            
            valor_total = (df_salida['Cantidad'] * df_salida['Precio de Venta']).sum()

            st.table(df_salida.set_index('ID Movimiento', drop=True))

            st.success(f"Valor recaudado de venta del inventario: ${valor_total:,.0f}")
        else:
            st.warning("No se encontraron registros de salida de productos.")

mostrar_inventario()
