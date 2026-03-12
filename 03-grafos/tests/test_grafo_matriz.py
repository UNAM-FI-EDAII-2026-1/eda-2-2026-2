import unittest
from src.grafo_matriz import GrafoMatriz

class TestGrafoMatriz(unittest.TestCase):
    def test_agregar_arista(self):
        g = GrafoMatriz(3)
        g.agregar_arista(0, 1)
        self.assertEqual(g.matriz[0][1], 1)
        self.assertEqual(g.matriz[1][0], 1)

    def test_vecinos(self):
        g = GrafoMatriz(3)
        g.agregar_arista(0, 2)
        self.assertListEqual(g.vecinos(0), [2])

    def test_grafo_dirigido(self):
        g = GrafoMatriz(3, dirigido=True)
        g.agregar_arista(0, 1)
        self.assertEqual(g.matriz[1][0], 0)

if __name__ == "__main__":
    unittest.main()
