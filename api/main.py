import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

DATABASE_URL = "postgresql://carteradb_qe9z_user:AwsuVYcjmkAG71BMiILOHqjRM8MIcARc@dpg-d7grhq3eo5us739ja110-a.oregon-postgres.render.com/carteradb_qe9z"

def get_connection():
    return psycopg.connect(DATABASE_URL)

@app.get("/")
def home():
    return {"mensaje": "API de cartera funcionando"}

#Retorna los primeros 100 registros de la cartera.
@app.get("/cartera")
def obtener_cartera():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cartera LIMIT 100;")
    columnas = [desc[0] for desc in cur.description]
    resultado = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return resultado

@app.get("/cartera/entidad/{entidad}")
def cartera_por_entidad(entidad: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM cartera
        WHERE LOWER(nombre_entidad) = LOWER(%s)
    """, (entidad,))
    columnas = [desc[0] for desc in cur.description]
    resultado = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return resultado

#Filtra la cartera por tipo (ej: 'credito rotativo').
@app.get("/cartera/tipo/{tipo}")
def cartera_por_tipo(tipo: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM cartera
        WHERE unaccent(LOWER(tipo_cartera)) = unaccent(LOWER(%s))
    """, (tipo,))
    columnas = [desc[0] for desc in cur.description]
    resultado = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return resultado

@app.get("/cartera/fecha/{fecha}")
def cartera_por_fecha(fecha: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM cartera
        WHERE fecha_corte = %s
    """, (fecha,))
    columnas = [desc[0] for desc in cur.description]
    resultado = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return resultado

@app.get("/metricas")
def metricas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            SUM(saldo_cartera) AS total_cartera,
            SUM(cartera_vencida) AS total_vencida,
            SUM(clientes_mora) AS total_clientes_mora
        FROM cartera
    """)
    fila = cur.fetchone()
    cur.close()
    conn.close()
    return {
        "total_cartera": fila[0],
        "total_vencida": fila[1],
        "clientes_mora": fila[2]
    }