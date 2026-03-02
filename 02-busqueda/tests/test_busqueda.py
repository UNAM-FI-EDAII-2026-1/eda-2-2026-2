import unittest
from src.main import busqueda_lineal, busqueda_lineal_recursiva, busqueda_binaria, busqueda_binaria_recursiva

class TestBusqueda(unittest.TestCase):
    def test_busqueda_lineal(self):
        lista = [3, 5, 7, 9, 11]
        self.assertEqual(busqueda_lineal(lista, 7), 2)
        self.assertEqual(busqueda_lineal(lista, 3), 0)
        self.assertEqual(busqueda_lineal(lista, 11), 4)
        self.assertEqual(busqueda_lineal(lista, 4), -1)

    def test_busqueda_lineal_recursiva(self):
        lista = [3, 5, 7, 9, 11]
        self.assertEqual(busqueda_lineal_recursiva(lista, 7), 2)
        self.assertEqual(busqueda_lineal_recursiva(lista, 3), 0)
        self.assertEqual(busqueda_lineal_recursiva(lista, 11), 4)
        self.assertEqual(busqueda_lineal_recursiva(lista, 4), -1)

    def test_busqueda_binaria(self):
        lista = [1, 2, 4, 8, 16, 32]
        self.assertEqual(busqueda_binaria(lista, 8), 3)
        self.assertEqual(busqueda_binaria(lista, 1), 0)
        self.assertEqual(busqueda_binaria(lista, 32), 5)
        self.assertEqual(busqueda_binaria(lista, 7), -1)

    def test_busqueda_binaria_recursiva(self):
        lista = [1, 2, 4, 8, 16, 32]
        self.assertEqual(busqueda_binaria_recursiva(lista, 8), 3)
        self.assertEqual(busqueda_binaria_recursiva(lista, 1), 0)
        self.assertEqual(busqueda_binaria_recursiva(lista, 32), 5)
        self.assertEqual(busqueda_binaria_recursiva(lista, 7), -1)

if __name__ == "__main__":
    unittest.main()
