from clasenodo import *

class ListaEncadenada:
    __cantidad: int
    __cabeza : Nodo

    def __init__(self):
        self.__cantidad = 0
        self.__cabeza = None

    def vacia(self):
        return self.__cabeza == None
    
    def primer_elemento(self):
        if self.vacia():
            return None
        return self.__cabeza.getDato()
    
    def ultimo_elemento(self):
        if self.vacia():
            return None
        aux = self.__cabeza
        while aux.getSiguiente() is not None:
            aux = aux.getSiguiente()
        return aux.getDato()
    
    def siguiente(self, posicion):
        if posicion < 0 or posicion >= self.__cantidad - 1:
            return None
        aux = self.__cabeza
        i = 0
        while i < posicion:
            aux = aux.getSiguiente()
            i += 1
        return aux.getSiguiente()
    
    def anterior(self, posicion):
        if posicion <= 0 or posicion > self.__cantidad:
            return None
        aux = self.__cabeza
        i = 0
        while i < posicion - 1:
            aux = aux.getSiguiente()
            i += 1
        return aux
    
    def insertar(self, item, posicion):
        if posicion < 0 or posicion > self.__cantidad:
            print("Error")
            return
        
        nuevonodo = Nodo(item)
        
        if posicion == 0:
            nuevonodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevonodo
        else:
            anterior = self.anterior(posicion)
            nuevonodo.setSiguiente(anterior.getSiguiente())
            anterior.setSiguiente(nuevonodo)
        
        self.__cantidad += 1

    def suprimir(self, posicion):
        if posicion < 0 or posicion >= self.__cantidad or self.vacia():
            print("Error, Posicion Invalida")
            return
        if posicion == 0:
            aux = self.__cabeza
            self.__cabeza = aux.getSiguiente()
        else:
            anterior = self.anterior(posicion)
            aux= anterior.getSiguiente()
            anterior.setSiguiente(aux.getSiguiente())
        self.__cantidad -=1 
        return aux.getDato()
    
    def recuperar(self,posicion):
        if posicion < 0 or posicion >= self.__cantidad or self.vacia():
            print("Error, Posicion invalida")
            return
        else:
            i=0
            aux=self.__cabeza
            while i < posicion:
                aux = aux.getSiguiente()
                i+=1
            return aux.getDato()
        
    def buscar(self,elemento):
        i=0
        band=False
        aux = self.__cabeza
        while i < self.__cantidad and band is False:
            if aux.getDato() == elemento:
                band=True
                print(f"Se encontro el elemento en la posicion {i}")
                return i
            aux = aux.getSiguiente()
            i+=1
        if band is False:
            print("No se encontro el elemento buscado")
            return None
    
    def recorrer(self):
        aux=self.__cabeza
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()


if __name__ == '__main__':
    lista = ListaEncadenada()
    print("¿La lista está vacía?", lista.vacia())
    lista.insertar(10, 0)
    lista.insertar(20, 1)
    lista.insertar(30, 2)
    print("Primer elemento:", lista.primer_elemento())
    print("Último elemento:", lista.ultimo_elemento())
    print("Elemento en posición 1:", lista.recuperar(1))
    print("Buscar elemento 20:", lista.buscar(20))
    print("Recorrer la lista:")
    lista.recorrer()
    print("Suprimir elemento en posición 1:", lista.suprimir(1))
    print("Recorrer la lista después de suprimir:")
    lista.recorrer()
    lista.insertar(40,1)
    print("---------")
    lista.recorrer()
    lista.insertar(50,1)
    print("---------")
    lista.recorrer()

            
        


        


        

            





    


        