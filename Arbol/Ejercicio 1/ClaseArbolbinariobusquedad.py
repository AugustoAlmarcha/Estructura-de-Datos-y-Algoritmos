from nodoArbol import NodoArbol

class ArbolBinarioBusqueda:
    __raiz : NodoArbol
    __cantidad : int

    def __init__(self):
        self.__raiz = None
        self.__cantidad = 0

    def vacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz

    def insertar (self, dato):
        nuevonodo = NodoArbol(dato)
        if self.vacio():
            self.__raiz = nuevonodo
            self.__cantidad += 1
            return
        else:
            self.insertarrecursivo(self.__raiz, dato)     #Hago doble insertar ya que la especificacion en la teoria dice que la encabezado es Insertar(A,X) 

    def insertarrecursivo (self, raizx, dato):
        if dato == raizx.getDato():
            print("El dato ya existe")
            return
        elif dato < raizx.getDato():
            if raizx.getIzquierdo() == None:
                nuevonodo = NodoArbol(dato)
                raizx.setIzquierdo(nuevonodo)
                self.__cantidad += 1
                return
            else:
                self.insertarrecursivo(raizx.getIzquierdo(), dato)
        elif dato > raizx.getDato():
            if raizx.getDerecho() == None:
                nuevonodo = NodoArbol(dato)
                raizx.setDerecho(nuevonodo)
                self.__cantidad += 1
                return
            else:
                self.insertarrecursivo(raizx.getDerecho(), dato)

    def suprimir(self,dato):
        if self.vacio():
            print("El arbol esta vacio")
            return
        else:
            self.__raiz = self.suprimirrecursivo(self.__raiz, dato)
    
    def suprimirrecursivo(self, nodo, dato):
        if nodo == None:
            print("El dato no existe")
            return nodo
        if dato < nodo.getDato():
            nodo.setIzquierdo(self.suprimirrecursivo(nodo.getIzquierdo(), dato)) #dato es menor, buscar en subárbol izquierdo
        elif dato > nodo.getDato():
            nodo.setDerecho(self.suprimirrecursivo(nodo.getDerecho(), dato)) #dato es mayor, buscar en subárbol derecho
        else: # nodo con el dato encontrado
            # Nodo hoja (grado 0)
            if nodo.getIzquierdo() is None and nodo.getDerecho() is None:
                self.__cantidad -= 1
                return None
            # Nodo con un solo hijo (grado 1)
            elif nodo.getIzquierdo() is None:
                self.__cantidad -= 1
                return nodo.getDerecho()
            elif nodo.getDerecho() is None:
                self.__cantidad -= 1
                return nodo.getIzquierdo()
            # Nodo con dos hijos (grado 2)
            else:
                # Buscar máximo del subárbol izquierdo
                temp = self.maxValorNodo(nodo.getIzquierdo())
                # Reemplazar el dato del nodo a borrar con el máximo
                nodo.setDato(temp.getDato())
                # Eliminar el nodo duplicado en el subárbol izquierdo
                nodo.setIzquierdo(self.suprimirrecursivo(nodo.getIzquierdo(), temp.getDato()))

        return nodo
        
    def maxValorNodo(self, nodo):
        actual = nodo
        while actual.getDerecho() is not None:
            actual = actual.getDerecho()
        return actual
    
    def buscar(self, dato):
        if self.vacio():
            print("Error: árbol vacío")
            return None
        else:
            return self.buscarRecursivo(self.__raiz, dato)

    def buscarRecursivo(self, nodo, dato):
        if nodo is None:
            print("Error: el dato no existe")
            return None

        if dato == nodo.getDato():
            # Nodo encontrado
            print(f"Éxito: elemento {dato} encontrado")
            return nodo
        elif dato < nodo.getDato():
            # Buscar en subárbol izquierdo
            return self.buscarRecursivo(nodo.getIzquierdo(), dato)
        else:
            # Buscar en subárbol derecho
            return self.buscarRecursivo(nodo.getDerecho(), dato)
        
        # Recorrido InOrden: Izquierda -> Nodo -> Derecha
    def inOrden(self):
        if self.vacio():
            print("Árbol vacío")
        else:
            self.inOrdenRecursivo(self.__raiz)
            print()  # salto de línea al final

    def inOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.inOrdenRecursivo(nodo.getIzquierdo())
            print(nodo.getDato(), end=" ")
            self.inOrdenRecursivo(nodo.getDerecho())


    # Recorrido PreOrden: Nodo -> Izquierda -> Derecha
    def preOrden(self):
        if self.vacio():
            print("Árbol vacío")
        else:
            self.preOrdenRecursivo(self.__raiz)
            print()

    def preOrdenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo.getDato(), end=" ")
            self.preOrdenRecursivo(nodo.getIzquierdo())
            self.preOrdenRecursivo(nodo.getDerecho())


    # Recorrido PostOrden: Izquierda -> Derecha -> Nodo
    def postOrden(self):
        if self.vacio():
            print("Árbol vacío")
        else:
            self.postOrdenRecursivo(self.__raiz)
            print()

    def postOrdenRecursivo(self, nodo):
        if nodo is not None:
            self.postOrdenRecursivo(nodo.getIzquierdo())
            self.postOrdenRecursivo(nodo.getDerecho())
            print(nodo.getDato(), end=" ")

    def nivel(self, dato):
        if self.vacio():
            print("Error: árbol vacío")
            return -1
        else:
            return self.nivelRecursivo(self.__raiz, dato, 0)

    def nivelRecursivo(self, nodo, dato, nivelActual):
        if nodo is None:
            print("Error: el dato no existe")
            return -1

        if dato == nodo.getDato():
            return nivelActual
        elif dato < nodo.getDato():
            return self.nivelRecursivo(nodo.getIzquierdo(), dato, nivelActual + 1)
        else:
            return self.nivelRecursivo(nodo.getDerecho(), dato, nivelActual + 1)
        
    def hoja(self, dato):
        if self.vacio():
            print("Error: árbol vacío")
            return False
        else:
            return self.hojaRecursivo(self.__raiz, dato)

    def hojaRecursivo(self, nodo, dato):
        if nodo is None:
            print("Error: el dato no existe")
            return False

        if dato == nodo.getDato():
            # Verificamos si es hoja
            return nodo.getIzquierdo() is None and nodo.getDerecho() is None
        elif dato < nodo.getDato():
            return self.hojaRecursivo(nodo.getIzquierdo(), dato)
        else:
            return self.hojaRecursivo(nodo.getDerecho(), dato)
        
    def hijo(self, datoX, datoZ):
        if self.vacio():
            print("Error: árbol vacío")
            return False
        else:
            nodoZ = self.buscar(datoZ)
            if nodoZ is None:
                print(f"Error: el nodo {datoZ} no existe")
                return False
            # Verificamos si X es hijo directo
            izquierdo = nodoZ.getIzquierdo()
            derecho = nodoZ.getDerecho()
            if (izquierdo is not None and izquierdo.getDato() == datoX) or \
            (derecho is not None and derecho.getDato() == datoX):
                return True
            else:
                return False
            
    def padre(self, datoX, datoZ):
        # Solo llama a la función hijo, porque son recíprocas
        return self.hijo(datoZ, datoX)
    
    def camino(self, origen, destino):
        nodo_origen = self.buscar(origen)
        if nodo_origen is None:
            print(f"ERROR: el nodo {origen} no existe")
            return None
        camino_lista = []
        if not self.caminoRecursivo(nodo_origen, destino, camino_lista):
            print(f"ERROR: {origen} no es ancestro de {destino}")
            return None
        return camino_lista

    def caminoRecursivo(self, nodo, destino, lista):
        if nodo is None:
            return False
        lista.append(nodo.getDato())  # Agregamos nodo actual
        if nodo.getDato() == destino:
            return True
        if self.caminoRecursivo(nodo.getIzquierdo(), destino, lista):
            return True
        if self.caminoRecursivo(nodo.getDerecho(), destino, lista):
            return True
        lista.pop()  # No se encontró en este camino → retrocedemos
        return False
    
    def altura(self):
        return self.alturaRecursivo(self.__raiz)

    def alturaRecursivo(self, nodo):
        if nodo is None:
            return -1  # Árbol vacío
        altura_izq = self.alturaRecursivo(nodo.getIzquierdo())
        altura_der = self.alturaRecursivo(nodo.getDerecho())
        return 1 + max(altura_izq, altura_der)
    
