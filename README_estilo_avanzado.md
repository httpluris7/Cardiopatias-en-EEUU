
<!-- FONDO Y TÍTULO -->
<div align="center">
  <h1>❤️ Predicción de Riesgo Cardiovascular en Estados Unidos</h1>
  <p>
    <strong>Modelo de Machine Learning para estimar el riesgo de enfermedad cardíaca a partir de variables clínicas y hábitos de vida.</strong>
  </p>

  <!-- BADGES -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&style=for-the-badge" />
    <img src="https://img.shields.io/badge/Scikit--Learn-green?logo=scikit-learn&style=for-the-badge" />
    <img src="https://img.shields.io/badge/Pandas-yellow?logo=pandas&style=for-the-badge" />
    <img src="https://img.shields.io/badge/Streamlit-ff4b4b?logo=streamlit&style=for-the-badge" />
    <img src="https://img.shields.io/badge/XGBoost-orange?logo=xgboost&style=for-the-badge" />
  </p>
</div>

<br />

### 👤 Autor  
- [Luis Manuel](https://github.com/httpluris7)

---

## 📋 Resumen del Proyecto

Este proyecto tiene como objetivo construir una herramienta predictiva basada en **Machine Learning** que permita estimar el **riesgo de enfermedad cardiovascular** en pacientes, utilizando datos de salud recopilados en Estados Unidos durante los años **2020 y 2022**.

La solución desarrollada busca servir de apoyo en la **detección temprana de pacientes en riesgo**, permitiendo intervenciones preventivas más eficientes. Se ha creado además una **aplicación interactiva** con interfaz amigable para profesionales de la salud y usuarios generales.

---

## 🔧 Herramientas Utilizadas

| Herramienta       | Propósito                                      |
|-------------------|-----------------------------------------------|
| **Python**        | Desarrollo de lógica y manipulación de datos  |
| **Pandas**        | Limpieza y transformación de datos            |
| **Scikit-learn**  | Modelado y evaluación de algoritmos ML        |
| **XGBoost**       | Clasificador de boosting de alto rendimiento  |
| **Streamlit**     | Visualización interactiva y predicción web    |

---

## 🧠 Flujo de Trabajo

1. **Carga y Preprocesamiento**
   - Limpieza de valores faltantes.
   - Codificación de variables categóricas.
   - Escalado con StandardScaler y balanceo con SMOTE.

2. **Modelado y Evaluación**
   - Entrenamiento con: KNN, Random Forest, Gradient Boosting, AdaBoost y XGBoost.
   - Evaluación con métricas: Accuracy, Precision, Recall y F1-Score.
   - Comparación con y sin SMOTE.

3. **Optimización**
   - Ajuste de hiperparámetros con GridSearchCV.
   - Selección del mejor modelo según sensibilidad clínica.

4. **Aplicación Web**
   - Desarrollo de una app en Streamlit con formulario interactivo y visualización de resultados.

---

## 🩺 Resultados Destacados

📌 El modelo **XGBoost** fue seleccionado como el más robusto, logrando:
- **Recall superior al 80%** en escenarios clínicos relevantes.
- Interpretación clara de variables más influyentes.
- Predicción eficiente y en tiempo real desde la aplicación.

---

## 💡 Recomendaciones Finales

✔️ Utilizar XGBoost con ajuste de umbral personalizado para maximizar la sensibilidad clínica.  
✔️ Ampliar la base de datos incluyendo más años o nuevas variables.  
✔️ Desplegar el modelo como API o sistema de apoyo médico con ética y privacidad.  
✔️ Adaptar la aplicación a plataformas móviles para mayor accesibilidad.

---

<!-- FOOTER -->
<div align="center">
  <p>Made with ❤️ by Luis Manuel</p>
</div>
