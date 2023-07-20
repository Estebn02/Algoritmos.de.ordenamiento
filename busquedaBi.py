import time

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def ejecutar_algoritmo1(datos, target):
    # Medir el tiempo de ejecución
    start_time = time.time()
    index = binarySearch(datos, target)
    end_time = time.time()

    # Devolver los resultados
    if index != -1:
        return f"El valor {target} se encuentra en la posición {index} de la lista."
    else:
        return f"El valor {target} no se encuentra en la lista."
    return "Tiempo de ejecución:", end_time - start_time, "segundos"

