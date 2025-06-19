
# ❤️ Predicción de Riesgo Cardiovascular en Estados Unidos

Modelo de Machine Learning para estimar el riesgo de enfermedad cardíaca a partir de variables clínicas y hábitos de vida.

---

## 👤 Autor
Luis Manuel

---

## 📋 Resumen del Proyecto

Este proyecto tiene como objetivo construir una herramienta predictiva basada en **Machine Learning** que permita estimar el **riesgo de enfermedad cardiovascular** en pacientes, utilizando datos de salud recopilados en Estados Unidos durante los años **2020 y 2022**.

La solución desarrollada busca servir de apoyo en la **detección temprana de pacientes en riesgo**, permitiendo intervenciones preventivas más eficientes. Se ha creado además una **aplicación interactiva** con interfaz amigable para profesionales de la salud y usuarios generales.

---

## 🔧 Herramientas Utilizadas

| Herramienta     | Propósito                                    |
|-----------------|----------------------------------------------|
| Python          | Desarrollo de lógica y manipulación de datos |
| Pandas          | Limpieza y transformación de datos           |
| Scikit-learn    | Modelado y evaluación de algoritmos ML       |
| XGBoost         | Clasificador principal basado en boosting    |
| Streamlit       | Visualización interactiva y predicción web   |

---

## 🧠 Flujo de Trabajo

### 1. Carga y Preprocesamiento
- Limpieza de datos y manejo de valores faltantes
- Codificación de variables categóricas
- Escalado con `StandardScaler`
- Balanceo de clases con **SMOTE**

### 2. Modelado y Evaluación
- Entrenamiento con múltiples modelos: `KNN`, `Random Forest`, `Gradient Boosting`, `AdaBoost` y `XGBoost`
- Evaluación con métricas clave: `Accuracy`, `Recall`, `Precision` y `F1-Score`
- Comparación de resultados con y sin SMOTE

### 3. Optimización
- Ajuste de hiperparámetros con `GridSearchCV` (XGBoost)
- Selección del mejor modelo con enfoque clínico (mayor **Recall**)

### 4. Aplicación Web
- Construcción de una app en **Streamlit** con:
  - Formulario interactivo para el ingreso de datos clínicos
  - Visualización de la predicción
  - Gráfico de variables más influyentes en el modelo

---

## 🩺 Resultados Destacados

📌 El modelo **XGBoost** fue el más equilibrado entre rendimiento y precisión clínica, logrando:

- Recall superior al 80% en algunos escenarios
- Visualización clara de variables con mayor peso en la predicción
- Implementación eficiente en tiempo real mediante una aplicación web

---

## 💡 Recomendaciones Finales

✔️ Usar el modelo XGBoost con ajuste de umbral personalizado (threshold) para maximizar la sensibilidad clínica  
✔️ Ampliar la base de datos incluyendo más años o fuentes regionales  
✔️ Desplegar el modelo como API médica con protección ética y de privacidad  
✔️ Adaptar la aplicación para su uso en dispositivos móviles

---

**Made with ❤️ by Luis Manuel**
