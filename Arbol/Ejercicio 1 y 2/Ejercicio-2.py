from ClaseArbolbinariobusquedad import ArbolBinarioBusqueda


class ArbolExtension(ArbolBinarioBusqueda):
    """
    Clase que extiende la funcionalidad de ArbolBinarioBusqueda 
    para incluir los métodos del Ejercicio N°2.
    """
    def __init__(self):
        super().__init__() 

    # ----------------------------------------------------
    # Ejercicio N°2 - Inciso a): Padre y Hermano
    # ----------------------------------------------------
    def padreYHermano(self, dato):
        if self.vacio(): 
            print("Árbol vacío: no hay padre ni hermano.")
            return None, None
        if self.getRaiz().getDato() == dato: #El dato es la raíz
            print(f"Nodo ingresado: {dato}")
            print(f"Padre: El nodo es la raíz, no tiene padre.")
            print(f"Hermano: El nodo es la raíz, no tiene hermano.")
            return None, None
        return self.padreYHermanoRecursivo(self.getRaiz(), dato)

    def padreYHermanoRecursivo(self, nodo, dato):
        if nodo is None:
            print(f"Error: El dato {dato} no existe en el árbol.")
            return None, None 

        hijo_izq = nodo.getIzquierdo()
        hijo_der = nodo.getDerecho()

        if (hijo_izq is not None and hijo_izq.getDato() == dato) or \
           (hijo_der is not None and hijo_der.getDato() == dato):

            padre = nodo.getDato()
            hermano = None
            
            if hijo_izq is not None and hijo_der is not None:
                hermano = hijo_der.getDato() if hijo_izq.getDato() == dato else hijo_izq.getDato()
            
            print(f"Nodo ingresado: {dato}")
            print(f"Padre: {padre}")
            print(f"Hermano: {hermano if hermano is not None else 'No tiene hermano.'}")
            
            return padre, hermano
        
        if dato < nodo.getDato():
            return self.padreYHermanoRecursivo(hijo_izq, dato)

        elif dato > nodo.getDato():
            return self.padreYHermanoRecursivo(hijo_der, dato)

        return None, None
    
    # ----------------------------------------------------
    # Ejercicio N°2 - Inciso b): Cantidad de Nodos Recursiva
    # ----------------------------------------------------
    def contarNodos(self):
        if self.vacio():
            return 0
        cantidad = self.contarNodosRecursivo(self.getRaiz())
        print(f"Cantidad total de nodos (recursivo): {cantidad}")
        return cantidad

    def contarNodosRecursivo(self, nodo):
        if nodo is None:
            return 0
        # Es 1 (el nodo actual) + la cuenta del subárbol izquierdo + la cuenta del subárbol derecho.
        return 1 + self.contarNodosRecursivo(nodo.getIzquierdo()) + \
                   self.contarNodosRecursivo(nodo.getDerecho())

    # ----------------------------------------------------
    # Ejercicio N°2 - Inciso b): Cantidad de Nodos Recursiva (versión alternativa)
    # ----------------------------------------------------
    def mostrar(self):
        if self.vacio():
            print("El arbol esta vacio.")
        else:
            contador = self.mostrarRecursivo(self.getRaiz())
            print(f"Cantidad total de nodos (recursivo - versión alternativa): {contador}")
    def mostrarRecursivo(self,nodo):
        if nodo is not None:
            contador = 1 + self.mostrarRecursivo(nodo.getIzquierdo()) + \
            self.mostrarRecursivo(nodo.getDerecho())
            print(f"Nodo: {nodo.getDato()}")
            return contador
        else:
            return 0
        
    #---------------------------------------------------
    #Mostrar la Altura de un Arbol
    #---------------------------------------------------
    def alturax(self):
        if self.vacio():
            print("El arbol esta vacio")
            return
        else:
            altura=self.alturaxrecursivo(self.getRaiz()) 
        print(f"La altura del arbol es de {altura}")

    def alturaxrecursivo(self,nodox):
        if nodox is not None:
            izquierdo = self.alturaxrecursivo(nodox.getIzquierdo())
            derecho = self.alturaxrecursivo(nodox.getDerecho())
            return 1 + max(izquierdo, derecho)
        else:
            return -1

    # ----------------------------------------------------
    # Ejercicio N°2 - Inciso c): Mostrar Sucesores
    # ----------------------------------------------------
    def mostrarDescendientes(self, clave):
        nodo_origen = self.buscarRecursivo(self.getRaiz(), clave) 
        if nodo_origen is None:
            print(f"Error: El nodo {clave} no existe o el árbol está vacío.")
            return
        print(f"Descendientes del nodo {clave} (PreOrden):")
        
        # Recorrer e imprimir el subárbol izquierdo (si existe)
        if nodo_origen.getIzquierdo() is not None:
            print("  Por su Izquierda: ", end="")
            self.imprimirSubarbol(nodo_origen.getIzquierdo())
            print()
            
        # Recorrer e imprimir el subárbol derecho (si existe)
        if nodo_origen.getDerecho() is not None:
            print("  Por su Derecha: ", end="")
            self.imprimirSubarbol(nodo_origen.getDerecho())
            print()
            
        if nodo_origen.getIzquierdo() is None and nodo_origen.getDerecho() is None:
             print("  No tiene descendientes.")
    #------------------------------------------------------
    #Mostrar Los sucesores alternativo
    #------------------------------------------------------
    def mostrarsucesores(self,clave):
        if self.vacio():
            print("El arbol esta vacio")
            return
        else:
            nodobuscado = self.buscar(clave)
            if nodobuscado is None:
                print("El nodo no se encuentra en el arbol")
                return 
            elif nodobuscado.getIzquierdo() is None and nodobuscado.getDerecho() is None:
                print("El nodo no tiene sucesores")
                return
            else:
                self.mostrarsucesoresrecursivo(nodobuscado,clave)

    def mostrarsucesoresrecursivo(self,nodobuscado,clave):
        if nodobuscado is not None:
            self.mostrarsucesoresrecursivo(nodobuscado.getIzquierdo(),clave)
            print(f"Sucesor de {clave} es: {nodobuscado.getDato()}" if nodobuscado.getDato() != clave else "")
            self.mostrarsucesoresrecursivo(nodobuscado.getDerecho(),clave)




    # Función auxiliar para recorrer e imprimir el subárbol (Recorrido PreOrden)
    def imprimirSubarbol(self, nodo):
        if nodo is not None:
            print(f"{nodo.getDato()} -", end=" ")
            self.imprimirSubarbol(nodo.getIzquierdo())
            self.imprimirSubarbol(nodo.getDerecho())


    #Otra version de buscar padre y hermano  

    def buscarpadreyhermano(self,x):
        if self.vacio():
            print("El árbol está vacío.")
            return
        else:
            self.buscarpadreyhermanoRecursivo(self.getRaiz(),x)

    def buscarpadreyhermanoRecursivo(self,nodox,datox):
        if datox == self.getRaiz().getDato():
            print("El nodo ingresado es la raíz, no tiene padre ni hermano.")
            return
        if nodox is None:
            print("No se encontro el nodo con el dato ingresado.")
            return
        if nodox.getIzquierdo() is not None and nodox.getIzquierdo().getDato() == datox or nodox.getDerecho() is not None and nodox.getDerecho().getDato() == datox:
            padre = nodox
        else:
            padre = None
        if datox < nodox.getDato():
            self.buscarpadreyhermanoRecursivo(nodox.getIzquierdo(),datox)
        else:
            self.buscarpadreyhermanoRecursivo(nodox.getDerecho(),datox)
        hermano = None
        if padre is not None and padre.getIzquierdo() is not None and padre.getIzquierdo().getDato() != datox:
            hermano = padre.getIzquierdo()
        elif padre is not None and padre.getDerecho() is not None and padre.getDerecho().getDato() != datox:
            hermano = padre.getDerecho()
        if padre is not None or hermano is not None:
            print(f"El padre del nodo {datox} es: {padre.getDato()} y el hermano es: {hermano.getDato() if hermano is not None else 'No tiene hermano.'}")

