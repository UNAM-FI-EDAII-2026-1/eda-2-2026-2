# Práctica 5: Grafos y BFS

## Objetivos
- Implementar representación de grafos (lista de adyacencia)
- Implementar BFS (Búsqueda en anchura)
- Encontrar caminos más cortos en grafos no ponderados

## Fecha límite
**Semana 6 - Viernes**

## Ejercicios

### Ejercicio 1: Grafo con lista de adyacencia (40 pts)

```python
class Grafo:
    def __init__(self, dirigido: bool = False):
        """Inicializa grafo vacío."""
        pass
    
    def agregar_vertice(self, v: int) -> None:
        """Agrega un vértice al grafo."""
        pass
    
    def agregar_arista(self, u: int, v: int) -> None:
        """Agrega arista entre u y v."""
        pass
    
    def obtener_vecinos(self, v: int) -> list[int]:
        """Retorna lista de vecinos de v."""
        pass
    
    def existe_arista(self, u: int, v: int) -> bool:
        """Verifica si existe arista entre u y v."""
        pass
```

### Ejercicio 2: BFS (40 pts)

```python
def bfs(grafo: Grafo, inicio: int) -> list[int]:
    """
    Recorrido BFS desde el vértice inicio.
    Retorna lista de vértices en orden de visita.
    """
    pass

def bfs_camino(grafo: Grafo, inicio: int, fin: int) -> list[int]:
    """
    Encuentra el camino más corto entre inicio y fin.
    Retorna lista de vértices del camino, o lista vacía si no existe.
    """
    pass
```

### Ejercicio 3: Aplicación (20 pts)

```python
def niveles_bfs(grafo: Grafo, inicio: int) -> dict[int, int]:
    """
    Calcula la distancia (en aristas) desde inicio a cada vértice.
    Retorna diccionario {vertice: distancia}.
    """
    pass
```
