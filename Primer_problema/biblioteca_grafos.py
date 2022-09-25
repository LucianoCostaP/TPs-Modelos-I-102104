import grafo

def crear_grafo_completo(graph, tiempos):
    completo = grafo.Grafo()
    vertices = graph.obtener_todos_los_vertices()
    for v in vertices:
        completo.agregar_vertice(v)
    for v in vertices:
        for w in vertices:
            if graph.vertices_conectados(v,w) is None:
                peso = tiempos[v] + tiempos[w]
            else:
                peso = graph.vertices_conectados(v,w)
            completo.agregar_arista(v,w, peso, True)
    return completo

def calcular_complemento(graph, tiempos):
    aristas = graph.obtener_aristas()
    completo = crear_grafo_completo(graph, tiempos)
    aristas_completo = completo.obtener_aristas()
    complemento = grafo.Grafo()
    vertices_completos = completo.obtener_todos_los_vertices()
    for v in vertices_completos:
        complemento.agregar_vertice(v)
    for e in aristas_completo:
        if e in aristas:
            continue
        peso = completo.vertices_conectados(e[0], e[1])
        complemento.agregar_arista(e[0], e[1], peso, True)
    return complemento

def eliminar_vertices(grafo, vertices):
    for v in vertices:
        grafo.sacar_vertice(v)