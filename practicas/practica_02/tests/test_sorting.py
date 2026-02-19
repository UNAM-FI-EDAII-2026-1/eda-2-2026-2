"""
Tests para Práctica 2: Merge Sort y Quick Sort
"""
import pytest
import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solucion import (
    merge, merge_sort, 
    partition, quick_sort, quick_sort_inplace,
    quick_sort_random_pivot
)


class TestMerge:
    """Tests para la función merge"""
    
    def test_merge_vacias(self):
        assert merge([], []) == []
    
    def test_merge_una_vacia(self):
        assert merge([1, 2], []) == [1, 2]
        assert merge([], [3, 4]) == [3, 4]
    
    def test_merge_un_elemento(self):
        assert merge([1], [2]) == [1, 2]
        assert merge([2], [1]) == [1, 2]
    
    def test_merge_intercalado(self):
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    
    def test_merge_consecutivo(self):
        assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


class TestMergeSort:
    """Tests para merge_sort"""
    
    def test_lista_vacia(self):
        assert merge_sort([]) == []
    
    def test_un_elemento(self):
        assert merge_sort([5]) == [5]
    
    def test_lista_ordenada(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_lista_inversa(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_lista_aleatoria(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_elementos_repetidos(self):
        assert merge_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]
    
    def test_negativos(self):
        assert merge_sort([-3, 1, -4, 2, 0]) == [-4, -3, 0, 1, 2]
    
    def test_estabilidad(self):
        """Merge Sort debe ser estable"""
        arr = list(range(100))
        random.shuffle(arr)
        assert merge_sort(arr) == list(range(100))


class TestQuickSort:
    """Tests para quick_sort"""
    
    def test_lista_vacia(self):
        assert quick_sort([]) == []
    
    def test_un_elemento(self):
        assert quick_sort([5]) == [5]
    
    def test_lista_ordenada(self):
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_lista_inversa(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_lista_aleatoria(self):
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_elementos_repetidos(self):
        assert quick_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]
    
    def test_negativos(self):
        assert quick_sort([-3, 1, -4, 2, 0]) == [-4, -3, 0, 1, 2]


class TestQuickSortInplace:
    """Tests para quick_sort_inplace"""
    
    def test_lista_vacia(self):
        arr = []
        quick_sort_inplace(arr)
        assert arr == []
    
    def test_lista_aleatoria(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        quick_sort_inplace(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_modifica_original(self):
        arr = [5, 4, 3, 2, 1]
        original_id = id(arr)
        quick_sort_inplace(arr)
        assert id(arr) == original_id  # Debe ser la misma lista
        assert arr == [1, 2, 3, 4, 5]


class TestQuickSortRandomPivot:
    """Tests para quick_sort con pivote aleatorio"""
    
    def test_lista_vacia(self):
        assert quick_sort_random_pivot([]) == []
    
    def test_lista_ordenada(self):
        assert quick_sort_random_pivot([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_lista_inversa(self):
        assert quick_sort_random_pivot([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_lista_grande(self):
        arr = list(range(1000))
        random.shuffle(arr)
        assert quick_sort_random_pivot(arr) == list(range(1000))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
