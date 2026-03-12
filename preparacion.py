import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///ecommerce_olist.db')

# Traemos los datos unificados mediante SQL
query_unificada = """
SELECT 
    o.order_id,
    o.customer_id,
    o.order_purchase_timestamp,
    o.order_status,
    i.price,
    i.freight_value,
    p.product_category_name,
    c.customer_city,
    c.customer_state
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON i.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered';
"""

df = pd.read_sql(query_unificada, engine)

# --- LIMPIEZA ---

# 1. Eliminar filas con datos faltantes en categorías
df = df.dropna(subset=['product_category_name'])

# 2. Convertir la fecha a formato datetime y extraer características
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['mes'] = df['order_purchase_timestamp'].dt.month
df['dia_semana'] = df['order_purchase_timestamp'].dt.dayofweek
df['hora'] = df['order_purchase_timestamp'].dt.hour

# 3. Ver el resultado
print("✅ Dataset preparado para Machine Learning")
print(f"Total de registros: {len(df)}")
print(df.head())

# Guardamos este dataset limpio para no tener que hacer todo de nuevo
df.to_csv('dataset_limpio.csv', index=False)
