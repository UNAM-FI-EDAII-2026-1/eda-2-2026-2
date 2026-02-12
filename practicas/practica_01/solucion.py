# Práctica 1: Insertion Sort
# Nombre: 
# Número de cuenta:

def insertion_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista usando Insertion Sort.
    
    Args:
        arr: Lista de enteros a ordenar
        
    Returns:
        Lista ordenada (modifica in-place y retorna la misma lista)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    pass


def insertion_sort_desc(arr: list[int]) -> list[int]:
    """
    Ordena una lista de mayor a menor usando Insertion Sort.
    
    Args:
        arr: Lista de enteros a ordenar
        
    Returns:
        Lista ordenada de mayor a menor
    """
    # TODO: Implementar
    pass


def insertion_sort_count(arr: list[int]) -> tuple[list[int], int]:
    """
    Ordena y cuenta el número de comparaciones realizadas.
    
    Args:
        arr: Lista de enteros a ordenar
        
    Returns:
        Tupla (lista_ordenada, num_comparaciones)
    """
    # TODO: Implementar
    pass
