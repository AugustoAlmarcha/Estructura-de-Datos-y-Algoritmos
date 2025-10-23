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

    # Función auxiliar para recorrer e imprimir el subárbol (Recorrido PreOrden)
    def imprimirSubarbol(self, nodo):
        if nodo is not None:
            print(f"{nodo.getDato()} -", end=" ")
            self.imprimirSubarbol(nodo.getIzquierdo())
            self.imprimirSubarbol(nodo.getDerecho())


if __name__ == '__main__':
    arbol = ArbolExtension() 
    
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)

    print("\n--- Recorrido InOrden del Árbol ---")
    arbol.inOrden()
    print("-" * 30)

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

