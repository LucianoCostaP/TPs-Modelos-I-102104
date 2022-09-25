def swap(lista, padre, pos):
    parcial = lista[padre]
    lista[padre] = lista[pos]
    lista[pos] = parcial

def upheap(arreglo, pos, cmp = False):
    if pos == 0:
        return
    padre = (pos - 1) // 2
    if not cmp:
        if arreglo[padre] > arreglo[pos]:
            swap(arreglo, padre, pos)
            upheap(arreglo, padre)
    else:
        if cmp(arreglo[padre], arreglo[pos]) > 0:
            swap(arreglo, padre, pos)
            upheap(arreglo, padre, cmp)

def downheap(arreglo, tam, pos, cmp = False):
    if pos >= tam:
        return
    minimo = pos
    izq = 2 * pos + 1
    der = 2 * pos + 2
    if not cmp:
        if izq < tam and arreglo[izq] < arreglo[minimo]:
            minimo = izq
        if der < tam and arreglo[der] < arreglo[minimo]:
            minimo = der
    else:
        if izq < tam and cmp(arreglo[izq], arreglo[minimo]) < 0:
            minimo = izq
        if der < tam and cmp(arreglo[der], arreglo[minimo]) < 0:
            minimo = der
    if(minimo != pos):
        swap(arreglo, minimo, pos)
        downheap(arreglo, tam, minimo, cmp) 

class Heap:

    def __init__(self):
        self.datos = []
        self.cantidad = 0
    
    def cantidad(self):
        return self.cantidad
    
    def esta_vacio(self):
        return self.cantidad == 0
    
    def ver_max(self):
        if self.cantidad == 0:
            raise Exception("El heap se encuentra vacio")
        return self.datos[0]
    
    def desencolar(self, cmp = False):
        if self.cantidad == 0:
            raise Exception("El heap se encuentra vacio")
        elemento = self.datos[0]
        swap(self.datos, 0, self.cantidad - 1)
        self.cantidad -= 1
        downheap(self.datos, self.cantidad, 0, cmp)
        self.datos.pop()
        return elemento
    
    def encolar(self, dato, cmp = False):
        if dato is None:
            raise TypeError("No se puede encolar este elemento")
        self.datos.append(dato)
        upheap(self.datos, self.cantidad, cmp)
        self.cantidad +=1

    def __str__(self):
        cadena = '['
        for i in range(len(self.datos)):
            cadena += str(self.datos[i])
            if i != len(self.datos) - 1:
                cadena += ','
        cadena += ']'
        return cadena
    
    def __repr__(self):
        return str(self)

