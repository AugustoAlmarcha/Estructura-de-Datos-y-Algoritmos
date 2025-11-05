from clasenodoavl import Nodo

class AVLTree:
    def __init__(self):
        self.raiz = None

    # --- Métodos de Rotación ---

    def _rotacion_simple_izq(self, p):
        p1 = p.izq
        p.izq = p1.der
        p1.der = p
        return p1

    def _rotacion_simple_der(self, p):
        p1 = p.der
        p.der = p1.izq
        p1.izq = p
        return p1

    # --- Métodos de Balanceo (durante la Inserción) ---
    # Nota: El parámetro 'h' se usa como una bandera booleana (True/False)
    # y se pasa como una lista [h] para simular el paso por referencia de C++.

    def _balancear_insercion_izq(self, p, h):
        # 'h' es la bandera que indica si la altura de la rama izquierda creció
        p1, p2 = p.izq, None

        if p1.bal == -1: # Rotación simple izquierda
            p = self._rotacion_simple_izq(p)
            p.bal = 0
        else: # Rotación doble izquierda (con pivote en p1.der)
            p2 = p1.der
            p1.der = p2.izq
            p2.izq = p1
            p.izq = p2.der
            p2.der = p

            # Ajuste de factores de balanceo
            if p2.bal == -1:
                p.bal = 1
            else:
                p.bal = 0
            if p2.bal == 1:
                p1.bal = -1
            else:
                p1.bal = 0
            p = p2
        
        # Después de la rotación, el subárbol queda balanceado
        p.bal = 0
        h[0] = False
        return p

    def _balancear_insercion_der(self, p, h):
        # 'h' es la bandera que indica si la altura de la rama derecha creció
        p1, p2 = p.der, None

        if p1.bal == 1: # Rotación simple derecha
            p = self._rotacion_simple_der(p)
            p.bal = 0
        else: # Rotación doble derecha (con pivote en p1.izq)
            p2 = p1.izq
            p1.izq = p2.der
            p2.der = p1
            p.der = p2.izq
            p2.izq = p

            # Ajuste de factores de balanceo
            if p2.bal == 1:
                p.bal = -1
            else:
                p.bal = 0
            if p2.bal == -1:
                p1.bal = 1
            else:
                p1.bal = 0
            p = p2
            
        # Después de la rotación, el subárbol queda balanceado
        p.bal = 0
        h[0] = False
        return p
    
    # --- Inserción (función recursiva) ---

    def _insertar_recursivo(self, p, x, h):
        if p is None:
            p = Nodo(x)
            h[0] = True # El subárbol creció
            return p

        if p.key > x:
            p.izq = self._insertar_recursivo(p.izq, x, h)
            if h[0]: # La rama izquierda creció
                if p.bal == 1:
                    p.bal = 0
                    h[0] = False
                elif p.bal == 0:
                    p.bal = -1
                else: # p.bal == -1: Necesita rebalancear
                    p = self._balancear_insercion_izq(p, h)

        elif p.key < x:
            p.der = self._insertar_recursivo(p.der, x, h)
            if h[0]: # La rama derecha creció
                if p.bal == -1:
                    p.bal = 0
                    h[0] = False
                elif p.bal == 0:
                    p.bal = 1
                else: # p.bal == 1: Necesita rebalancear
                    p = self._balancear_insercion_der(p, h)
        else:
            p.con += 1 # Llave duplicada, solo incrementa el contador
            h[0] = False # La altura no cambia

        return p

    def insertar(self, x):
        h = [False] # Simula el paso por referencia (bandera de cambio de altura)
        self.raiz = self._insertar_recursivo(self.raiz, x, h)

    # --- Balanceo (durante la Supresión) ---

    def _balani(self, p, h): # Rebalanceo si se eliminó en la rama derecha (rama izquierda "crece")
        p1, p2, b1, b2 = None, None, 0, 0
        
        # Mapea el switch-case de C++
        if p.bal == -1:
            p.bal = 0
            # h sigue siendo True
        elif p.bal == 0:
            p.bal = 1
            h[0] = False # Ya no propaga el cambio de altura
        elif p.bal == 1: # Necesita rebalancear
            p1 = p.der
            b1 = p1.bal
            if b1 >= 0: # Rotación simple derecha (Incluye caso b1=0)
                p = self._rotacion_simple_der(p)
                if b1 == 0: # Caso especial: la altura no se reduce, solo se balancea
                    p.bal = 1
                    p1.bal = -1
                    h[0] = False
                else:
                    p.bal = 0
                    p1.bal = 0
            else: # Rotación doble (p1.bal == -1)
                p2 = p1.izq
                b2 = p2.bal
                
                # Rotación doble (rotación simple izquierda en p1 y luego simple derecha en p)
                p1.izq = p2.der
                p2.der = p1
                p.der = p2.izq
                p2.izq = p

                # Ajuste de factores de balanceo
                if b2 == 1:
                    p.bal = -1
                else:
                    p.bal = 0
                if b2 == -1:
                    p1.bal = 1
                else:
                    p1.bal = 0
                p = p2
                p2.bal = 0
        
        return p

    def _baland(self, p, h): # Rebalanceo si se eliminó en la rama izquierda (rama derecha "crece")
        p1, p2, b1, b2 = None, None, 0, 0
        
        # Mapea el switch-case de C++
        if p.bal == 1:
            p.bal = 0
            # h sigue siendo True
        elif p.bal == 0:
            p.bal = -1
            h[0] = False # Ya no propaga el cambio de altura
        elif p.bal == -1: # Necesita rebalancear
            p1 = p.izq
            b1 = p1.bal
            if b1 <= 0: # Rotación simple izquierda (Incluye caso b1=0)
                p = self._rotacion_simple_izq(p)
                if b1 == 0: # Caso especial: la altura no se reduce, solo se balancea
                    p.bal = -1
                    p1.bal = 1
                    h[0] = False
                else:
                    p.bal = 0
                    p1.bal = 0
            else: # Rotación doble (p1.bal == 1)
                p2 = p1.der
                b2 = p2.bal
                
                # Rotación doble (rotación simple derecha en p1 y luego simple izquierda en p)
                p1.der = p2.izq
                p2.izq = p1
                p.izq = p2.der
                p2.der = p

                # Ajuste de factores de balanceo
                if b2 == -1:
                    p.bal = 1
                else:
                    p.bal = 0
                if b2 == 1:
                    p1.bal = -1
                else:
                    p1.bal = 0
                p = p2
                p2.bal = 0

        return p

    # --- Supresión (Rutina de búsqueda del Sucesor Inorden) ---

    def _sup(self, r, h, c): # 'r' es el nodo actual, 'c' es el sucesor encontrado
        if r.der is not None:
            r.der = self._sup(r.der, h, c)
            if h[0]:
                r = self._baland(r, h)
        else:
            # Encontramos el sucesor inorden (el nodo más a la derecha en la rama izquierda)
            c[0] = r # 'c' ahora apunta al sucesor
            r = r.izq # Reemplaza r con su hijo izquierdo (que puede ser None)
            h[0] = True # La altura de este subárbol se redujo
        
        return r

    # --- Supresión (función principal recursiva) ---

    def _suprimir_recursivo(self, p, x, h):
        if p is None:
            print(f"\nLa llave {x} no está en el arbol")
            return None

        if p.key > x:
            p.izq = self._suprimir_recursivo(p.izq, x, h)
            if h[0]:
                p = self._balani(p, h)
        elif p.key < x:
            p.der = self._suprimir_recursivo(p.der, x, h)
            if h[0]:
                p = self._baland(p, h)
        else:
            # Caso: p.key == x (el nodo a eliminar)
            if p.con > 1:
                p.con -= 1
                h[0] = False # No hay cambio de altura
            else:
                q = p
                if q.der is None:
                    p = q.izq
                    h[0] = True
                elif q.izq is None:
                    p = q.der
                    h[0] = True
                else:
                    # El nodo tiene dos hijos: buscar sucesor inorden
                    c = [None] # Usamos una lista para simular el puntero a 'c'
                    q.izq = self._sup(q.izq, h, c) # Buscar el sucesor a la izquierda
                    
                    # Reemplazar la llave y el contador del nodo a eliminar con los del sucesor
                    p.key = c[0].key
                    p.con = c[0].con

                    if h[0]:
                        p = self._balani(p, h)

                #print(f"Llave {q.key} eliminada.") # Para debug/seguimiento
        
        return p

    def suprimir(self, x):
        h = [False] # Simula el paso por referencia
        self.raiz = self._suprimir_recursivo(self.raiz, x, h)

    # --- Mostrar (Recorrido) ---

    def _mostrar_recursivo(self, p):
        if p is not None:
            print(f"Llave: {p.key}, Factor Balanceo: {p.bal}, Conteo: {p.con}")
            print(f"  Izquierda de {p.key}:")
            self._mostrar_recursivo(p.izq)
            print(f"  Derecha de {p.key}:")
            self._mostrar_recursivo(p.der)

    def mostrar(self):
        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            print("\n--- ÁRBOL AVL ---")
            self._mostrar_recursivo(self.raiz)
            print("-----------------")


# --- Código de Prueba (Simula la función main) ---

def main_avl():
    arbol = AVLTree()
    opcion = 0
    
    while opcion != 4:
        # Esto reemplaza clrscr() y el menú de C++
        print("\n\n Menú AVL")
        print(" 1_ Insertar")
        print(" 2_ Suprimir")
        print(" 3_ Mostrar")
        print(" 4_ Salir")
        
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            opcion = 0
            continue

        if opcion == 1:
            print("Ingrese elementos a insertar (finaliza con 0):")
            while True:
                try:
                    elemento = int(input("Elemento: "))
                    if elemento == 0:
                        break
                    arbol.insertar(elemento)
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")

        elif opcion == 2:
            print("Ingrese elementos a suprimir (finaliza con 0):")
            while True:
                try:
                    elemento = int(input("Elemento: "))
                    if elemento == 0:
                        break
                    arbol.suprimir(elemento)
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")
        
        elif opcion == 3:
            arbol.mostrar()
            input("Presione Enter para continuar...") # Simula getchar()
        
        elif opcion == 4:
            print("Saliendo del programa.")
        
        else:
            print("Opción no válida.")


main_avl()