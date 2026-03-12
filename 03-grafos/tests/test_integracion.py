import unittest
from src.grafo_matriz import GrafoMatriz
from src.grafo_lista import GrafoLista
from src.dfs import dfs
from src.bfs import bfs

class TestIntegracion(unittest.TestCase):
    def test_conexo_matriz(self):
        g = GrafoMatriz(5)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        g.agregar_arista(2, 3)
        g.agregar_arista(3, 4)
        visitados = dfs(g, 0)
        self.assertEqual(len(visitados), 5)

    def test_conexo_lista(self):
        g = GrafoLista(5)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        g.agregar_arista(2, 3)
        g.agregar_arista(3, 4)
        visitados = bfs(g, 0)
        self.assertEqual(len(visitados), 5)

    def test_grafo_vacio(self):
        g = GrafoMatriz(3)
        visitados = dfs(g, 0)
        self.assertEqual(visitados, {0})

    def test_grafo_ciclico(self):
        g = GrafoLista(3)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        g.agregar_arista(2, 0)
        visitados = bfs(g, 0)
        self.assertSetEqual(visitados, {0, 1, 2})

if __name__ == "__main__":
    unittest.main()
