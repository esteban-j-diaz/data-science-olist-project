import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Configuramos la conexión
engine = create_engine('sqlite:///ecommerce_olist.db')


def procesar_e_ingresar(carpeta_datos):
    # Verificamos si la carpeta existe
    if not os.path.exists(carpeta_datos):
        print(
            f"❌ Error: No encuentro la carpeta '{carpeta_datos}'. Asegurate de que esté al lado de este script.")
        return

    archivos = [f for f in os.listdir(carpeta_datos) if f.endswith('.csv')]

    if not archivos:
        print(f"⚠️ No encontré archivos .csv en la carpeta '{carpeta_datos}'.")
        return

    for archivo in archivos:
        nombre_tabla = archivo.replace(
            'olist_', '').replace('_dataset.csv', '')
        print(f"⏳ Procesando {archivo}...")

        df = pd.read_csv(os.path.join(carpeta_datos, archivo))

        # Convertimos fechas automáticamente
        for col in df.columns:
            if 'date' in col or 'timestamp' in col:
                df[col] = pd.to_datetime(df[col])

        df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)
        print(f"✅ Tabla '{nombre_tabla}' cargada.")

    print("\n🚀 ¡Todo listo! La base de datos 'ecommerce_olist.db' ya tiene los datos.")


# --- ESTA ES LA LÍNEA QUE FALTA EN TU CAPTURA ---
# Le decimos que busque los archivos en la carpeta 'data'
procesar_e_ingresar('data')
