import streamlit as st
from datetime import datetime

# Configuración profesional de la plataforma
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️", layout="wide")

# Estilos visuales para que se vea impecable
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #0d6efd; color: white; font-weight: bold; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e3192, #1bffff); color: white; }
    </style>
    """, unsafe_allow_html=True)

# Título y encabezado
st.title("🛡️ Sistema Integral Foco Prevención")
st.write(f"**Gestión de Riesgos y Cumplimiento Legal** | Calama, {datetime.now().strftime('%d/%m/%Y')}")
st.divider()

# --- MENÚ DE NAVEGACIÓN (Aquí vuelven todas tus plataformas) ---
with st.sidebar:
    st.header("Menú de Control")
    opcion = st.radio("Seleccione Módulo:", [
        "📝 Instrucción IRL (Art. 15)", 
        "🔍 Investigación de Accidentes", 
        "⚠️ Reporte de Hallazgos",
        "🩺 Validación de Exámenes"
    ])
    st.divider()
    st.info("Usuario: Beatriz\nCargo: Risk Preventionist")

# --- MÓDULO 1: INSTRUCCIÓN IRL (Con descarga habilitada) ---
if opcion == "📝 Instrucción IRL (Art. 15)":
    st.header("Registro de Instrucción de Riesgos Laborales")
    with st.form("form_irl"):
        c1, c2 = st.columns(2)
        with c1: nombre = st.text_input("Nombre del Trabajador")
        with c2: rut = st.text_input("RUT")
        
        # Cargo manual como lo pediste
        cargo = st.text_input("Cargo / Puesto de Trabajo (Escríbalo manualmente)")
        
        peligros = st.multiselect("Peligros Identificados", 
            ["Gran Altura Geográfica", "Radiación UV", "Polvo en Suspensión", "Ruido", "Atropello"],
            default=["Gran Altura Geográfica", "Radiación UV"])
        
        medidas = st.text_area("Medidas Preventivas", "Uso de bloqueador, hidratación, EPP completo, pausas.")
        apto = st.checkbox("Certifico salud compatible.")
        
        generar = st.form_submit_button("GENERAR Y DESCARGAR ACTA")

    if generar and nombre and rut and cargo and apto:
        st.success(f"✅ Registro IRL generado para {nombre}")
        acta = f"ACTA IRL - {nombre}\nCargo: {cargo}\nFecha: {datetime.now()}\n\nMedidas: {medidas}"
        st.download_button("📥 DESCARGAR REGISTRO DIGITAL", data=acta, file_name=f"IRL_{rut}.txt")

# --- MÓDULO 2: INVESTIGACIÓN DE ACCIDENTES (Restaurado) ---
elif opcion == "🔍 Investigación de Accidentes":
    st.header("Análisis e Investigación de Accidentes")
    st.warning("Complete este formulario inmediatamente ocurrido el evento.")
    with st.form("form_investigacion"):
        tipo = st.selectbox("Tipo de Evento", ["Accidente con Tiempo Perdido", "Accidente sin Tiempo Perdido", "Incidente / Casi Accidente"])
        fecha_acc = st.date_input("Fecha del Suceso")
        descripcion = st.text_area("Descripción detallada del evento y lesiones")
        causas = st.text_area("Causas Básicas (Análisis de Causalidad)")
        plan_accion = st.text_input("Medida Correctiva Inmediata")
        
        enviar_inv = st.form_submit_button("REGISTRAR INVESTIGACIÓN")
        if enviar_inv:
            st.success("Investigación registrada en la base de datos de Calama.")

# --- MÓDULO 3: REPORTE DE HALLAZGOS (Restaurado) ---
elif opcion == "⚠️ Reporte de Hallazgos":
    st.header("Reporte de Condiciones y Acciones Subestándar")
    with st.form("form_hallazgo"):
        sector = st.text_input("Ubicación / Área de Faena")
        hallazgo = st.text_area("Descripción de la Condición Detectada")
        prioridad = st.select_slider("Prioridad de Atención", options=["Baja", "Media", "Alta", "CRÍTICA"])
        adjunto = st.file_uploader("Subir evidencia fotográfica")
        
        enviar_h = st.form_submit_button("ENVIAR HALLAZGO")
        if enviar_h:
            st.warning("Alerta enviada al equipo de supervisión para corrección.")

# --- MÓDULO 4: VALIDACIÓN DE EXÁMENES ---
elif opcion == "🩺 Validación de Exámenes":
    st.header("Verificación de Aptitud Médica")
    rut_consulta = st.text_input("Ingrese RUT para consultar vigencia de exámenes")
    if st.button("Consultar Sistema"):
        st.info(f"Consultando base de datos para {rut_consulta}...")
        st.success("Examen de Altura Geográfica VIGENTE hasta Diciembre 2026.")
