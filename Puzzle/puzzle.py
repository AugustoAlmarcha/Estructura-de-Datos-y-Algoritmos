import numpy as np
from Nodos import Nodos as abc_Nodos
from Estruc import Estructura as abc_Estruc


class Nodos(abc_Nodos):

    def __init__(self, dimension, tablero, sig=None):
        self.__tablero = tablero
        self.__dim = dimension
        self.__sig = sig
        self._h = None
        self._h2 = None

    @property
    def sig(self):
        return self.__sig

    def expandir(self):
        i, j = self.buscaHueco()
        nhijos = 0
        listaHijos = []
        if i < (self.__dim-1):
            # copiar(n,p)
            t = self.__tablero.copy()
            # mueve el aujero hacia abajo (i+1)
            t[i][j] = t[i+1][j]
            t[i+1][j] = 0
            # agregar el tablero a un array de hijos
            nt = Nodos(self.__dim, t, sig=self)
            listaHijos.append(nt)
        if j < (self.__dim-1):
            t = self.__tablero.copy()
            # mueve el aujero a la derecha(j+1)
            t[i][j] = t[i][j+1]
            t[i][j+1] = 0
            # agregar el tablero a un array de hijos
            nt = Nodos(self.__dim, t, sig=self)
            # agregar el tablero a un array de hijos
            listaHijos.append(nt)
        if (i-1) >= 0:
            t = self.__tablero.copy()
            # mueve el aujero hacia arriba(i-1)
            t[i][j] = t[i-1][j]
            t[i-1][j] = 0
            # agregar el tablero a un array de hijos
            nt = Nodos(self.__dim, t, sig=self)
            # agregar el tablero a un array de hijos
            listaHijos.append(nt)
        if (j-1) >= 0:
            nhijos += 1
            t = self.__tablero.copy()
            # mueve el aujero hacia la izquierda(j-1)
            t[i][j] = t[i][j-1]
            t[i][j-1] = 0
            # agregar el tablero a un array de hijos
            nt = Nodos(self.__dim, t, sig=self)
            # agregar el tablero a un array de hijos
            listaHijos.append(nt)

        return listaHijos

    def buscaHueco(self):
        i = 0
        j = 0
        while self.__tablero[i][j] != 0 and i < len(self.__tablero):
            if j >= (len(self.__tablero[i])-1):
                j = 0
                i += 1
            else:
                j += 1
        return (i, j)

    def esAceptable(self):
        aux = self.__sig
        while aux is not None and (aux.__tablero != self.__tablero).any():
            aux = aux.__sig
        return aux is None

    def __eq__(self, o):
        return (self.__tablero == o.__tablero).all()

    def fueraDeLugar(self, i, j):
        esta = self.__tablero[i][j]
        corresp = 0 if i == (self.__dim-1) and j == (self.__dim - 1)\
            else ((j+i*self.__dim)) + 1
        return esta != corresp

    def h(self):
        if self._h is None:
            self._h = sum(sum(1 for j in range(len(self.__tablero[i]))
                          if self.fueraDeLugar(i, j))
                          for i in range(len(self.__tablero)))
        return self._h

    def h2(self):
        """Suma distancias manhattan"""
        if self._h2 is None:
            self._h2 = 0
            for i in range(0, self.__dim):
                for j in range(0, self.__dim):
                    if self.__tablero[i][j] == 0:
                        x = self.__dim-1
                        y = self.__dim-1
                    else:
                        x, y = divmod((self.__tablero[i][j]-1), self.__dim)
                    self._h2 += abs(i-x)+abs(j-y)
        return self._h2

    def esSolucion(self):
        return self.h() == 0

    def ponerCota(self, cota):
        pass

    def valor(self):
        pass

    def eliminar(self):
        pass

    def noHaySolucion(self):
        return None

    def imprimir(self):
        print(self.__tablero)

    def __str__(self):
        return f'{self.__tablero}'

    def mostrar_postOrder(self):
        if self.sig is not None:
            self.sig.mostrar_postOrder()
        print(self)


class ColaDePrioridad(abc_Estruc):
    # la estrategia es LC, es decir hay que hacer un monticulo de valor maximo
    def __init__(self, niveles):
        self.__cap = (2**niveles)
        self.__tam = 0
        self.arr = np.empty(self.__cap, dtype=Nodos)

    def agregar(self, objeto, prioridad):
        if self.__tam < self.__cap:
            try:
                self.arr[self.__tam] = [prioridad, objeto]
            except IndexError as e:
                print(self.__tam, self.__cap, self.arr.shape())
                raise e

            self._burbujear()
            self.__tam += 1
        else:
            raise Exception("Cola de prioridad llena")

    def _hijos(self, i):
        return (2*i+1, 2*i+2)

    def _padre(self, i):
        return (i - 1)//2

    def _burbujear(self):
        i = self.__tam
        hijo = self.arr[i]
        padre = self.arr[self._padre(i)]
        while i > 0 and hijo[0] < padre[0]:
            # swap
            self.arr[i], self.arr[self._padre(i)] = padre, hijo
            i = self._padre(i)
            hijo = self.arr[i]
            padre = self.arr[self._padre(i)]

    def extraer(self):
        max_val = self.arr[0]
        # vamos al ultimo elemento
        self.__tam -= 1
        self.arr[0] = self.arr[self.__tam]
        self.arr[self.__tam] = None
        self._hundir()
        return max_val[1]

    def _hundir(self):
        index = 0
        lc, rc = self._hijos(index)
        smallest = index
        if lc < self.__tam and self.arr[lc][0] < self.arr[smallest][0]:
            index = lc
        if rc < self.__tam and self.arr[rc][0] < self.arr[smallest][0]:
            index = rc
        while smallest != index and smallest < self.__tam:
            # intercambio padre-hijo
            self.arr[index], self.arr[smallest] = (
                self.arr[smallest], self.arr[index])
            lc, rc = self._hijos(index)
            smallest = index
            if lc < self.__tam and self.arr[lc][0] < self.arr[smallest][0]:
                index = lc
            if rc < self.__tam and self.arr[rc][0] < self.arr[smallest][0]:
                index = rc

    def esVacia(self):
        return self.__tam == 0

    def tamano(self):
        return self.__tam

    def destruir(self):
        pass
