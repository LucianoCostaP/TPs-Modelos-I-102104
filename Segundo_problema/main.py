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
    grafo, tiempos = crear_incompatibilidades('segundo_problema.txt')
    asignar_tiempos(grafo, tiempos)
    orden = ordenar_prendas(tiempos)
    lavados = obtener_mejor_combinacion(grafo, orden, tiempos)
    tiempo_final = obtener_tiempo_final(tiempos, lavados)
    escribir_solucion(lavados)
    print(tiempo_final)

main()