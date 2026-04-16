import requests
import os

# Crear carpeta data si no existe
os.makedirs("data", exist_ok=True)

url = "https://www.datos.gov.co/resource/rvii-eis8.csv"

response = requests.get(url)

if response.status_code == 200:
    with open("data/cartera.csv", "wb") as file:
        file.write(response.content)
    print("Datos descargados correctamente")
else:
    print("Error al descargar los datos")