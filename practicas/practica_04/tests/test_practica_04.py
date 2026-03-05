import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

MOD_PATH = Path(__file__).resolve().parents[1] / "solucion.py"
sol = SourceFileLoader("solucion", str(MOD_PATH)).load_module()


def test_linear_search_found():
    arr = [5, 3, 8, 1, 9]
    assert sol.linear_search(arr, 8) == 2


def test_linear_search_missing():
    arr = [1, 2, 3]
    assert sol.linear_search(arr, 10) == -1


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5, 6]
    assert sol.binary_search(arr, 4) == 3
    assert sol.binary_search(arr, 1) == 0
    assert sol.binary_search(arr, 6) == 5


def test_binary_search_missing():
    arr = [1, 3, 5, 7]
    assert sol.binary_search(arr, 4) == -1


def test_hashtable_basic():
    ht = sol.HashTable(size=5)
    assert ht.load_factor() == 0.0
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    assert ht.search("a") == 1
    assert ht.search("b") == 2
    assert ht.search("c") == 3
    assert ("a" in ht) is True
    assert ht.delete("b") is True
    assert ht.search("b") is None


def test_hashtable_update_and_resize():
    ht = sol.HashTable(size=3)
    ht.insert("x", 10)
    ht.insert("y", 20)
    ht.insert("z", 30)
    # update
    ht.insert("x", 11)
    assert ht.search("x") == 11
    old_lf = ht.load_factor()
    ht.resize(7)
    # after resize elements still present
    assert ht.search("x") == 11
    assert ht.search("y") == 20
    assert ht.search("z") == 30
    assert ht.load_factor() <= 1.0
