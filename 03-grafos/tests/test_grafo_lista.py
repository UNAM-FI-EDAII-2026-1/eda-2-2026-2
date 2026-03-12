import unittest
from src.grafo_lista import GrafoLista

class TestGrafoLista(unittest.TestCase):
    def test_agregar_arista(self):
        g = GrafoLista(3)
        g.agregar_arista(0, 1)
        self.assertIn(1, g.lista[0])
        self.assertIn(0, g.lista[1])

    def test_vecinos(self):
        g = GrafoLista(3)
        g.agregar_arista(1, 2)
        self.assertListEqual(g.vecinos(1), [2])

    def test_grafo_dirigido(self):
        g = GrafoLista(3, dirigido=True)
        g.agregar_arista(0, 1)
        self.assertNotIn(0, g.lista[1])

if __name__ == "__main__":
    unittest.main()
