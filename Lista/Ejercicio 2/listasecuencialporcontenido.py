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
    
    def insertar_ordenado(self, elemento):
        if self.__ultimo + 1 >= self.__tamaño:
            print("Error: La lista está llena.")
            return
        posicion = 0
        while posicion <= self.__ultimo and self.__lista[posicion] < elemento: # Buscar la posición correcta para mantener el orden
            posicion += 1

        i = self.__ultimo 
        while i >= posicion:                            # Desplazar los elementos a la derecha
            self.__lista[i + 1] = self.__lista[i]
            i -= 1
        
        self.__lista[posicion] = elemento  # Insertar el elemento
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
    
    def buscar(self, elemento):
        inferior = 0
        superior = self.__ultimo
        while inferior <= superior:
            mitad = (inferior + superior) // 2
            if self.__lista[mitad] == elemento:
                return mitad
            elif self.__lista[mitad] > elemento:
                superior = mitad - 1
            else:
                inferior = mitad + 1
        return None

    def recorrer(self):
        i=0
        while i<=self.__ultimo:
            print(self.__lista[i])
            i+=1


if __name__ == '__main__':
    lista = ListaSecuencial()
    print("¿La lista está vacía?", lista.vacia())
    lista.insertar_ordenado(10)
    lista.insertar_ordenado(5)
    lista.insertar_ordenado(20)
    lista.insertar_ordenado(15)
    print("Elementos en la lista después de inserciones ordenadas:")
    lista.recorrer()
    print("¿La lista está vacía?", lista.vacia())
    print("Primer elemento:", lista.primer_elemento())
    print("Último elemento:", lista.ultimo_elemento())
    pos = lista.buscar(15)
    if pos is not None:
        print(f"Elemento 15 encontrado en la posición: {pos}")
    eliminado = lista.suprimir(1)
    print(f"Elemento eliminado en la posición 1: {eliminado}")
    print("Elementos en la lista después de eliminación:")
    lista.recorrer()

    