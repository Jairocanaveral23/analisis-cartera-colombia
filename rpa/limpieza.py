import pandas as pd

# Cargar datos
df = pd.read_csv("data/cartera.csv")

# Ver columnas originales
print("Columnas originales:")
print(df.columns)

# Limpiar nombres de columnas
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Quitar caracteres raros
df.columns = df.columns.str.replace("á", "a").str.replace("é", "e") \
                    .str.replace("í", "i").str.replace("ó", "o") \
                    .str.replace("ú", "u").str.replace("ñ", "n")

# Convertir fecha
df["fecha_corte"] = pd.to_datetime(df["fecha_corte"])

# Convertir columnas numéricas automáticamente
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

# Guardar limpio
df.to_csv("data/cartera_limpia.csv", index=False)

print("Limpieza completada")