def busqueda_lineal(lista, objetivo):
    """Búsqueda lineal iterativa."""
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    """Búsqueda lineal recursiva."""
    if indice >= len(lista):
        return -1
    if lista[indice] == objetivo:
        return indice
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)

def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria iterativa. La lista debe estar ordenada."""
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    """Búsqueda binaria recursiva. La lista debe estar ordenada."""
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)
