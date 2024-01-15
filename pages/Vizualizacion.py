import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

st.set_page_config(page_title="Gestion De Inventario", page_icon="⭕", layout="wide")
st.sidebar.info("### Sistema de Gestion de Inventario")
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='Negocio'
    )


with st.container():
    st.write("##")
    st.markdown("<h1 style='text-align: center;'>Análisis Visual de Movimientos del Inventario de Productos</h1>", unsafe_allow_html=True)
    st.write("##")

            # Conectar a la base de datos y recuperar los datos del inventario
    with conectar_bd() as conexion, conexion.cursor() as cursor:
        # Consulta SQL
        query_inventario = """
        SELECT p.Nombre AS Nombre_Producto, p.Stock, p.PrecioCompra, p.PrecioVenta, p.Categoria, e.UbicacionAlmacen, e.FechaEntrada, e.FechaCaducidad
        FROM Existencias e
        INNER JOIN Productos p ON e.ID_Productos = p.ID_Productos
        WHERE p.Stock > 0  # Solo seleccionar productos con stock mayor que cero
        """

                # Ejecutar la consulta
        cursor.execute(query_inventario)
        datos_inventario = cursor.fetchall()

            # Inicializar tabla_inventario como None
        tabla_inventario = None

            # Crear tabla_inventario si hay datos en datos_inventario
        if datos_inventario:
            tabla_inventario = pd.DataFrame(datos_inventario, columns=["Producto", "Stock", "Precio Unitario", "Precio de Venta", "Categoría", "Ubicación en Almacén", "Fecha de Entrada", "Fecha de Caducidad"])

            columna_uno, columna_dos = st.columns(2)

            with columna_uno:
                # Gráfico de pastel
                fig_pie = px.pie(tabla_inventario, names='Producto', values='Stock', title='Distribución del Stock por Producto')
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                fig_pie.update_layout(
                    width=600,
                    height=400,
                    margin=dict(t=40, b=60),
                    showlegend=True,
                    legend=dict(x=1, y=0.5),
                )
                fig_pie.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
                fig_pie.update_traces(
                    hovertemplate='<b>%{label}</b><br>Stock: %{percent}<br>',
                )

                    # Mostrar el gráfico de pastel en Streamlit
                st.plotly_chart(fig_pie, use_container_width=True)

            with columna_dos:
                # Gráfico de barras
                tabla_inventario['Valor Total'] = tabla_inventario['Stock'] * tabla_inventario['Precio Unitario']

                fig_bar = px.bar(tabla_inventario, x='Producto', y='Valor Total', color='Producto', title='Valor Total por Producto')

                fig_bar.update_traces(
                    textfont_size=12,
                    textangle=0,
                    textposition="outside",
                    cliponaxis=False,
                    textfont_color='black',
                    hovertemplate='<b>%{y}</b><br>Stock: %{y:,.0f}<br>',
                )
                fig_bar.update_layout(
                    xaxis_title='Stock',
                    yaxis_title='Producto',
                    width=600,
                    height=400,
                    margin=dict(l=75, r=25, t=75, b=25),
                    bargap=0.3,
                    showlegend=False,
                    yaxis=dict(showgrid=False)
                )
                fig_bar.update_traces(
                    hovertemplate='%{y}',  # Formato del hover
                    hoverinfo='x+y',  # Información en el hover
                )
                fig_bar.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))

                # Mostrar el valor total general en el título
                valor_total = tabla_inventario['Valor Total'].sum()
                fig_bar.update_layout(title_text=f'Valor total del Stock: {valor_total:,.0f}')

                # Mostrar el gráfico solo si hay datos
                st.plotly_chart(fig_bar, use_container_width=True)

            with st.container():
                fig_bar = px.bar(tabla_inventario, y='Ubicación en Almacén', x='Stock', color='Ubicación en Almacén', title='Stock de Productos por Ubicación en Almacén')

                fig_bar.update_traces(
                    textfont_size=12,
                    textangle=0,
                    textposition="outside",
                    cliponaxis=False,
                    textfont_color='black',
                    hovertemplate='<b>%{x}</b><br>Stock: %{x:,.0f}<br>',
                )
                fig_bar.update_layout(
                    xaxis_title='Stock',
                    yaxis_title='Ubicación en Almacén',
                    width=600,
                    height=400,
                    margin=dict(l=75, r=25, t=75, b=25),
                    bargap=0.3,
                    showlegend=False,
                    yaxis=dict(showgrid=False)
                )
                fig_bar.update_traces(
                    hovertemplate='%{x}',  # Formato del hover
                    hoverinfo='x+y',  # Información en el hover
                )
                fig_bar.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))

                # Mostrar el gráfico solo si hay datos
                st.plotly_chart(fig_bar, use_container_width=True)

