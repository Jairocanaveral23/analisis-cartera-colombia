import pandas as pd

# Leer archivo original
df = pd.read_csv("data/cartera.csv", encoding="latin1")

print("Columnas originales:")
print(df.columns)

# Estandarizar nombres
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Normalizar caracteres
df.columns = (
    df.columns
    .str.normalize('NFKD')
    .str.encode('ascii', 'ignore')
    .str.decode('utf-8')
)

# Convertir fecha
df["fecha_corte"] = pd.to_datetime(df["fecha_corte"])

# Convertir columnas numéricas
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

#  guardar en UTF-8
df.to_csv("data/cartera_limpia.csv", index=False, encoding="utf-8")

print("Limpieza completada")