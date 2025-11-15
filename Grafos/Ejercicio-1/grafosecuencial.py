import numpy as np
from Colasecuencial import cola

class GrafoSecuencial:
    __grafo: np.ndarray 
    __tamanio: int      

    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__grafo = np.zeros((tamanio,tamanio), dtype=object)

    def agregar_arista(self, u, v):
        if 0 <= u < self.__tamanio and 0 <= v < self.__tamanio:
            self.__grafo[u, v] = 1
            self.__grafo[v, u] = 1
        else:
            print(f"Error: los nodos {u} o {v} están fuera de rango.")

    def Adyacentes(self, u):
        if not (0 <= u < self.__tamanio):
            print("Nodo fuera de rango")
            return []
        
        lista = []
        v = 0
        while v < self.__tamanio:
            if self.__grafo[u][v] == 1:
                lista.append(v)
            v += 1
        return lista

    
    def Camino(self, u, v): #Recorrido en Anchura
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
            
            for i in range(self.__tamanio):
                if self.__grafo[actual][i] == 1 and not visitado[i]:
                    visitado[i] = True
                    predecesor[i] = actual
                    c.insertar(i)
        print("No existe camino entre", u, "y", v)
        return None
    
    def conexo(self):
        visitado = [False] * self.__tamanio
        c = cola(self.__tamanio)
        visitado[0] = True
        c.insertar(0)

        while not c.vacia():
            actual = c.suprimir()

            for i in range(self.__tamanio):
                if self.__grafo[actual][i] == 1 and not visitado[i]:
                    visitado[i] = True
                    c.insertar(i)
        return all(visitado)
    
    def REA(self, origen=0):
        vi = [float('inf')] * self.__tamanio 
        vi[origen] = 0                        
        c = cola(self.__tamanio)
        c.insertar(origen)

        while not c.vacia():
            ac = c.suprimir()
            print(f"Nodo procesado: {ac}")

            for i in range(self.__tamanio):
                if self.__grafo[ac][i] == 1 and vi[i] == float('inf'):
                    vi[i] = vi[ac] + 1 
                    c.insertar(i)
        return vi

    def REP(self):
        descubrimiento = [0] * self.__tamanio
        fin = [0] * self.__tamanio
        tiempo = [0]

        for i in range(self.__tamanio):
            if descubrimiento[i] == 0:
                self.REP_visita(i, descubrimiento, fin, tiempo, detectar_ciclo=False, procesar_nodo=True)

    def REP_visita(self, i, desc, fin, tiempo, padre=None, detectar_ciclo=False, procesar_nodo=False):
        tiempo[0] += 1
        desc[i] = tiempo[0]

        if procesar_nodo:
            print(f"Nodo procesado: {i}")

        for j in range(self.__tamanio):
            if self.__grafo[i][j] == 1:
                if desc[j] == 0:
                    if not self.REP_visita(j, desc, fin, tiempo, i, detectar_ciclo, procesar_nodo):
                        return False
                elif detectar_ciclo and fin[j] == 0 and j != padre:
                    return False

        tiempo[0] += 1
        fin[i] = tiempo[0]
        return True
    
    def aciclico(self):
        des = [0] * self.__tamanio
        fin = [0] * self.__tamanio
        tiempo = [0]

        for i in range(self.__tamanio):
            if des[i] == 0:
                if not self.REP_visita(i, des, fin, tiempo, padre=-1, detectar_ciclo=True, procesar_nodo=False):
                    return False
        return True

# if __name__ == "__main__":
#     # Creamos un grafo de 5 nodos (0 a 4)
#     g = GrafoSecuencial(5)

#     # Agregamos algunas aristas
#     g.agregar_arista(0, 1)
#     g.agregar_arista(0, 2)
#     g.agregar_arista(1, 3)
#     g.agregar_arista(3, 4)
#     g.agregar_arista(2, 4)

#     # Probamos Adyacentes
#     print("Nodos adyacentes a 0:", g.Adyacentes(0))

#     # Probamos Camino
#     print("Camino de 0 a 4:", g.Camino(0, 4))

#     # Verificamos si el grafo es conexo
#     print("¿Grafo conexo?", g.conexo())

#     # Recorrido en anchura desde nodo 0
#     print("Recorrido en anchura (REA) desde 0:")
#     g.REA(0)

#     # Recorrido en profundidad
#     print("Recorrido en profundidad (REP):")
#     g.REP()

#     # Verificamos si es acíclico
#     print("¿Grafo acíclico?", g.aciclico())


    
    

        




    

    

    

    

