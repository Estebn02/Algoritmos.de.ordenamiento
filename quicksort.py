import random
import time

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def sort(arr):
    quickSort(arr, 0, len(arr) - 1)

def ejecutar_algoritmo4(datos):
    # Medir el tiempo de ejecución
    start_time = time.time()
    sort(datos)
    end_time = time.time()

    # Devolver los resultados
    return f"Lista ordenada:\n{datos}\nTiempo de ejecución: {end_time - start_time} segundos"
