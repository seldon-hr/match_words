#Crea una función que mida la distancia entre dos palabras y devuelva la distancia de Levenshtein entre ellas.
##EScribe tu código aquí##
def levenshtein_distance(a, b):
    if len(a) > len(b):
        a, b = b, a
    if len(b) == 0:
        return len(a)
    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

# Prueba tu función
print(levenshtein_distance("Ojo de Agua", "Hacienda  Ojo de agua")) # 1