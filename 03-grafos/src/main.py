from grafo_matriz import GrafoMatriz
from grafo_lista import GrafoLista
from dfs import dfs
from bfs import bfs

if __name__ == "__main__":
    print("Ejemplo con matriz de adyacencia:")
    gm = GrafoMatriz(5)
    gm.agregar_arista(0, 1)
    gm.agregar_arista(0, 2)
    gm.agregar_arista(1, 3)
    gm.agregar_arista(3, 4)
    print("DFS:", dfs(gm, 0))
    print("BFS:", bfs(gm, 0))

    print("\nEjemplo con listas ligadas:")
    gl = GrafoLista(5)
    gl.agregar_arista(0, 1)
    gl.agregar_arista(0, 2)
    gl.agregar_arista(1, 3)
    gl.agregar_arista(3, 4)
    print("DFS:", dfs(gl, 0))
    print("BFS:", bfs(gl, 0))
