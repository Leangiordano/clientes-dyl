import streamlit as st
import urllib.parse

# Configuración responsive para celulares
st.set_page_config(page_title="Clientes DyL", page_icon="🖨️", layout="centered")

st.title("🖨️ Clientes DyL")
st.caption("Prospección y generación de propuestas 3D")

# 1. Filtros de Búsqueda
st.subheader("1. Buscar Prospectos")
zona = st.selectbox("Zona", ["CABA", "Zona Sur - Avellaneda", "Zona Sur - Quilmes", "Zona Sur - Lanús / Lomas"])
rubro = st.selectbox("Rubro Objetivo", ["Estudios de Arquitectura", "Talleres Mecánicos", "Agencias / Merchandising", "Locales de Regalería"])

# 2. Base de datos simulada de ejemplo (se puede conectar a la API de Google Maps)
base_ejemplos = [
    {
        "nombre": "Pallone Arquitectura",
        "zona": "CABA",
        "rubro": "Estudios de Arquitectura",
        "tel": "5491154016796",
        "direccion": "Puerto Madero, CABA",
        "pitch": "Hola! Vimos sus proyectos. En DyL hacemos maquetas volumétricas y prototipado 3D de alta precisión. ¿Les gustaría recibir una muestra sin cargo?"
    },
    {
        "nombre": "Taller Mecánico GOE",
        "zona": "Zona Sur - Avellaneda",
        "rubro": "Talleres Mecánicos",
        "tel": "541123614453",
        "direccion": "Av. Roca 997, Avellaneda",
        "pitch": "Hola! En DyL fabricamos repuestos discontinuados, bujes y soportes plásticos en 3D (PETG/ABS) para talleres. ¿Podemos enviarles un catálogo?"
    },
    {
        "nombre": "Agencia Chula",
        "zona": "Zona Sur - Quilmes",
        "rubro": "Agencias / Merchandising",
        "tel": "541135835438",
        "direccion": "Brandsen 368, Quilmes",
        "pitch": "Hola! En DyL desarrollamos merchandising 3D, llaveros con QR e identificadores corpóreos para marcas. ¿Te muestro algunos ejemplos?"
    }
]

# Filtrar resultados
resultados = [c for c in base_ejemplos if c["zona"] == zona and c["rubro"] == rubro]

st.subheader("2. Prospectos Encontrados")

if resultados:
    for cli in resultados:
        with st.container(border=True):
            st.markdown(f"**{cli['nombre']}**")
            st.caption(f"📍 {cli['direccion']}")
            
            # Edición rápida de propuesta antes de enviar
            mensaje = st.text_area("Mensaje a enviar:", value=cli['pitch'], key=cli['nombre'], height=100)
            
            # Botón directo para abrir WhatsApp App en el celular
            link_wa = f"https://api.whatsapp.com/send?phone={cli['tel']}&text={urllib.parse.quote(mensaje)}"
            
            st.link_button("📲 Enviar Propuesta por WhatsApp", link_wa, use_container_width=True)
else:
    st.info("No hay clientes en esta categoría en la base demostrativa. Agregá tu clave de Google Places para traer resultados en vivo.")
