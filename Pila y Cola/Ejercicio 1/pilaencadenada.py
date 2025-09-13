from clasenodo import *

class Pilaencadenada:
    __cantidad:int
    __tope: Nodo

    def __init__(self):
        self.__cantidad = 0
        self.__tope = None
    
    def vacia (self):
        return self.__cantidad == 0
    
    def insertar(self, dato):
        nuevonodo = Nodo(dato)
        nuevonodo.setSiguiente(self.__tope)
        self.__tope = nuevonodo
        self.__cantidad += 1
        return nuevonodo.getDato()
    
    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
            return None
        else:
            x=self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__cantidad -= 1
            return x
    
    def mostrar(self):
        aux = self.__tope
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
        
if __name__=="__main__":
    pila = Pilaencadenada()
    pila.insertar(5)
    pila.insertar(10)
    pila.insertar(15)
    pila.mostrar()
    print("----")
    pila.suprimir()
    pila.mostrar()


