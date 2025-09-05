import numpy as np

class PilaSecuencial:
    __tope : int
    __cantidad : int
    __elementos : np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope= -1
        self.__elementos = np.empty(self.__cantidad, dtype=object)

    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, dato):
        if self.__tope < self.__cantidad - 1:
            self.__tope += 1
            self.__elementos[self.__tope] = dato
            return dato
        
    def suprimir(self):
        if self.vacia():
            print("La pila esta vacia")
            return None
        else:
            x= self.__elementos[self.__tope]
            self.__tope -=1
            return x
    
    def mostrar(self):
        i=self.__tope
        if not self.vacia():
            while i >= 0:
                print(self.__elementos[i])
                i-=1
        else:
            print("La pila esta vacia")
