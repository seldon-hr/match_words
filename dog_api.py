import requests

# URL base de la API
base_url = "https://api.thedogapi.com/v1"

# Headers para indicar que estamos consumiendo la API pública
headers = {
    "x-api-key": "" # Aquí debes colocar tu clave de API (si la necesitas)
}

# Endpoint para obtener una lista de razas de perros
endpoint = "/breeds"
url = base_url + endpoint

# Realizar la solicitud GET
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos de la respuesta en formato JSON
    data = response.json()

    # Recorrer la lista de razas
    for breed in data:
        print(f"Nombre: {breed['name']}")
        print(f"Grupo: {breed['breed_group']}")
        print(f"Vida: {breed['life_span']}")
        print(f"Temperamento: {breed['temperament']}")
        print("-------------------")
else:
    print(f"Error: {response.status_code}")