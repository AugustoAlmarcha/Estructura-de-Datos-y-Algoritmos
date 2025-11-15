import numpy as np
from Colasecuencial import cola
from ClaseNodo import Nodo

class GrafoEnlazado:
    __grafo:np.ndarray
    __tamanio:int

    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__grafo = np.array([None]*tamanio, dtype=object)

    def agregar_arista(self, u, v):
        if 0 <= u < self.__tamanio and 0 <= v < self.__tamanio:
            nuevo_nodo_v = Nodo(v)
            nuevo_nodo_v.setSiguiente(self.__grafo[u])
            self.__grafo[u] = nuevo_nodo_v

            nuevo_nodo_u = Nodo(u)
            nuevo_nodo_u.setSiguiente(self.__grafo[v])
            self.__grafo[v] = nuevo_nodo_u
        else:
            print(f"Error: los nodos {u} o {v} están fuera de rango.")

    def adyacentes(self, u):
        if not (0 <= u < self.__tamanio):
            print("Nodo fuera de rango")
            return []
        lista = []
        actual = self.__grafo[u]
        while actual is not None:
            lista.append(actual.getDato())
            actual = actual.getSiguiente()
        return lista
    
    def camino(self, u, v): #Recorrido en Anchura
        if not (0 <= u < self.__tamanio and 0 <= v < self.__tamanio):
            print("Error: nodos fuera de rango.")
            return None
        visitado = [False] * self.__tamanio
        predecesor = [-1] * self.__tamanio
        c = cola(self.__tamanio)
        visitado[u] = True
        c.insertar(u)

        while not c.vacia():
            actual = c.suprimir()
            if actual == v:
                # reconstrucción del camino
                camino = []
                while actual != -1:
                    camino.insert(0, actual)
                    actual = predecesor[actual]
                return camino
            
            actualnodo = self.__grafo[actual]
            while actualnodo is not None:
                adyacente = actualnodo.getDato()
                if not visitado[adyacente]:
                    visitado[adyacente] = True
                    predecesor[adyacente] = actual
                    c.insertar(adyacente)
                actualnodo = actualnodo.getSiguiente()
        print("No existe camino entre", u, "y", v)
        return None
    
    def conexo(self):
        visitado = [False] * self.__tamanio
        c = cola(self.__tamanio)
        c.insertar(0)
        visitado[0] = True

        while not c.vacia():
            actual = c.suprimir()
            
            actualnodo = self.__grafo[actual]
            while actualnodo is not None:
                adyacente = actualnodo.getDato()
                if not visitado[adyacente]:
                    visitado[adyacente] = True
                    c.insertar(adyacente)
                actualnodo = actualnodo.getSiguiente()
        return all(visitado)
    
    def REA(self, origen=0):
        d = [float('inf')] * self.__tamanio 
        d[origen] = 0                        
        c = cola(self.__tamanio)
        c.insertar(origen)

        while not c.vacia():
            actual = c.suprimir()
            
            actualnodo = self.__grafo[actual]
            while actualnodo is not None:
                adyacente = actualnodo.getDato()
                if d[adyacente] == float('inf'):
                    d[adyacente] = d[actual] + 1
                    c.insertar(adyacente)
                actualnodo = actualnodo.getSiguiente()
        return d
    
    def REP(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]
        for i in range(self.__tamanio):
            if d[i] == 0:
                self.REP_visita(i, d, f, tiempo, detectar_ciclo=False, procesar_nodo=True)

    def REP_visita(self, v, d, f, tiempo, detectar_ciclo=False, procesar_nodo=False, padre=None):
        tiempo[0] += 1
        d[v] = tiempo[0]
        nodo_adyacente = self.__grafo[v]
        while nodo_adyacente is not None:
            u = nodo_adyacente.getDato()
            if d[u] == 0:
                if not self.REP_visita(u, d, f, tiempo, detectar_ciclo, procesar_nodo, v):
                    return False
            elif detectar_ciclo and f[u] == 0 and u != padre:
                return False
            nodo_adyacente = nodo_adyacente.getSiguiente()
        tiempo[0] += 1
        f[v] = tiempo[0]
        if procesar_nodo:
            print(f"Nodo {v} procesado en tiempo {tiempo[0]}")
        return True
    
    def aciclico(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]
        for i in range(self.__tamanio):
            if d[i] == 0:
                if not self.REP_visita(i, d, f, tiempo, detectar_ciclo=True, procesar_nodo=False):
                    return False
        return True

# if __name__ == "__main__":
#     # Crear un grafo con 5 nodos
#     g = GrafoEnlazado(5)

#     # Agregar aristas
#     g.agregar_arista(0, 1)
#     g.agregar_arista(0, 2)
#     g.agregar_arista(1, 3)
#     g.agregar_arista(2, 4)
#     g.agregar_arista(3, 4)

#     # Mostrar nodos adyacentes
#     for i in range(5):
#         print(f"Nodos adyacentes a {i}: {g.adyacentes(i)}")

#     # Camino de 0 a 4
#     camino = g.camino(0, 4)
#     if camino:
#         print(f"Camino de 0 a 4: {camino}")
#     else:
#         print("No existe camino de 0 a 4")

#     # Verificar si el grafo es conexo
#     print("¿Grafo conexo?", g.conexo())

#     # Recorridos
#     print("Recorrido en profundidad (REP):")
#     g.REP()

#     print("Recorrido en anchura (REA) desde 0:")
#     d = g.REA(0)
#     print(d)

#     # Verificar si el grafo es acíclico
#     print("¿Grafo acíclico?", g.aciclico())