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

st.title("Sistema de Vehículos - Serpost")

# =========================
# MENÚ
# =========================

opcion = st.sidebar.selectbox(
    "Menú",
    ["Registrar vehículo", "Reportar incidencia"]
)

# =========================
# REGISTRAR VEHÍCULO
# =========================

if opcion == "Registrar vehículo":

    st.subheader("Registro de vehículo")

    placa = st.text_input("Placa del vehículo").upper()

    tipo_vehiculo = st.selectbox(
        "Tipo de vehículo",
        ["MOTO", "CAMIONETA"]
    )

    administracion = st.selectbox(
        "Administración",
        [
            "ABANCAY","AREQUIPA","AYACUCHO","BREÑA","CAJAMARCA","CALLAO",
            "CERRO DE PASCO","CHACHAPOYAS","CHICLAYO","CHIMBOTE","CHOSICA",
            "COMAS","CUSCO","HUACHO","HUANCAVELICA","HUANCAYO","HUANUCO",
            "HUARAZ","ICA","INGENIERIA","IQUITOS","JESUS MARIA","JULIACA",
            "LA VICTORIA","LIMA","LINCE","MIRAFLORES","MOQUEGUA","PIURA",
            "PUCALLPA","PUERTO MALDONADO","PUNO","TACNA","TARAPOTO",
            "TRUJILLO","TUMBES","VMT"
        ]
    )

    oficina = st.text_input("Oficina / Sede específica")

    # =========================
    # ESTADO DEL VEHÍCULO
    # =========================

    estado = st.selectbox(
        "Estado del vehículo",
        ["Operativa", "Inoperativa"]
    )

    detalle = ""

    if estado == "Inoperativa":
        detalle = st.selectbox(
            "Motivo",
            ["Malograda", "Robada", "En reparación", "Otro"]
        )

        if detalle == "Otro":
            detalle = st.text_input("Especificar motivo")

    # =========================
    # VALIDACIÓN
    # =========================

    campos_completos = all([
        placa.strip() != "",
        oficina.strip() != "",
        (estado == "Operativa") or (detalle.strip() != "")
    ])

    if not campos_completos:
        st.warning("Completa todos los campos antes de registrar")

    # =========================
    # BOTÓN
    # =========================

    if st.button("Registrar vehículo"):

        if not campos_completos:
            st.error("Faltan campos obligatorios")
        else:
            data = {
                "placa": placa,
                "tipo": tipo_vehiculo,
                "administracion": administracion,
                "oficina": oficina,
                "estado": estado,
                "detalle": detalle,
                "fecha": str(datetime.now())
            }

            try:
                supabase.table("vehiculos").insert(data).execute()
                st.success("Vehículo registrado correctamente")
            except Exception as e:
                st.error(f"Error: {e}")

# =========================
# REPORTAR INCIDENCIA
# =========================

elif opcion == "Reportar incidencia":

    st.subheader("Reporte de incidencia")

    placa = st.text_input("Placa del vehículo").upper()

    tipo_incidente = st.selectbox(
        "Tipo de incidencia",
        ["Malograda", "Robada", "En mantenimiento", "Otro"]
    )

    detalle = tipo_incidente

    if tipo_incidente == "Otro":
        detalle = st.text_input("Especificar incidencia")

    # =========================
    # VALIDACIÓN
    # =========================

    campos_completos = all([
        placa.strip() != "",
        detalle.strip() != ""
    ])

    if not campos_completos:
        st.warning("Completa todos los campos antes de reportar")

    # =========================
    # BOTÓN
    # =========================

    if st.button("Reportar incidencia"):

        if not campos_completos:
            st.error("Faltan campos obligatorios")
        else:
            data = {
                "placa": placa,
                "tipo_incidente": tipo_incidente,
                "detalle": detalle,
                "fecha": str(datetime.now())
            }

            try:
                supabase.table("reportes").insert(data).execute()
                st.success("Incidencia registrada correctamente")
            except Exception as e:
                st.error(f"Error: {e}")
