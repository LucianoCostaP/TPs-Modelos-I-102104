import grafo
import heap
import random
import math
REPETICIONES = 100

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
                grafo_nuevo.agregar_arista(line[1], line[2],0, False)
            if line[0] == 'n':
                tiempos[line[1]] = int(line[2])
    return grafo_nuevo, tiempos

def asignar_tiempos(grafo, tiempos):
    for e in grafo.obtener_aristas():
        v1 = e[0]
        v2 = e[1]
        tiempo = tiempos[v1] + tiempos[v2]
        grafo.cambiar_peso(v1, v2, tiempo, False)

def comparar_tiempos(prenda1, prenda2):
    if prenda1[1] > prenda2[1]: return -1
    return 1

def ordenar_prendas(tiempos):
    orden = heap.Heap()
    prendas = list(tiempos.keys())
    random.shuffle(prendas)
    for v in prendas:
        prenda = (v, tiempos[v])
        orden.encolar(prenda, comparar_tiempos)
    return orden

def agregar_lavado(lavados, prenda):
    lavados.append([prenda[0]])

def es_lavado_compatible(grafo, prenda, lavado):
    for v in lavado:
        prenda_actual = prenda[0]
        if grafo.vertices_conectados(v, prenda_actual):
            return False
    return True

def obtener_lavados(grafo, orden):
    lavados = []
    while not orden.esta_vacio():
        prenda = orden.desencolar(comparar_tiempos)
        esta_agregada = False
        for l in lavados:
            if es_lavado_compatible(grafo, prenda, l):
                l.append(prenda[0])
                esta_agregada = True
                break
        if not esta_agregada:
            agregar_lavado(lavados, prenda)
    return lavados    

def obtener_mayor_tiempo(tiempos, comunes):
    mayor_tiempo = 0
    for v in comunes:
        if not tiempos[v] > mayor_tiempo:
            continue
        mayor_vertice = v
        mayor_tiempo = tiempos[v]
    return mayor_vertice

def obtener_tiempo_final(tiempos, lavados):
    final = 0
    for l in lavados:
        mayor = obtener_mayor_tiempo(tiempos, l)
        tiempo_parcial = tiempos[mayor]
        final += tiempo_parcial
    return final

def obtener_mejor_combinacion(grafo, orden, tiempos):
    mejor_tiempo = math.inf
    for i in range(REPETICIONES):
        lavados = obtener_lavados(grafo, orden)
        tiempo_actual = obtener_tiempo_final(tiempos, lavados)
        orden = ordenar_prendas(tiempos)
        if tiempo_actual < mejor_tiempo:
            mejor_tiempo = tiempo_actual
            mejor_lavado = lavados
    return mejor_lavado