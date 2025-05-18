# app_ccl_anomalias.py

import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="Análisis de Anomalías CCL", layout="wide")

# Título
st.title("📊 Análisis de Anomalías en Señal CCL")
st.markdown("""
Esta aplicación permite visualizar la señal **CCL normalizada** y el **score de anomalía** estimado por el modelo Isolation Forest.
Usá los selectores para navegar entre diferentes pozos y etapas.
""")

# Carga de datos
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Developer\fundamentos\data\ccl_anomaly_scores.csv")

df = load_data()

# Filtros interactivos
pozos = sorted(df["pozo"].dropna().unique())
pozo_sel = st.selectbox("Seleccionar pozo", pozos)

etapas = sorted(df[df["pozo"] == pozo_sel]["etapa"].dropna().unique())
etapa_sel = st.selectbox("Seleccionar etapa", etapas)

# Filtro del dataframe
df_sel = df[(df["pozo"] == pozo_sel) & (df["etapa"] == etapa_sel)].sort_values("DEPT")

# Gráfico interactivo
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_sel["CCL_norm"],
    y=df_sel["DEPT"],
    mode='lines',
    name='CCL Normalizado',
    line=dict(color='blue')
))

fig.add_trace(go.Scatter(
    x=df_sel["score_iso"],
    y=df_sel["DEPT"],
    mode='lines',
    name='Score de Anomalía',
    line=dict(color='red', dash='dot')
))

fig.update_layout(
    yaxis_title="Profundidad (DEPT)",
    xaxis_title="Valor",
    yaxis_autorange='reversed',
    height=600,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# Información final
st.markdown(f"""
**Pozo seleccionado:** `{pozo_sel}`  
**Etapa seleccionada:** `{etapa_sel}`  
Registros totales en esta etapa: `{len(df_sel)}`  
""")
