def multiplicar(arreglo1, arreglo2):
    tam = len(arreglo1) + len(arreglo2)
    resultado = [0] * tam

    for i in range(len(arreglo2)):
        for j in range(len(arreglo1)):
            resultado[i+j+1] += arreglo1[j] * arreglo2[i]

    for k in range(tam-1, 0, -1):
        resultado[k-1] += resultado[k] // 10
        resultado[k] %= 10

    return resultado