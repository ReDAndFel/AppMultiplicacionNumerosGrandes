def multiplicar_dinamico(arreglo1, arreglo2):
    tam = len(arreglo1) + len(arreglo2)
    resultado = [0] * tam

    for i in range(len(arreglo2)):
        for j in range(len(arreglo1)):
            if len(resultado) <= i + j + 1:
                resultado.append(0)
            resultado[i+j+1] += arreglo1[j] * arreglo2[i]

    for k in range(tam-1, 0, -1):
        resultado[k-1] += resultado[k] // 10
        resultado[k] %= 10

    # Eliminar ceros a la izquierda
    while len(resultado) > 1 and resultado[0] == 0:
        del resultado[0]

    return resultado