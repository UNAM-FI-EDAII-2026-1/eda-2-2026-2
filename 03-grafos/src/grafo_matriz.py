class GrafoMatriz:
    def __init__(self, num_vertices, dirigido=False):
        self.num_vertices = num_vertices
        self.dirigido = dirigido
        self.matriz = [[0]*num_vertices for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino):
        self.matriz[origen][destino] = 1
        if not self.dirigido:
            self.matriz[destino][origen] = 1

    def vecinos(self, v):
        return [i for i, val in enumerate(self.matriz[v]) if val]
