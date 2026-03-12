import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Cargamos los datos
df = pd.read_csv('dataset_limpio.csv')

# 2. Seleccionamos las "Features" (lo que usamos para predecir)
# y el "Target" (lo que queremos adivinar)
X = df[['price', 'mes', 'dia_semana', 'hora']]
y = df['freight_value']

# 3. Separamos los datos: 80% para entrenar y 20% para probar
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 4. Creamos el modelo y lo entrenamos
print("⏳ Entrenando el modelo de IA... (esto puede tardar unos segundos)")
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 5. Rendimos el examen: hacemos predicciones con los datos que el modelo no conocía
predicciones = modelo.predict(X_test)

# 6. Evaluamos el desempeño
mae = mean_absolute_error(y_test, predicciones)
score = r2_score(y_test, predicciones)

print("\n--- RESULTADOS DEL MODELO ---")
print(f"Error Medio Absoluto (MAE): ${mae:.2f}")
print(f"Precisión del modelo (R2 Score): {score:.2f}")
