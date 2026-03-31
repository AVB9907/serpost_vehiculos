import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# UI

st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    text-align: center;
    transition: 0.2s;
}

.card:hover {
    transform: scale(1.03);
}

st.markdown("""
<style>
.titulo {
    font-size: 30px;
    font-weight: 700;
    color: #1f4e79;
    text-align: center;
    margin-bottom: 10px;
}

.sub {
    text-align: center;
    color: #6c757d;
    font-size: 18px;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button {
    height: 120px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    background-color: white;
    border: 1px solid #ddd;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    transition: 0.2s;
}

div.stButton > button:hover {
    background-color: #f0f4f8;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.boton-volver button {
    background-color: #28a745 !important;
    color: white !important;
    font-size: 14px !important;
    padding: 6px 16px !important;
    border-radius: 8px !important;
    border: none !important;
    width: auto !important;
}

.boton-volver button:hover {
    background-color: #218838 !important;
}
</style>
""", unsafe_allow_html=True)

# SUPABASE

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# USUARIOS

def login(usuario, password):
    res = supabase.table("usuarios").select("*").eq("usuario", usuario).eq("password", password).execute()
    return len(res.data) > 0

# SESSION STATE

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if st.session_state.pagina == "inicio":

    st.markdown('<p class="titulo">Administración de Canales - Serpost</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Vehículos", use_container_width=True):
            st.session_state.pagina = "vehiculos"
            st.rerun()

    with col2:
        if st.button("Demoras operativas", use_container_width=True):
            st.session_state.pagina = "demoras"
            st.rerun()

    with col3:
        if st.button("Apartados postales", use_container_width=True):
            st.session_state.pagina = "apartados"
            st.rerun()

    with col4:
        if st.button("No distribuibles", use_container_width=True):
            st.session_state.pagina = "nodist"
            st.rerun()
            
elif st.session_state.pagina == "vehiculos":

    st.markdown("## Módulo Vehículos")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Registrar vehículo"):
            st.session_state.pagina = "registro"
            st.rerun()

    with col2:
        if st.button("Reportar incidencia"):
            st.session_state.pagina = "incidencia"
            st.rerun()

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

elif st.session_state.pagina == "apartados":
    st.subheader("Apartados postales")
    st.write("Módulo en construcción")

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

elif st.session_state.pagina == "nodist":
    st.subheader("No distribuibles")
    st.write("Módulo en construcción")

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()
