import streamlit as st
from datetime import datetime

# Configuración profesional
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️", layout="wide")

# Título
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

# --- MÓDULO 1: INSTRUCCIÓN IRL (Con Lista de Riesgos Solicitada) ---
if opcion == "📝 Instrucción IRL (Art. 15)":
    st.header("Registro de Instrucción de Riesgos Laborales")
    with st.form("form_irl"):
        c1, c2 = st.columns(2)
        with c1: nombre = st.text_input("Nombre del Trabajador")
        with c2: rut = st.text_input("RUT")
        
        cargo = st.text_input("Cargo / Puesto de Trabajo (Escriba manualmente)")
        
        st.subheader("Selección de Riesgos (Tickear los que apliquen)")
        # Lista completa de riesgos que me pediste
        lista_riesgos = [
            "Caída al mismo nivel", "Exposición a ruido", "Humos metálicos", 
            "Humos de soldadura", "Exposición radiación UV", "Proyección de partícula", 
            "Riesgo psicosocial", "Trastornos musculoesqueléticos", "Caída distinto nivel", 
            "Arco por soldadura", "Interacción hombre máquina", "Atrapamiento", 
            "Aprisionamiento", "Corte", "Carga suspendidas", "Resbalamiento", 
            "Golpeado por", "Corte por hoja", "Riesgo de incendio", "Shock eléctrico"
        ]
        
        riesgos_seleccionados = st.multiselect("Riesgos Identificados:", lista_riesgos)
        
        otros_riesgos = st.text_input("Otros riesgos no listados (opcional):")
        
        medidas = st.text_area("Medidas Preventivas Sugeridas", 
            "Uso de EPP completo, Hidratación constante, Bloqueador solar, Pausas activas, Inspección de herramientas.")
            
        apto = st.checkbox("Certifico que el trabajador cuenta con salud compatible para el puesto.")
        
        generar = st.form_submit_button("GENERAR Y DESCARGAR ACTA")

    if generar and nombre and rut and riesgos_seleccionados and apto:
        st.success(f"✅ Registro IRL generado para {nombre}")
        
        # Combinar riesgos de la lista con los manuales
        todos_los_riesgos = ", ".join(riesgos_seleccionados)
        if otros_riesgos:
            todos_los_riesgos += f", {otros_riesgos}"
        
        # Formato del acta para descarga
        acta_texto = f"""
        REGISTRO DE INSTRUCCIÓN DE RIESGOS (IRL)
        ---------------------------------------
        FECHA: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        UBICACIÓN: Calama, Antofagasta.
        
        DATOS DEL TRABAJADOR:
        Nombre: {nombre}
        RUT: {rut}
        Cargo: {cargo}
        
        RIESGOS IDENTIFICADOS (TICKEO):
        {todos_los_riesgos}
        
        MEDIDAS DE CONTROL APLICADAS:
        {medidas}
        
        VALIDACIÓN:
        El trabajador ha sido instruido sobre los riesgos y medidas de control.
        Estado: Salud Compatible Validada.
        ---------------------------------------
        Emitido por: Beatriz - Risk Preventionist
        """
        
        st.download_button(
            label="📥 DESCARGAR ACTA OFICIAL",
            data=acta_texto,
            file_name=f"IRL_{rut}.txt",
            mime="text/plain"
        )
    elif generar:
        st.error("⚠️ Falta información crítica (Nombre, RUT, Riesgos o Salud).")

# --- Mantenemos los otros módulos sin cambios para no borrar nada ---
elif opcion == "🔍 Investigación de Accidentes":
    st.header("Análisis e Investigación de Accidentes")
    st.info("Módulo operativo para reporte de eventos.")

elif opcion == "⚠️ Reporte de Hallazgos":
    st.header("Reporte de Hallazgos en Terreno")

elif opcion == "🩺 Validación de Exámenes":
    st.header("Verificación de Aptitud Médica")
