# Práctica 4: Tablas Hash
# Nombre: 
# Número de cuenta:

from typing import Any, Optional


def hash_function(key: str, size: int) -> int:
    """
    Simple hash: sum of character ordinals modulo size.
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return sum(ord(c) for c in key) % size


def linear_search(arr: list, target: Any) -> int:
    """Return the index of target in arr or -1 if not found."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr: list, target: Any) -> int:
    """Assumes arr is sorted. Return the index of target or -1 if not found."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


class HashTable:
    """Hash table with chaining (list of buckets)."""

    def __init__(self, size: int = 10):
        if size <= 0:
            raise ValueError("size must be > 0")
        self._size = size
        self._buckets: list[list[tuple[str, Any]]] = [[] for _ in range(size)]
        self._count = 0

    def insert(self, key: str, value: Any) -> None:
        idx = hash_function(key, self._size)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def search(self, key: str) -> Optional[Any]:
        idx = hash_function(key, self._size)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        idx = hash_function(key, self._size)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return True
        return False

    def __contains__(self, key: str) -> bool:
        return self.search(key) is not None

    def load_factor(self) -> float:
        return self._count / self._size

    def resize(self, new_size: int) -> None:
        if new_size <= 0:
            raise ValueError("new_size must be > 0")
        old_items = []
        for bucket in self._buckets:
            for k, v in bucket:
                old_items.append((k, v))
        self._size = new_size
        self._buckets = [[] for _ in range(new_size)]
        self._count = 0
        for k, v in old_items:
            self.insert(k, v)

