#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

st.title("Consulta de Datos")

# Solicitar al usuario que ingrese la query
query = st.text_input("Ingrese su query")

# Mostrar la query ingresada por el usuario
st.write("Query ingresada:", query)

# Hacer una petición a la API para obtener los datos
url = "https://api.example.com/data"
params = {"query": query}
response = requests.get(url, params=params)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Obtener la respuesta en formato JSON
    data = response.json()
    # Mostrar la respuesta en la interfaz de usuario
    st.write("Respuesta:", data)
else:
    # Mostrar un mensaje de error si la petición falló
    st.write("Error al obtener la respuesta")
