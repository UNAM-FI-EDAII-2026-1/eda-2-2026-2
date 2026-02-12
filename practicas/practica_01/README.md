# Práctica 1: Insertion Sort

## Objetivos
- Implementar el algoritmo Insertion Sort
- Analizar su complejidad temporal y espacial
- Comparar rendimiento con diferentes tipos de entrada

## Fecha límite
**Semana 1 - Viernes**

## Descripción

Insertion Sort es un algoritmo de ordenamiento simple que construye la secuencia ordenada elemento por elemento. Es eficiente para listas pequeñas y parcialmente ordenadas.

### Complejidad
- **Mejor caso:** O(n) - lista ya ordenada
- **Caso promedio:** O(n²)
- **Peor caso:** O(n²) - lista en orden inverso
- **Espacio:** O(1) - in-place

## Ejercicios

### Ejercicio 1: Implementación básica (40 pts)

Implementa la función `insertion_sort(arr)` que ordene una lista de números enteros de menor a mayor.

```python
def insertion_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista usando Insertion Sort.
    
    Args:
        arr: Lista de enteros a ordenar
        
    Returns:
        Lista ordenada (modifica in-place y retorna la misma lista)
    """
    pass
```

### Ejercicio 2: Ordenamiento descendente (20 pts)

Implementa `insertion_sort_desc(arr)` que ordene de mayor a menor.

```python
def insertion_sort_desc(arr: list[int]) -> list[int]:
    """Ordena una lista de mayor a menor usando Insertion Sort."""
    pass
```

### Ejercicio 3: Contador de comparaciones (20 pts)

Implementa `insertion_sort_count(arr)` que retorne una tupla con la lista ordenada y el número de comparaciones realizadas.

```python
def insertion_sort_count(arr: list[int]) -> tuple[list[int], int]:
    """
    Ordena y cuenta comparaciones.
    
    Returns:
        Tupla (lista_ordenada, num_comparaciones)
    """
    pass
```

### Ejercicio 4: Análisis experimental (20 pts)

En el archivo `analisis.py`, genera gráficas del tiempo de ejecución para:
- Listas aleatorias de tamaño n = 100, 500, 1000, 2000, 5000
- Listas ya ordenadas (mejor caso)
- Listas en orden inverso (peor caso)

## Archivos a entregar

```
practica_01/
├── solucion.py      # Tu implementación
├── analisis.py      # Código del análisis experimental
└── analisis.png     # Gráfica generada
```

## Ejecución de tests

```bash
cd practicas/practica_01
pytest tests/
```

## Rúbrica

| Criterio | Puntos |
|----------|--------|
| Ejercicio 1: Implementación correcta | 40 |
| Ejercicio 2: Ordenamiento descendente | 20 |
| Ejercicio 3: Contador de comparaciones | 20 |
| Ejercicio 4: Análisis experimental | 20 |
| **Total** | **100** |
