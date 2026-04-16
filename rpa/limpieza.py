import pandas as pd

# Cargar el dataset original
df = pd.read_csv("data/cartera.csv", encoding="latin1")

# Visualizar columnas originales para identificar inconsistencias
print("Columnas originales:")
print(df.columns)

# Estandarizar nombres de columnas (minúsculas y sin espacios)
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Normalizar caracteres especiales para evitar problemas en base de datos
df.columns = (
    df.columns
    .str.normalize('NFKD')
    .str.encode('ascii', 'ignore')
    .str.decode('utf-8')
)
# Convertir la columna de fecha a tipo datetime para análisis temporal
df["fecha_corte"] = pd.to_datetime(df["fecha_corte"])

# Convertir columnas numéricas que vienen como texto
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            # Se ignoran columnas que no pueden convertirse (ej: nombres)
            pass

# Guardar dataset limpio para siguientes etapas del proyecto
df.to_csv("data/cartera_limpia.csv", index=False)

print("Limpieza completada")