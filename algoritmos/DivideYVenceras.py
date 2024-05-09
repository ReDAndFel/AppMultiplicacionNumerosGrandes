def ajustar_tamanio(arreglo1, arreglo2):
    # Obtener la longitud máxima de los dos arreglos y asegurarse de que sea par
    max_length = max(len(arreglo1), len(arreglo2))
    if max_length % 2 != 0:
        max_length += 1

    # Ajustar el tamaño del arreglo 1
    if len(arreglo1) < max_length:
        arreglo1 = [0] * (max_length - len(arreglo1)) + arreglo1

    # Ajustar el tamaño del arreglo 2
    if len(arreglo2) < max_length:
        arreglo2 = [0] * (max_length - len(arreglo2)) + arreglo2

    return arreglo1, arreglo2

def arreglo_a_numero(arreglo):
    return int(''.join(map(str, arreglo)))

def multiplicar(arreglo1, arreglo2):
    arreglo1, arreglo2 = ajustar_tamanio(arreglo1, arreglo2)

    # Obtener el tamaño de los arreglos
    n = len(arreglo1)

    if n == 2:  # Caso base, usar algoritmo clásico
        resultado = [0] * (len(arreglo1) + len(arreglo2) - 1)
        for i in range(len(arreglo1)):
            for j in range(len(arreglo2)):
                resultado[i + j] += arreglo1[i] * arreglo2[j]
        return resultado

    # Obtener las mitades de los arreglos
    mitad = n // 2

    # Dividir los arreglos en mitades izquierda y derecha
    w = arreglo1[:mitad]
    x = arreglo1[mitad:]
    y = arreglo2[:mitad]
    z = arreglo2[mitad:]

    a=multiplicar(w,y)
    b=multiplicar(w,z)
    c=multiplicar(x,y)
    d=multiplicar(x,z)


    for _ in range(n):
        a.append(0)
    for _ in range(n//2):
        b.append(0)
        c.append(0)

    # Calculamos la longitud máxima
    max_len = max(len(a), len(b), len(c), len(d))

    # Aseguramos que todos los arrays tengan la misma longitud
    a = [0] * (max_len - len(a)) + a
    b = [0] * (max_len - len(b)) + b
    c = [0] * (max_len - len(c)) + c
    d = [0] * (max_len - len(d)) + d

    # Inicializamos el array resultante como una lista vacía
    resultado = []

    # Inicializamos el acarreo como 0
    carry = 0

    # Iteramos desde la última posición hasta la primera
    for i in range(max_len - 1, -1, -1):
        # Sumamos los elementos de los cuatro arrays y el acarreo
        suma = a[i] + b[i] + c[i] + d[i] + carry

        # Actualizamos el acarreo y el resultado
        carry = suma // 10
        resultado.insert(0, suma % 10)  # Insertamos el dígito en la posición 0 del resultado

    # Si aún queda un acarreo al final, lo añadimos al resultado
    if carry:
        resultado.insert(0, carry)

    indice_inicio = 0
    while indice_inicio < len(resultado) and resultado[indice_inicio] == 0:
        indice_inicio += 1

    return resultado[indice_inicio:]

    # Realizar las operaciones según la fórmula dada
    #resultado = ((10 ** n) * w * y) + ((10 ** (n // 2)) * w * z) + ((10 ** (n // 2))* x * y) + x * z