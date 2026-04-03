import streamlit as st
from datetime import datetime
from supabase import create_client

# SESSION USER

if "user" not in st.session_state:
    st.session_state.user = None

    st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>

/* BOTON VOLVER */

div[data-testid="stForm"] {
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
}

/* FIJADO */
.volver-fixed {
    position: fixed;
    top: 80px;        
    left: 20px;       
    z-index: 9999;
}

.volver-fixed button {
    background-color: #0ea5e9 !important; 
    color: white !important;
    border: none !important;
    padding: 8px 14px !important;
    font-size: 14px !important;
    border-radius: 10px !important;
    cursor: pointer;
}

/* BOTONES DE FORM (LOGIN + VOLVER) */
div[data-testid="stForm"] button {
    background-color: transparent !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 8px 16px !important;
    font-size: 14px !important;
}

/* QUITAR EFECTOS DE TEMA */
div[data-testid="stForm"] button:focus,
div[data-testid="stForm"] button:active {
    outline: none !important;
    box-shadow: none !important;
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
    font-size: 25px;
}

/* 🔥 CARDS NIVEL DIOS */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div.stButton > button {

    height: 200px !important;
    border-radius: 22px !important;

    display: flex !important;
    flex-direction: column !important;
    align-items: center;
    justify-content: center;

    gap: 12px;

    font-size: 20px !important;
    font-weight: 600;

    color: white !important;

    border: 1px solid rgba(255,255,255,0.15) !important;

    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);

    box-shadow: 0 10px 30px rgba(0,0,0,0.35);

    transition: all 0.25s ease;

    position: relative;
    overflow: hidden;
}

/* BRILLO INTERNO */
div[data-testid="stHorizontalBlock"] div.stButton > button::before {
    content: "";
    position: absolute;
    width: 120%;
    height: 120%;
    background: radial-gradient(circle, rgba(255,255,255,0.15), transparent 60%);
    top: -20%;
    left: -20%;
    opacity: 0;
    transition: 0.3s;
}

/* HOVER PRO */
div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}

div[data-testid="stHorizontalBlock"] div.stButton > button:hover::before {
    opacity: 1;
}

/* COLORES PRO TRANSPARENTES */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background: linear-gradient(135deg, rgba(16,185,129,0.85), rgba(4,120,87,0.85)) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background: linear-gradient(135deg, rgba(245,158,11,0.85), rgba(180,83,9,0.85)) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
    background: linear-gradient(135deg, rgba(99,102,241,0.85), rgba(55,48,163,0.85)) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(4) button {
    background: linear-gradient(135deg, rgba(239,68,68,0.85), rgba(153,27,27,0.85)) !important;
}

/* EFECTO GLOW ABAJO */
div[data-testid="stHorizontalBlock"] div.stButton > button::after {
    content: "";
    position: absolute;
    bottom: 12px;
    width: 40%;
    height: 4px;
    border-radius: 10px;
    background: rgba(255,255,255,0.6);
    opacity: 0.6;
}

/* CERRAR SESION */
div.stButton:nth-of-type(1) > button {
    background-color: #0ea5e9 !important;   
    box-shadow: inset 0 0 0 1px rgba(14,165,233,0.3);
}

""", unsafe_allow_html=True)

# SUPABASE

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# INGRESAR

if st.session_state.user is None:

    st.markdown('<p class="titulo">INICIAR SESIÓN</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        with st.form("login_form"):
            usuario = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")

            submitted = st.form_submit_button("Ingresar")

            if submitted:
                res = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()

                if len(res.data) > 0:
                    user = res.data[0]

                    if user["password"] == password:
                        st.session_state.user = user
                        st.rerun()
                    else:
                        st.error("Contraseña incorrecta")
                else:
                    st.error("Usuario no existe")
# APP

else:

    st.sidebar.write(f"{st.session_state.user['usuario']}")
    
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.user = None
        st.rerun()
    
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

# MODULOS

    elif st.session_state.pagina == "vehiculos":
        
        st.markdown("## Módulo Vehículos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Registrar vehículo", use_container_width=True):
                st.session_state.pagina = "registro"
                st.rerun()
        
        with col2:
            if st.button("Reportar incidencia", use_container_width=True):
                st.session_state.pagina = "incidencia"
                st.rerun()
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.pagina == "demoras":
        
        st.markdown("## Demoras Operativas")
        st.markdown("Reporta problemas por clima, huaicos u otros eventos")
        
        st.link_button(
            "Ir al formulario de demoras",
            "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform?usp=sharing"
        )
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "apartados":
        
        st.markdown("## Apartados Postales")
        st.write("Módulo en construcción")
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "nodist":
        
        st.markdown("## Envíos no distribuibles")
        st.write("Módulo en construcción")
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
