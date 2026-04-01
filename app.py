import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>

/* FONDO */
[data-testid="stAppViewContainer"] {
    background-image: url("https://webservice.serpost.com.pe/prj_online/Imagen/Seguimiento_Linea.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* TÍTULO */
.titulo {
    font-size: 40px !important;
    font-weight: 800 !important;
    color: #f0f0f0 !important;
    text-align: center !important;
    margin-bottom: 30px !important;
}

/* SUBTÍTULO */
.sub {
    text-align: center;
    color: #f0f0f0 !important;
    font-size: 20px !important;
}

/* BOTONES GRANDES */
div.stButton > button {
    height: 140px !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    border-radius: 16px !important;
    background-color: white !important;
    border: 1px solid #e0e0e0 !important;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08) !important;
    transition: all 0.2s ease;
}

/*COLORES DE MODULOS*/

div.stButton > button {
    border: none !important;
    border-radius: 10px !important;
    background-color: #ffffff !important;
    transition: all 0.2s ease-in-out;
}

div.stButton:nth-of-type(1) > button {
    box-shadow: 0 0 0 2px rgba(31,119,180,0.15) !important;
}

div.stButton:nth-of-type(2) > button {
    box-shadow: 0 0 0 2px rgba(220,53,69,0.15);
}

div.stButton:nth-of-type(3) > button {
    box-shadow: 0 0 0 2px rgba(255,193,7,0.2);
}

div.stButton:nth-of-type(4) > button {
    box-shadow: 0 0 0 2px rgba(108,117,125,0.2);
}

/* HOVER */
div.stButton > button:hover {
    transform: scale(1.02);
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

    st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Gestión de vehículos", use_container_width=True):
            st.session_state.pagina = "vehiculos"
            st.rerun()

    with col2:
        if st.button("Reportar demoras", use_container_width=True):
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

# MÓDULO VEHICULOS

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

    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()
            
# MÓDULO DEMORAS OPERATIVAS

elif st.session_state.pagina == "demoras":

    st.subheader("Demoras operativas")

    st.markdown("Reporta problemas por clima, huaicos u otros eventos")

    st.link_button(
        "Ir al formulario de demoras",
        "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform?usp=sharing"
    )

    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()

# MÓDULO APARTADOS

elif st.session_state.pagina == "apartados":
    st.subheader("Apartados postales")
    st.write("Módulo en construcción")

    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()
# MÓDULO NO DISTRIBUIBLES

elif st.session_state.pagina == "nodist":
    st.subheader("No distribuibles")
    st.write("Módulo en construcción")
    
    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()
