#App realizada por el equipo de trabajo basados en las diapositivas de classroom

def multiplicar(arreglo1, arreglo2):
    k = len(arreglo1) + len(arreglo2) - 1
    pos = len(arreglo1) + len(arreglo2) - 1
    resultado = [0] * (len(arreglo1) + len(arreglo2))

    for i in range(len(arreglo1) - 1, -1, -1):
        for j in range(len(arreglo2) - 1, -1, -1):
            resultado[k] += arreglo1[i] * arreglo2[j]
            if resultado[k] > 9:
                resultado[k - 1] += resultado[k] // 10
                resultado[k] %= 10
            k -= 1
        k = pos
        pos -= 1
        k -= 1

    return resultado
