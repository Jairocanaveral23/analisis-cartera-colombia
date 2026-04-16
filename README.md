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

## 📌 Autor

* John Jairo Cañaveral Gutierrez
