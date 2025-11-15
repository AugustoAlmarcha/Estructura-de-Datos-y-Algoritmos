from abc import ABC, abstractmethod


class Nodos(ABC):
    def __init__(self,):
        pass

    # @abstractmethod
    # def nodoInicial():
    #     pass
    #
    @abstractmethod
    def expandir(self):
        pass

    @abstractmethod
    def esAceptable(self):
        pass

    @abstractmethod
    def esSolucion(self):
        pass

    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def ponerCota(self):
        pass

    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

    @abstractmethod
    def noHaySolucion(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass
