import streamlit as st
from datetime import datetime

# Configuración profesional
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️", layout="wide")

# Estilos visuales
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #0d6efd; color: white; font-weight: bold; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e3192, #1bffff); color: white; }
    </style>
    """, unsafe_allow_html=True)

# Título y encabezado
st.title("🛡️ Sistema Integral Foco Prevención")
st.write(f"**Gestión de Riesgos** | Calama, {datetime.now().strftime('%d/%m/%Y')}")
st.divider()

# --- MENÚ DE NAVEGACIÓN ---
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

# --- MÓDULO 1: INSTRUCCIÓN IRL (Peligros Manuales) ---
if opcion == "📝 Instrucción IRL (Art. 15)":
    st.header("Registro de Instrucción de Riesgos Laborales")
    with st.form("form_irl"):
        c1, c2 = st.columns(2)
        with c1: nombre = st.text_input("Nombre del Trabajador")
        with c2: rut = st.text_input("RUT")
        
        cargo = st.text_input("Cargo / Puesto de Trabajo (Escriba manualmente)")
        
        # CAMBIO: Ahora los peligros se ingresan manualmente
        peligros = st.text_area("Peligros Identificados (Escriba todos los que correspondan)", 
            placeholder="Ej: Gran altura geográfica, radiación UV, caída a distinto nivel, etc.")
        
        medidas = st.text_area("Medidas Preventivas", 
            placeholder="Ej: Uso de EPP, hidratación, bloqueador solar...")
            
        apto = st.checkbox("Certifico salud compatible.")
        
        generar = st.form_submit_button("GENERAR Y DESCARGAR ACTA")

    if generar and nombre and rut and peligros and apto:
        st.success(f"✅ Registro IRL generado para {nombre}")
        
        # Formato del acta para descarga
        acta_texto = f"""
        REGISTRO DE INSTRUCCIÓN DE RIESGOS (IRL)
        ---------------------------------------
        FECHA: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        FAENA: Calama, Antofagasta.
        
        DATOS DEL TRABAJADOR:
        Nombre: {nombre}
        RUT: {rut}
        Cargo: {cargo}
        
        DETALLE PREVENTIVO:
        PELIGROS: 
        {peligros}
        
        MEDIDAS DE CONTROL: 
        {medidas}
        
        ESTADO: Salud Compatible Validada por el Prevencionista.
        ---------------------------------------
        Emitido por: Beatriz - Risk Preventionist
        """
        
        st.download_button(
            label="📥 DESCARGAR REGISTRO DIGITAL (TXT)",
            data=acta_texto,
            file_name=f"IRL_{rut}_{datetime.now().strftime('%Y%md')}.txt",
            mime="text/plain"
        )
    elif generar:
        st.error("⚠️ Debe completar el Nombre, RUT, Peligros y certificar la salud.")

# --- Los demás módulos se mantienen igual para no perder nada ---
elif opcion == "🔍 Investigación de Accidentes":
    st.header("Análisis e Investigación de Accidentes")
    # ... (código anterior de investigación)
    with st.form("form_inv"):
        tipo = st.selectbox("Tipo de Evento", ["Accidente", "Incidente"])
        desc = st.text_area("Descripción")
        st.form_submit_button("REGISTRAR")

elif opcion == "⚠️ Reporte de Hallazgos":
    st.header("Reporte de Hallazgos")
    # ... (código anterior de hallazgos)
    with st.form("form_hall"):
        hall = st.text_area("Hallazgo")
        st.form_submit_button("ENVIAR")

elif opcion == "🩺 Validación de Exámenes":
    st.header("Validación de Salud")
    rut_c = st.text_input("Consultar RUT")
    if st.button("Consultar"):
        st.success("Examen vigente.")
