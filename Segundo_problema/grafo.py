import random
import math

class Grafo:

    '''
    Modela el TDA GRAFO.
    '''

    def __init__(self):
        '''
        Constructor de la clase grafo.
        '''
        self.grafo = {}
        self.largo = 0
        self.vertices = []
        self.maximo_peso = 0
        self.arista_mas_pesada = []
        self.cantidad_aristas = 0

    def agregar_vertice(self, vertice):
        '''
        Agrega un vertice al grafo.
        '''
        if vertice in self.grafo:
            return None
        self.grafo[vertice] = {}
        self.largo += 1
        self.vertices.append(vertice)

    def agregar_arista(self, vertice_1, vertice_2, peso, dirigida):
        '''
        Recibe dos vertices, agrega una arista que apunta desde.
        vertice_1 a vertice_2.
        Pre: Los dos vertices se encuentran en el grafo.
        Post: Hay una nueva arista que apunta desde vertice_1 a vertice_2.
        '''
        if not vertice_1 in self.grafo or not vertice_2 in self.grafo: 
            return None
        if vertice_2 in self.grafo[vertice_1]:
            return None
        if not dirigida and vertice_1 in self.grafo[vertice_2]:
            return None
        if not dirigida:
            self.cantidad_aristas += 1
            self.grafo[vertice_2][vertice_1] = peso
        self.grafo[vertice_1][vertice_2] = peso
        if peso > self.maximo_peso: self.arista_mas_pesada = [vertice_1, vertice_2]
        self.maximo_peso = peso
        self.cantidad_aristas += 1

    def vertices_conectados(self, vertice_a, vertice_b):
        '''
        Recibe dos vertices (vertice_a y vertice_b).
        Verifica si existe una arista que se dirige del vertice_a al vertice_b.
        Devuelve su peso.
        Pre: vertice_a se encuentra en el grafo.
        '''
        if not vertice_a in self.grafo:
            return None
        if vertice_b in self.grafo[vertice_a]:
            return self.grafo[vertice_a][vertice_b]
        return None
    
    def sacar_vertice(self, vertice):
        '''
        Elimina un vertice del grafo
        Pre: El vertice se encuentra en el grafo.
        Post: El vertice no esta mas en el grafo.
        '''
        if not vertice in self.grafo:
            return None
        self.grafo.pop(vertice)
        for v in self.grafo:
            if vertice in self.grafo[v].keys():
                self.cantidad_aristas -= 1
                self.grafo[v].pop(vertice)
        self.largo -= 1
        self.vertices.remove(vertice)

    def sacar_arista(self, vertice_1, vertice_2, dirigida):
        '''
        Quita la arista que conecta el vertice_1 hacia el vertice_2.
        Pre: Existe la arista.
        '''
        if not (vertice_1 in self.grafo or vertice_2 in self.grafo):
            return None
        if not vertice_2 in self.grafo[vertice_1]:
            return None
        if not dirigida:
            self.cantidad_aristas -= 1
            self.grafo[vertice_2].pop(vertice_1)
        self.grafo[vertice_1].pop(vertice_2)
        self.cantidad_aristas -= 1

    def cantidad_adyacentes(self, vertice):
        if not vertice in self.grafo:
            return None
        return len(self.grafo[vertice])

    def adyacentes(self, vertice):
        '''
        Recibe un vertice del grafo.
        Devuelve un diccionario con sus adyacentes.
        Pre: El vertice se encuentra en el grafo.
        '''
        if not vertice in self.grafo:
            return None
        return self.grafo[vertice]

    def obtener_vertice_random(self):
        '''
        Devuelve un vertice al azar del grafo.
        '''
        l = self.vertices
        random.shuffle(l)
        i = random.randrange(len(self.vertices))
        return l[i]

    def obtener_todos_los_vertices(self):
        '''
        Devuelve una lista de todos los vertices.
        '''
        return self.vertices
    
    def cantidad_vertices(self):
        '''
        Devuelve la cantidad de vertices del grafo
        '''
        return self.largo
    
    def __iter__(self):
        return iter(self.grafo.keys())

    def obtener_grado(self):
        return self.largo

    def obtener_aristas(self):
        aristas = []
        for v in self.vertices:
            for w in self.grafo[v]:
                if v != w:
                    aristas.append([v,w])
        return aristas

    def obtener_arista_mas_pesada(self):
        pesada = []
        peso_maximo = math.inf * (-1)
        for v in self.vertices:
            for w in self.grafo[v]:
                peso = self.vertices_conectados(v, w)
                if peso > peso_maximo:
                    peso_maximo =  peso
                    pesada.append([v,w])
        return pesada.pop()

    def obtener_pesos(self):
        pesos = []
        for v in self.vertices:
            for w in self.grafo[v]:
                peso = self.grafo[v][w]
                pesos.append(pesos)
        return pesos

    def obtener_adyacentes_comunes(self, v1, v2):
        comunes = []
        if not v1 in self.grafo or not v2 in self.grafo:
            return None
        adyacentes_v1 = self.grafo[v1]
        adyacentes_v2 = self.grafo[v2]
        for w in adyacentes_v1:
            if w in adyacentes_v2:
                comunes.append(w)
        return comunes

    def obtener_secuencia_grados(self):
        secuencia = []
        for v in self.vertices:
            secuencia.append(len(self.adyacentes(v)))
        secuencia.sort()
        return secuencia.reverse()

    def cambiar_peso(self, v1, v2, peso, dirigida = False):
        if not dirigida: 
            self.grafo[v2][v1] = peso
        self.grafo[v1][v2] = peso
    
    def obtener_cantidad_aristas(self):
        return self.cantidad_aristas