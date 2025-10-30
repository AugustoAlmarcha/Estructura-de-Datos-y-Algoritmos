class Nodo:
    __dato:object
    __peso: float
    __siguiente = object
    
    def __init__(self, dato, peso=1.0):
        self.__dato = dato
        self.__peso = peso
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
    
    def setDato(self,dato):
        self.__dato = dato

    def getPeso(self):
        return self.__peso
    
    def setPeso(self,peso):
        self.__peso = peso