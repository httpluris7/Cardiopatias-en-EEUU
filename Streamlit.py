
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Predicción Salud Cardiovascular", layout="centered")
st.title("❤️ Predicción de Riesgo Cardiovascular")
st.markdown("Usando modelos de Machine Learning (XGBoost) entrenados con datos reales de 2020 y 2022")
st.markdown("---")

# --- SELECCIÓN DE AÑO Y THRESHOLD ---
año = st.sidebar.selectbox("Selecciona el año del estudio", ["2020", "2022"])
threshold = st.sidebar.slider("Threshold de predicción", 0.1, 0.9, 0.5, step=0.01)

# --- CARGA DE MODELOS, ESCALADORES Y COLUMNAS ---
modelo = joblib.load(f"{año}_model.joblib")
scaler = joblib.load(f"{año}_scaler.joblib")
with open(f"{año}_columns.json", "r") as f:
    columnas_modelo = json.load(f)
with open(f"{año}_importancias.json", "r") as f:
    importancias = json.load(f)

# --- FORMULARIO SEGÚN AÑO ---
st.subheader(f"📋 Formulario para datos del paciente ({año})")
if año == "2020":
    inputs = {
        "BMI": st.number_input("BMI", 10.0, 60.0, 25.0),
        "Smoking": st.selectbox("Fuma", ["Yes", "No"]),
        "AlcoholDrinking": st.selectbox("Bebe alcohol", ["Yes", "No"]),
        "DiffWalking": st.selectbox("Dificultad para caminar", ["Yes", "No"]),
        "Sex": st.selectbox("Sexo", ["Male", "Female"]),
        "AgeCategory": st.selectbox("Rango de edad", ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older']),
        "Race": st.selectbox("Raza", ['White','Black','Asian','American Indian/Alaskan Native','Other','Hispanic']),
        "Diabetic": st.selectbox("Diabético", ["Yes", "No", "Yes (during pregnancy)", "No, borderline diabetes"]),
        "PhysicalActivity": st.selectbox("Actividad física regular", ["Yes", "No"]),
        "GenHealth": st.selectbox("Salud general", ['Poor','Fair','Good','Very good','Excellent']),
        "SleepTime": st.slider("Horas de sueño", 0, 24, 7),
        "Asthma": st.selectbox("Asma", ["Yes", "No"]),
        "SkinCancer": st.selectbox("Cáncer de piel", ["Yes", "No"]),
    }
    target_variable = "HeartDisease"
else:
    inputs = {
        "BMI": st.number_input("BMI", 10.0, 60.0, 25.0),
        "Smoking": st.selectbox("Fuma", ["Yes", "No"]),
        "AgeCategory": st.selectbox("Rango de edad", ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older']),
        "SleepTime": st.slider("Horas de sueño", 0, 24, 7),
        "Sex": st.selectbox("Sexo", ["Male", "Female"]),
        "Race": st.selectbox("Raza", ['White','Black','Asian','American Indian/Alaskan Native','Other','Hispanic']),
        "PhysicalActivity": st.selectbox("Actividad física", ["Yes", "No"]),
        "GenHealth": st.selectbox("Salud general", ['Poor','Fair','Good','Very good','Excellent']),
        "DiffWalking": st.selectbox("Dificultad al caminar", ["Yes", "No"]),
        "Diabetic": st.selectbox("Diabético", ["Yes", "No", "Yes (during pregnancy)", "No, borderline diabetes"]),
        "AlcoholDrinking": st.selectbox("Toma alcohol", ["Yes", "No"]),
        "Asthma": st.selectbox("Tiene asma", ["Yes", "No"]),
        "SkinCancer": st.selectbox("Tuvo cáncer de piel", ["Yes", "No"]),
    }
    target_variable = "HadHeartAttack"

# --- INPUT DEL USUARIO ---
input_df = pd.DataFrame([inputs])
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=columnas_modelo, fill_value=0)
input_scaled = scaler.transform(input_encoded)

# --- BOTÓN DE EJECUCIÓN ---
if st.button("🔍 Aplicar predicción"):
    prob = modelo.predict_proba(input_scaled)[0][1]
    pred = int(prob >= threshold)

    st.markdown("---")
    st.subheader("🧠 Resultado de la predicción")
    st.write(f"Probabilidad de clase positiva: **{prob:.2%}**")
    st.progress(float(prob))

    if pred == 0:
        st.success("✅ Predicción: SIN riesgo")
    else:
        st.error("⚠️ Predicción: CON riesgo")

# --- GRÁFICO DE IMPORTANCIAS ---
st.markdown("---")
st.subheader("🔍 Top 10 variables más influyentes en el modelo")

importancias_ordenadas = sorted(importancias.items(), key=lambda x: x[1], reverse=True)[:10]
vars_top, vals_top = zip(*importancias_ordenadas)

fig = go.Figure(go.Bar(
    x=list(vals_top),
    y=list(vars_top),
    orientation='h',
    marker=dict(color='indianred')
))
fig.update_layout(
    xaxis_title="Importancia",
    yaxis_title="Variable",
    yaxis=dict(autorange="reversed"),
    height=400
)
st.plotly_chart(fig, use_container_width=True)
