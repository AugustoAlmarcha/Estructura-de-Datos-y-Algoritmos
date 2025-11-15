from Nodos import Nodos
from abc import ABC, abstractmethod


class Estructura(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def agregar(self, n: Nodos, prioridad: int):
        pass

    @abstractmethod
    def extraer(self):
        pass

    @abstractmethod
    def esVacia(self):
        pass

    @abstractmethod
    def tamano(self):
        pass

    @abstractmethod
    def destruir(self):
        pass
