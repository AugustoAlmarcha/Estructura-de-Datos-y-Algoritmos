from nodo import Nodo
class ColaEncadenada:
    __primero:Nodo
    __ultimo:Nodo
    __cantidad:int

    def __init__(self):
        self.__primero=None
        self.__ultimo=None
        self.__cantidad=0
    
    def getcantidad(self):
        return self.__cantidad
    
    def vacia(self):
        return self.__cantidad==0

    def insertar(self, elemento):
        nuevonodo=Nodo(elemento)
        nuevonodo.setSiguiente(None)
        if self.__ultimo is None:
            self.__primero=nuevonodo
        else:
            self.__ultimo.setSiguiente(nuevonodo)
        self.__ultimo=nuevonodo
        self.__cantidad+=1
    
    def suprimir(self):
        if self.vacia():
            return None
        else:
            elemento=self.__primero.getDato()
            self.__primero=self.__primero.getSiguiente()
            if self.__primero is None:
                self.__ultimo=None
            self.__cantidad-=1
            return elemento
    
    def getprimero(self):
        if self.vacia():
            print("Cola vacia")
            return None
        else:
            return self.__primero.getDato()
    
    def recorrer(self):
        if self.vacia():
            print("Cola vacia")
        else:
            actual=self.__primero
            while actual is not None:
                print(actual.getDato())
                actual=actual.getSiguiente()

# if __name__ == "__main__":
#     c=ColaEncadenada()
#     c.insertar(1)
#     c.insertar(2)
#     c.insertar(3)
#     c.insertar(4)
#     c.insertar(5)
#     c.recorrer()
#     print("Eliminando un elemento")
#     c.suprimir()
#     c.recorrer()
#     print("Insertando un elemento")
#     c.insertar(6)
#     c.recorrer()
#     print("El primero es:", c.getprimero())