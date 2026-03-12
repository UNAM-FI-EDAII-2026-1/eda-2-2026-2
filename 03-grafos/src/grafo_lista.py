class GrafoLista:
    def __init__(self, num_vertices, dirigido=False):
        self.num_vertices = num_vertices
        self.dirigido = dirigido
        self.lista = [[] for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino):
        self.lista[origen].append(destino)
        if not self.dirigido:
            self.lista[destino].append(origen)

    def vecinos(self, v):
        return self.lista[v]
