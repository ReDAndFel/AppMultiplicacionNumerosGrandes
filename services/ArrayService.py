import json
import random

# Ruta absoluta para el archivo JSON
json_matrix_file_path = "array.json"

def generar_array(n):
    array = []
    for _ in range(n):
        numero = random.randint(1, 9)  # Generar número aleatorio de 1 dígito
        array.append(numero)
    return array

def exec():
    data = {}
    n=28 

    for i in range(3):
        size = n
        case_name = f"caso{i+1}"
        array1 = generar_array(size)
        array2 = generar_array(size)
        data[case_name] = {"array1": array1, "array2": array2}
        print(f"Array1 de tamaño {size}")
        print(f"Array2 de tamaño {size}")
        n+=1

    with open(json_matrix_file_path, 'w') as file_json:
        json.dump(data, file_json)
