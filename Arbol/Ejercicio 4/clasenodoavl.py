class Nodo:
    """
    Estructura del nodo del Árbol AVL.
    key: valor de la llave.
    con: contador de ocurrencias (manejo de duplicados).
    bal: factor de balanceo (altura de la rama derecha - altura de la rama izquierda).
         -1: izquierda pesada, 0: balanceado, 1: derecha pesada.
    izq, der: punteros a los nodos hijo.
    """
    def __init__(self, key):
        self.key = key
        self.con = 1  # Contador de ocurrencias
        self.bal = 0  # Factor de balanceo
        self.izq = None
        self.der = None