st.write("---")              
with st.container():
            st.markdown("<h1 style='text-align: center;'>Análisis Visual de Movimientos de Salida de Productos</h1>", unsafe_allow_html=True)
            st.write("##")
            # Conectar a la base de datos
            # Conectar a la base de datos
            conexion = conectar_bd()
            cursor = conexion.cursor()

            # Consulta para obtener datos del registro de salida de productos
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

            # Verificar si hay datos
            if salida_data:
                # Crear DataFrame
                df_salida = pd.DataFrame(salida_data, columns=["ID Movimiento", "Nombre Producto", "Ubicación Producto", "Cantidad", "Tipo de Movimiento", "Fecha de Movimiento", "Precio de Venta"])

                columna_uno, columna_dos = st.columns(2)

                with columna_uno:
                    # Gráfico de pastel
                    fig_pie = px.pie(df_salida, names='Nombre Producto', values='Cantidad', title='Proporción de Movimientos')

                    # Configuración del gráfico
                    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                    fig_pie.update_layout(
                        width=600,
                        height=400,
                        margin=dict(t=40, b=60),
                        showlegend=True,
                        legend=dict(x=1, y=0.5),
                    )
                    fig_pie.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
                    fig_pie.update_traces(
                        hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<br>',
                    )

                    # Mostrar el gráfico de pastel en Streamlit
                    st.plotly_chart(fig_pie, use_container_width=True)

                with columna_dos:
                    # Calcular el valor total y agregar una columna al DataFrame
                    valor_total = (df_salida['Cantidad'] * df_salida['Precio de Venta']).sum()
                    df_salida['Valor Total'] = df_salida['Cantidad'] * df_salida['Precio de Venta']

                    # Crear gráfico de barras
                    fig_bar = px.bar(df_salida, x='Nombre Producto', y='Valor Total', color='Nombre Producto', title='Valor Total de Productos por Tipo de Movimiento')

                    # Configuración del gráfico
                    fig_bar.update_traces(
                        textfont_size=12,
                        textangle=0,
                        textposition="outside",
                        cliponaxis=False,
                        textfont_color='black',
                        hovertemplate='<b>%{y:,.0f}</b><br>Cantidad: %{y:,.0f}<br>',
                    )
                    fig_bar.update_layout(
                        xaxis_title='Nombre Producto',
                        yaxis_title='Valor Total',
                        width=600,
                        height=400,
                        margin=dict(l=75, r=25, t=75, b=25),
                        bargap=0.3,
                        showlegend=False,
                        yaxis=dict(showgrid=False)
                    )
                    fig_bar.update_traces(
                        hovertemplate='%{y:,.0f}',  # Formato del hover
                        hoverinfo='y',  # Información en el hover
                    )
                    fig_bar.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))

                    # Mostrar el valor total general en el título
                    fig_bar.update_layout(title_text=f'Valor de la Cantidad Vendida: {valor_total:,.0f}')

                    if not df_salida.empty:
                        # Mostrar el gráfico solo si hay datos
                        st.plotly_chart(fig_bar, use_container_width=True)
                    else:
                        st.write("No hay datos de salida para mostrar.")

                with st.container():
                    # Crear DataFrame
                    df_salida = pd.DataFrame(salida_data, columns=["ID Movimiento", "Nombre Producto", "Ubicación Producto", "Cantidad", "Tipo de Movimiento", "Fecha de Movimiento", "Precio de Venta"])

                    # Agregar hovertext
                    df_salida['hovertext'] = df_salida['Nombre Producto']

                    # Crear gráfico de barras
                    fig_bar = px.bar(df_salida, x='Fecha de Movimiento', y='Cantidad', color='Fecha de Movimiento', title='Cantidad Total de Productos por Fecha de Movimiento', text='hovertext')

                    # Configuración del gráfico
                    fig_bar.update_traces(
                        textfont_size=12,
                        textangle=0,
                        textposition="outside",
                        cliponaxis=False,
                        textfont_color='black',
                        hovertemplate='<b>%{x}</b><br>Nombre Producto: %{text}<br>Cantidad: %{y:,.0f}<br>',
                    )

                    fig_bar.update_layout(
                        xaxis_title='Fecha de Movimiento',
                        yaxis_title='Cantidad',
                        width=800,  # Ajusta el ancho del gráfico para mostrar mejor las etiquetas de fecha
                        height=500,
                        margin=dict(l=100, r=25, t=75, b=25),
                        bargap=0.3,
                        showlegend=False,
                        yaxis=dict(showgrid=False)
                    )

                    fig_bar.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))

                    # Mostrar el gráfico solo si hay datos
                    if not df_salida.empty:
                        st.plotly_chart(fig_bar, use_container_width=True)
                    else:
                        st.write("No hay datos de salida para mostrar.")
