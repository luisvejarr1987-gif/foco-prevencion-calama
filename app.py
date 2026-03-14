import streamlit as st
from datetime import datetime

# Configuración de la plataforma
st.set_page_config(page_title="Foco Prevención - Calama", page_icon="🛡️")

st.title("🛡️ Plataforma Foco Prevención")
st.write(f"**Gestión Técnica - Art. 15 Dec. 44** | Calama, {datetime.now().strftime('%d/%m/%Y')}")
st.divider()

# Formulario de entrada
with st.form("form_irl"):
    nombre = st.text_input("Nombre Completo del Trabajador")
    rut = st.text_input("RUT (ej: 12.345.678-9)")
    cargo = st.selectbox("Cargo / Puesto de Trabajo", ["Operador Maquinaria", "Conductor", "Supervisor", "Mecánico"])
    apto = st.checkbox("Certifico que el trabajador cuenta con salud compatible para el puesto.")
    
    generar = st.form_submit_button("GENERAR REGISTRO DIGITAL")

if generar:
    if nombre and rut and apto:
        st.success(f"✅ Registro procesado exitosamente para {nombre}")
        
        # Este es el contenido del documento legal
        acta_texto = f"""
        REGISTRO DE INSTRUCCIÓN DE RIESGOS (IRL) - ART. 15 DEC. 44
        -------------------------------------------------------
        FECHA: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        UBICACIÓN: Calama, Chile.
        
        DATOS DEL TRABAJADOR:
        Nombre: {nombre}
        RUT: {rut}
        Cargo: {cargo}
        
        CONTENIDO DE LA INSTRUCCIÓN:
        Peligros Detectados: Gran Altura Geográfica, Radiación UV.
        Medidas de Control: Uso de EPP, Hidratación constante, Control de signos.
        
        ESTADO DE SALUD: Certificado como Apto para Faena.
        -------------------------------------------------------
        Validado por: Beatriz - Risk Preventionist
        """
        
        # AQUÍ APARECE EL BOTÓN PARA DESCARGAR EL ARCHIVO
        st.download_button(
            label="📥 DESCARGAR ACTA (TXT)",
            data=acta_texto,
            file_name=f"IRL_{nombre.replace(' ', '_')}.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Error: Debe completar todos los campos y validar la salud del trabajador.")
