
# Importamos librerias
import pandas as pd
import streamlit as st
import plotly.express as px

# Leemos el archivo
car_data = pd.read_csv(
    # leer los datos del archivo
    'C:/Users/Cristian/OneDrive/Documents/Cristian Avila/Tripleten/Proyecto Sprint 7/vehicles_us.csv')

# Contenido de la aplicacion

# Encabezado
st.header('Informacion vehicular entre los años 1929 y 2019')


# Creamos un titulo para el ususario
st.write('''
         ## Crea un Histograma con la informacion Vehicular
         ''')

# Boton que al seleccionarlo crea histograma

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button == True:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", nbins=20, title="Relación entre kilometraje y vehículos vendidos",
                       labels={"odometer": "Kilometraje", "count": "Cantidad de Vehiculos vendidos"})

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.write('''
         ## Crea un Gráfico de dispersión con la informacion Vehicular
         ''')
scatter_checkbox = st.checkbox(
    'Construir Gráfica de Dispersión ', value=True)  # crear una casilla de validacion

if scatter_checkbox == True:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un Gráfica de Dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un grafico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", color="model_year", title="Relación entre kilometraje y precio de vehículos",
                     labels={"odometer": "Kilometraje", "price": "Precio (USD)", "model_year": "Año"})

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
