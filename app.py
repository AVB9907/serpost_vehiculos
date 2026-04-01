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

/* BUTTON LAYER (CLICKABLE) */
div.stButton > button {
    height: 180px;
    background: rgba(255,255,255,0.95);
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    font-weight: 600;
    font-size: 16px;
    color: #2c3e50;
    transition: all 0.25s ease;
    white-space: pre-line; /* IMPORTANT for line breaks */
}

div.stButton > button:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
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

# ===== SESSION STATE ===== #

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "inicio"
    
# ===== MAIN NAVIGATION ===== #

if st.session_state["pagina"] == "inicio":

    st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # ===== VEHICULOS =====
    with col1:
        if st.button("🚚\n\nGestión de vehículos\nRegistro y control de la flota", 
                 key="vehiculos_btn", 
                 use_container_width=True):
        st.session_state["pagina"] = "vehiculos"
                     
    # ===== DEMORAS =====
    with col2:
        if st.button(" ", key="demoras_btn", use_container_width=True):
            st.session_state["pagina"] = "demoras"

        st.markdown("""
        <div class="card">
            <div class="card-icon">⏱️</div>
            <div class="card-title">Demoras operativas</div>
            <div class="card-sub">Incidencias externas</div>
        </div>
        """, unsafe_allow_html=True)

    # ===== APARTADOS =====
    with col3:
        if st.button(" ", key="apartados_btn", use_container_width=True):
            st.session_state["pagina"] = "apartados"

        st.markdown("""
        <div class="card">
            <div class="card-icon">📦</div>
            <div class="card-title">Apartados</div>
            <div class="card-sub">Gestión de apartados</div>
        </div>
        """, unsafe_allow_html=True)

    # ===== NO DISTRIBUIBLES =====
    with col4:
        if st.button(" ", key="nodist_btn", use_container_width=True):
            st.session_state["pagina"] = "nodist"

        st.markdown("""
        <div class="card">
            <div class="card-icon">⚠️</div>
            <div class="card-title">No distribuibles</div>
            <div class="card-sub">Envíos no entregados</div>
        </div>
        """, unsafe_allow_html=True)

# ===== VEHICULOS (WITH SUBMENU) =====
elif st.session_state.pagina == "vehiculos":

    # subestado interno
    if "subvehiculos" not in st.session_state:
        st.session_state.subvehiculos = "menu"

    st.markdown("## 🚚 Módulo Vehículos")

    # ===== MENU =====
    if st.session_state.subvehiculos == "menu":

        st.markdown("Seleccione una opción:")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Registrar vehículo", use_container_width=True):
                st.session_state.subvehiculos = "registro"

        with col2:
            if st.button("Reportar incidencia", use_container_width=True):
                st.session_state.subvehiculos = "incidencia"

    # ===== REGISTRO =====
    elif st.session_state.subvehiculos == "registro":

        st.markdown("### 📝 Registro de vehículo")

        placa = st.text_input("Placa")
        tipo = st.selectbox("Tipo", ["Camión", "Van", "Auto"])
        capacidad = st.number_input("Capacidad (kg)", min_value=0)

        if st.button("Guardar"):
            st.success("Vehículo registrado")

        if st.button("← Volver"):
            st.session_state.subvehiculos = "menu"

    # ===== INCIDENCIA =====
    elif st.session_state.subvehiculos == "incidencia":

        st.markdown("### ⚠️ Reporte de incidencia")

        placa = st.text_input("Placa")
        descripcion = st.text_area("Descripción")
        fecha = st.date_input("Fecha")

        if st.button("Enviar"):
            st.success("Incidencia registrada")

        if st.button("← Volver"):
            st.session_state.subvehiculos = "menu"

    st.divider()

    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"
        st.session_state.subvehiculos = "menu"


# ===== DEMORAS =====
elif st.session_state.pagina == "demoras":

    st.markdown("## ⏱️ Demoras operativas")

    st.markdown("Reporta problemas por clima, huaicos u otros eventos")

    st.link_button(
        "Ir al formulario",
        "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform"
    )

    st.divider()

    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"


# ===== APARTADOS =====
elif st.session_state.pagina == "apartados":

    st.markdown("## 📦 Apartados postales")
    st.write("Módulo en construcción")

    st.divider()

    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"


# ===== NO DISTRIBUIBLES =====
elif st.session_state.pagina == "nodist":

    st.markdown("## ⚠️ No distribuibles")
    st.write("Módulo en construcción")

    st.divider()

    if st.button("← Volver al inicio"):
        st.session_state.pagina = "inicio"
