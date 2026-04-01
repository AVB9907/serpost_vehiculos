import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>
div.volver-btn button {
    background-color: black !important;
    color: #94a3b8 !important;
    border: none !important;
    font-size: 14px !important;
    padding: 6px 8px !important;
}

/* Hover */
.volver-btn button:hover {
    color: #0ea5e9 !important;
    background-color: rgba(14,165,233,0.1) !important;
}

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

/* TÍTULOS DENTRO DE LOS MÓDULOS */
h2 {
    color: #f0f0f0 !important;
}

/* TEXTOS EN GENERAL */
p {
    color: #f0f0f0 !important;
    font-size: 14px;
}

/* BOTONES GRANDES */

div.stButton > button {
    width: 100% !important;
    height: 140px !important; 
    border-radius: 16px !important;

    display: flex !important;
    align-items: center;
    justify-content: center;

    font-size: 18px !important;
    font-weight: 600;

    border: 1px solid #e5e7eb; 
    background-color: transparent !important;   

    transition: all 0.25s ease;
}

/*HOVER*/
div.stButton > button:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
}

/*MODULOS*/
div.stButton:nth-of-type(1) > button {
    border-top: 5px solid #0ea5e9 !important;
    box-shadow: inset 0 0 0 1px rgba(14,165,233,0.3);
}

div.stButton:nth-of-type(2) > button {
    border-top: 5px solid #f43f5e !important;
    box-shadow: inset 0 0 0 1px rgba(244,63,94,0.3);
}

div.stButton:nth-of-type(3) > button {
    border-top: 5px solid #facc15 !important;
    box-shadow: inset 0 0 0 1px rgba(250,204,21,0.4);
}

div.stButton:nth-of-type(4) > button {
    border-top: 5px solid #334155 !important;
    box-shadow: inset 0 0 0 1px rgba(51,65,85,0.4);
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
        st.markdown('<div class="volver-btn">', unsafe_allow_html=True)

        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
    
# MÓDULO DEMORAS OPERATIVAS

elif st.session_state.pagina == "demoras":

    st.markdown("## Demoras Operativas")

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
    st.markdown("## Apartados Postales")
    st.write("Módulo en construcción")

    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()
# MÓDULO NO DISTRIBUIBLES

elif st.session_state.pagina == "nodist":
    st.markdown("## Envíos no distribuibles")
    st.write("Módulo en construcción")
    
    col1, col2 = st.columns([1,10])
    
    with col1:
        if st.button("← Volver", help="Volver"):
            st.session_state.pagina = "inicio"
            st.rerun()
