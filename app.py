import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("Reporte de Incidencias - Serpost")

vehiculos = ["EJEMPLO1", "EJEMPLO2", "EJEMPLO3"]

vehiculo = st.selectbox("Selecciona el vehículo", vehiculos)

problema = st.selectbox(
    "Tipo de problema",
    ["Falla mecánica", "Accidente", "Retraso", "Documentación", "Otro"]
)

comentario = st.text_input("Comentario (opcional)")

if st.button("Reportar incidencia"):

    nueva_data = {
        "Fecha": [datetime.now()],
        "Vehiculo": [vehiculo],
        "Problema": [problema],
        "Comentario": [comentario]
    }

    df_nuevo = pd.DataFrame(nueva_data)

    archivo = "incidencias.xlsx"

    if os.path.exists(archivo):
        df_existente = pd.read_excel(archivo)
        df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
    else:
        df_final = df_nuevo

    df_final.to_excel(archivo, index=False)

    st.success(f"Incidencia guardada para {vehiculo}")
