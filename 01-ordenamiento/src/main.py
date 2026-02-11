def bubble_sort(arr):
    ## codifo del bubble
    return 

def merge_sort(arr):
    ## codigo del merge sort
    return 

## def merge(...) ## crea el merge del merge sort aqui!

def quick_sort(arr):
    """
    Implementa el algoritmo Quick Sort.
    
    Args:
        arr (List[int]): Lista de números a ordenar
        
    Returns:
        List[int]: Lista ordenada
    """
    ## Tu implementación aquí
    return None

def heapify(arr, n, i):
    """
    Función auxiliar para heap_sort que mantiene la propiedad de heap.
    """
    ## Tu implementación aquí
    pass

def heap_sort(arr):
    """
    Implementa el algoritmo Heap Sort.
    
    Args:
        arr (List[int]): Lista de números a ordenar
        
    Returns:
        List[int]: Lista ordenada
    """
    ## Tu implementación aquí
    return None

def counting_sort(arr):
    """
    Implementa el algoritmo Counting Sort.
    
    Args:
        arr (List[int]): Lista de números no negativos a ordenar
        
    Returns:
        List[int]: Lista ordenada
        
    Ejemplo:
        >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
    """
    ## Tu implementación aquí
    return None

def counting_sort_for_radix(arr, exp):
    """
    Implementa Counting Sort modificado para ser usado en Radix Sort.
    
    Args:
        arr (List[int]): Lista de números a ordenar
        exp (int): Exponente para obtener el dígito actual (1, 10, 100, etc.)
        
    Returns:
        List[int]: Lista ordenada por el dígito actual
    """
    ## Tu implementación aquí
    return arr

def radix_sort(arr):
    """
    Implementa el algoritmo Radix Sort usando el método LSD (Least Significant Digit).
    
    Args:
        arr (List[int]): Lista de números no negativos a ordenar
        
    Returns:
        List[int]: Lista ordenada
        
    Ejemplo:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    ## Tu implementación aquí
    return None

# Example usage
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(sample_array.copy()))
    print("Merge Sort:", merge_sort(sample_array.copy()))
    print("Quick Sort:", quick_sort(sample_array.copy()))
    print("Heap Sort:", heap_sort(sample_array.copy()))
    print("Counting Sort:", counting_sort(sample_array.copy()))
    print("Radix Sort:", radix_sort(sample_array.copy()))
