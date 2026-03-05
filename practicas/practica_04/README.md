# Práctica 4: Tablas Hash

## Objetivos
- Implementar una tabla hash con encadenamiento
- Implementar funciones hash básicas
- Manejar colisiones correctamente

## Fecha límite
**Semana 4 - Viernes**

## Exercises

This practice now contains three tasks. Implement the following in `solucion.py`:

1) Linear search (20 pts)

```python
def linear_search(arr: list, target: any) -> int:
    """Return the index of target in arr or -1 if not found."""
```

2) Binary search (30 pts)

```python
def binary_search(arr: list, target: any) -> int:
    """Assumes arr is sorted. Return the index of target or -1."""
```

3) Hash table with chaining (50 pts)

Implement a `HashTable` class with the following behaviour:

- `hash_function(key: str, size: int) -> int`: sum of character codes modulo size.
- `HashTable.insert(key, value)`: insert or update.
- `HashTable.search(key)`: return value or None.
- `HashTable.delete(key)`: remove key, return True if removed else False.
- `HashTable.__contains__(key)`: support `key in table`.
- `HashTable.load_factor()`: current number of elements / table size.
- `HashTable.resize(new_size)`: resize and rehash existing elements.

Place your implementations in `solucion.py`. Tests are provided in `tests/` and will be executed by CI.

---
You can run the tests locally from the repository root:

```bash
python -m pytest practicas/practica_04/tests -q
```
