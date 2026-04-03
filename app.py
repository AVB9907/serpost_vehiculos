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

/* SIDEBAR BASE */
section[data-testid="stSidebar"] {
    background: rgba(43,45,66,0.95) !important;  /* tu índigo */
}

/* TEXTO SIDEBAR */
section[data-testid="stSidebar"] * {
    color: #edf2f4 !important;  /* platinum */
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

/* CARDS NIVEL DIOS */
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

/* HOVER PRO */
div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}

/* INDIGO PRO */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background: #2b2d42b3 !important;

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.15) !important;

    box-shadow:
        inset 0 0 20px rgba(43,45,66,0.5),
        0 10px 30px rgba(0,0,0,0.3);
}

/* LAVENDER GREY PRO */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background: #8d99aeb3 !important;

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.15) !important;

    box-shadow:
        inset 0 0 20px rgba(141,153,174,0.5),
        0 10px 30px rgba(0,0,0,0.3);
}

/* PLATINUM PRO */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
    background: #edf2f4b3 !important;

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.3) !important;

    box-shadow:
        inset 0 0 25px rgba(237,242,244,0.7),
        0 10px 30px rgba(0,0,0,0.25);

    color: #2b2d42 !important;
}

/* PUNCH RED PRO */
div[data-testid="stHorizontalBlock"] > div:nth-child(4) button {
    background: #ef233c !important;

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.15) !important;

    box-shadow:
        inset 0 0 20px rgba(239,35,60,0.5),
        0 10px 30px rgba(0,0,0,0.3);
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

    st.sidebar.write(f"{st.session_state.user['usuario']}")

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

        st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Gestión de vehículos"):
                st.session_state.pagina = "vehiculos"
                st.session_state.subpagina = "menu"
                st.rerun()

        with col2:
            if st.button("Reportar demoras"):
                st.session_state.pagina = "demoras"
                st.rerun()

        with col3:
            if st.button("Apartados postales"):
                st.session_state.pagina = "apartados"
                st.rerun()

        with col4:
            if st.button("No distribuibles"):
                st.session_state.pagina = "nodist"
                st.rerun()

    # ======================
    # VEHICULOS
    # ======================
    elif st.session_state.pagina == "vehiculos":

        if st.session_state.subpagina == "menu":

            st.markdown("## Módulo Vehículos")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Registrar vehículo"):
                    st.session_state.subpagina = "registro"
                    st.rerun()

            with col2:
                if st.button("Reportar incidencia"):
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
                        st.error("❌ Esta placa ya existe")
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

                st.success("Vehículo registrado 🚀")

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

                    st.success("Incidencia registrada 🚨")

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
    # OTROS
    # ======================
    elif st.session_state.pagina == "apartados":

        st.markdown("## Apartados Postales")

        with st.form("volver_apartados"):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()

    elif st.session_state.pagina == "nodist":

        st.markdown("## No distribuibles")

        with st.form("volver_nodist"):
            if st.form_submit_button("← Volver"):
                st.session_state.pagina = "inicio"
                st.rerun()
