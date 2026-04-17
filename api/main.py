from fastapi import FastAPI
import psycopg

app = FastAPI()

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="cartera_db",
        user="postgres",
        password="postgres123"
    )

@app.get("/")
def home():
    return {"mensaje": "API de cartera funcionando"}

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