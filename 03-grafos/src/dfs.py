def dfs(grafo, inicio, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(inicio)
    for vecino in grafo.vecinos(inicio):
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
    return visitado
