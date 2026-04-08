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

/* USERNAME */
.sidebar-user {
    text-align: left !important;
    font-weight: 600;
    font-size: 15px;
    padding: 6px 10px;
    margin-bottom: 10px;
}

/* TÍTULOS */
div[data-testid="stMarkdownContainer"] h2 {
    color: #f0f0f0 !important;
    text-align: center !important;
    font-size: 40px !important;
    font-weight: 800 !important;
}

/* TEXTO */
div[data-testid="stMarkdownContainer"] p {
    color: #f0f0f0 !important;
    font-size: 20px !important;
    text-align: center !important;
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

/* SIDEBAR BASE */
section[data-testid="stSidebar"] {
    background: rgba(43,45,66,0.95) !important; 
}

/* TEXTO SIDEBAR */
section[data-testid="stSidebar"] * {
    color: #edf2f4 !important;  
}

/* BOTÓN SIDEBAR */
section[data-testid="stSidebar"] button {
    background-color: rgba(141,153,174,0.2) !important;
    color: #edf2f4 !important;
    border-radius: 8px !important;
}

/* HOVER */
section[data-testid="stSidebar"] button:hover {
    background-color: rgba(141,153,174,0.4) !important;
}

/* FONDO */
[data-testid="stAppViewContainer"] {
    background-image: url("https://webservice.serpost.com.pe/prj_online/Imagen/Seguimiento_Linea.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* HOVER */
div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}

/* BOTONES */
div[data-testid="stHorizontalBlock"] div.stButton > button {
    width: 100% !important;
    height: 220px !important;

    border-radius: 22px !important;

    display: flex !important;
    align-items: center;
    justify-content: center;

    font-size: 20px !important;
    font-weight: 600;
}

/* VEHICULOS */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button {
    background: #2b2d42cc !important;
}

/* DEMORAS */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button {
    background: #8d99aecc !important;
}

/* APARTADOS */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div.stButton > button {
    background: #edf2f4cc !important;
    color: #2b2d42 !important;
}

/* NO DISTRIBUIBLES */
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div.stButton > button {
    background: #ef233ccc !important;
}

/* HOVER PRO NIVEL EMPRESA */
div[data-testid="stHorizontalBlock"] div.stButton > button {
    transition: all 0.25s ease !important;
    position: relative;
    overflow: hidden;
}

/* ELEVACIÓN */
div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}

/* EFECTO GLOW SUAVE */
div[data-testid="stHorizontalBlock"] div.stButton > button::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top, rgba(255,255,255,0.25), transparent 60%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

div[data-testid="stHorizontalBlock"] div.stButton > button:hover::before {
    opacity: 1;
}

/* BRILLO EN MOVIMIENTO */
div[data-testid="stHorizontalBlock"] div.stButton > button::after {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        120deg,
        transparent,
        rgba(255,255,255,0.2),
        transparent
    );
    transform: rotate(25deg);
    opacity: 0;
    transition: opacity 0.3s ease;
}

div[data-testid="stHorizontalBlock"] div.stButton > button:hover::after {
    opacity: 1;
}

