# app.py

import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Panel de Control de Datos de Vehículos')

# --- Botón para el Histograma de Kilometraje ---
st.write("Haz clic para ver la distribución de kilometraje.")
hist_button = st.button('Construir histograma de kilometraje')

if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer",
                       title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)


# --- Botón para el Gráfico de Dispersión ---
st.write("Haz clic para ver la relación entre kilometraje y precio.")
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión de kilometraje vs. precio')
    fig_scatter = px.scatter(
        car_data, x="odometer", y="price", title='Relación entre kilometraje y precio')
    st.plotly_chart(fig_scatter, use_container_width=True)


# --- Botón para el Histograma de Año del Vehículo ---
st.write("Haz clic para ver la distribución de los años de los vehículos.")
year_hist_button = st.button('Construir histograma de año')

if year_hist_button:
    st.write('Creación de un histograma para los años de los vehículos')
    fig_hist_year = px.histogram(
        car_data, x='model_year', title='Distribución de años de los vehículos')
    st.plotly_chart(fig_hist_year, use_container_width=True)


# --- Botón para el Gráfico de Barras de Tipo de Combustible ---
st.write("Haz clic para ver la distribución por tipo de combustible.")
fuel_bar_button = st.button('Construir gráfico de tipo de combustible')

if fuel_bar_button:
    st.write(
        'Creación de un gráfico de barras para la frecuencia por tipo de combustible')
    # Preparar los datos
    df_fuel = car_data['fuel'].value_counts().reset_index()
    df_fuel.columns = ['fuel_type', 'count']
    # Crear el gráfico
    fig_bar_fuel = px.bar(df_fuel, x='fuel_type', y='count',
                          labels={'fuel_type': 'Tipo de combustible',
                                  'count': 'Cantidad'},
                          title='Frecuencia por tipo de combustible')
    st.plotly_chart(fig_bar_fuel, use_container_width=True)
