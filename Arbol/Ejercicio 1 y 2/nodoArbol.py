class NodoArbol:
    __dato : object
    __izquierdo : object
    __derecho : object

    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def getDato(self):
        return self.__dato
    
    def getIzquierdo(self):
        return self.__izquierdo
    
    def getDerecho(self):
        return self.__derecho
    
    def setIzquierdo(self, izquierdo):
        self.__izquierdo = izquierdo

    def setDerecho(self, derecho):
        self.__derecho = derecho

    def setDato(self, dato):
        self.__dato = dato
        