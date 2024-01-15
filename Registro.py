import streamlit as st
import pandas as pd
import mysql.connector
import re
from datetime import date

# Función para conectar a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='Negocio'
    )

# Streamlit App
st.set_page_config(page_title="Gestion De Inventario", page_icon="⭕", layout="wide")

st.sidebar.info("### Sistema de Gestion de Inventario")

def validar_telefono(telefono):
    return bool(re.match("^[0-9]*$", telefono))

def validar_correo(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def mostrar_inicio():
    with st.container():
        st.markdown("<h1 style='text-align: center;'>Proveedores</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'> Aquí podrás ingresar los datos esenciales de tus proveedores. Sigue los pasos a continuación para completar el registro de información de proveedores.</h6>", unsafe_allow_html=True)

        # Recopilación de datos del usuario
        columna1, columna2 = st.columns(2)
        with columna1:
            NombreProveedor = st.text_input("Nombre del Proveedor")
            Telefono = st.text_input("Teléfono del Proveedor")

            # Validar que solo se ingresen números en el campo de teléfono
            if not validar_telefono(Telefono):
                st.warning("Por favor, ingrese un número de teléfono válido.")
        with columna2:
            Email = st.text_input("Email del Proveedor")

            # Validar el formato del correo electrónico
            if not validar_correo(Email):
                st.warning("Por favor, ingrese un correo electrónico válido.")
            Ubicacion = st.text_input("Ingrese la Ubicación del Proveedor")

        if st.button("Registrar Proveedor", key="registrar_proveedor"):
            # Validar campos obligatorios
            if not NombreProveedor or not Ubicacion:
                st.error("Por favor, ingrese el nombre y la ubicación del proveedor.")
            else:
                with conectar_bd() as conexion:
                    try:
                        with conexion.cursor() as cursor:
                            # Inserción de datos en la base de datos
                            consulta = "INSERT INTO Proveedores (NombreProveedor, Ubicacion, Telefono, Email) VALUES (%s, %s, %s, %s)"
                            datos = (NombreProveedor, Ubicacion, Telefono, Email)
                            cursor.execute(consulta, datos)
                            conexion.commit()
                            st.success("Los datos del proveedor se han registrado exitosamente.")
                    except mysql.connector.Error as e:
                        st.error("Error al registrar el proveedor: {}".format(e))

        # Mostrar la tabla de proveedores
        with st.expander("Ver Proveedores Registrados"):
            try:
                with conectar_bd() as conexion:
                    try:
                        with conexion.cursor() as cursor:
                            query = "SELECT Proveedor_ID, NombreProveedor, Ubicacion, Telefono, Email FROM Proveedores"
                            cursor.execute(query)
                            Proveedores = cursor.fetchall()
                            df = pd.DataFrame(Proveedores, columns=["ID", "Nombre Proveedor", "Ubicación", "Teléfono", "Email"])
                            st.table(df.set_index('ID', drop=True))
                        
                        if st.button("Eliminar Última Fila de Proveedores", key="eliminar_ultima_fila_proveedores"):
                            if not df.empty:
                                ultimo_id = int(df.iloc[-1]["ID"])

                                try:
                                    with conexion.cursor() as cursor:
                                        delete_productos_query = "DELETE FROM Productos WHERE Proveedor_ID = %s"
                                        cursor.execute(delete_productos_query, (ultimo_id,))

                                        delete_proveedores_query = "DELETE FROM Proveedores WHERE Proveedor_ID = %s"
                                        cursor.execute(delete_proveedores_query, (ultimo_id,))

                                    conexion.commit()
                                    st.success("La última fila de proveedores y las filas relacionadas en productos han sido eliminadas.")
                                except mysql.connector.Error as e:
                                    st.error("Error al eliminar el proveedor y sus productos relacionados: {}".format(e))
                            else:
                                st.warning("La tabla de Proveedores ya está vacía.")
                    except mysql.connector.Error as e:
                        st.error("Error al obtener los datos de los proveedores: {}".format(e))
            except mysql.connector.Error as e:
                st.error("Error al conectar con la base de datos: {}".format(e))

    st.write("---")
    with st.container():
        st.markdown("<h1 style='text-align: center;'>Productos</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>Aquí podrás ingresar la información detallada de tus productos. Sigue los pasos a continuación para completar el registro de tus productos.</h6>", unsafe_allow_html=True)

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query_proveedores = "SELECT Proveedor_ID, NombreProveedor FROM Proveedores"
        cursor.execute(query_proveedores)
        proveedores = cursor.fetchall()
        proveedores_dict = {str(proveedor[0]): proveedor[1] for proveedor in proveedores}

        Proveedor_ID = st.selectbox("Selecciona un Proveedor:", options=list(proveedores_dict.keys()))

        # Recopilación de datos del usuario
        column1, column2 = st.columns(2)
        with column1:
                Nombre = st.text_input("Nombre del Producto:")
                Descripcion = st.text_input("Descripción del Producto:")
                Categoria = st.text_input("Categoría del Producto:")
        with column2:
                PrecioCompra = st.number_input("Precio de Compra del Producto:", min_value=0, max_value=10000000)
                PrecioVenta = st.number_input("Precio de Venta del Producto:", min_value=0, max_value=10000000)
                Stock = st.number_input("Cantidad en Stock:", min_value=0, max_value=10000000)

        if st.button("Registrar Producto", key="registrar_producto"):
                if not Proveedor_ID or not Nombre or not PrecioCompra or not PrecioVenta or not Stock:
                    st.error("Por favor, complete todos los campos obligatorios.")
                else:
                    with conectar_bd() as conexion:
                        cursor = conexion.cursor()

                        consulta = "INSERT INTO Productos (Proveedor_ID, Nombre, Descripcion, Categoria, PrecioCompra, PrecioVenta, Stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        datos = (Proveedor_ID, Nombre, Descripcion, Categoria, PrecioCompra, PrecioVenta, Stock)

                        try:
                            cursor.execute(consulta, datos)
                            conexion.commit()
                            st.success("Los datos se han registrado exitosamente.")
                        except mysql.connector.Error as e:
                            st.error("Error al registrar el producto.")
                        finally:
                            cursor.close()

        # Sección para mostrar los productos en una tabla
        with st.expander("Ver Productos Registrados"):
            try:
                with conectar_bd() as conexion:
                    with conexion.cursor() as cursor:
                        query = """
                        SELECT p.ID_Productos, pr.NombreProveedor, p.Nombre, p.Descripcion, p.Categoria,
                            p.PrecioCompra, p.PrecioVenta, p.Stock
                        FROM Productos p
                        INNER JOIN Proveedores pr ON p.Proveedor_ID = pr.Proveedor_ID
                        """

                        cursor.execute(query)
                        productos = cursor.fetchall()
                        df = pd.DataFrame(productos, columns=["ID", "Proveedor", "Nombre", "Descripción", "Categoría",
                                                            "Precio Compra", "Precio Venta", "Stock"])

                        st.table(df.set_index('ID', drop=True))

                        if st.button("Eliminar Última Fila de Productos", key="eliminar_ultima_fila_productos"):
                            if not df.empty:
                                ultimo_id = int(df.iloc[-1]["ID"])

                                try:
                                    delete_existencias_query = "DELETE FROM Existencias WHERE ID_Productos = %s"
                                    cursor.execute(delete_existencias_query, (ultimo_id,))

                                    delete_productos_query = "DELETE FROM Productos WHERE ID_Productos = %s"
                                    cursor.execute(delete_productos_query, (ultimo_id,))

                                    conexion.commit()
                                    df = df.iloc[:-1]
                                    st.success("La última fila de productos ha sido eliminada.")
                                except mysql.connector.Error as e:
                                    st.error("Error al eliminar el producto y sus existencias relacionadas: {}".format(e))
                            else:
                                st.warning("La tabla de productos ya está vacía.")
            except mysql.connector.Error as e:
                st.error("Error al conectar con la base de datos: {}".format(e))
    
    st.write("---")
    with st.container():
        st.markdown("<h1 style='text-align: center;'>Gestión de Almacenes</h1>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>En esta sección, podrás ingresar la información necesaria para la gestión de almacenes. A continuación, se te guiará para registrar los datos pertinentes.</h6>", unsafe_allow_html=True)

        try:
            with conectar_bd() as conexion:
                with conexion.cursor() as cursor:
                    # Obtener productos para seleccionar
                    query_Productos = "SELECT ID_Productos, Nombre FROM Productos"
                    cursor.execute(query_Productos)
                    Productos = cursor.fetchall()
                    Productos_dict = {str(producto[0]): f"{producto[0]} - {producto[1]}" for producto in Productos}

                    # Interfaz de usuario para ingresar información del almacén
                    ID_Productos = st.selectbox("Selecciona un Producto por ID:", options=list(Productos_dict.keys()))

                    # Obtener opciones de ubicación del almacén (puedes obtenerlas de la base de datos si es necesario)
                    UbicacionAlmacen_options = ["almacen 1", "almacen 2", "almacen 3"]
                    UbicacionAlmacen = st.selectbox("Seleccione la Ubicación del Almacén:", options=UbicacionAlmacen_options)

                    # Columnas para entrada de fechas
                    column1, column2 = st.columns(2)
                    with column1:
                        FechaEntrada = st.date_input("Fecha de Entrada del Producto:", value=date.today())
                    with column2:
                        FechaCaducidad = st.date_input("Fecha de Caducidad del Producto:")

                    # Botón para registrar el almacén
                    if st.button("Registrar Almacén", key="registrar_Almacen"):
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "INSERT INTO Existencias (ID_Productos, UbicacionAlmacen, FechaEntrada, FechaCaducidad) VALUES (%s, %s, %s, %s)"
                                datos = (ID_Productos, UbicacionAlmacen, FechaEntrada, FechaCaducidad)

                                cursor.execute(consulta, datos)
                                conexion.commit()
                                st.success("Los datos del almacén se han registrado exitosamente.")
                        except mysql.connector.Error as e:
                            st.error("Error al registrar el almacén: {}".format(e))
        except mysql.connector.Error as e:
            st.error("Error al conectar con la base de datos: {}".format(e))


mostrar_inicio()
