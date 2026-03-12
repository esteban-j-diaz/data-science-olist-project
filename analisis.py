import pandas as pd
from sqlalchemy import create_engine

# Nos conectamos a la base que creaste recién
engine = create_engine('sqlite:///ecommerce_olist.db')

# Esta consulta une (JOIN) las ventas con los nombres de productos
query = """
SELECT 
    p.product_category_name AS categoria,
    ROUND(SUM(i.price), 2) AS facturacion_total
FROM order_items i
JOIN products p ON i.product_id = p.product_id
GROUP BY categoria
ORDER BY facturacion_total DESC
LIMIT 10;
"""

# Ejecutamos
df_top_ventas = pd.read_sql(query, engine)

print("🏆 TOP 10 CATEGORÍAS QUE MÁS FACTURAN:")
print(df_top_ventas)
