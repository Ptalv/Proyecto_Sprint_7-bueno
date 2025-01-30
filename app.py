import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Bienvenidos a mi proyecto :)", divider="grey")

car_data = pd.read_csv("./vehicles_us.csv")
hist_button = st.button('Construir histograma')

if hist_button:

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir Grafico de Dispersión")

if scatter_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches, entre odometro y precio")

    fig2 = px.scatter(car_data, x="odometer", y="price",
                      color="type", title="Dispersion de odometro y precio")
    st.plotly_chart(fig2, use_container_width=True)

surpise_button = st.button("Botton sorpresa")

if surpise_button:
    st.write("HOLA :P")
