###############################################
# 💼 STARTUP SIMULATOR — SISTINE VIVANCO (UPC)
# Proyecto académico — Negocios y Tendencias Digitales 2025
# Lenguaje: Python
# Librerías: Streamlit, Pandas, Matplotlib
###############################################

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Startup Simulator", page_icon="💼", layout="wide")

# --- TÍTULO Y DESCRIPCIÓN ---
st.title("💼 Startup Simulator")
st.markdown("""
Bienvenido a **Startup Simulator**, una aplicación educativa creada para analizar el **rendimiento financiero**
de un negocio digital.  
Permite simular ingresos, costos y ganancias mensuales, además de visualizar el punto de equilibrio 📊.
""")

# --- PANEL LATERAL: PARÁMETROS DEL NEGOCIO ---
st.sidebar.header("📊 Parámetros de tu startup")
precio = st.sidebar.number_input("💰 Precio promedio de venta (S/)", min_value=1.0, value=50.0, step=1.0)
usuarios = st.sidebar.number_input("👥 Usuarios activos iniciales", min_value=1, value=1000, step=100)
costo_fijo = st.sidebar.number_input("🏢 Costos fijos mensuales (S/)", min_value=0.0, value=10000.0, step=500.0)
costo_variable = st.sidebar.number_input("⚙️ Costo variable por usuario (S/)", min_value=0.0, value=20.0, step=1.0)
crecimiento = st.sidebar.slider("📈 Tasa de crecimiento mensual (%)", 0, 100, 10)

# --- CÁLCULOS ---
meses = list(range(1, 13))
usuarios_mes = [usuarios * ((1 + crecimiento / 100) ** i) for i in range(12)]
ingresos_mes = [precio * u for u in usuarios_mes]
costos_mes = [costo_fijo + (costo_variable * u) for u in usuarios_mes]
ganancia_mes = [ing - cost for ing, cost in zip(ingresos_mes, costos_mes)]

# --- CREAR DATAFRAME ---
df = pd.DataFrame({
    "Mes": meses,
    "Usuarios": usuarios_mes,
    "Ingresos (S/)": ingresos_mes,
    "Costos (S/)": costos_mes,
    "Ganancia (S/)": ganancia_mes
})

# --- PUNTO DE EQUILIBRIO ---
if precio > costo_variable:
    punto_equilibrio = costo_fijo / (precio - costo_variable)
else:
    punto_equilibrio = None

# --- MOSTRAR RESULTADOS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Resultados mensuales")
    st.dataframe(df.style.format({
        "Ingresos (S/)": "S/{:,.2f}",
        "Costos (S/)": "S/{:,.2f}",
        "Ganancia (S/)": "S/{:,.2f}"
    }))

with col2:
    st.subheader("📈 Gráfico de desempeño")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Mes"], df["Ingresos (S/)"], label="Ingresos", linewidth=2)
    ax.plot(df["Mes"], df["Costos (S/)"], label="Costos", linewidth=2)
    ax.plot(df["Mes"], df["Ganancia (S/)"], label="Ganancia", linewidth=2)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Soles (S/)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# --- RESUMEN FINANCIERO ---
st.markdown("---")
st.header("📋 Resumen financiero")

ganancia_total = sum(ganancia_mes)
ganancia_promedio = sum(ganancia_mes) / len(ganancia_mes)

col3, col4, col5 = st.columns(3)
col3.metric("💸 Ganancia total anual", f"S/{ganancia_total:,.2f}")
col4.metric("📆 Ganancia promedio mensual", f"S/{ganancia_promedio:,.2f}")
if punto_equilibrio:
    col5.metric("⚖️ Punto de equilibrio (usuarios)", f"{punto_equilibrio:,.0f}")
else:
    col5.metric("⚠️ Punto de equilibrio", "No calculable")

# --- INTERPRETACIÓN ---
st.markdown("""
---
### 💡 Interpretación:
- Si las **ganancias son positivas** desde los primeros meses, tu modelo es **rentable**.  
- Si los **costos superan los ingresos**, revisa tus precios o reduce los costos variables.  
- El **punto de equilibrio** te muestra cuántos usuarios necesitas para **no tener pérdidas**.

---
📍 *Proyecto académico desarrollado por Sistine Vivanco — UPC (2025)*  
Curso: **Negocios y Tendencias Digitales**
""")

# --- INFORMACIÓN ADICIONAL (README INTEGRADO) ---
with st.expander("📘 Ver información técnica del proyecto"):
    st.markdown("""
    ## 💼 Startup Simulator

    **Startup Simulator** es una aplicación creada con **Streamlit** que simula las ventas, costos y crecimiento de un negocio digital.

    ### 🚀 Características:
    - Cálculo de ingresos, costos y ganancias mensuales.
    - Determinación del punto de equilibrio.
    - Gráfico dinámico del desempeño financiero.
    - Resumen de resultados anuales.

    ### 🧩 Tecnologías utilizadas:
    - Python 3  
    - Streamlit  
    - Pandas  
    - Matplotlib  

    ### 💻 Cómo ejecutarlo localmente:
    ```bash
    pip install streamlit pandas matplotlib
    streamlit run startup_simulator.py
    ```

    ### 📍 Autor:
    **Sistine Vivanco**  
    Universidad Peruana de Ciencias Aplicadas (UPC)  
    Curso: *Negocios y Tendencias Digitales — 2025*
    """)
