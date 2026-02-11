import random
import time
from typing import List, Callable

def generate_random_data(size: int) -> List[int]:
    """
    Genera una lista de números enteros aleatorios.
    
    Args:
        size: Tamaño de la lista a generar
        
    Returns:
        Lista de enteros aleatorios
    """
    return [random.randint(0, 10000) for _ in range(size)]

def generate_nearly_sorted(size: int, swaps: int = None) -> List[int]:
    """
    Genera una lista casi ordenada, haciendo algunos intercambios aleatorios.
    
    Args:
        size: Tamaño de la lista
        swaps: Número de intercambios (default: size//10)
        
    Returns:
        Lista casi ordenada
    """
    if swaps is None:
        swaps = size // 10
        
    arr = list(range(size))
    for _ in range(swaps):
        i = random.randint(0, size-2)
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def generate_reversed(size: int) -> List[int]:
    """
    Genera una lista ordenada inversamente.
    
    Args:
        size: Tamaño de la lista
        
    Returns:
        Lista ordenada inversamente
    """
    return list(range(size, 0, -1))

def measure_time(func: Callable, arr: List[int]) -> float:
    """
    Mide el tiempo de ejecución de un algoritmo.
    
    Args:
        func: Función a medir (algoritmo de ordenamiento)
        arr: Lista a ordenar
        
    Returns:
        Tiempo de ejecución en segundos
    """
    arr_copy = arr.copy()  # No modificar el arreglo original
    start_time = time.time()
    func(arr_copy)
    end_time = time.time()
    return end_time - start_time
