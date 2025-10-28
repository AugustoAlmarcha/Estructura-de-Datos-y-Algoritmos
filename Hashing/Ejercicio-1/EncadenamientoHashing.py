#Encadenamiento
#Objeto de datos y Nodo
import numpy as np

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



    