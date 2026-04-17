# Análisis de Cartera Financiera en Colombia

Este proyecto tiene como objetivo extraer, procesar y analizar datos de cartera financiera reportados por entidades en Colombia, utilizando herramientas de automatización, bases de datos y visualización.

## 🧰 Tecnologías utilizadas

* Python
* PostgreSQL
* Power BI

## 📁 Estructura del proyecto

```
analisis-cartera-colombia/
│
├── rpa/        # Scripts de extracción y limpieza de datos
├── db/         # Scripts relacionados con base de datos
├── api/        # API para consumo de datos
├── data/       # Archivos CSV
├── docs/       # Documentación adicional
```

## ⚙️ Proceso del proyecto

1. Extracción de datos desde fuente oficial (RPA en Python)
2. Limpieza y transformación de datos
3. Almacenamiento en PostgreSQL
4. Exposición de datos mediante API
5. Visualización en Power BI

## ▶️ Ejecución

1. Ejecutar el script de extracción:

```
python rpa/extractor.py
```

2. Ejecutar limpieza de datos:

```
python rpa/limpieza.py
```

## 📊 Fuente de datos

Datos abiertos del gobierno de Colombia:
https://www.datos.gov.co/

🗄️ Base de datos (PostgreSQL)

Se creó una base de datos para almacenar los datos procesados y facilitar su análisis.

Creación de la base de datos:
CREATE DATABASE cartera_db;

Creación de la tabla:
CREATE TABLE cartera (
    id SERIAL PRIMARY KEY,
    tipo_entidad INTEGER,
    codigo_entidad INTEGER,
    nombre_entidad TEXT,
    fecha_corte DATE NOT NULL,
    tipo_cartera TEXT NOT NULL,
    saldo_cartera NUMERIC(18, 2),
    cartera_vencida NUMERIC(18, 2),
    clientes_mora INTEGER
);

Carga de datos:

Se insertaron los datos desde el archivo limpio (cartera_limpia.csv) usando Python.

python db/insert_data.py

Validación
SELECT COUNT(*) FROM cartera;

Resultado esperado:

1000 registros cargados correctamente

## 📌 Autor

* John Jairo Cañaveral Gutierrez
