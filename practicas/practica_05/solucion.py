# Práctica 5: Grafos y BFS
# Nombre: 
# Número de cuenta:

from collections import deque


class Grafo:
    """Grafo implementado con lista de adyacencia."""
    
    def __init__(self, dirigido: bool = False):
        """
        Inicializa un grafo vacío.
        
        Args:
            dirigido: True si el grafo es dirigido, False si no
        """
        # TODO: Implementar
        pass
    
    def agregar_vertice(self, v: int) -> None:
        """Agrega un vértice al grafo."""
        # TODO: Implementar
        pass
    
    def agregar_arista(self, u: int, v: int) -> None:
        """
        Agrega una arista entre u y v.
        Si el grafo no es dirigido, agrega en ambas direcciones.
        """
        # TODO: Implementar
        pass
    
    def obtener_vecinos(self, v: int) -> list[int]:
        """Retorna la lista de vecinos del vértice v."""
        # TODO: Implementar
        pass
    
    def existe_arista(self, u: int, v: int) -> bool:
        """Verifica si existe una arista de u a v."""
        # TODO: Implementar
        pass
    
    def obtener_vertices(self) -> list[int]:
        """Retorna lista de todos los vértices."""
        # TODO: Implementar
        pass


def bfs(grafo: Grafo, inicio: int) -> list[int]:
    """
    Recorrido BFS desde el vértice inicio.
    
    Args:
        grafo: Grafo a recorrer
        inicio: Vértice inicial
        
    Returns:
        Lista de vértices en orden de visita BFS
    """
    # TODO: Implementar
    pass


def bfs_camino(grafo: Grafo, inicio: int, fin: int) -> list[int]:
    """
    Encuentra el camino más corto entre inicio y fin usando BFS.
    
    Args:
        grafo: Grafo a recorrer
        inicio: Vértice inicial
        fin: Vértice destino
        
    Returns:
        Lista de vértices del camino, o lista vacía si no existe
    """
    # TODO: Implementar
    pass


def niveles_bfs(grafo: Grafo, inicio: int) -> dict[int, int]:
    """
    Calcula la distancia desde inicio a cada vértice alcanzable.
    
    Args:
        grafo: Grafo a analizar
        inicio: Vértice inicial
        
    Returns:
        Diccionario {vertice: distancia}
    """
    # TODO: Implementar
    pass
