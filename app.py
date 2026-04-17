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

/* TEMP */

div.stButton > button {
    line-height: 1.6;
    white-space: pre-line;
    text-align: center;
}

div.stButton > button span {
    display: inline-block;
}

/* PRIMERA LÍNEA (título) */
div.stButton > button::first-line {
    font-size: 22px;
    font-weight: 700;
}

/* SEGUNDA LÍNEA (descripción simulada) */
div.stButton > button {
    font-size: 15px;
    font-weight: 400;
}

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
    
    transform: translateX(10px);
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

/* TABS */
div[data-testid="stRadio"] {
    display: flex;
    justify-content: center !important;
}

/* OPCIONES */
div[role="radiogroup"] {
    justify-content: center !important;
    gap: 30px;
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
    background: #0A2540CC !important;
}

/* DEMORAS */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button {
    background: #2B4F7CCC !important;
}

/* APARTADOS */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div.stButton > button {
    background: #D6DEE9CC !important;
    color: #2b2d42 !important;
}

/* NO DISTRIBUIBLES */
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div.stButton > button {
    background: #E6C9A8CC !important;
}

/* REGISTRO TERCEROS */
div[data-testid="stHorizontalBlock"] > div:nth-child(5) div.stButton > button {
    background: #A80E1ACC !important;  /* pick any color */
}

/* HOVER */
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

div.stButton > button {
    line-height: 1.4;
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
        
                    if user["cambiar_password"]:
                        st.session_state.pagina = "cambiar_password"
                    else:
                        st.session_state.pagina = "inicio"
        
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
        
        col1, col2, col3 = st.columns([2.8,2,2])

        with col2:
            vista = st.radio(
                "",
                ["Operación", "Dashboards"],
                horizontal=True
        )
    
        if vista == "Operación":
            
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                if st.button("Gestión de vehículos",use_container_width=True):
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
                        if st.button("Registro terceros", use_container_width=True):
                            st.session_state.pagina = "RT"
                            st.rerun()
        elif vista == "Dashboards":

            st.markdown("## Centro de Control")

            tab1, tab2, tab3 = st.tabs([
                "Backlog",
                "Envíos OPV",
                "Operaciones"
            ])

            with tab1:
                st.components.v1.iframe(
                    "https://datastudio.google.com/embed/reporting/99cc086d-b857-4291-8666-6f2b69437467/page/QvNcE",
                    height=1000
                )
                        
            st.markdown('</div>', unsafe_allow_html=True)
            
    # ======================
    # CONTRASEÑAS
    # ======================      
    
    elif st.session_state.pagina == "cambiar_password":

        import time
    
        st.markdown("## Cambiar contraseña")
    
        with st.form("form_password"):
    
            nueva = st.text_input("Nueva contraseña", type="password")
            confirmar = st.text_input("Confirmar contraseña", type="password")
    
            submitted = st.form_submit_button("Guardar")
    
            if submitted:
                if nueva != confirmar:
                    st.error("Las contraseñas no coinciden")
    
                elif len(nueva) < 6:
                    st.error("Mínimo 6 caracteres")
    
                else:
                    supabase.table("usuarios").update({
                        "password": nueva,
                        "cambiar_password": False
                    }).eq("id", st.session_state.user["id"]).execute()
    
                    st.success("Contraseña actualizada correctamente")
    
                    time.sleep(1)
    
                    st.session_state.pagina = "inicio"
                    st.rerun()
                    
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
    
        st.markdown(
            """
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdCh7MQIHQ0npFOWVksEj58awAu19bXg_Fl78_oP6WRwpepGA/viewform?usp=header"
            width="100%"
            height="800"
            frameborder="0"
            marginheight="0"
            marginwidth="0">
            </iframe>
            """,
            unsafe_allow_html=True
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
    
            st.markdown("## No Distribuibles")
        
            from datetime import datetime
        
            MOTIVOS = [
                "AUSENTE",
                "DIRECCIÓN ERRADA",
                "NO RECLAMADO",
                "DEFICIENTE",
                "OTROS"
            ]
        
            with st.form("form_nodist"):
        
                col1, col2 = st.columns(2)
        
                with col1:
                    admin = st.selectbox("Administración", ADMINISTRACIONES)
                    codigo = st.text_input("Código de envío")
                    destinatario = st.text_input("Destinatario")
        
                with col2:
                    direccion = st.text_input("Dirección")
                    motivo = st.selectbox("Motivo", MOTIVOS)
                    fecha = st.date_input("fecha")
        
                obs = st.text_area("Observaciones")
        
                submitted = st.form_submit_button("Registrar")
        
                if submitted:
        
                    if not codigo:
                        st.error("El código es obligatorio")
                        st.stop()
        
                    existe = supabase.table("no_distribuibles") \
                        .select("codigo_envio") \
                        .eq("codigo_envio", codigo) \
                        .execute()
        
                    if existe.data:
                        st.warning("Este envío ya fue registrado")
                        st.stop()
        
                    supabase.table("no_distribuibles").insert({
                        "administracion": admin,
                        "codigo_envio": codigo.strip(),
                        "destinatario": destinatario.strip(),
                        "direccion": direccion.strip(),
                        "motivo": motivo,
                        "fecha": str(fecha),
                        "observacion": obs.strip(),
                        "usuario": st.session_state.user["usuario"],
                    }).execute()
        
                    st.success("Registro guardado correctamente")
        
            with st.form("volver_nodist"):
                if st.form_submit_button("← Volver"):
                    st.session_state.pagina = "inicio"
                    st.rerun()
                    
    # ======================
    # REPORTE TERCEROS
    # ======================

    elif st.session_state.pagina == "RT":
    
            import pandas as pd
        
            st.markdown("## Registro de terceros")
        
            data = supabase.table("REPORTE_TERCEROS").select("*").execute().data
        
            if not data:
                st.warning("No hay datos cargados en BD_TERCEROS")
        
            else:
                df = pd.DataFrame(data)
        
                administraciones = sorted(df["ADMINISTRACIÓN"].dropna().unique())
        
                meses = [
                    "Enero","Febrero","Marzo","Abril","Mayo","Junio",
                    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
                ]
        
                with st.form("registro_terceros"):
        
                    admin_sel = st.selectbox("Administración", administraciones)
        
                    personas = df[df["ADMINISTRACIÓN"] == admin_sel]["APELLIDOS Y NOMBRES"].dropna().unique()
                    persona_sel = st.selectbox("Seleccionar persona", sorted(personas))
        
                    mes_sel = st.selectbox("Mes", meses)
        
                    monto = st.number_input("Monto", min_value=0.0, step=10.0)
        
                    submitted = st.form_submit_button("Registrar")
        
                    if submitted:
                        if monto <= 0:
                            st.error("Ingrese un monto válido")
                        else:
                            supabase.table("bd_gastos").insert({
                                "administracion": admin_sel,
                                "nombre": persona_sel,
                                "mes": mes_sel,
                                "monto": monto
                            }).execute()
        
                            st.success("Registro guardado correctamente")
        
            with st.form("volver_main"):
                    if st.form_submit_button("← Volver"):
                        st.session_state.pagina = "inicio"
                        st.rerun()
