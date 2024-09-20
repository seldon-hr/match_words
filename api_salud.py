import requests
import json

BASE_URL = "https://pagofacturasqa.qualitassalud.com.mx/apilink/"
LOGIN_URL = f"{BASE_URL}login"
GEN_LINK_URL = f"{BASE_URL}genLink"

USERNAME = "wp_qs"
PASSWORD = "LqZ7YV0Wk3Ts"

payload = {
    "token": "eyJhbGciOiJIUzUxMiJ9.eyJhdXRob3JpdGllcyI6Ilt7XCJhdXRob3JpdHlcIjpcIlJPTEVfVVNFUlwifV0iLCJzdWIiOiJ3cF9xcyIsImlhdCI6MTcyNjc2OTA4NiwiZXhwIjoxNzI2Nzk3ODg2fQ.VXdCp40w-3kYWR-P6vbqLAY_ywYAYpMNNkppWTGf02vWjkWFHmvBBNJvVzEg-BwtwwK86rUiLvLY_4Oq5Np4Ag",
    "poliza": "370000197301",
    "email": "daanmaro99june@gmail.com",
    "telefono": "",
    "domi": "0",
}

response = requests.post(GEN_LINK_URL, json=payload)

print("Código de estado:", response.status_code)
print("Respuesta:")
# print(json.dumps(response.json(), indent=2, ensure_ascii=False))
print(response)