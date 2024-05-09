import time
import services.AlgorithmsService as AS
import services.ArrayService as ArrS
import services.GraphsService as GS
import services.JsonService as JS

json_arrays_file_path = "./array.json"

# Se generan los array del caso 1 y 2. Descomentar si aun no los ha generado
#ArrS.exec()
"""
for i in range(3):

    print(f"Vuelta del caso{i+1}")

    json_times_file_path = f"times{i+1}.json"

    array1, array2 = JS.read_json_array(json_arrays_file_path, i + 1)
    print(f"tamaño de array1: ", len(array1))
    print(f"tamaño de array2: ", len(array2))

    # Se ejecuta el algoritmo americano iterativo estatico
    start_time = time.time()
    array_result = AS.americanoIterativoEstatico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "AmericanoIterativoEstatico", elapsed_time)
    print(
        "Tiempo de ejecución de americano iterativo estatico: ",
        elapsed_time,
        "segundos",
    )

    # Se ejecuta el algoritmo americano iterativo dinamico
    start_time = time.time()
    array_result = AS.americanoIterativoDinamico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "AmericanoIterativoDinamico", elapsed_time)
    print(
        "Tiempo de ejecución de americano iterativo dinamico: ",
        elapsed_time,
        "segundos",
    )

    # Se ejecuta el algoritmo americano recursivo estatico
    start_time = time.time()
    array_result = AS.americanoaRecursivoEstatico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "AmericanoRecursivoEstatico", elapsed_time)
    print(
        "Tiempo de ejecución de americano recursivo estatico: ",
        elapsed_time,
        "segundos",
    )

    # Se ejecuta el algoritmo americano recursivo dinamico
    start_time = time.time()
    array_result = AS.americanoRecursivoDinamico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "AmericanoRecursivoDinamico", elapsed_time)
    print(
        "Tiempo de ejecución de americano recursivo dinamico: ",
        elapsed_time,
        "segundos",
    )

    # Se ejecuta el algoritmo divide y venceras
    start_time = time.time()
    array_result = AS.divideYVenceras(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "DivideYVenceras", elapsed_time)
    print("Tiempo de ejecución de divide y venceras: ", elapsed_time, "segundos")

    # Se ejecuta el algoritmo hindu iterativo estatico
    start_time = time.time()
    array_result = AS.hinduIterativoEstatico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "HinduIterativoEstatico", elapsed_time)
    print("Tiempo de ejecución de hindu iterativo estatico: ", elapsed_time, "segundos")

    # Se ejecuta el algoritmo inglesa iterativo estatico
    start_time = time.time()
    array_result = AS.inglesaIterativoEstatico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "InglesaIterativoEstatico", elapsed_time)
    print(
        "Tiempo de ejecución de inglesa iterativo estatico: ", elapsed_time, "segundos"
    )

    # Se ejecuta el algoritmo inglesa iterativo dinamico
    start_time = time.time()
    array_result = AS.inglesaIterativoDinamico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "InglesaIterativoDinamico", elapsed_time)
    print(
        "Tiempo de ejecución de inglesa iterativo dinamico: ", elapsed_time, "segundos"
    )

    # Se ejecuta el algoritmo inglesa recursivo dinamico
    start_time = time.time()
    array_result = AS.inglesaRecursivoDinamico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "InglesaRecursivoDinamico", elapsed_time)
    print(
        "Tiempo de ejecución de inglesa recursivo dinamico: ", elapsed_time, "segundos"
    )

    # Se ejecuta el algoritmo inglesa recursivo estatico
    start_time = time.time()
    array_result = AS.inglesaRecursivoEstatico(array1, array2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    JS.modify_property(json_times_file_path, "InglesaRecursivoEstatico", elapsed_time)
    print(
        "Tiempo de ejecución de inglesa recursivo estatico: ", elapsed_time, "segundos"
    )"""

GS.exec()
