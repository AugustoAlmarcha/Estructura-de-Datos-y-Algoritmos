import numpy as np
from Colasecuencial import cola

class digrafoSecuencial:
    __grafo:np.ndarray
    __tamanio:int

    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__grafo=np.zeros((tamanio,tamanio),dtype=object)
    
    def agregarArista(self, u , v):
        if 0 <= u < self.__tamanio and 0 <= v < self.__tamanio:
            self.__grafo[u][v] = 1
        else:
            print("Error: Vertice fuera de rango")

    def adyacentes(self, u):
        if not (0 <= u < self.__tamanio):
            print("Error: Vertice fuera de rango")
            return None
        else:
            lista = []
            for i in range(self.__tamanio):
                if self.__grafo[u][i] == 1:
                    lista.append(i)
            return lista

        
    def CaminoPonderado(self, u, v):
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
    
    def CaminoAnchura (self, u, v):
        if not (0 <= u < self.__tamanio and 0 <= v < self.__tamanio):
            print("Error: nodos fuera de rango.")
            return None
        visitado = [False] * self.__tamanio
        predecesor = [-1] * self.__tamanio
        c = cola(self.__tamanio)
        c.insertar(u)
        visitado[u] = True

        while not c.vacia():
            actual = c.suprimir()
            if actual == v:
                camino = []
                while actual != -1:
                    camino.insert(0,actual)
                    actual = predecesor[actual]
                return camino
            
            for i in range(self.__tamanio):
                if self.__grafo[actual][i] == 1 and not visitado[i]:
                    visitado[i] = True
                    predecesor[i] = actual
                    c.insertar(i)
        print("No se encontro camino")
        return

    
    def fuertementeconexo(self):
        for origen in range(self.__tamanio):
            visitado = [False] * self.__tamanio
            c = cola(self.__tamanio)
            c.insertar(origen)
            visitado[origen] = True
            while not c.vacia():
                actual = c.suprimir()
                for i in range(self.__tamanio):
                    if self.__grafo[actual][i] == 1 and not visitado[i]:
                        visitado[i] = True
                        c.insertar(i)
            if not all(visitado):
                return False
        return True
    
    def REA(self, origen=0):
        vi = [float('inf')] * self.__tamanio 
        vi[origen] = 0                        
        c = cola(self.__tamanio)
        c.insertar(origen)

        while not c.vacia():
            ac = c.suprimir()
            print(f"Nodo procesado: {ac}")

            for i in range(self.__tamanio):
                if self.__grafo[ac][i] != 0 and vi[i] == float('inf'):
                    vi[i] = vi[ac] + 1 
                    c.insertar(i)
        return vi
    
    def REP(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]

        for i in range(self.__tamanio):
            if d[i] == 0:
                self.REP_visita(i, d, f, tiempo)

    def REP_visita(self, i , d, f, tiempo, padre=None, detectar_ciclo=False, procesar_nodo=False):
        tiempo[0] += 1
        d[i] = tiempo[0]

        for j in range(self.__tamanio):
            if self.__grafo[i][j] != 0:
                if d[j] == 0:
                    if not self.REP_visita(j , d, f, tiempo, i, detectar_ciclo, procesar_nodo):
                        return False
                elif detectar_ciclo and f[j] == 0 and j != padre:
                    return False

        tiempo[0] += 1
        f[i] = tiempo[0]
        if procesar_nodo:
            print(f"Nodo procesado: {i}")

        return True
    
    def aciclico(self):
        d = [0] * self.__tamanio
        f = [0] * self.__tamanio
        tiempo = [0]

        for i in range(self.__tamanio):
            if d[i] == 0:
                if not self.REP_visita(i, d, f, tiempo, padre=-1, detectar_ciclo=True, procesar_nodo=False):
                    return False
        return True
    
    def GradoEntrada(self, v):
        if not (0 <= v < self.__tamanio):
            print("Error: Vertice fuera de rango")
            return None
        else:
            entrada = 0
            for i in range(self.__tamanio):
                if self.__grafo[i][v] == 1:
                    entrada += 1
            return entrada
    
    def GradoSalida(self, u):
        if not (0 <= u < self.__tamanio):
            print("Error: Vertice fuera de rango")
            return None
        else:
            salida = 0
            for i in range(self.__tamanio):
                if self.__grafo[u][i] == 1:
                    salida += 1
            return salida

    
    def NodoFuente(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        if grad_entrada == 0 and grad_salida > 0:
            print("Es un nodo fuente")
            return True
        else:
            print("No es un nodo fuente")
            return False
    
    def NodoSumidero(self, v):
        grad_entrada = self.GradoEntrada(v)
        grad_salida = self.GradoSalida(v)
        if grad_entrada > 0 and grad_salida == 0:
            print("Es un nodo sumidero")
            return True
        else:
            print("No es un nodo sumidero")
            return False
    
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



    
    

        


