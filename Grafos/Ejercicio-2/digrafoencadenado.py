#Digrafo Encadenado Ponderado
import numpy as np
from Colasecuencial import cola
from ClaseNodo import Nodo

class GrafoEnlazado:
    __grafo: np.ndarray
    __tamanio: int

    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__grafo = np.array([None] * tamanio, dtype=object)

    def agregar_arista(self, u, v, peso=1.0):
        if 0 <= u < self.__tamanio and 0 <= v < self.__tamanio:
            nuevo_nodo_v = Nodo(v, peso)
            nuevo_nodo_v.setSiguiente(self.__grafo[u])
            self.__grafo[u] = nuevo_nodo_v
        else:
            print(f"Error: los nodos {u} o {v} están fuera de rango.")

    def adyacentes(self, u):
        if not (0 <= u < self.__tamanio):
            print("Nodo fuera de rango")
            return []
        lista = []
        actual = self.__grafo[u]
        while actual is not None:
            lista.append((actual.getDato(), actual.getPeso()))
            actual = actual.getSiguiente()
        return lista
    
    def Camino(self, u, v):
        # Tabla T: [0: conocido, 1: distancia, 2: predecesor]
        T = np.zeros((self.__tamanio, 3), dtype=object)
        T[:, 0] = False
        T[:, 1] = float('inf')
        T[:, 2] = -1
        T[u, 1] = 0

        nodos_conocidos = 0

        while nodos_conocidos < self.__tamanio:
            # --- Buscar nodo con distancia mínima no conocido ---
            min_dist = float('inf')
            v_actual = -1
            i = 0
            while i < self.__tamanio:
                if T[i, 0] == False and T[i, 1] < min_dist:
                    min_dist = T[i, 1]
                    v_actual = i
                i += 1

            if v_actual == -1:  # No quedan nodos accesibles
                break

            # Marcar como conocido
            T[v_actual, 0] = True
            nodos_conocidos += 1

            if v_actual == v:
                break  # Llegamos al destino

            # --- Relajar aristas ---
            actual = self.__grafo[v_actual]
            while actual is not None:
                w = actual.getDato()
                peso = actual.getPeso()
                if not T[w, 0]:  # Si w no es conocido
                    nueva_dist = T[v_actual, 1] + peso
                    if nueva_dist < T[w, 1]:
                        T[w, 1] = nueva_dist
                        T[w, 2] = v_actual
                actual = actual.getSiguiente()

        # Reconstrucción del camino
        if T[v, 1] == float('inf'):
            print(f"No existe camino de {u} a {v}.")
            return None

        camino = []
        actual = v
        while actual != -1:
            camino.insert(0, actual)
            actual = T[actual, 2]

        return camino
    
    def fuertementeconexo(self):
        for origen in range(self.__tamanio):
            visitado = [False] * self.__tamanio
            c = cola(self.__tamanio)
            c.insertar(origen)
            visitado[origen] = True

            while not c.vacia():
                actual = c.suprimir()
                nodo_adyacente = self.__grafo[actual]  # cabeza de la lista enlazada
                while nodo_adyacente is not None:
                    w = nodo_adyacente.getDato()
                    if not visitado[w]:
                        visitado[w] = True
                        c.insertar(w)
                    nodo_adyacente = nodo_adyacente.getSiguiente()

            if not all(visitado):
                return False

        return True
    
    def REA(self, origen=0):
        d = [float('inf')] * self.__tamanio
        d[origen] = 0
        c = cola(self.__tamanio)
        c.insertar(origen)

        while not c.vacia():
            actual = c.suprimir()
            nodo_adyacente = self.__grafo[actual]
            while nodo_adyacente is not None:
                adyacente = nodo_adyacente.getDato()
                if d[adyacente] == float('inf'):
                    d[adyacente] = d[actual] + 1
                    c.insertar(adyacente)
                nodo_adyacente = nodo_adyacente.getSiguiente()

        return d
    
    def REP(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]

        for v in range(self.__tamanio):
            if d[v] == 0:
                self.REP_visita(v, d, f, tiempo)

    def REP_visita(self, s, d, f, tiempo, padre=None, detectar_ciclo=False, procesar_nodo=False):
        tiempo[0] += 1
        d[s] = tiempo[0]

        nodo_adyacente = self.__grafo[s]
        while nodo_adyacente is not None:
            u = nodo_adyacente.getDato()
            if d[u] == 0:
                if not self.REP_visita(u, d, f, tiempo, s, detectar_ciclo, procesar_nodo):
                    return False
            elif detectar_ciclo and f[u] == 0 and u != padre:
                return False
            nodo_adyacente = nodo_adyacente.getSiguiente()

        tiempo[0] += 1
        f[s] = tiempo[0]

        return True
    
    def aciclico(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]

        for v in range(self.__tamanio):
            if d[v] == 0:
                if not self.REP_visita(v, d, f, tiempo, detectar_ciclo=True):
                    return False
        return True
    
    def GradoEntrada(self, v):
        if not (0 <= v < self.__tamanio):
            print("Nodo fuera de rango")
            return None
        grado = 0
        for i in range(self.__tamanio):
            actual = self.__grafo[i]
            while actual is not None:
                if actual.getDato() == v:
                    grado += 1
                actual = actual.getSiguiente()
        return grado
    
    def GradoSalida(self, v):
        if not (0 <= v < self.__tamanio):
            print("Nodo fuera de rango")
            return None
        grado = 0
        actual = self.__grafo[v]
        while actual is not None:
            grado += 1
            actual = actual.getSiguiente()
        return grado
    
    def NodoFuente(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        return grad_salida > 0 and grad_entrada == 0
    
    def NodoSumidero(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        return grad_entrada > 0 and grad_salida == 0
    
# if __name__ == "__main__":
#     g = GrafoEnlazado(5)
#     g.agregar_arista(0, 1, 2.0)
#     g.agregar_arista(0, 2, 4.0)
#     g.agregar_arista(1, 2, 1.0)
#     g.agregar_arista(1, 3, 7.0)
#     g.agregar_arista(2, 4, 3.0)
#     g.agregar_arista(3, 4, 1.0)

#     print("Camino mínimo de 0 a 4:", g.Camino(0, 4))
#     print("¿El grafo es fuertemente conexo?", g.fuertementeconexo())
#     print("Recorrido en amplitud desde el nodo 0:", g.REA(0))
#     print("¿El grafo es acíclico?", g.aciclico())
#     print("Grado de entrada del nodo 2:", g.GradoEntrada(2))
#     print("Grado de salida del nodo 1:", g.GradoSalida(1))
#     print("¿El nodo 0 es fuente?", g.NodoFuente(0))
#     print("¿El nodo 4 es sumidero?", g.NodoSumidero(4))
    

    



