import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* ===== FONDO ===== */
[data-testid="stAppViewContainer"] {
    background-image: url("https://webservice.serpost.com.pe/prj_online/Imagen/Seguimiento_Linea.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Make content appear above overlay */
[data-testid="stAppViewContainer"] > div {
    position: relative;
    z-index: 1;
}

/* ===== TITULOS ===== */
.titulo {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    text-align: center !important;
    margin-bottom: 10px !important;
    letter-spacing: 1px !important;
}

.sub {
    text-align: center !important;
    color: #dbe6ff !important;
    font-size: 18px !important;
    margin-bottom: 30px !important;
}

/* ===== MARKDOWN ===== */
h1, h2, h3, h4, h5, h6, p {
    color: #ffffff !important;
}

/* ===== BUTTON AS CARD ===== */

div.stButton > button {
    height: 200px;
    width: 90%;

    background: rgba(255,255,255,0.95);
    border-radius: 20px;
    border: none;

    box-shadow: 0 10px 30px rgba(0,0,0,0.25);

    font-weight: 600;
    font-size: 16px;
    color: #2c3e50;

    transition: all 0.25s ease;
    white-space: pre-line;

    padding: 20px;
}

/* ===== HOVER EFFECT (FIXED) ===== */
div.stButton > button:hover {
    background: rgba(255,255,255,0.95) !important; 
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
    }

/* ===== OPTIONAL: CENTER TEXT NICELY ===== */
div.stButton > button {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

/* ===== REMOVE STREAMLIT DEFAULT FOCUS BORDER ===== */
div.stButton > button:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.3);
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

# ===== SESSION STATE ===== #

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "inicio"
    
# ===== MAIN NAVIGATION ===== #

if st.session_state["pagina"] == "inicio":

    st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # VEHICULOS
    with col1:
        if st.button("🚚\n\nGestión de vehículos\nRegistro y control de la flota", 
                 key="vehiculos_btn", 
                 use_container_width=True):
            st.session_state["pagina"] = "vehiculos"
            st.rerun()
                     
    # DEMORAS
    with col2:
        if st.button("⏱️\n\nDemoras operativas\nIncidencias externas",
                key="demoras_btn",
                use_container_width=True):
            st.session_state["pagina"] = "demoras"
            st.rerun()

    # APARTADOS
    with col3:
        if st.button("📦\n\nApartados\nGestión de apartados",
                key="apartados_btn",
                use_container_width=True):
            st.session_state["pagina"] = "apartados"
            st.rerun()
        
    # NO DISTRIBUIBLES
    with col4:
        if st.button("⚠️\n\nNo distribuibles\nEnvíos no entregados",
                key="nodist_btn",
                use_container_width=True):
            st.session_state["pagina"] = "nodist"
            st.rerun()

# ===== MODULO VEHICULOS =====
elif st.session_state.pagina == "vehiculos":

    # subestado interno
    if "subvehiculos" not in st.session_state:
        st.session_state.subvehiculos = "menu"
        st.rerun()

    st.markdown("## 🚚 Módulo Vehículos")

    # MENU
    if st.session_state.subvehiculos == "menu":

        st.markdown("Seleccione una opción:")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Registrar vehículo", use_container_width=True):
                st.session_state.subvehiculos = "registro"
                st.rerun()

        with col2:
            if st.button("Reportar incidencia", use_container_width=True):
                st.session_state.subvehiculos = "incidencia"
                st.rerun()

    # REGISTRO
    elif st.session_state.subvehiculos == "registro":

        st.markdown("### 📝 Registro de vehículo")

        placa = st.text_input("Placa")
        tipo = st.selectbox("Tipo", ["Camión", "Van", "Auto"])
        capacidad = st.number_input("Capacidad (kg)", min_value=0)

        if st.button("Guardar"):
            st.success("Vehículo registrado")
            st.rerun()
            
        st.divider()

        col1, col2, col3 = st.columns([1, 2, 1])  # center it
    
        with col2:
            if st.button("← Volver al inicio"):
                st.session_state["pagina"] = "inicio"
                st.rerun()

    # INCIDENCIA
    elif st.session_state.subvehiculos == "incidencia":

        st.markdown("### ⚠️ Reporte de incidencia")

        placa = st.text_input("Placa")
        descripcion = st.text_area("Descripción")
        fecha = st.date_input("Fecha")

        if st.button("Enviar"):
            st.success("Incidencia registrada")
            st.rerun()

        if st.button("← Volver", key="volver_btn"):
            st.session_state.subvehiculos = "menu"
            st.rerun()

        st.divider()
    
        col1, col2, col3 = st.columns([1, 2, 1])  # center it
    
        with col2:
            if st.button("← Volver al inicio"):
                st.session_state["pagina"] = "inicio"
                st.rerun()

# ===== MODULO DEMORAS =====
elif st.session_state.pagina == "demoras":

    st.markdown("## ⏱️ Demoras operativas")

    st.markdown("Reporta problemas por clima, huaicos u otros eventos")

    st.link_button(
        "Ir al formulario",
        "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform"
    )

    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])  # center it
    
    with col2:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.rerun()

# ===== MODULO APARTADOS =====
elif st.session_state.pagina == "apartados":

    st.markdown("## 📦 Apartados postales")
    st.write("Módulo en construcción")

    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])  # center it
    
    with col2:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.rerun()

# ===== MODULO NO DISTRIBUIBLES =====
elif st.session_state.pagina == "nodist":

    st.markdown("## ⚠️ No distribuibles")
    st.write("Módulo en construcción")

    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])  # center it
    
    with col2:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.rerun()
