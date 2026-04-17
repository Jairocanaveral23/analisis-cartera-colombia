import requests
import os

# Crear carpeta de almacenamiento si no existe
os.makedirs("data", exist_ok=True)

# Endpoint del dataset en formato CSV
url = "https://www.datos.gov.co/resource/rvii-eis8.csv"

# Realizar petición HTTP para obtener los datos
response = requests.get(url)

# Validar que la descarga fue exitosa
if response.status_code == 200:
    # Guardar archivo localmente
    with open("data/cartera.csv", "wb") as file:
        file.write(response.content)
    print("Datos descargados correctamente")
else:
    print("Error al descargar los datos")