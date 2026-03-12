# 📊 E-commerce Data Pipeline & Predictive Analytics (Olist Dataset)

Este proyecto fue desarrollado como parte de mi preparación técnica para el rol de **Data Scientist Jr.**. El objetivo principal es transformar datos crudos de un e-commerce en insights de negocio y un modelo predictivo funcional.

## 🚀 Resumen del Proyecto
El proyecto cubre el ciclo de vida completo de un dato:
1. **Ingesta (ETL):** Automatización de carga de archivos CSV a una base de datos relacional SQLite.
2. **Análisis (EDA):** Identificación de categorías estrella y tendencias de facturación.
3. **Machine Learning:** Entrenamiento de un modelo para predecir costos de logística (freight value).

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.12
* **Librerías de Datos:** Pandas, NumPy
* **Base de Datos:** SQLite con SQLAlchemy
* **Visualización:** Matplotlib & Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)

## 📁 Estructura del Repositorio
* `ingestion.py`: Script de procesamiento y carga de datos.
* `analisis.py`: Consultas SQL para obtener el Top 10 de categorías.
* `graficos.py`: Generación de visualizaciones de tendencias temporales.
* `modelo_ia.py`: Pipeline de Machine Learning (entrenamiento y evaluación).

## 📈 Resultados Destacados
* **Insight de Negocio:** La categoría "Belleza y Salud" lidera las ventas con una facturación superior a los $1.2M.
* **Modelo Predictivo:** Se logró un Error Medio Absoluto (MAE) de **$7.77** en la predicción de fletes, sentando las bases para una optimización de costos logísticos.

---
*Desarrollado por [Esteban J. Diaz](https://github.com/esteban-j-diaz)*