""", unsafe_allow_html=True)

# ======================
# SESSION USER
# ======================
if "user" not in st.session_state:
    st.session_state.user = None

# ======================
# SUPABASE
# ======================
SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ======================
# LOGIN
# ======================
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

# ======================
# APP
# ======================
else:

    st.sidebar.markdown(
    f'<div class="sidebar-user">{st.session_state.user["usuario"]}</div>',
    unsafe_allow_html=True
)

    if st.sidebar.button("Cerrar sesión"):
        st.session_state.user = None
        st.rerun()

    # ======================
    # SESSION STATE
    # ======================
    if "pagina" not in st.session_state:
        st.session_state.pagina = "inicio"

    if "subpagina" not in st.session_state:
        st.session_state.subpagina = "menu"

    ADMINISTRACIONES = [
        "ABANCAY","AREQUIPA","AYACUCHO","BREÑA","CAJAMARCA","CALLAO",
        "CERRO DE PASCO","CHACHAPOYAS","CHICLAYO","CHIMBOTE","CHOSICA",
        "COMAS","CUSCO","HUACHO","HUANCAVELICA","HUANCAYO","HUANUCO",
        "HUARAZ","ICA","INGENIERIA","IQUITOS","JESUS MARIA","JULIACA",
        "LA VICTORIA","LIMA","LINCE","MIRAFLORES","MOQUEGUA","PIURA",
        "PUCALLPA","PUERTO MALDONADO","PUNO","TACNA","TARAPOTO",
        "TRUJILLO","TUMBES","VMT"
    ]

    # ======================
    # INICIO
    # ======================
    if st.session_state.pagina == "inicio":

        st.markdown("## ADMINISTRACIÓN DE CANALES")
        st.write("Seleccione un módulo")
        st.markdown('<div class="modulos">', unsafe_allow_html=True)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            if st.button("Gestión de vehículos", use_container_width=True):
                st.session_state.pagina = "vehiculos"
                st.session_state.subpagina = "menu"
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
                
        with col5:
                    if st.button("REGISTRO TERCEROS", use_container_width=True):
                        st.session_state.pagina = "RT"
                        st.rerun()

        
        st.markdown('</div>', unsafe_allow_html=True)
        
    # ======================
    # VEHICULOS
    # ======================
    elif st.session_state.pagina == "vehiculos":

        if st.session_state.subpagina == "menu":

            st.markdown("## Módulo Vehículos")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Registrar vehículo", use_container_width=True):
                    st.session_state.subpagina = "registro"
                    st.rerun()

            with col2:
                if st.button("Reportar incidencia", use_container_width=True):
                    st.session_state.subpagina = "incidencia"
                    st.rerun()

            with st.form("volver_main"):
                if st.form_submit_button("← Volver"):
                    st.session_state.pagina = "inicio"
                    st.rerun()

        elif st.session_state.subpagina == "registro":

            st.markdown("## Registrar vehículo")

            tipo = st.selectbox("Tipo", ["Moto", "Camioneta", "Bicicleta"])

            if tipo != "Bicicleta":
                placa = st.text_input("Placa")
            else:
                placa = "SIN-PLACA"

            administracion = st.selectbox("Administración", ADMINISTRACIONES)
            oficina = st.text_input("Oficina")
            estado = st.selectbox("Estado", ["Operativo","En mantenimiento","Fuera de servicio"])
            detalle = st.text_area("Detalle")

            disabled = False
            if tipo != "Bicicleta" and not placa:
                disabled = True
            if not oficina:
                disabled = True

            if st.button("Registrar", disabled=disabled):

                if tipo != "Bicicleta":
                    existente = supabase.table("vehiculos").select("*").eq("placa", placa).execute()
                    if len(existente.data) > 0:
                        st.error("Esta placa ya existe")
                        st.stop()

                supabase.table("vehiculos").insert({
                    "placa": placa,
                    "tipo": tipo,
                    "administracion": administracion,
                    "oficina": oficina,
                    "estado": estado,
                    "detalle": detalle,
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }).execute()

                st.success("Vehículo registrado")

            with st.form("volver_reg"):
                if st.form_submit_button("← Volver"):
                    st.session_state.subpagina = "menu"
                    st.rerun()

        elif st.session_state.subpagina == "incidencia":

            st.markdown("## Reportar incidencia")

            vehiculos = supabase.table("vehiculos").select("placa").execute()
            placas = [v["placa"] for v in vehiculos.data]

            if not placas:
                st.warning("No hay vehículos registrados")
            else:
                placa = st.selectbox("Placa", placas)
                tipo = st.selectbox("Tipo", ["Falla","Accidente","Retraso","Otro"])
                detalle = st.text_area("Detalle")

                if st.button("Reportar"):
                    supabase.table("reportes").insert({
                        "placa": placa,
                        "tipo_incidente": tipo,
                        "detalle": detalle,
                        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }).execute()

                    st.success("Incidencia registrada")

            with st.form("volver_inc"):
                if st.form_submit_button("← Volver"):
                    st.session_state.subpagina = "menu"
                    st.rerun()

    # ======================
    # DEMORAS
    # ======================
    elif st.session_state.pagina == "demoras":

        st.markdown("## Demoras Operativas")

        st.link_button(
            "Ir al formulario",
            "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform"
        )

        with st.form("volver_demoras"):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()

    # ======================
    # APARTADOS
    # ======================
    
    elif st.session_state.pagina == "apartados":

        st.markdown("## Apartados Postales")

        with st.form("volver_apartados"):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
                
    # ======================
    # NO DISTRIBUIBLES
    # ======================

    elif st.session_state.pagina == "nodist":

        st.markdown("## No distribuibles")

        with st.form("volver_nodist"):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()

    # ======================
    # REPORTE TERCEROS
    # ======================

  elif st.session_state.pagina == "nodist":

        st.markdown("## REPORTE TERCEROS")

        with st.form(""):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
