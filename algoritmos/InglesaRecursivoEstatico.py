def multiplicar_recursivo(arreglo1, arreglo2, i=0, j=0, resultado=None):
    if resultado is None:
        tam = len(arreglo1) + len(arreglo2)
        resultado = [0] * tam

    if i < len(arreglo2):
        if j < len(arreglo1):
            resultado[i+j+1] += arreglo1[j] * arreglo2[i]
            multiplicar_recursivo(arreglo1, arreglo2, i, j+1, resultado)
        else:
            multiplicar_recursivo(arreglo1, arreglo2, i+1, 0, resultado)

    actualizar_resultado(resultado)

    return resultado

def actualizar_resultado(resultado, k=None):
    if k is None:
        k = len(resultado) - 1

    if k > 0:
        resultado[k-1] += resultado[k] // 10
        resultado[k] %= 10
        actualizar_resultado(resultado, k-1)

    return resultado