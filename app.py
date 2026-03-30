import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# =========================
# CONEXIÓN SUPABASE
# =========================

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# ESTADO DE NAVEGACIÓN
# =========================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    
if st.session_state.pagina == "inicio":

    st.title("Sistema Logístico - Serpost")

    st.markdown("### Selecciona una opción")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Registrar vehículo", use_container_width=True):
            st.session_state.pagina = "registro"

    with col2:
        if st.button("Reportar incidencia", use_container_width=True):
            st.session_state.pagina = "incidencia"

    with col3:
        if st.button("Reportar demoras", use_container_width=True):
            st.session_state.pagina = "demoras"
elif st.session_state.pagina == "registro":

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

    campos_completos = all([
        placa.strip() != "",
        oficina.strip() != "",
        (estado == "Operativa") or (detalle.strip() != "")
    ])

    if not campos_completos:
        st.warning("Completa todos los campos")

    if st.button("Registrar vehículo"):

        if not campos_completos:
            st.error("Faltan campos")
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

    # BOTÓN VOLVER
    if st.button("Volver"):
        st.session_state.pagina = "inicio"

elif st.session_state.pagina == "incidencia":

    st.subheader("Reporte de incidencia")

    placa = st.text_input("Placa del vehículo").upper()

    tipo_incidente = st.selectbox(
        "Tipo de incidencia",
        ["Malograda", "Robada", "En mantenimiento", "Otro"]
    )

    detalle = tipo_incidente

    if tipo_incidente == "Otro":
        detalle = st.text_input("Especificar incidencia")

    campos_completos = all([
        placa.strip() != "",
        detalle.strip() != ""
    ])

    if not campos_completos:
        st.warning("Completa todos los campos")

    if st.button("Reportar incidencia"):

        if not campos_completos:
            st.error("Faltan campos")
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

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
elif st.session_state.pagina == "demoras":

    st.subheader("Demoras operativas")

    st.markdown("Reporta problemas por clima, huaicos u otros eventos")

    st.link_button(
        "Ir al formulario de demoras",
        "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform?usp=sharing&ouid=109605618064294682889"
    )

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
