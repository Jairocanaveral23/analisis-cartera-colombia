import pandas as pd
import psycopg

# Leer archivo limpio
df = pd.read_csv("data/cartera_limpia.csv")

# Conexión
conn = psycopg.connect(
    host="localhost",
    dbname="cartera_db",
    user="postgres",
    password="postgres123"
)

cur = conn.cursor()

# Insertar datos
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO cartera (
            tipo_entidad,
            codigo_entidad,
            nombre_entidad,
            fecha_corte,
            tipo_cartera,
            saldo_cartera,
            cartera_vencida,
            clientes_mora
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get("tipo_entidad"),
        row.get("codigo_entidad"),
        row.get("nombreentidad"),
        row.get("fecha_corte"),
        row.get("descrip_uc"),
        row.get("_1_saldo_de_la_cartera_a"),
        row.get("_5_vencida_1_3_meses"),
        row.get("_16_n_mero_de_clientes_mora")
    ))

conn.commit()

cur.close()
conn.close()

print("Datos insertados correctamente")