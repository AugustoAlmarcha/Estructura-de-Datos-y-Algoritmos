import numpy as np

class ListaSecuencial:
    __lista : np.ndarray
    __ultimo : int
    __tamaño :int

    def __init__(self, tamaño = 10):
        self.__tamaño = tamaño
        self.__lista = np.empty(self.__tamaño, dtype=object)
        self.__ultimo = -1

    def vacia(self):
        return self.__ultimo == -1
    
    def primer_elemento(self):
        if self.vacia():
            return None
        return self.__lista[0]
    
    def ultimo_elemento(self):
        if self.vacia():
            return None
        return self.__lista[self.__ultimo]
    
    def siguiente(self, posicion):
        if posicion < 0 or posicion >= self.__ultimo:
            return None 
        return self.__lista[posicion + 1]

    def anterior(self, posicion):
        if posicion <= 0 or posicion > self.__ultimo:
            return None  
        return self.__lista[posicion - 1]
    
    def insertar(self, elemento, posicion):
        if self.__ultimo + 1 >= self.__tamaño:
            print("Error: La lista está llena.")
            return
        elif posicion < 0 or posicion > self.__ultimo + 1:
            print("Error: Posición inválida.")
            return
        if posicion <= self.__ultimo:
            i = self.__ultimo
            while i >= posicion:
                self.__lista[i + 1] = self.__lista[i]
                i -= 1
        self.__lista[posicion] = elemento
        self.__ultimo += 1
    
    def suprimir(self, posicion):
        if posicion < 0 or posicion > self.__ultimo or self.vacia():
            print("Error: Posicion Invalida")
            return
        aux = self.__lista[posicion]
        i=posicion
        while i < self.__ultimo:
            self.__lista[i] = self.__lista[i+1]
            i+=1
        self.__ultimo -=1
        return aux
    
    def recuperar(self,posicion):
        if posicion < 0 or posicion > self.__ultimo or self.vacia():
            print("Error, Posicion invalida")
            return
        else:
            return self.__lista[posicion]
    
    def buscar(self,elemento):
        i=0
        band=False
        while i <= self.__ultimo and band is False:
            if self.__lista[i] == elemento:
                band=True
                print(f"Se encontro el elemento buscado en la posicion {i} (Comienza del 0)")
                return i
            i+=1
        if band is False:
            print("No se encontro el elemento buscado")
            return None

    def recorrer(self):
        for i in range(self.__ultimo + 1):
            print(self.__lista[i])

    

if __name__ =="__main__":
    lista = ListaSecuencial()
    lista.insertar(10, 0)
    lista.insertar(20, 1)
    lista.insertar(30, 2)
    print("Lista después de insertar 10, 20, 30:")
    lista.recorrer()
    lista.insertar(15, 1)
    print("Lista después de insertar 15 en la posición 1:")
    lista.recorrer()
    lista.insertar(100, 5)
    lista.recorrer()
    lista.suprimir(5)
    elemento=lista.recuperar(0)
    print(elemento)
    posicion = lista.buscar(30)



            



    

