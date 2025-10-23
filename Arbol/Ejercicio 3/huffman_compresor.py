from nodo_huffman import NodoHuffman
import heapq
from collections import defaultdict
import os # Para la gestión de archivos

class HuffmanCompresor:
    
    def __init__(self):
        self.codigos = {}
        self.arbol_raiz = None

    # PASO 1: Calcular la frecuencia de cada carácter
    def calcular_frecuencias(self, nombre_archivo):
        """Lee el archivo y retorna un diccionario de frecuencias."""
        frecuencias = defaultdict(int)
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                for caracter in contenido:
                    frecuencias[caracter] += 1
        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
            return None, ""
        return frecuencias, contenido

    # PASO 2: Construir el Árbol de Huffman
    def construir_arbol(self, frecuencias):
        """Genera el árbol de Huffman a partir de las frecuencias."""
        
        # Generar una lista de árboles binarios iniciales (nodos hoja) [cite: 54]
        lista_nodos = [NodoHuffman(caracter, freq) for caracter, freq in frecuencias.items()]
        heapq.heapify(lista_nodos) # Convierte la lista en una cola de prioridad (min-heap)

        # Repetir la fusión hasta que solo quede un nodo (la raíz) [cite: 69, 99]
        while len(lista_nodos) > 1:
            # Extraer los dos nodos/subárboles con la menor frecuencia
            nodo1 = heapq.heappop(lista_nodos)
            nodo2 = heapq.heappop(lista_nodos)

            # Crear un nuevo nodo interno (árbol) cuya frecuencia es la suma [cite: 70]
            # La nueva raíz es la suma de las frecuencias de sus subárboles.
            nodo_fusion = NodoHuffman(
                caracter=None, # Nodo interno no tiene carácter
                frecuencia=nodo1.frecuencia + nodo2.frecuencia,
                izquierdo=nodo1,
                derecho=nodo2
            )
            
            # Insertar el nuevo nodo en la lista ordenada [cite: 69]
            heapq.heappush(lista_nodos, nodo_fusion)
        
        # El único nodo restante es la raíz del Árbol de Huffman
        self.arbol_raiz = lista_nodos[0]
        return self.arbol_raiz

    # PASO 3a: Generar los códigos binarios a partir del árbol
    def generar_codigos(self, nodo, codigo_actual=""):
        """
        Recorre el árbol para asignar códigos. 
        Rama izquierda = 0, Rama derecha = 1[cite: 125].
        """
        if nodo is None:
            return

        # Si es un nodo hoja, hemos encontrado un código de carácter
        if nodo.caracter is not None:
            self.codigos[nodo.caracter] = codigo_actual
            return

        # Recorrer subárbol izquierdo (0)
        self.generar_codigos(nodo.izquierdo, codigo_actual + "0")
        
        # Recorrer subárbol derecho (1)
        self.generar_codigos(nodo.derecho, codigo_actual + "1")

    # PASO 3b: Comprimir el contenido
    def comprimir(self, nombre_archivo_entrada, nombre_archivo_salida):
        """
        Función principal que ejecuta los 3 pasos de la compresión.
        """
        frecuencias, contenido = self.calcular_frecuencias(nombre_archivo_entrada)
        if frecuencias is None:
            return

        # 1. Construir el Árbol y generar los códigos
        self.construir_arbol(frecuencias)
        self.generar_codigos(self.arbol_raiz)

        # 2. Generar el mensaje codificado
        mensaje_codificado = "".join([self.codigos[caracter] for caracter in contenido])

        with open(nombre_archivo_salida, 'w') as salida:
            salida.write(mensaje_codificado)
        
        print("\n--- Resultados de la Compresión ---")
        print(f"Códigos Generados: {self.codigos}")
        print(f"Longitud original (caracteres): {len(contenido)}")
        print(f"Longitud codificada (bits, simplificado): {len(mensaje_codificado)}")
        print(f"Archivo codificado guardado en: {nombre_archivo_salida}")

# -----------------------------------------------------------------
# PRUEBA DE EJECUCIÓN
# -----------------------------------------------------------------
if __name__ == '__main__':
    # Generar un archivo de prueba si no existe
    archivo_entrada = "mensaje_original.txt"
    contenido_prueba = "HACE HACE CEDE" # Ejemplo: H(2), A(2), C(3), E(3), D(1)
    
    with open(archivo_entrada, 'w') as f:
        f.write(contenido_prueba)

    compresor = HuffmanCompresor()
    compresor.comprimir(archivo_entrada, "mensaje_comprimido.huf")