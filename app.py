import streamlit as st
from datetime import datetime
from supabase import create_client

# =========================
# CONEXIÓN SUPABASE
# =========================

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# TÍTULO
# =========================

st.title("Registro de Vehículos - Serpost")

# =========================
# INPUTS
# =========================

administracion = st.selectbox(
    "Administración",
    [
        "ABANCAY","AREQUIPA","AYACUCHO","BREÑA","CAJAMARCA","CALLAO",
        "CERRO DE PASCO","CHACHAPOYAS","CHICLAYO","CHIMBOTE","CHOSICA",
        "COMAS","CUSCO","HUACHO","HUANCAVELICA","HUANCAYO","HUÁNUCO",
        "HUARAZ","ICA","INGENIERÍA","IQUITOS","JESÚS MARÍA","JULIACA",
        "LA VICTORIA","LIMA","LINCE","MIRAFLORES","MOQUEGUA","PIURA",
        "PUCALLPA","PUERTO MALDONADO","PUNO","TACNA","TARAPOTO",
        "TRUJILLO","TUMBES","VMT"
    ]
)

tipo_vehiculo = st.selectbox(
    "Tipo de vehículo",
    ["MOTO", "BICICLETA", "CAMIONETA"]
)

placa = st.text_input("Placa del vehículo")

estado = st.selectbox(
    "Estado del vehículo",
    ["Operativa", "Inoperativa"]
)

detalle = ""

if estado == "Inoperativa":
    detalle = st.selectbox(
        "Motivo",
        ["Malograda", "Robada", "En mantenimiento", "Otro"]
    )

    if detalle == "Otro":
        detalle = st.text_input("Especificar motivo")

# =========================
# BOTÓN GUARDAR
# =========================

if st.button("Registrar"):

    if placa == "":
        st.warning("Ingresa la placa del vehículo")
    else:
        data = {
            "fecha": str(datetime.now()),
            "administracion": administracion,
            "tipo": tipo_vehiculo,
            "placa": placa,
            "estado": estado,
            "detalle": detalle
        }

        try:
            supabase.table("vehiculos").insert(data).execute()
            st.success("Registro guardado en la nube")
        except Exception as e:
            st.error(f"Error al guardar: {e}")

# =========================
# PANEL ADMIN
# =========================

password = st.text_input(" ", type="password")

if password:
    if password == "068566":
        st.success("Acceso concedido")

        # Obtener datos
        response = supabase.table("vehiculos").select("*").execute()

        if response.data:
            st.subheader("Registros actuales")
            st.dataframe(response.data)

        # Botón borrar TODO
        if st.button("Borrar registros"):
            supabase.table("vehiculos").delete().neq("id", 0).execute()
            st.success("Todos los registros eliminados")

    else:
        st.error("Clave incorrecta")
