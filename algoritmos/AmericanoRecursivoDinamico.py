def multiplicar_recursivo_dinamico(arreglo1, arreglo2, i=0, j=0, resultado=None):
    if resultado is None:
        resultado = [0] * (len(arreglo1) + len(arreglo2)) # Inicializamos resultado con ceros

    if i < len(arreglo1):
        if j < len(arreglo2):
            if len(resultado) <= i + j + 1:
                resultado.append(0) # Agregamos un elemento si es necesario
            resultado[i+j+1] += arreglo1[i] * arreglo2[j]
            multiplicar_recursivo_dinamico(arreglo1, arreglo2, i, j+1, resultado)
        else:
            multiplicar_recursivo_dinamico(arreglo1, arreglo2, i+1, 0, resultado)

    actualizar_resultado(resultado)

    return resultado

def actualizar_resultado(resultado, k=None):
    if k is None:
        k = len(resultado) - 1

    if k > 0:
        resultado[k-1] += resultado[k] // 10
        resultado[k] %= 10
        actualizar_resultado(resultado, k-1)

    # Eliminar ceros a la izquierda
    while len(resultado) > 1 and resultado[0] == 0:
        del resultado[0]

    return resultado
