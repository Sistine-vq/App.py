import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN BÁSICA ---
st.set_page_config(page_title="Elecciones Perú 2026", page_icon="🇵🇪", layout="wide")

st.title("🇵🇪 Análisis de las Elecciones Presidenciales del Perú 2026")
st.write("""
Esta aplicación presenta información **real y actualizada (2025)** sobre las próximas elecciones generales del Perú.  
Se incluyen datos de intención de voto, confianza ciudadana y contexto político según **Infobae, Reuters, Ipsos y Freedom House**.
""")

# --- DATOS GENERALES ---
st.header("📆 Datos Generales de las Elecciones")
info = {
    "Fecha de Elecciones": ["12 de abril de 2026"],
    "Cargos a Elegir": ["Presidente, 130 diputados y 60 senadores"],
    "Desaprobación del Gobierno (marzo 2025)": ["93 %"],
    "Ciudadanos que no confían en los candidatos": ["84 %"],
    "Número estimado de postulantes": ["40 - 50 candidatos"]
}
df_info = pd.DataFrame(info)
st.table(df_info)

# --- DATOS DE INTENCIÓN DE VOTO ---
st.header("📊 Principales Candidatos y Nivel de Apoyo (2025)")
data = {
    "Candidato": [
        "Rafael López Aliaga",
        "Keiko Fujimori",
        "Carlos Álvarez",
        "Alfonso López Chau",
        "César Acuña"
    ],
    "Partido": [
        "Renovación Popular",
        "Fuerza Popular",
        "País para Todos",
        "Ahora Nación",
        "Alianza para el Progreso"
    ],
    "Intención de Voto (%)": [11, 10, 7, 4, 3],
    "Fuente": [
        "Reuters / Ipsos (2025)",
        "Infobae (2025)",
        "Infobae (2025)",
        "Ipsos (2025)",
        "Infobae (2025)"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# --- GRÁFICO DE BARRAS ---
fig = px.bar(
    df,
    x="Candidato",
    y="Intención de Voto (%)",
    color="Partido",
    text="Intención de Voto (%)",
    title="📈 Intención de voto presidencial en Perú (2025)",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

# --- GRÁFICO DE INDECISOS ---
st.header("🤔 Porcentaje de votantes indecisos o sin preferencia")
indecisos = pd.DataFrame({
    "Categoría": ["Indecisos / Blanco", "Votantes definidos"],
    "Porcentaje": [51, 49]
})
fig2 = px.pie(
    indecisos,
    names="Categoría",
    values="Porcentaje",
    title="Distribución de votantes según preferencia (Ipsos, 2025)",
    color_discrete_sequence=px.colors.sequential.RdBu
)
st.plotly_chart(fig2, use_container_width=True)

# --- CONTEXTO POLÍTICO ---
st.header("📉 Contexto Político Actual")
st.write("""
- La desaprobación del gobierno de **Dina Boluarte** supera el **90 %** (FTI Consulting, 2025).  
- El **84 % de los peruanos** dice no confiar en los candidatos presidenciales actuales (Infobae, septiembre 2025).  
- Se espera una campaña con **alta fragmentación política** y posible inscripción de **más de 40 candidatos** (Radio Nacional, 2025).  
- Los temas más importantes para los votantes son: **inseguridad ciudadana**, **corrupción**, **empleo** y **situación económica**.
""")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Datos reales: Infobae (2025), Reuters (2025), Ipsos Perú (2025), FTI Consulting (2025), Radio Nacional (2025). Aplicación creada por Sistine 💻")

