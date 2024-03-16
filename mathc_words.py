import json
from difflib import get_close_matches
""" from Levenshtein import distance """

# Tu lista de JSON
data = [
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "55770",
            "nombre": "San Pedro (El Terremoto)",
            "codigoAsentamiento": "0001",
            "tipoAsentamiento": "09",
            "ccMunicipioId": 760,
            "ccEstadoId": 15,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "081",
                "nombre": "Tecámac",
                "ccEstadoId": 15,
                "esActivo": 1,
                "id": 760
            },
            "ccEstado": {
                "nombre": "ESTADO DE MEXICO",
                "clave": "MC",
                "esActivo": 1,
                "id": 15
            },
            "id": 73815
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "55770",
            "nombre": "Rinconada San Pedro",
            "codigoAsentamiento": "0006",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 760,
            "ccEstadoId": 15,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "081",
                "nombre": "Tecámac",
                "ccEstadoId": 15,
                "esActivo": 1,
                "id": 760
            },
            "ccEstado": {
                "nombre": "ESTADO DE MEXICO",
                "clave": "MC",
                "esActivo": 1,
                "id": 15
            },
            "id": 73816
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "55770",
            "nombre": "Ojo de Agua",
            "codigoAsentamiento": "3949",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 760,
            "ccEstadoId": 15,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "081",
                "nombre": "Tecámac",
                "ccEstadoId": 15,
                "esActivo": 1,
                "id": 760
            },
            "ccEstado": {
                "nombre": "ESTADO DE MEXICO",
                "clave": "MC",
                "esActivo": 1,
                "id": 15
            },
            "id": 73817
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "55770",
            "nombre": "San Pedro Atzompa",
            "codigoAsentamiento": "3950",
            "tipoAsentamiento": "28",
            "ccMunicipioId": 760,
            "ccEstadoId": 15,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "081",
                "nombre": "Tecámac",
                "ccEstadoId": 15,
                "esActivo": 1,
                "id": 760
            },
            "ccEstado": {
                "nombre": "ESTADO DE MEXICO",
                "clave": "MC",
                "esActivo": 1,
                "id": 15
            },
            "id": 73818
        },
        ##Objeto de ejemplo nuevo.
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "55770",
            "nombre": "Hacienda Ojo de agua",
            "codigoAsentamiento": "3949",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 760,
            "ccEstadoId": 15,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "081",
                "nombre": "Tecámac",
                "ccEstadoId": 15,
                "esActivo": 1,
                "id": 760
            },
            "ccEstado": {
                "nombre": "ESTADO DE MEXICO",
                "clave": "MC",
                "esActivo": 1,
                "id": 15
            },
            "id": 73819
        }
    ]

""" nombre_devuelto = "Ojo de Agua" """
nombre_devuelto = input("Ingrese el nombre de la propiedad nombre: ").lower()

# Obtener una lista de nombres la lista de JSON
nombres = [elemento["nombre"] for elemento in data]

# Encontrar la coincidencia más cercana al nombre devuelto
coincidencias = get_close_matches(nombre_devuelto, nombres, n = 2, cutoff = 0.3)

if coincidencias:
    nombre_coincidencia = coincidencias[0]
    indice_coincidencia = nombres.index(nombre_coincidencia)
    json_coincidencia = data[indice_coincidencia]
    print("Array",coincidencias)
    print("///////////////////////")
    print("Coincidencia encontrada:")
    print(json.dumps({"nombre": json_coincidencia["nombre"], "id": json_coincidencia["id"]}, indent=4))
else:
    print("No se encontraron coincidencias cercanas.")
