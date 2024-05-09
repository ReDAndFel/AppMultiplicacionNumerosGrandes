def multiplicar_dinamico(arreglo1, arreglo2):
    k = len(arreglo1) + len(arreglo2) - 1
    pos = len(arreglo1) + len(arreglo2) - 1
    resultado = [0] * (len(arreglo1) + len(arreglo2))

    for i in range(len(arreglo1)-1, -1, -1):
        for j in range(len(arreglo2)-1, -1, -1):
            resultado[k] += arreglo1[i] * arreglo2[j]
            if resultado[k] > 9:
                if k == 0:
                    resultado.insert(0, 0)
                    pos += 1
                resultado[k-1] += resultado[k] // 10
                resultado[k] %= 10
            k -= 1
        k = pos
        pos -= 1
        k -= 1

    # Eliminar ceros a la izquierda
    while len(resultado) > 1 and resultado[0] == 0:
        del resultado[0]

    return resultado
