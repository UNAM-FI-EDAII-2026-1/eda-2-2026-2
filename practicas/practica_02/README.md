# Práctica 2: Merge Sort y Quick Sort

## Objetivos
- Implementar algoritmos de ordenamiento con estrategia divide y vencerás
- Entender las diferencias entre Merge Sort y Quick Sort
- Analizar complejidad y comportamiento con diferentes entradas

## Fecha límite
**1 semana despues de hacer merge de tu PR**

## Descripción

### Merge Sort
Algoritmo que divide la lista en mitades, ordena recursivamente y fusiona.
- **Complejidad:** O(n log n) en todos los casos
- **Espacio:** O(n) - requiere memoria auxiliar

### Quick Sort
Algoritmo que selecciona un pivote, particiona y ordena recursivamente.
- **Mejor/Promedio:** O(n log n)
- **Peor caso:** O(n²) - pivote mal elegido
- **Espacio:** O(log n) para la pila de recursión

## Ejercicios

### Ejercicio 1: Merge Sort (30 pts)

```python
def merge_sort(arr: list[int]) -> list[int]:
    """
    Ordena usando Merge Sort.
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Nueva lista ordenada
    """
    pass

def merge(left: list[int], right: list[int]) -> list[int]:
    """Fusiona dos listas ordenadas en una sola lista ordenada."""
    pass
```

### Ejercicio 2: Quick Sort (30 pts)

```python
def quick_sort(arr: list[int]) -> list[int]:
    """
    Ordena usando Quick Sort (versión que retorna nueva lista).
    """
    pass

def quick_sort_inplace(arr: list[int], low: int = 0, high: int = None) -> None:
    """
    Ordena usando Quick Sort in-place.
    Modifica la lista original.
    """
    pass

def partition(arr: list[int], low: int, high: int) -> int:
    """
    Particiona el arreglo y retorna el índice del pivote.
    Usa el último elemento como pivote.
    """
    pass
```

### Ejercicio 3: Comparación experimental (20 pts)

En `comparacion.py`, compara el tiempo de ejecución de ambos algoritmos:
- Listas aleatorias: n = 1000, 5000, 10000, 20000
- Genera una gráfica comparativa

### Ejercicio 4: Quick Sort con pivote aleatorio (20 pts)

```python
def quick_sort_random_pivot(arr: list[int]) -> list[int]:
    """
    Quick Sort con selección aleatoria de pivote.
    Reduce la probabilidad del peor caso.
    """
    pass
```

## Archivos a entregar

```
practica_02/
├── solucion.py       # Implementaciones
├── comparacion.py    # Análisis experimental
└── comparacion.png   # Gráfica
```

## Ejecución de tests

```bash
cd practicas/practica_02
pytest tests/
```

## Rúbrica

| Criterio | Puntos |
|----------|--------|
| Merge Sort correcto | 30 |
| Quick Sort correcto | 30 |
| Comparación experimental | 20 |
| Quick Sort pivote aleatorio | 20 |
| **Total** | **100** |


## NO OLVIDES HACER TU REPORTE! --- OJO SUPER IMPORTANTE
