import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el dataset limpio que generaste en el paso anterior
df = pd.read_csv('dataset_limpio.csv')

# Convertimos la fecha a formato real otra vez por seguridad
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# 1. Agrupar ventas por mes para ver la tendencia
ventas_mensuales = df.resample('M', on='order_purchase_timestamp')[
    'price'].sum().reset_index()

# 2. Configurar el estilo del gráfico
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# 3. Crear el gráfico de líneas
sns.lineplot(data=ventas_mensuales, x='order_purchase_timestamp',
             y='price', marker='o', color='teal')

# 4. Personalización (Esto es lo que hace que un gráfico sea profesional)
plt.title('Evolución Histórica de Ventas (Facturación)', fontsize=15)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Total Ventas ($)', fontsize=12)
plt.xticks(rotation=45)

# Guardar el gráfico para tu portfolio
plt.savefig('tendencia_ventas.png')
print("✅ Gráfico guardado como 'tendencia_ventas.png'")

# Mostrar el gráfico en pantalla
plt.show()
