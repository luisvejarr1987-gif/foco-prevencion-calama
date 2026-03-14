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

# --- MÓDULO 1: INSTRUCCIÓN IRL ---
if opcion == "📝 Instrucción IRL (Art. 15)":
    st.header("Registro de Instrucción de Riesgos Laborales")
    with st.form("form_irl"):
        c1, c2 = st.columns(2)
        with c1: nombre = st.text_input("Nombre del Trabajador")
        with c2: rut = st.text_input("RUT")
        
        cargo = st.text_input("Cargo / Puesto de Trabajo")
        
        # --- SECCIÓN DE RIESGOS ---
        st.subheader("1. Selección de Riesgos (Tickear)")
        lista_riesgos = [
            "Caída al mismo nivel", "Exposición a ruido", "Humos metálicos", 
            "Humos de soldadura", "Exposición radiación UV", "Proyección de partícula", 
            "Riesgo psicosocial", "Trastornos musculoesqueléticos", "Caída distinto nivel", 
            "Arco por soldadura", "Interacción hombre máquina", "Atrapamiento", 
            "Aprisionamiento", "Corte", "Carga suspendidas", "Resbalamiento", 
            "Golpeado por", "Corte por hoja", "Riesgo de incendio", "Shock eléctrico"
        ]
        riesgos_sel = st.multiselect("Riesgos Identificados:", lista_riesgos)
        
        # --- SECCIÓN DE MEDIDAS (Nueva lista solicitada) ---
        st.subheader("2. Medidas Preventivas (Tickear)")
        lista_medidas = [
            "Uso del bloqueador solar", "Uso de guante apropiado para la actividad", 
            "Uso del respirador 2 vías con filtro mixto", "Uso del protector auditivo", 
            "Atento a las condiciones del entorno", "No exponer extremidades a la línea de fuego", 
            "No exponerse a la línea de fuego", "Uso de careta de soldador", 
            "Uso de careta facial", "Uso de lentes apropiados", 
            "No levantar pesos superiores a 25 kg hombres y 20 kg mujeres", 
            "No usar teléfono al subir o bajar por las escalas", 
            "Solo personal autorizado podrá intervenir tableros", 
            "Choque", "Colisión", "Atropello"
        ]
        medidas_sel = st.multiselect("Medidas de Control Aplicadas:", lista_medidas)
        
        # Espacio manual por si falta algo
        otros_detalles = st.text_input("Otras observaciones o medidas adicionales:")
        
        apto = st.checkbox("Certifico que el trabajador cuenta con salud compatible para el puesto.")
        
        generar = st.form_submit_button("GENERAR Y DESCARGAR ACTA")

    if generar and nombre and rut and riesgos_sel and medidas_sel and apto:
        st.success(f"✅ Registro IRL generado para {nombre}")
        
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
        
        RIESGOS IDENTIFICADOS:
        {", ".join(riesgos_sel)}
        
        MEDIDAS DE CONTROL COMPROMETIDAS:
        {", ".join(medidas_sel)}
        
        OBSERVACIONES ADICIONALES:
        {otros_detalles if otros_detalles else "Ninguna."}
        
        VALIDACIÓN LEGAL:
        El trabajador declara haber recibido instrucción sobre los riesgos 
        y medidas preventivas (Art. 15 Dec. 44).
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
        st.error("⚠️ Error: Debe completar Nombre, RUT, seleccionar al menos un Riesgo, una Medida y marcar la casilla de Salud.")

# --- Módulos restantes (se mantienen igual) ---
elif opcion == "🔍 Investigación de Accidentes":
    st.header("Análisis e Investigación de Accidentes")

elif opcion == "⚠️ Reporte de Hallazgos":
    st.header("Reporte de Hallazgos en Terreno")

elif opcion == "🩺 Validación de Exámenes":
    st.header("Verificación de Aptitud Médica")
