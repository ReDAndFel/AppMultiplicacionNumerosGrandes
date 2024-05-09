# App realizada por el equipo de trabajo apoyados con IA

from . import JsonService as JS

import matplotlib.pyplot as plt
import numpy as np

json_times_file_path = "times3.json"

def exec():
    data = JS.read_json(json_times_file_path)
    labels = list(data.keys())
    values = list(data.values())

    # Ordenar los valores junto con las etiquetas de forma ascendente
    sorted_data = sorted(zip(labels, values), key=lambda x: x[1])

    # Extraer las etiquetas y los valores ordenados
    sorted_labels, sorted_values = zip(*sorted_data)

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(sorted_labels))
    width = 0.4

    rects = ax.bar(x - width/2, sorted_values, width)

    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Tiempo en segundos')
    ax.set_title('Comparación de tiempos algoritmos de ordenamiento')
    ax.set_xticks(x)
    ax.set_xticklabels(sorted_labels, rotation=90)

    plt.tight_layout()
    plt.show()