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
4. Exposición de datos mediante API(FastApi)
5. Deploy de la API en Render(acceso publico)
6. Visualización en Power BI

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

## 🗄️ Base de datos (PostgreSQL)

Se creó una base de datos para almacenar los datos procesados y facilitar su análisis.

Creación de la base de datos:
```sql
CREATE DATABASE cartera_db;
```

Creación de la tabla:
```sql
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
```

Validación:
```sql
SELECT COUNT(*) FROM cartera;
-- Resultado: 1000 registros cargados correctamente
```

## 🚀 API (FastAPI)

Se construyó una API REST con FastAPI para exponer los datos almacenados en PostgreSQL.

### Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Estado de la API |
| GET | `/cartera` | Primeros 100 registros |
| GET | `/cartera/tipo/{tipo}` | Filtrar por tipo de cartera |
| GET | `/cartera/fecha/{fecha}` | Filtrar por fecha de corte |
| GET | `/metricas` | Totales generales de cartera |

### Documentación interactiva

La API cuenta con documentación interactiva generada automáticamente por FastAPI:

🔗 https://analisis-cartera-colombia.onrender.com/docs

### URL pública

🌐 https://analisis-cartera-colombia.onrender.com

La API está desplegada en **Render** con base de datos PostgreSQL en la nube, accesible públicamente.

## 📌 Autor

* John Jairo Cañaveral Gutierrez
