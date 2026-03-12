import unittest
from src.grafo_matriz import GrafoMatriz
from src.grafo_lista import GrafoLista
from src.bfs import bfs

class TestBFS(unittest.TestCase):
    def test_bfs_matriz(self):
        g = GrafoMatriz(4)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        visitados = bfs(g, 0)
        self.assertSetEqual(visitados, {0, 1, 2})

    def test_bfs_lista(self):
        g = GrafoLista(4)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 3)
        visitados = bfs(g, 0)
        self.assertSetEqual(visitados, {0, 1, 3})

    def test_bfs_ciclo(self):
        g = GrafoLista(3)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        g.agregar_arista(2, 0)
        visitados = bfs(g, 0)
        self.assertSetEqual(visitados, {0, 1, 2})

if __name__ == "__main__":
    unittest.main()
