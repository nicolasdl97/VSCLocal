# Predicción de precios en el mercado inmobiliario de Madrid mediante Machine Learning
Este proyecto tiene como objetivo implementar un modelo de predicción de precios para el mercado inmobiliario de la ciudad de Madrid, utilizando técnicas de Machine Learning y análisis de datos a gran escala. La motivación parte de la necesidad de comprender y anticipar el comportamiento de los precios de vivienda, un problema especialmente relevante para nuevos inversores y compradores en una ciudad altamente competitiva.

## Fuentes de datos
Se utilizó la API de Idealista, el portal líder de bienes raíces en España, para recolectar más de 10,000 registros de propiedades en venta en Madrid entre febrero y mayo. Los datos incluyen variables como el tamaño, número de habitaciones, ubicación geográfica, presencia de ascensor, plaza de garaje, entre otros.

Los datos recolectados fueron limpiados, transformados y enriquecidos con variables derivadas mediante ingeniería de características, como el precio por metro cuadrado por distrito y vecindario, tamaño medio de habitaciones y relaciones entre variables como baños/habitaciones.

## Metodología
Se desarrollaron modelos predictivos utilizando algoritmos como Linear Regression, Random Forest Regressor, Gradient Boosting Regressor y XGBoost. Se aplicaron técnicas de codificación (TargetEncoder), escalado (StandardScaler), validación cruzada, y búsqueda aleatoria de hiperparámetros (RandomizedSearchCV).

La evaluación del rendimiento se realizó mediante métricas como MAE, RMSE, MAPE y R². El modelo final seleccionado fue el GradientBoostingRegressor, el cual obtuvo un R² de 0.9985 y un MAPE del 1.3%, demostrando una alta capacidad predictiva.

## Aplicaciones de negocio
Se desarrollaron dos casos de uso principales:

1. Detección de ofertas subvaluadas: se identifican propiedades cuyo precio de venta es significativamente inferior al estimado por el modelo, lo cual representa una oportunidad de inversión.

2. Valoración de inmuebles: agencias inmobiliarias pueden usar el modelo para estimar precios realistas de propiedades, mejorando la negociación y confianza con clientes.

## Herramientas utilizadas
Lenguaje: Python

Entornos: Jupyter Notebook, Google Colab

Librerías: Pandas, NumPy, Matplotlib, scikit-learn, XGBoost, GeoPandas, category_encoders

Los datos fueron procesados y almacenados en DataFrames, y enriquecidos con datos geoespaciales mediante archivos .geojson para analizar la densidad inmobiliaria por distritos.

## Estructura del repositorio
Este repositorio incluye:

📁 data/TFM: archivos de datos relevantes y procesados (idealista_02.csv, idealista_03.csv, etc.).

📁 code/tfm/: notebooks seleccionados del desarrollo.

📄 README.md: documento de presentación del proyecto.

## Créditos
Este proyecto fue desarrollado como parte del Trabajo Final del Máster Universitario en Data Science for Finance en EAE Business School (promoción 2023–2024). El equipo estuvo conformado por:

Nimrod Abraham Saigg

Nicolás Delgado Lorino

Manuel Anthony Gonzales Aparco

José Rodríguez Muñoz

Víctor Hugo Yáñez Villagómez

Tutorizado por el Prof. Roberto Maestre Martínez.