if __name__ == '__main__':
    arbol = ArbolExtension() 
    
    arbol.insertar(10)
    arbol.insertar(7)
    arbol.insertar(5)
    arbol.insertar(9)
    arbol.insertar(15)

    print("\n--- Recorrido InOrden del Árbol ---")
    arbol.inOrden()
    print("-" * 30)

    print("Metodos Alternativos")
    arbol.buscarpadreyhermano(10)
    arbol.mostrar()
    arbol.alturax()
    arbol.mostrarsucesores(15)

    print("--- Prueba del Ejercicio N°2 a) ---")
    print("\n[Busqueda: 40]")
    arbol.padreYHermano(40)
    print("\n[Busqueda: 70]")
    arbol.padreYHermano(70)
    print("\n[Busqueda: 60]")
    arbol.padreYHermano(60)

    # ----------------------------------------------------
    # PRUEBA: Ejercicio N°2 b) - Cantidad de Nodos Recursiva
    # ----------------------------------------------------
    print("\n--- Ejercicio N°2 b): Cantidad de Nodos ---")
    arbol.contarNodos()
    # ----------------------------------------------------
    # PRUEBA: Ejercicio N°2 c) - Mostrar Descendientes
    # ----------------------------------------------------
    print("\n--- Ejercicio N°2 c): Mostrar Descendientes ---")
    
    # Prueba 1: Descendientes de 30 (20, 40)
    print("\n[Descendientes de 30]")
    arbol.mostrarDescendientes(30)
    
    # Prueba 2: Descendientes de 70 (60)
    print("\n[Descendientes de 70]")
    arbol.mostrarDescendientes(70)
    
    # Prueba 3: Nodo Hoja (20)
    print("\n[Descendientes de 20]")
    arbol.mostrarDescendientes(20) 
    
    print("\n------------------ FIN DE PRUEBAS ------------------")

