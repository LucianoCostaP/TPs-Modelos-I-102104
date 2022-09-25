from biblioteca_grafos import *
from lavados import *

def escribir_solucion(lavados):
    solucion = open('Solucion.txt', 'w')
    for i in range(len(lavados)):
        for j in range(len(lavados[i])):
            prenda = lavados[i][j]
            if i == 0 and j == 0: 
                solucion.write(f'{prenda} {i + 1}')
            else:
                solucion.write(f'\n{prenda} {i + 1}')
    solucion.close()

def main():
    grafo, tiempos = crear_incompatibilidades('primer_problema.txt')
    asignar_tiempos(grafo, tiempos)
    compatibles = calcular_complemento(grafo, tiempos)
    lavados  = obtener_lavados(compatibles, tiempos)
    escribir_solucion(lavados)

main()