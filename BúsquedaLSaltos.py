import math
import time

def linearJumpSearch(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1

def ejecutar_algoritmo2(datos, target):
    # Medir el tiempo de ejecución
    start_time = time.time()
    index = linearJumpSearch(datos, target)
    end_time = time.time()

    # Devolver los resultados
    if index != -1:
        return f"El valor {target} se encuentra en la posición {index} de la lista."
    else:
        return f"El valor {target} no se encuentra en la lista."
    return "Tiempo de ejecución:", end_time - start_time, "segundos"

