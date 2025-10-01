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
        while i <= posicion:
            aux = aux.getSiguiente()
            i += 1
        return aux
    
    def anterior(self, posicion):
        if posicion <= 0 or posicion > self.__cantidad:
            return None
        aux = self.__cabeza
        i = 0
        while i < posicion - 1:
            aux = aux.getSiguiente()
            i += 1
        return aux
    
    def insertar_ordenado(self, elemento):
        nuevonodo = Nodo(elemento)
        if self.vacia() or elemento < self.__cabeza.getDato(): #Lista vacía o el elemento es menor que la cabeza
            nuevonodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevonodo
        else:
            aux = self.__cabeza
            while aux.getSiguiente() is not None and aux.getSiguiente().getDato() < elemento: # Buscar la posición correcta
                aux = aux.getSiguiente()
            nuevonodo.setSiguiente(aux.getSiguiente()) # Insertar el nodo
            aux.setSiguiente(nuevonodo)
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
        if posicion == 0:
            aux = self.__cabeza
        else:
            anterior = self.anterior(posicion)
            aux= anterior.getSiguiente()
        return aux.getDato()
        

    def buscar(self,elemento):
        i=0
        band=False
        aux = self.__cabeza
        while aux is not None and band is False and aux.getDato() <= elemento:
            if aux.getDato() == elemento:
                band=True
            else:
                aux = aux.getSiguiente()
                i+=1
        if band is False:
            print("No se encontro el elemento buscado")
            return None
        else:
            print(f"Se encontro el elemento en la posicion {i} ('Comienza del 0')")
            return i
    
    def recorrer(self):
        aux=self.__cabeza
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()

if __name__ == "__main__":
    lista = ListaEncadenada()
    lista.insertar_ordenado(5)
    lista.insertar_ordenado(3)
    lista.insertar_ordenado(8)
    lista.insertar_ordenado(1)
    lista.recorrer()
    print("Elemento en la posicion 2:", lista.recuperar(2))
    print("Buscar elemento 3:", lista.buscar(3))
    print("Primer elemento:", lista.primer_elemento())
    print("Ultimo elemento:", lista.ultimo_elemento())
    print("Siguiente de la posicion 1:", lista.siguiente(1).getDato())
    print("Anterior de la posicion 2:", lista.anterior(2).getDato())
    print("Suprimir elemento en la posicion 1:", lista.suprimir(1))
    lista.recorrer()