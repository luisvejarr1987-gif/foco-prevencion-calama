import streamlit as st
from datetime import datetime

# Configuración técnica de la plataforma
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️", layout="centered")

# Estilos visuales
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Plataforma Foco Prevención")
st.write(f"**Gestión Técnica de Riesgos Laborales** | Calama, {datetime.now().year}")
st.divider()

# Menú de navegación lateral
menu = st.sidebar.selectbox("Seleccione Módulo", [
    "Instrucción IRL (Art. 15 Dec. 44)", 
    "Reporte de Condiciones Subestándar",
    "Validación de Exámenes Médicos"
])

# --- MÓDULO 1: INSTRUCCIÓN DE RIESGOS (IRL) ---
if menu == "Instrucción IRL (Art. 15 Dec. 44)":
    st.header("📝 Registro de Instrucción IRL")
    st.info("Este registro da cumplimiento al Artículo 15 del Decreto 44.")
    
    with st.form("form_irl"):
        nombre = st.text_input("Nombre Completo del Trabajador")
        rut = st.text_input("RUT (ej: 12.345.678-9)")
        cargo = st.selectbox("Cargo / Puesto de Trabajo", ["Operador Maquinaria", "Conductor Liviano", "Supervisor", "Mecánico", "Eléctrico"])
        
        st.subheader("Peligros Identificados en Calama")
        peligros = st.multiselect("Seleccione Peligros", 
            ["Gran Altura Geográfica", "Radiación UV", "Polvo en Suspensión", "Tránsito Vehicular", "Uso de Herramientas"],
            default=["Gran Altura Geográfica", "Radiación UV"])
            
        medidas = st.text_area("Medidas de Control Aplicadas", "Uso de EPP, Hidratación constante, Control de signos vitales, Pausas activas.")
        
        apto = st.checkbox("Certifico que el trabajador cuenta con salud compatible para el puesto.")
        
        submitted = st.form_submit_button("GENERAR REGISTRO DIGITAL")
        
        if submitted:
            if nombre and rut and apto:
                st.success(f"✅ Registro IRL generado exitosamente para {nombre}.")
                st.balloons()
                # Aquí se puede agregar la lógica para guardar en Google Sheets
            else:
                st.error("⚠️ Error: Debe completar todos los campos y validar la aptitud de salud.")

# --- MÓDULO 2: REPORTE DE HALLAZGOS ---
elif menu == "Reporte de Condiciones Subestándar":
    st.header("⚠️ Reporte de Hallazgos en Terreno")
    with st.form("form_hallazgo"):
        descripcion = st.text_area("Descripción de la Condición Detectada")
        ubicacion = st.text_input("Sector / Área de la Faena")
        gravedad = st.select_slider("Nivel de Riesgo", options=["Bajo", "Medio", "Alto", "Crítico"])
        foto = st.file_uploader("Subir evidencia fotográfica", type=["jpg", "png"])
        
        enviar = st.form_submit_button("ENVIAR ALERTA DE SEGURIDAD")
        
        if enviar:
            st.warning(f"Notificación de riesgo {gravedad} enviada al equipo de supervisión.")

# --- MÓDULO 3: VALIDACIÓN DE SALUD ---
elif menu == "Validación de Exámenes Médicos":
    st.header("🩺 Control de Aptitud Médica")
    st.write("Verificación de exámenes para trabajos en Gran Altura Geográfica.")
    
    trabajador_busqueda = st.text_input("Ingrese RUT para verificar vigencia")
    if st.button("Consultar Base de Datos"):
        # Simulación de respuesta de base de datos
        st.write(f"Estado del trabajador {trabajador_busqueda}: **VIGENTE** hasta 15/12/2026")
        st.success("Apto para trabajar sobre los 3.000 msnm.")

st.sidebar.divider()
st.sidebar.write(f"**Usuario:** Beatriz - Risk Preventionist")
st.sidebar.caption("Plataforma protegida bajo estándares de la Ley 16.744")
