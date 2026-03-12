import pytest

from practicas.practica_05.solucion import Grafo, bfs, bfs_camino, niveles_bfs


def build_sample_graph(directed: bool = False):
    # Grafo de ejemplo:
    # 1 -- 2 -- 4
    # |    |
    # 3    5
    g = Grafo(dirigido=directed)
    for v in [1, 2, 3, 4, 5]:
        g.agregar_vertice(v)
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 3)
    g.agregar_arista(2, 4)
    g.agregar_arista(2, 5)
    return g


def test_grafo_undirected_basic():
    g = build_sample_graph(directed=False)
    verts = set(g.obtener_vertices())
    assert verts == {1, 2, 3, 4, 5}

    vecinos_1 = set(g.obtener_vecinos(1))
    assert vecinos_1 == {2, 3}

    # Arista debe existir en ambos sentidos para grafo no dirigido
    assert g.existe_arista(1, 2)
    assert g.existe_arista(2, 1)


def test_grafo_directed_behavior():
    g = Grafo(dirigido=True)
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_arista(1, 2)
    assert g.existe_arista(1, 2)
    assert not g.existe_arista(2, 1)


def test_bfs_order():
    g = build_sample_graph(directed=False)
    order = bfs(g, 1)
    # Orden esperado BFS: 1, 2, 3, 4, 5 (dependiendo del orden de vecinos,
    # con las inserciones hechas debe darse este orden)
    assert order[0] == 1
    assert set(order) == {1, 2, 3, 4, 5}
    # Aseguramos que 2 y 3 aparecen antes que 4 y 5
    assert order.index(2) < order.index(4)
    assert order.index(2) < order.index(5)


def test_bfs_camino_shortest():
    g = build_sample_graph(directed=False)
    # Camino más corto de 4 a 3: 4 -> 2 -> 1 -> 3
    path = bfs_camino(g, 4, 3)
    assert path == [4, 2, 1, 3]


def test_niveles_bfs():
    g = build_sample_graph(directed=False)
    levels = niveles_bfs(g, 1)
    expected = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
    assert levels == expected


def test_bfs_disconnected_vertex():
    # Grafo con vértice aislado
    g = Grafo()
    for v in [1, 2, 3]:
        g.agregar_vertice(v)
    g.agregar_arista(1, 2)
    order = bfs(g, 1)
    assert 3 not in order
    # niveles_bfs no debe contener vértices no alcanzables
    levels = niveles_bfs(g, 1)
    assert 3 not in levels
