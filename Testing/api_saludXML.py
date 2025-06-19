import requests
""" import json """
import xml.etree.ElementTree as ET

# URLs de la API (actualizada)
BASE_URL = "https://siniestros.qualitassalud.com.mx:57003/wsQsalud/Movimiento"
WSDL_URL = f"{BASE_URL}?WSDL"


def load_xml(path):
    try:
        with open(path, 'r', encoding= 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise Exception(f"No found file: {path}")
    except Exception as e:
        raise Exception(f"Error to read file: {str(e)}")


def getMovimiento(path):
    headers = {
         "Content-Type": "application/xml",
         "Accept": "application/xml"
    }
    payload = load_xml(path)
    print("Sent Payload")
    print(payload)

    try:
        response = requests.post(BASE_URL, data=xml_payload, headers=headers, timeout=30)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        return response.text
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error en la petición XML: {str(e)}")

def format_xml_response(xml_string):
    """Formatea la respuesta XML para mejor visualización"""
    try:
        root = ET.fromstring(xml_string)
        rough_string = ET.tostring(root, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    except ET.ParseError:
        return xml_string  # Retorna sin formato si no es XML válido



def main():
    xml_payload_file = "./Movimiento.xml" 
    try:
        result = getMovimiento(xml_payload_file)
        print("\n" + "="*50)
        print("Respuesta XML recibida:")
        print("="*50)
        formatted_response = format_xml_response(result)
        print(formatted_response)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()