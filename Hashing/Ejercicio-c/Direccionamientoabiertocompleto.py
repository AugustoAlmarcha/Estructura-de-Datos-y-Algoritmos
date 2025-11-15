#Metodo de Divisiones 
#Se ejecuta escribiendo: ↓ en la terminal
#  py -m Ejercicio-c.Direccionamientoabiertocompleto 

import numpy as np
import random
from Transformaciones.todaslastransformaciones import *

class TablaHash:
    __tabla:np.ndarray
    __tamanio:int

    def __init__(self, tamanio:int):
        self.__tamanio = int(tamanio / 0.7) # Factor de carga 0.7
        self.__tabla = np.empty(self.__tamanio, dtype=object)
    
    #----------------------------------------------------------------------#
    #Metodo Insertar y Buscar con la politica de secuencia de prueba lineal
    #----------------------------------------------------------------------#
    def insertarlineal(self, clave):
        # calculamos la posición usando el método de división
        pos = TransformacionesHashing.metodo_division(clave, self.__tamanio) #Modificar aqui para usar cualquier metodo de transformación
        i = 0
        while self.__tabla[pos] is not None and i < self.__tamanio:
            pos = (pos + 1) % self.__tamanio
            i += 1
        if i == self.__tamanio:
            print("Tabla llena, no se puede insertar")
        else:
            self.__tabla[pos] = clave

    def buscarlineal(self, clave):
        pos = TransformacionesHashing.metodo_division(clave, self.__tamanio) #Modificar aqui para usar cualquier metodo de transformación
        i = 0
        while self.__tabla[pos] != clave and self.__tabla[pos] is not None and i < self.__tamanio:
            pos = (pos + 1) % self.__tamanio
            i += 1
        if self.__tabla[pos] == clave:
            return f"Clave {clave} encontrada en posición {pos}"
        else:
            return f"Clave {clave} no encontrada"
    
    #----------------------------------------------------------------------#
    #Metodo Insertar y Buscar con la politica de doble hash"""
    #----------------------------------------------------------------------#
    def insertar_doblehash(self, clave):
        h1 = TransformacionesHashing.metodo_division(clave, self.__tamanio)
        h2 = 1 + (clave % (self.__tamanio - 1))
        pos = h1
        i = 0
        while self.__tabla[pos] is not None and i < self.__tamanio:
            pos = (h1 + i * h2) % self.__tamanio
            i += 1
        if i == self.__tamanio:
            print("Tabla llena, no se puede insertar")
        else:
            self.__tabla[pos] = clave

    def buscar_doblehash(self, clave):
        h1 = TransformacionesHashing.metodo_division(clave, self.__tamanio)
        h2 = 1 + (clave % (self.__tamanio - 1))
        pos = h1
        i = 0
        while self.__tabla[pos] != clave and self.__tabla[pos] is not None and i < self.__tamanio:
            pos = (h1 + i * h2) % self.__tamanio
            i += 1
        if self.__tabla[pos] == clave:
            return f"Clave {clave} encontrada en posición {pos}"
        else:
            return f"Clave {clave} no encontrada"
    #----------------------------------------------------------------------#
    #Metodo Insertar y Buscar con la politica de direccionamiento aleatorio
    #----------------------------------------------------------------------#
    def insertaraleatorio(self, clave):
        pos = TransformacionesHashing.metodo_division(clave, self.__tamanio)
        random.seed(clave)  # semilla fija para que siempre genere la misma secuencia
        i = 0
        while self.__tabla[pos] is not None and i < self.__tamanio:
            salto = random.randint(1, self.__tamanio - 1)
            pos = (pos + salto) % self.__tamanio
            i += 1
        if i == self.__tamanio:
            print("Tabla llena, no se puede insertar")
        else:
            self.__tabla[pos] = clave

    def buscaraleatorio(self, clave):
        pos = TransformacionesHashing.metodo_division(clave, self.__tamanio)
        random.seed(clave)
        i = 0
        while self.__tabla[pos] != clave and self.__tabla[pos] is not None and i < self.__tamanio:
            salto = random.randint(1, self.__tamanio - 1)
            pos = (pos + salto) % self.__tamanio
            i += 1
        if self.__tabla[pos] == clave:
            return f"Clave {clave} encontrada en posición {pos}"
        else:
            return f"Clave {clave} no encontrada"
    #----------------------------------------------------------------------#

    def mostrar(self):
        i = 0
        while i < self.__tamanio:
            print(f"Posición {i}: {self.__tabla[i]}")
            i += 1
    
if __name__ == "__main__":
    # Crear la tabla hash
    hash = TablaHash(10)
    hash.insertarlineal(23)
    hash.insertarlineal(43)
    hash.insertarlineal(24)
    hash.insertarlineal(13)
    hash.insertarlineal(27)
    hash.insertarlineal(33)
    hash.mostrar()
    print("\nBuscando claves:")
    print("Clave 43:", hash.buscarlineal(43))
    print("Clave 99:", hash.buscarlineal(99))
    print("Clave 13:", hash.buscarlineal(13))

# Pruebas con claves alfanuméricas
# if __name__ == "__main__":
#     hash = TablaHash(10)

#     print("--- Proceso de Inserción ---")
#     hash.insertarlineal("ROMA") 
#     hash.insertarlineal("SANCHEZ") 
#     hash.insertarlineal("AMOR") 
#     hash.insertarlineal("CLARA")

#     print("\n--- Estado Final de la Tabla ---")
#     hash.mostrar()

#     print("\n--- Pruebas de Búsqueda ---")
#     print("Buscando 'CLARA':", hash.buscarlineal("CLARA"))
#     print("Buscando 'ALFA':", hash.buscarlineal("ALFA"))
#     print("Buscando 'CLAVE_FALSA':", hash.buscarlineal("CLAVE_FALSA"))

    