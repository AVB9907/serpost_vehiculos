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
    font-size: 25px;
}

/* BOTONES GRANDES */

div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div.stButton > button {

    width: 100% !important;
    height: 140px !important;

    display: flex !important;
    align-items: center;
    justify-content: center;

    font-size: 18px !important;
    font-weight: 600;

    border: 1px solid #e5e7eb; 
    background-color: #0ea5e9 !important;   

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

""", unsafe_allow_html=True)

# SUPABASE

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# LOGIN

if st.session_state.user is None:

    st.markdown('<p class="titulo">INICIAR SESIÓN</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("Ingresar"):
            
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

    st.sidebar.write(f"👤 {st.session_state.user['usuario']}")
    
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
        
        col_volver, _ = st.columns([1,10])
        
        with col_volver:
            st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
        
            if st.button("← Volver"):
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
        
        col_volver, _ = st.columns([1,10])
        
        with col_volver:
            st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
        
            if st.button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
        
            st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "apartados":
        
        st.markdown("## Apartados Postales")
        st.write("Módulo en construcción")
        
        col_volver, _ = st.columns([1,10])
        
        with col_volver:
            st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
        
            if st.button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
        
            st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "nodist":
        
        st.markdown("## Envíos no distribuibles")
        st.write("Módulo en construcción")
        
        col_volver, _ = st.columns([1,10])
        
        with col_volver:
            st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
        
            if st.button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
        
            st.markdown('</div>', unsafe_allow_html=True)
