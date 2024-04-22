from . import JsonService as JS
import matplotlib.pyplot as plt
import numpy as np

json_times_file_path = "times3.json"

def exec():
    data = JS.read_json(json_times_file_path)
    labels = list(data.keys())
    values = list(data.values())

    # Ordenar los valores de manera descendente
    sorted_values = sorted(values, reverse=True)
    sorted_labels = [label for _, label in sorted(zip(values, labels), reverse=True)]

    # Asegurarse de que todas las listas tengan el mismo tamaño
    min_length = len(sorted_labels)
    sorted_labels = sorted_labels[:min_length]
    sorted_values = sorted_values[:min_length]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(min_length)
    width = 0.4
    rects = ax.bar(x - width/2, sorted_values, width)

    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Tiempo en segundos')
    ax.set_title('Comparación de tiempos algoritmos de ordenamiento')
    ax.set_xticks(x)
    ax.set_xticklabels(sorted_labels, rotation=90)
    plt.tight_layout()
    plt.show()