#Se ejecuta escribiendo ↓ en la terminal.
#py -m Ejercicio-c.Encadenamientocompleto 
import numpy as np
from Transformaciones.todaslastransformaciones import *

class Nodo:
    __dato:object
    __siguiente = object
    
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
    
    def setDato(self,dato):
        self.__dato = dato

class TablaHash:
    __tabla:np.ndarray
    __tamanio:int

    def __init__(self, tamanio:int):
        self.__tamanio = tamanio
        self.__tabla = np.empty(tamanio, dtype=object)
        for i in range(tamanio):
            self.__tabla[i] = None

    def insertar(self, clave):
        pos = TransformacionesHashing.metodo_extraccion(clave, self.__tamanio) #Modificar aqui para usar cualquier metodo de transformación
        nuevo = Nodo(clave)
        # Si la posición está vacía
        if self.__tabla[pos] is None:
            self.__tabla[pos] = nuevo
        else:
            # Si ya hay un nodo, lo encadenamos al final de la lista
            actual = self.__tabla[pos]
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nuevo)

    def buscar(self, clave):
        pos = TransformacionesHashing.metodo_extraccion(clave, self.__tamanio)  # función de transformación
        actual = self.__tabla[pos]
        while actual is not None:
            if actual.getDato() == clave:
                return f"Clave {clave} encontrada en posición {pos}"
            actual = actual.getSiguiente()
        return f"Clave {clave} no encontrada"

    def mostrar(self):
        for i in range(self.__tamanio):
            print(f"Posición {i}: ", end="")
            actual = self.__tabla[i]
            while actual is not None:
                print(f"{actual.getDato()} -> ", end="")
                actual = actual.getSiguiente()
            print("None")


if __name__ == "__main__":
    hash = TablaHash(10)
    hash.insertar(23)
    hash.insertar(43)
    hash.insertar(10)
    hash.insertar(32)
    hash.insertar(57)
    hash.mostrar()
    print("\nBuscar 43:", hash.buscar(43))
    print("Buscar 99:", hash.buscar(99))
