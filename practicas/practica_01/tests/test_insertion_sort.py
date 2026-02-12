"""
Tests para Práctica 1: Insertion Sort
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solucion import insertion_sort, insertion_sort_desc, insertion_sort_count


class TestInsertionSort:
    """Tests para insertion_sort básico"""
    
    def test_lista_vacia(self):
        assert insertion_sort([]) == []
    
    def test_un_elemento(self):
        assert insertion_sort([5]) == [5]
    
    def test_dos_elementos_ordenados(self):
        assert insertion_sort([1, 2]) == [1, 2]
    
    def test_dos_elementos_desordenados(self):
        assert insertion_sort([2, 1]) == [1, 2]
    
    def test_lista_ordenada(self):
        assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_lista_inversa(self):
        assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_lista_aleatoria(self):
        assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_elementos_repetidos(self):
        assert insertion_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]
    
    def test_negativos(self):
        assert insertion_sort([-3, 1, -4, 2, 0]) == [-4, -3, 0, 1, 2]
    
    def test_lista_grande(self):
        import random
        arr = list(range(100))
        random.shuffle(arr)
        assert insertion_sort(arr) == list(range(100))


class TestInsertionSortDesc:
    """Tests para insertion_sort_desc (ordenamiento descendente)"""
    
    def test_lista_vacia(self):
        assert insertion_sort_desc([]) == []
    
    def test_un_elemento(self):
        assert insertion_sort_desc([5]) == [5]
    
    def test_lista_ordenada_asc(self):
        assert insertion_sort_desc([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    
    def test_lista_ordenada_desc(self):
        assert insertion_sort_desc([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    
    def test_lista_aleatoria(self):
        assert insertion_sort_desc([3, 1, 4, 1, 5]) == [5, 4, 3, 1, 1]
    
    def test_negativos(self):
        assert insertion_sort_desc([-3, 1, -4, 2, 0]) == [2, 1, 0, -3, -4]


class TestInsertionSortCount:
    """Tests para insertion_sort_count (cuenta comparaciones)"""
    
    def test_lista_vacia(self):
        arr, count = insertion_sort_count([])
        assert arr == []
        assert count == 0
    
    def test_un_elemento(self):
        arr, count = insertion_sort_count([5])
        assert arr == [5]
        assert count == 0
    
    def test_lista_ordenada(self):
        """En lista ordenada, solo n-1 comparaciones (una por elemento)"""
        arr, count = insertion_sort_count([1, 2, 3, 4, 5])
        assert arr == [1, 2, 3, 4, 5]
        assert count == 4  # n-1 comparaciones en mejor caso
    
    def test_lista_inversa(self):
        """En lista inversa, comparaciones = n(n-1)/2"""
        arr, count = insertion_sort_count([5, 4, 3, 2, 1])
        assert arr == [1, 2, 3, 4, 5]
        assert count == 10  # 4+3+2+1 = 10 comparaciones
    
    def test_resultado_ordenado(self):
        arr, count = insertion_sort_count([3, 1, 4, 1, 5, 9, 2, 6])
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
        assert count > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
