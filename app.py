import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>

/* ===== FONDO ===== */
[data-testid="stAppViewContainer"] {
    background-image: url("https://webservice.serpost.com.pe/prj_online/Imagen/Seguimiento_Linea.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* ===== TITULOS ===== */
.titulo {
    font-size: 40px;
    font-weight: 800;
    color: #f0f0f0;
    text-align: center;
    margin-bottom: 30px;
}

.sub {
    text-align: center;
    color: #f0f0f0;
    font-size: 20px;
}

/* ===== CARD BASE ===== */
.card {
    background: rgba(255,255,255,0.95);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: all 0.25s ease;
    cursor: pointer;
}

/* ===== HOVER ===== */
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
}

/* ===== ICON ===== */
.card-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

/* ===== TEXT ===== */
.card-title {
    font-weight: 700;
    font-size: 18px;
    color: #2c3e50;
}

.card-sub {
    font-size: 14px;
    color: #666;
}

/* ===== LINK FIX ===== */
a {
    text-decoration: none !important;
    color: inherit !important;
}

/* ===== REMOVE STREAMLIT BUTTON STYLE ===== */
div.stButton > button {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
}

/* MAKE BUTTON INVISIBLE BUT CLICKABLE */
div.stButton > button {
    height: 160px;
    opacity: 0;
    position: absolute;
    z-index: 2;
}

/* CARD */
.card {
    position: relative;
    z-index: 1;
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

# Default page
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# Sync with URL (only if exists)
if "pagina" in st.query_params:
    st.session_state.pagina = st.query_params["pagina"]

col1, col2, col3, col4 = st.columns(4)

    # ===== VEHICULOS =====
    with col1:
        if st.button("vehiculos", key="vehiculos_btn", use_container_width=True):
            st.session_state.pagina = "vehiculos"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">🚚</div>
            <div class="card-title">Gestión de vehículos</div>
            <div class="card-sub">Registro y control de la flota vehicular</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ===== DEMORAS =====
    with col2:
        if st.button("demoras", key="demoras_btn", use_container_width=True):
            st.session_state.pagina = "demoras"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">⏱️</div>
            <div class="card-title">Reportar demoras</div>
            <div class="card-sub">Incidencias operativas</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ===== APARTADOS =====
    with col3:
        if st.button("apartados", key="apartados_btn", use_container_width=True):
            st.session_state.pagina = "apartados"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">📦</div>
            <div class="card-title">Apartados postales</div>
            <div class="card-sub">Gestión de apartados</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ===== NO DISTRIBUIBLES =====
    
    with col4:
        if st.button("nodist", key="nodist_btn", use_container_width=True):
            st.session_state.pagina = "nodist"
            st.rerun()
    
        st.markdown("""
        <div class="card">
            <div class="card-icon">⚠️</div>
            <div class="card-title">No distribuibles</div>
            <div class="card-sub">Envíos no entregados</div>
        </div>
        """, unsafe_allow_html=True)
    
# MÓDULO VEHICULOS

elif st.session_state.pagina == "vehiculos":

    st.markdown("## 🚚 Módulo Vehículos")

    st.markdown("Seleccione una opción:")

    col1, col2 = st.columns(2)

    # ===== REGISTRAR VEHÍCULO =====
    with col1:
        if st.button("Registrar vehículo", use_container_width=True):
            st.session_state.pagina = "registro_vehiculo"
            st.rerun()

    # ===== REPORTAR INCIDENCIA =====
    with col2:
        if st.button("Reportar incidencia", use_container_width=True):
            st.session_state.pagina = "incidencia"
            st.rerun()

    st.divider()

    # ===== BOTÓN VOLVER =====
    if st.button("← Volver"):
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
