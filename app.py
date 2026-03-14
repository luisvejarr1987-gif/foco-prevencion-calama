import streamlit as st
from datetime import datetime

# Configuración profesional
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️")

st.title("🛡️ Plataforma Foco Prevención")
st.write(f"**Gestión Técnica de Riesgos** | Calama, {datetime.now().strftime('%d/%m/%Y')}")
st.divider()

# Formulario Completo
with st.form("form_irl"):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre Completo del Trabajador")
    with col2:
        rut = st.text_input("RUT (ej: 12.345.678-9)")
    
    # CARGO LIBRE: Aquí tú puedes escribir el cargo manualmente
    cargo = st.text_input("Cargo / Puesto de Trabajo (Escríbalo aquí)")
    
    st.subheader("Análisis de Riesgos")
    # Volvemos a poner los Peligros
    peligros = st.multiselect("Peligros Identificados", 
        ["Gran Altura Geográfica", "Radiación UV", "Polvo en Suspensión", "Tránsito Vehicular", "Uso de Herramientas"],
        default=["Gran Altura Geográfica", "Radiación UV"])
    
    # Volvemos a poner las Medidas
    medidas = st.text_area("Medidas de Control Aplicadas", 
        "Uso de EPP, Hidratación constante, Control de signos vitales, Pausas activas.")
    
    apto = st.checkbox("Certifico que el trabajador cuenta con salud compatible para el puesto.")
    
    generar = st.form_submit_button("GENERAR REGISTRO Y ACTIVAR DESCARGA")

if generar:
    if nombre and rut and cargo and apto:
        st.success(f"✅ Registro procesado para {nombre} ({cargo})")
        
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
        Peligros: {', '.join(peligros)}
        Medidas: {medidas}
        
        ESTADO: Salud Compatible Validada.
        ---------------------------------------
        Emitido por: Beatriz - Risk Preventionist
        """
        
        st.download_button(
            label="📥 DESCARGAR ACTA OFICIAL (TXT)",
            data=acta_texto,
            file_name=f"IRL_{nombre.replace(' ', '_')}.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Falta información: Asegúrate de escribir el Cargo y marcar la casilla de salud.")
