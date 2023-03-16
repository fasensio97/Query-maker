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

response = 'esta es la respuesta'
st.write(response)
