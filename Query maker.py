#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Agregar un título a la página
st.title("Consulta a la base de datos")

# Crear un campo de entrada de texto para la consulta
query = st.text_input("Ingrese su consulta aquí:")

# Mostrar la consulta ingresada por el usuario
st.write("Consulta:", query)

# Si se ha ingresado una consulta, realizar una acción
if query:
    # Aquí podrías incluir la lógica necesaria para hacer la consulta a la base de datos
    # y almacenar la respuesta en la variable "answer"
    answer = "Esta es la respuesta a su consulta: " + query
    
    # Mostrar la respuesta obtenida
    st.write(answer)

