import grafo
from biblioteca_grafos import eliminar_vertices

def crear_incompatibilidades(ruta):
    grafo_nuevo = grafo.Grafo()
    tiempos = {}
    with open(ruta) as conexiones:
        for linea in conexiones:
            line = linea.split()
            if line[0] == 'c' or linea [0] == 'p': continue
            if line[0] == 'e':
                grafo_nuevo.agregar_vertice(line[1])
                grafo_nuevo.agregar_vertice(line[2])
                grafo_nuevo.agregar_arista(line[1], line[2],0, True)
            if line[0] == 'n':
                tiempos[line[1]] = int(line[2])
    return grafo_nuevo, tiempos

def asignar_tiempos(grafo, tiempos):
    for e in grafo.obtener_aristas():
        v1 = e[0]
        v2 = e[1]
        tiempo = tiempos[v1] + tiempos[v2]
        grafo.cambiar_peso(v1, v2, tiempo, True)

def obtener_mayor_tiempo(tiempos, comunes):
    mayor_tiempo = 0
    mayor_vertice = ''
    for v in comunes:
        if not tiempos[v] > mayor_tiempo:
            continue
        mayor_vertice = v
        mayor_tiempo = tiempos[v]
    return mayor_vertice

def completar_conexiones(grafo, tiempos, comunes, v1, v2):
    conexion_final = [v1, v2]
    while len(comunes) > 0:
        mayor_tiempo = obtener_mayor_tiempo(tiempos, comunes)
        comunes.remove(mayor_tiempo)
        for i in range(1, len(conexion_final)):
            if not grafo.vertices_conectados(mayor_tiempo, conexion_final[i]):
                if mayor_tiempo in conexion_final: conexion_final.remove(mayor_tiempo)
                break
            conexion_final.append(mayor_tiempo)
    return conexion_final

def obtener_lavados(grafo, tiempos):
    lavados = []
    while grafo.cantidad_vertices() > 0 and len(grafo.obtener_aristas()) > 0:
        arista_pesada = grafo.obtener_arista_mas_pesada()
        v1 = arista_pesada[0]
        v2 = arista_pesada[1]
        comunes = grafo.obtener_adyacentes_comunes(v1, v2)
        comunes_completos = completar_conexiones(grafo, tiempos,comunes, v1, v2)
        lavados.append(comunes_completos)
        eliminar_vertices(grafo, comunes_completos)
    vertices_restantes = grafo.obtener_todos_los_vertices()
    for v in vertices_restantes:
        l = []
        l.append(v)
        lavados.append(l)
    return lavados

def obtener_tiempo_final(tiempos, lavados):
    final = 0
    for l in lavados:
        mayor = obtener_mayor_tiempo(tiempos, l)
        tiempo_parcial = tiempos[mayor]
        final += tiempo_parcial
    return final