import numpy as np
class cola:
    __listacola:np.ndarray
    __maximo:int
    __primero:int
    __ultimo:int
    __cantidad:int

    def __init__(self, maximo=10):
        self.__listacola=np.empty(maximo,dtype=object)
        self.__maximo=maximo
        self.__primero=0
        self.__ultimo=0
        self.__cantidad=0
    
    def vacia(self):
        return self.__cantidad==0
    
    def insertar(self,elemento):
        if self.__cantidad < self.__maximo:
            self.__listacola[self.__ultimo]=elemento
            self.__ultimo=(self.__ultimo+1)%self.__maximo
            self.__cantidad+=1
        else:
            print("Cola llena")

    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return None
        else:
            elemento = self.__listacola[self.__primero]
            self.__primero=(self.__primero+1)%self.__maximo
            self.__cantidad-=1
            return elemento

    def recorrer(self):
        if self.vacia():
            print("Cola vacia")
        else:
            i=0
            indice=self.__primero
            while i < self.__cantidad:
                print(self.__listacola[indice])
                indice=(indice+1)%self.__maximo
                i+=1
# if __name__ == "__main__":
#     c=cola(5)
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