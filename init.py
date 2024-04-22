import time
import services.AlgorithmsService as AS
import services.ArrayService as ArrS
import services.GraphsService as GS
import services.JsonService as JS

json_matrix_file_path = "./array.json"

#Se generan los array del caso 1 y 2. Descomentar si aun no los ha generado
ArrS.exec()

for i in range(3):
    
    print(f"Vuelta del caso{i+1}")
    
    json_times_file_path = f"times{i+1}.json"

    array = JS.read_json_array(json_matrix_file_path, i+1)
    
    # Se ejecuta el algoritmo BitonicSort
    start_time = time.time()
    #array_result = AS.BitonicSort(array,len(array),True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    #JS.modify_property(json_times_file_path,"BitonicSort", elapsed_time)
    print("Tiempo de ejecución de "":", elapsed_time, "segundos")
   
GS.exec()