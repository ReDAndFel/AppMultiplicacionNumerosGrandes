#App realizada por el equipo de trabajo
import json

def modify_property(json_file_path, property_name, value):
        
        json_data = read_json(json_file_path)

        # Modificar la propiedad en el objeto JSON
        json_data[property_name] = value

        # Escribir el objeto JSON modificado de vuelta al archivo
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
            
def read_json(json_file_path):
    # Leer la matriz desde el archivo JSON
    with open(json_file_path, 'r') as json_matrix:
        return json.load(json_matrix) 
          
def read_json_array(json_matrix_file_path, case_index):
    with open(json_matrix_file_path, 'r') as json_matrix:
        data = json.load(json_matrix)
        case_key = f"caso{case_index}"
        array1 = data[case_key]["array1"]
        array2 = data[case_key]["array2"]
        return array1,array2
                