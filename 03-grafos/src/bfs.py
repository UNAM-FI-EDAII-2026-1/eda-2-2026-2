from collections import deque

def bfs(grafo, inicio):
    visitado = set([inicio])
    cola = deque([inicio])
    while cola:
        v = cola.popleft()
        for vecino in grafo.vecinos(v):
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)
    return visitado
