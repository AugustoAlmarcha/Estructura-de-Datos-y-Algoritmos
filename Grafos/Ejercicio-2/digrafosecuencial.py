#DIGRAFO PONDERADO
import numpy as np
from Colasecuencial import cola

class digrafoSecuencial:
    __grafo:np.ndarray
    __tamanio:int

    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__grafo=np.zeros((tamanio,tamanio),dtype=float)
    
    def agregarArista(self, inicio, fin, peso=1):
        if 0 <= inicio < self.__tamanio and 0 <= fin < self.__tamanio:
            self.__grafo[inicio][fin] = peso
        else:
            print("Error: Vertice fuera de rango")

    def adyacentes(self, vertice):
        if 0 <= vertice < self.__tamanio:
            lista = []
            for i in range(self.__tamanio):
                if self.__grafo[vertice][i] != 0:
                    lista.append(i)
            return lista
        else:
            print("Error: Vertice fuera de rango")
            return None
        
    def Camino(self, u, v):
        # T: [0: Conocido (bool), 1: Distancia (float), 2: Camino/Predecesor (int)]
        T = np.zeros((self.__tamanio, 3), dtype=object)
        T[:, 0] = False            
        T[:, 1] = float('inf')     
        T[:, 2] = -1               
        T[u, 1] = 0                # Distancia del origen u es 0

        nodos_conocidos = 0
        
        # Bucle Principal (Simula el 'Para i desde 1 hasta V hacer' )
        while nodos_conocidos < self.__tamanio:
            
            # --- 1. Búsqueda del Mínimo NO Conocido (O(|V|)) ---
            min_dist = float('inf')
            v_actual = -1
            
            i = 0
            while i < self.__tamanio:
                # Si NO Conocido AND Distancia actual es menor que min_dist
                if T[i, 0] == False and T[i, 1] < min_dist:
                    min_dist = T[i, 1]
                    v_actual = i
                i += 1
            
            if v_actual == -1: # No quedan nodos accesibles.
                break

            # --- 2. Marcar como Conocido ---
            T[v_actual, 0] = True
            nodos_conocidos += 1
            
            if v_actual == v: # Si encontramos el destino, salimos del bucle principal
                break

            # --- 3. Relajación de Aristas (O(|V|)) ---
            w = 0
            while w < self.__tamanio:
                peso_arco = self.__grafo[v_actual, w]
                
                # Chequeamos si el arco v_actual -> w existe (peso > 0) y si w no es Conocido [cite: 380]
                if peso_arco > 0 and T[w, 0] == False:
                    
                    nueva_distancia = T[v_actual, 1] + peso_arco
                    
                    # Regla de Relajación: Si la nueva ruta es más corta [cite: 382]
                    if nueva_distancia < T[w, 1]:
                        T[w, 1] = nueva_distancia # Reducir la distancia
                        T[w, 2] = v_actual        # Actualizar el predecesor [cite: 385]
                
                w += 1
        
        # --- 4. Reporte y Reconstrucción del Camino ---
        
        if T[v, 1] == float('inf'):
            print(f"No existe camino de {u} a {v}.")
            return None
        
        # Reconstrucción del Camino (usando while)
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
                for i in range(self.__tamanio):
                    if self.__grafo[actual][i] != 0 and not visitado[i]:
                        visitado[i] = True
                        c.insertar(i)
            if not all(visitado):
                return False
        return True
    
    def REA(self, origen=0):
        d = [float('inf')] * self.__tamanio 
        d[origen] = 0                        
        c = cola(self.__tamanio)
        c.insertar(origen)

        while not c.vacia():
            v = c.suprimir()
            print(f"Nodo procesado: {v}")

            for u in range(self.__tamanio):
                if self.__grafo[v][u] != 0 and d[u] == float('inf'):
                    d[u] = d[v] + 1 
                    c.insertar(u)
    
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

        for u in range(self.__tamanio):
            if self.__grafo[s][u] != 0:
                if d[u] == 0:
                    if not self.REP_visita(u, d, f, tiempo, s, detectar_ciclo, procesar_nodo):
                        return False
                elif detectar_ciclo and f[u] == 0 and u != padre:
                    return False

        tiempo[0] += 1
        f[s] = tiempo[0]

        if procesar_nodo:
            print(f"Nodo procesado: {s}")

        return True
    
    def aciclico(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]

        for v in range(self.__tamanio):
            if d[v] == 0:
                if not self.REP_visita(v, d, f, tiempo, padre=-1, detectar_ciclo=True, procesar_nodo=False):
                    return False
        return True
    
    def GradoEntrada(self, v):
        if 0 <= v < self.__tamanio:
            grado = 0
            for i in range(self.__tamanio):
                if self.__grafo[i][v] != 0:
                    grado += 1
            return grado
        else:
            print("Error: Vertice fuera de rango")
            return None
    
    def GradoSalida(self, v):
        if 0 <= v < self.__tamanio:
            grado = 0
            for i in range(self.__tamanio):
                if self.__grafo[v][i] != 0:
                    grado += 1
            return grado
        else:
            print("Error: Vertice fuera de rango")
            return None
    
    def NodoFuente(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        return grad_salida > 0 and grad_entrada == 0
    
    def NodoSumidero(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        return grad_entrada > 0 and grad_salida == 0
    
# if __name__ == "__main__":
#     g = digrafoSecuencial(5)
#     g.agregarArista(0, 1, 2)
#     g.agregarArista(0, 2, 4)
#     g.agregarArista(1, 2, 1)
#     g.agregarArista(1, 3, 7)
#     g.agregarArista(2, 4, 3)
#     g.agregarArista(3, 4, 1)

#     camino = g.Camino(0, 4)
#     print("Camino mínimo de 0 a 4:", camino)

#     print("¿El grafo es fuertemente conexo?", g.fuertementeconexo())

#     print("Recorrido en Anchura desde el nodo 0:")
#     g.REA(0)

#     print("Recorrido en Profundidad:")
#     g.REP()

#     print("¿El grafo es acíclico?", g.aciclico())

#     v = 2
#     print(f"Grado de entrada del nodo {v}:", g.GradoEntrada(v))
#     print(f"Grado de salida del nodo {v}:", g.GradoSalida(v))
#     print(f"¿El nodo {v} es fuente?", g.NodoFuente(v))
#     print(f"¿El nodo {v} es sumidero?", g.NodoSumidero(v))



    
    

        


