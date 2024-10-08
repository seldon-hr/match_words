import requests
import json

url = "https://pagosqa.qualitas.com.mx/api.php"

payloadGenLink = {
    "wptoken": "40890150a93a3b0591e0eaec652ad477",
    "m": "genWSPLink",
    "poliza": "2170054034",
    "tel": "7722294170",
    "id_branch": "666",
    "user": "0026SCUS1"
}

payloadCancelLink = {
    "wptoken": "40890150a93a3b0591e0eaec652ad477",
    "m": "cancellink",
    "poliza": "2170054034",    
}

payloadSMSLink = {
    "wptoken": "40890150a93a3b0591e0eaec652ad477",
    "m": "genSmsLink",
    "poliza": "2170054034",
    "tel": "7722294170",
}

responseWSP = requests.post(url, json=payloadGenLink)
responseSMS = requests.post(url, json=payloadSMSLink)
responseCancel = requests.post(url, json=payloadCancelLink) 

print("Código de estado:", response.status_code)
print("Respuesta:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))