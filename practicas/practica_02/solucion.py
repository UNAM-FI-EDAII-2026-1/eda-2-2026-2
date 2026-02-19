# Práctica 2: Merge Sort y Quick Sort
# Nombre: 
# Número de cuenta:

# ============== MERGE SORT ==============

def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.
    
    Args:
        left: Lista ordenada izquierda
        right: Lista ordenada derecha
        
    Returns:
        Lista fusionada y ordenada
    """
    # TODO: Implementar
    pass


def merge_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista usando Merge Sort.
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    # TODO: Implementar
    pass


# ============== QUICK SORT ==============

def partition(arr: list[int], low: int, high: int) -> int:
    """
    Particiona el arreglo usando el último elemento como pivote.
    
    Args:
        arr: Lista a particionar
        low: Índice inicial
        high: Índice final (pivote)
        
    Returns:
        Índice final del pivote
    """
    # TODO: Implementar
    pass


def quick_sort_inplace(arr: list[int], low: int = 0, high: int = None) -> None:
    """
    Ordena usando Quick Sort in-place.
    Modifica la lista original.
    
    Args:
        arr: Lista a ordenar
        low: Índice inicial
        high: Índice final
    """
    # TODO: Implementar
    pass


def quick_sort(arr: list[int]) -> list[int]:
    """
    Ordena usando Quick Sort (versión que retorna nueva lista).
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    # TODO: Implementar
    pass


# ============== QUICK SORT PIVOTE ALEATORIO ==============

def quick_sort_random_pivot(arr: list[int]) -> list[int]:
    """
    Quick Sort con selección aleatoria de pivote.
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    # TODO: Implementar
    pass