if __name__ == "__main__":
    # Crear árbol
    arbol = ArbolBinarioBusqueda()

    # Insertar elementos de a uno
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)

    # Recorridos
    print("Recorrido InOrden:")
    arbol.inOrden()

    print("Recorrido PreOrden:")
    arbol.preOrden()

    print("Recorrido PostOrden:")
    arbol.postOrden()

    # Buscar elementos
    arbol.buscar(40)
    arbol.buscar(100)  # Este no existe

    # Nivel de un nodo
    print(f"Nivel del nodo 60: {arbol.nivel(60)}")

    # Verificar hoja
    print(f"El nodo 20 es hoja?: {arbol.hoja(20)}")
    print(f"El nodo 30 es hoja?: {arbol.hoja(30)}")

    # Hijo y Padre
    print(f"¿30 es hijo de 50?: {arbol.hijo(30, 50)}")
    print(f"¿50 es padre de 30?: {arbol.padre(50, 30)}")

    # Altura del árbol
    print(f"Altura del árbol: {arbol.altura()}")

    # Camino de un nodo a otro
    camino = arbol.camino(50, 40)
    print(f"Camino de 50 a 40: {camino}")

    # Suprimir elementos
    print("Suprimiendo nodo 20 (hoja)")
    arbol.suprimir(20)
    print("InOrden después de suprimir 20:")
    arbol.inOrden()

    print("Suprimiendo nodo 30 (grado 1)")
    arbol.suprimir(30)
    print("InOrden después de suprimir 30:")
    arbol.inOrden()

    print("Suprimiendo nodo 50 (grado 2)")
    arbol.suprimir(50)
    print("InOrden después de suprimir 50:")
    arbol.inOrden()



    
