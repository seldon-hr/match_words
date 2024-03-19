import json
from difflib import get_close_matches
""" from Levenshtein import distance """

# Tu lista de JSON
data = [
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Bellavista",
            "codigoAsentamiento": "0177",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 263
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Loma Bonita",
            "codigoAsentamiento": "0178",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 264
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Nueva Castilla",
            "codigoAsentamiento": "0373",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 265
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Xenia Residencial",
            "codigoAsentamiento": "0393",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 266
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Vergel de la Cantera",
            "codigoAsentamiento": "0431",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 267
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Balandra",
            "codigoAsentamiento": "0439",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 268
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Carmel",
            "codigoAsentamiento": "0445",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 269
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Cantelli Residencial",
            "codigoAsentamiento": "0475",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 270
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Villas de La Cantera",
            "codigoAsentamiento": "0978",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 271
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Lic Manuel Gómez Morin",
            "codigoAsentamiento": "1035",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 272
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Residencial San Nicolás",
            "codigoAsentamiento": "1053",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 273
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Villas del Mediterráneo",
            "codigoAsentamiento": "1074",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 274
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Ex Hacienda La Cantera",
            "codigoAsentamiento": "1138",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 275
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "José Vasconcelos Calderón",
            "codigoAsentamiento": "1139",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 276
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Porta Canteras",
            "codigoAsentamiento": "1171",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 277
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Veteranos de la Revolución",
            "codigoAsentamiento": "1326",
            "tipoAsentamiento": "09",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 278
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Fuentes del Lago",
            "codigoAsentamiento": "1350",
            "tipoAsentamiento": "10",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 279
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "El Quelite",
            "codigoAsentamiento": "1435",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 280
        },
        {
            "fechaRegistro": "2023-11-08 17:30:37",
            "cp": "20200",
            "nombre": "Olinda",
            "codigoAsentamiento": "1442",
            "tipoAsentamiento": "21",
            "ccMunicipioId": 1,
            "ccEstadoId": 1,
            "esActivo": 1,
            "ccMunicipio": {
                "fechaRegistro": "2023-09-04 11:40:56",
                "clave": "001",
                "nombre": "Aguascalientes",
                "ccEstadoId": 1,
                "esActivo": 1,
                "id": 1
            },
            "ccEstado": {
                "nombre": "AGUASCALIENTES",
                "clave": "AS",
                "esActivo": 1,
                "id": 1
            },
            "id": 281
        }
    ]

""" nombre_devuelto = "Ojo de Agua" """
nombre_devuelto = input("Ingrese el nombre de la propiedad nombre: ").lower()

# Obtener una lista de nombres la lista de JSON
nombres = [elemento["nombre"] for elemento in data]

# Encontrar la coincidencia más cercana al nombre devuelto
coincidencias = get_close_matches(nombre_devuelto, nombres, n = 2  , cutoff = 0.5)

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
