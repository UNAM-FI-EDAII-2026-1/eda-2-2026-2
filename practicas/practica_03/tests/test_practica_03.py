import sys
from pathlib import Path
import random

# Ensure the practica_03 folder is importable (so we can import solucion.py)
HERE = Path(__file__).resolve().parent
PRAC_DIR = HERE.parent
sys.path.insert(0, str(PRAC_DIR))

from solucion import heap_sort, counting_sort, radix_sort


def test_heap_sort_basic():
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
    assert heap_sort([3, 1, 2]) == [1, 2, 3]
    assert heap_sort([5, 3, 5, 2, 8, 1]) == sorted([5, 3, 5, 2, 8, 1])
    assert heap_sort(list(range(10, 0, -1))) == list(range(1, 11))


def test_counting_sort_basic():
    assert counting_sort([]) == []
    assert counting_sort([0]) == [0]
    assert counting_sort([3, 1, 2, 1, 0]) == [0, 1, 1, 2, 3]
    assert counting_sort([5, 3, 5, 2, 8, 1]) == sorted([5, 3, 5, 2, 8, 1])


def test_radix_sort_basic():
    assert radix_sort([]) == []
    assert radix_sort([0]) == [0]
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == sorted([170, 45, 75, 90, 802, 24, 2, 66])


def test_random_equivalence_counting_radix():
    # generate random non-negative integers
    for _ in range(10):
        arr = [random.randint(0, 1000) for _ in range(50)]
        a = counting_sort(arr.copy())
        b = radix_sort(arr.copy())
        c = sorted(arr)
        assert a == c
        assert b == c
