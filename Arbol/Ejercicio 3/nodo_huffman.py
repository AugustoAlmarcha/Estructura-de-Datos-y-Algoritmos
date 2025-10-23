class NodoHuffman:
    def __init__(self, caracter=None, frecuencia=0, izquierdo=None, derecho=None):
        self.caracter = caracter  # Carácter (solo en nodos hoja)
        self.frecuencia = frecuencia
        self.izquierdo = izquierdo
        self.derecho = derecho

    # Método de comparación para usar la clase en una cola de prioridad (heapq)
    # Compara nodos basándose en su frecuencia.
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia
    
import heapq