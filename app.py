import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("Registro de Vehículos - Serpost")

# =========================
# INPUTS
# =========================

administracion = st.selectbox(
    "Administración",
    [
        "ABANCAY",
        "AREQUIPA",
        "AYACUCHO",
        "BREÑA",
        "CAJAMARCA",
        "CALLAO",
        "CERRO DE PASCO",
        "CHACHAPOYAS",
        "CHICLAYO",
        "CHIMBOTE",
        "CHOSICA",
        "COMAS",
        "CUSCO",
        "HUACHO",
        "HUANCAVELICA",
        "HUANCAYO",
        "HUÁNUCO",
        "HUARAZ",
        "ICA",
        "INGENIERÍA",
        "IQUITOS",
        "JESÚS MARÍA",
        "JULIACA",
        "LA VICTORIA",
        "LIMA",
        "LINCE",
        "MIRAFLORES",
        "MOQUEGUA",
        "PIURA",
        "PUCALLPA",
        "PUERTO MALDONADO",
        "PUNO",
        "TACNA",
        "TARAPOTO",
        "TRUJILLO",
        "TUMBES",
        "VMT"
    ]
)

# Tipo de vehículo
tipo_vehiculo = st.selectbox(
    "Tipo de vehículo",
    ["MOTO", "BICICLETA", "CAMIONETA"]
)

# Placa
placa = st.text_input("Placa del vehículo")

# Estado
estado = st.selectbox(
    "Estado del vehículo",
    ["Operativa", "Inoperativa"]
)

# Motivo si está inoperativa
detalle = ""

if estado == "Inoperativa":
    detalle = st.selectbox(
        "Motivo",
        ["Malograda", "Robada", "En mantenimiento", "Otro"]
    )

    if detalle == "Otro":
        detalle = st.text_input("Especificar motivo")

# =========================
# BOTÓN
# =========================

if st.button("Registrar"):

    # Validación básica
    if placa == "":
        st.warning("Ingresa la placa del vehículo")
    else:
        nueva_data = {
            "Fecha": [datetime.now()],
            "Tipo": [tipo_vehiculo],
            "Placa": [placa],
            "Estado": [estado],
            "Detalle": [detalle]
        }

        df_nuevo = pd.DataFrame(nueva_data)

        archivo = "vehiculos.xlsx"

        if os.path.exists(archivo):
            df_existente = pd.read_excel(archivo)
            df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
        else:
            df_final = df_nuevo

        df_final.to_excel(archivo, index=False)

        st.success("Registro guardado correctamente")

# =========================
# MOSTRAR DATA
# =========================

password = st.text_input(" ", type="password")

if password:
    if password == "068566":
        st.success("Acceso concedido")

        if st.button("Borrar registros"):
            if os.path.exists("vehiculos.xlsx"):
                os.remove("vehiculos.xlsx")
                st.success("Registros eliminados")
        if os.path.exists("vehiculos.xlsx"):
            st.subheader("Registros actuales")
            df = pd.read_excel("vehiculos.xlsx")
            st.dataframe(df)
    else:
        st.error("Clave incorrecta")
