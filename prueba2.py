import time
import random

# Implementación de los algoritmos de búsqueda y ordenamiento

# Búsqueda Binaria
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Búsqueda Lineal por Saltos
def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return False

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return False

    if arr[prev] == target:
        return True

    return False

# QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# MergeSort
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Experimento de análisis empírico

# Generación de datos de prueba
data_sizes = [100, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
num_executions = 2  # Número de ejecuciones por tamaño de datos

# Tabla para almacenar los tiempos de ejecución
table = [["Tamaño"] + data_sizes]  # Encabezado de la tabla

# Búsqueda Binaria vs Búsqueda Lineal por Saltos
binary_search_times = []
jump_search_times = []

# Generar datos de prueba
max_value = 1000000  # Valor máximo de los datos generados

for size in data_sizes:
    row_binary_search = []
    row_jump_search = []

    for _ in range(num_executions):
        test_data = [random.randint(0, max_value) for _ in range(size)]  # Generar datos de prueba para cada ejecución

        target = random.choice(test_data)

        start_time = time.time()
        binary_search(test_data, target)
        elapsed_time = time.time() - start_time
        row_binary_search.append(elapsed_time)

        start_time = time.time()
        jump_search(test_data, target)
        elapsed_time = time.time() - start_time
        row_jump_search.append(elapsed_time)

    binary_search_times.append(row_binary_search)
    jump_search_times.append(row_jump_search)

# QuickSort vs MergeSort
quicksort_times = []
mergesort_times = []

for size in data_sizes:
    row_quicksort = []
    row_mergesort = []

    for _ in range(num_executions):
        test_data = [random.randint(0, max_value) for _ in range(size)]  # Generar datos de prueba para cada ejecución

        start_time = time.time()
        quicksort(test_data)
        elapsed_time = time.time() - start_time
        row_quicksort.append(elapsed_time)

        start_time = time.time()
        mergesort(test_data)
        elapsed_time = time.time() - start_time
        row_mergesort.append(elapsed_time)

    quicksort_times.append(row_quicksort)
    mergesort_times.append(row_mergesort)

# Calcular la media aritmética de las mediciones
binary_search_averages = [sum(times) / num_executions for times in binary_search_times]
jump_search_averages = [sum(times) / num_executions for times in jump_search_times]
quicksort_averages = [sum(times) / num_executions for times in quicksort_times]
mergesort_averages = [sum(times) / num_executions for times in mergesort_times]

# Agregar las medias a la tabla
table.append(["Media Búsqueda Binaria"] + binary_search_averages)
table.append(["Media Búsqueda Lineal"] + jump_search_averages)
table.append(["Media QuickSort"] + quicksort_averages)
table.append(["Media MergeSort"] + mergesort_averages)

# Imprimir la tabla
for row in table:
    print("\t".join(str(val) for val in row))
