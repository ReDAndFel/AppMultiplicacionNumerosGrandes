def multiplicar(arreglo1, arreglo2):
    """
    Hindu iterative static multiplication algorithm
    """
    result = [0] * (len(arreglo1) + len(arreglo2))

    for i, digit1 in enumerate(reversed(arreglo1)):
        for j, digit2 in enumerate(reversed(arreglo2)):
            result[i + j] += digit1 * digit2
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    return result[::-1]