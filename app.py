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

/* HIDE DEFAULT BUTTON LOOK */
div.stButton > button {
    height: 160px !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* CARD DESIGN */

.card {
    cursor: pointer;
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
}

/* ICONO */
.card-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

/* TITULO */
.card-title {
    font-weight: 700;
    font-size: 18px;
    color: #2c3e50;
}

/* SUBTITULO */
.card-sub {
    font-size: 14px;
    color: #666;
}

/* OPTIONAL: COLORED TOP BORDER (nice touch) */
.card:nth-child(1) { border-top: 4px solid #1f77b4; }
.card:nth-child(2) { border-top: 4px solid #dc3545; }
.card:nth-child(3) { border-top: 4px solid #ffc107; }
.card:nth-child(4) { border-top: 4px solid #6c757d; }

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

query_params = st.query_params

if "pagina" in query_params:
    st.session_state.pagina = query_params["pagina"]

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if st.session_state.pagina == "inicio":

    st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

# VEHICULOS
    with col1:
    if st.markdown("""
    <a href="?page=vehiculos" target="_self" style="text-decoration: none;">
        <div class="card">
            <div class="card-icon">1</div>
            <div class="card-title">Gestión de vehículos</div>
            <div class="card-sub">Registro y control de la flota vehicular</div>
        </div>
    </a>
    """, unsafe_allow_html=True):
        pass
        
# DEMORAS
    with col2:
        if st.button(" ", key="demoras", use_container_width=True):
            st.session_state.pagina = "demoras"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">2</div>
            <div class="card-title">Reportar demoras</div>
            <div class="card-sub">Incidencias operativas por factores externos</div>
        </div>
        """, unsafe_allow_html=True)
    
    # APARTADOS
    with col3:
        if st.button(" ", key="apartados", use_container_width=True):
            st.session_state.pagina = "apartados"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">3</div>
            <div class="card-title">Apartados postales</div>
            <div class="card-sub">Gestión de apartados por administración</div>
        </div>
        """, unsafe_allow_html=True)
    
    # NO DISTRIBUIBLES
    with col4:
        if st.button(" ", key="nodist", use_container_width=True):
            st.session_state.pagina = "nodist"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">4</div>
            <div class="card-title">No distribuibles</div>
            <div class="card-sub">Reporte de envíos no distribuibles</div>
        </div>
        """, unsafe_allow_html=True)
    
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
