import requests
import json

# URLs de la API (actualizada)
BASE_URL = "https://pagofacturasqa.qualitassalud.com.mx/apilink/"
LOGIN_URL = f"{BASE_URL}login"
GEN_LINK_URL = f"{BASE_URL}genLink"

# Credenciales
USERNAME = "wp_qs"
PASSWORD = "LqZ7YV0Wk3Ts"

def login():
    """Realiza el login y devuelve el token de acceso."""
    params = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(LOGIN_URL, params=params)
    print(f"Full response: {response}")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        return data.get("token")
    else:
        raise Exception(f"Login failed: {response.status_code} - {response.text}")

# token, poliza, email, telefono, domi
def gen_link():
    # headers = {
    #     "Authorization": f"Bearer {token}",
    #     "Content-Type": "application/json"
    # }
    payload = {
        "poliza": "370000197301",
        "email": "daanmaro99june@gmail.com",
        # "telefono": telefono,
        "domi": "0"
    }
    print(payload)
    response = requests.post(GEN_LINK_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"genLink failed: {response.status_code} - {response.text}")

def main():
    try:
        # Paso 1: Login
        # print("Realizando login...")
        # token = login()
        # print("Login exitoso. Token obtenido.", token)

        # Paso 2: Generar link
        print("\nGenerando link de pago...")
        # result = gen_link(
        #     token="eyJhbGciOiJIUzUxMiJ9.eyJhdXRob3JpdGllcyI6Ilt7XCJhdXRob3JpdHlcIjpcIlJPTEVfVVNFUlwifV0iLCJzdWIiOiJ3cF9xcyIsImlhdCI6MTcyNjc2OTA4NiwiZXhwIjoxNzI2Nzk3ODg2fQ.VXdCp40w-3kYWR-P6vbqLAY_ywYAYpMNNkppWTGf02vWjkWFHmvBBNJvVzEg-BwtwwK86rUiLvLY_4Oq5Np4Ag",
        #     poliza="370000197301", 
        #     email="daanmaro99june@gmail.com",
        #     telefono="",
        #     domi="0"
        # )
        result = gen_link()
        print("Link generado exitosamente:")
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()