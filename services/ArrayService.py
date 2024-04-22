import json
import random

# Ruta absoluta para el archivo JSON
json_matrix_file_path = "array.json"

def generar_array(n):
    array = []
    for _ in range(n):
        numero = random.randint(10000000, 99999999)  # Generar número aleatorio de 6 dígitos
        array.append(numero)
    return array

def exec():
    data = {}
    n=13 

    for i in range(2):
        size = pow(2, n)
        case_name = f"caso{i+1}"
        array = generar_array(size)
        data[case_name] = {"array": array}
        print(f"Array de 2 a la {n} = {size}")
        n+=1

    with open(json_matrix_file_path, 'w') as file_json:
        json.dump(data, file_json)
