from puzzle import ColaDePrioridad as Estructura
# from puzzle import Pila as Estructura
from puzzle import Nodos
import numpy as np


class Esquema:
    def __init__(self, minheaplevels=10):
        self.numgenerados = 0
        self.numanalizados = 0
        self.numpodados = 0
        self.mhl = minheaplevels

    def RyP_una(self, n):
        self.numhijos = 0
        e = Estructura(self.mhl)
        e.agregar(n, n.h())
        while not e.esVacia():
            n = e.extraer()
            self.numanalizados += 1
            hijos = n.expandir()
            # print(*hijos, sep="\n")
            self.numgenerados += len(hijos)
            # n.eliminar()
            for i in range(len(hijos)):
                if hijos[i].esAceptable():
                    if hijos[i].esSolucion():
                        # eliminar hijos
                        # destruir la estructura
                        # devolver el i-esimo hijo
                        h = hijos[i]
                        return h
                        # endif
                    else:
                        try:
                            e.agregar(hijos[i], hijos[i].h())
                        except Exception as e:
                            print(e)
                            return hijos
                else:
                    self.numpodados += 1
                    #     del hijos[i]
                    # return n.noHaySolucion()
        return hijos

    def RyP_una_h2(self, n):
        self.numhijos = 0
        e = Estructura(self.mhl)
        e.agregar(n, n.h2())
        while not e.esVacia():
            n = e.extraer()
            self.numanalizados += 1
            hijos = n.expandir()
            # print(*hijos, sep="\n")
            self.numgenerados += len(hijos)
            # n.eliminar()
            for i in range(len(hijos)):
                if hijos[i].esAceptable():
                    if hijos[i].esSolucion():
                        # eliminar hijos
                        # destruir la estructura
                        # devolver el i-esimo hijo
                        h = hijos[i]
                        return h
                        # endif
                    else:
                        try:
                            e.agregar(hijos[i], hijos[i].h2())
                        except Exception as e:
                            print(e)
                            return hijos
                else:
                    self.numpodados += 1
                    #     del hijos[i]
                    # return n.noHaySolucion()
        return hijos


    @property
    def contadores(self):
        return {'numgenerados': self.numgenerados,
                'numanalizados': self.numanalizados,
                'numpodados': self.numpodados}

    def resetearContadores(self):
        self.numpodados, self.numanalizados, self.numgenerados = 0, 0, 0


def resolver(tabla, esquema):
    e = esquema
    e.resetearContadores()
    nt = Nodos(tabla.shape[0], tabla)
    una = e.RyP_una(nt)
    print("contadores: ", e.contadores)
    if isinstance(una, Nodos):
        print("Solucion: ", una)
        print(una.h())
        una.mostrar_postOrder()
    else:
        print("No se encontro solucion\n\n")
        print(len(una))
        print(list(x.h() for x in una))
        print(*una, sep="\n")

    e.resetearContadores()
    print("Usando distancias de manhattan")
    una = e.RyP_una_h2(nt)
    print("contadores: ", e.contadores)
    if isinstance(una, Nodos):
        print("Solucion: ", una)
        print(una.h())
        una.mostrar_postOrder()
    else:
        print("No se encontro soluciuon\n\n")
        print(len(una))
        print(list(x.h2() for x in una))
        print(*una, sep="\n")
    print("\n\n")
    e.resetearContadores()
    print("k"*10)
    una = e.RyP_una_h3(nt)
    print("contadores: ", e.contadores)
    if isinstance(una, Nodos):
        print("Solucion: ", una)
        print(una.h())
        una.mostrar_postOrder()
    else:
        print("No se encontro soluciuon\n\n")
        print(len(una))
        print(list(x.h() for x in una))
        print(list(x.h2() for x in una))
        print(*una, sep="\n")


def main():
    e = Esquema(minheaplevels=16)

    t = np.array([[1, 5, 2], [4, 3, 0], [7, 8, 6]])
    print("Nuevo tablero\n", t)
    resolver(t, e)

    t = np.array([[1, 3, 5], [7, 0, 2], [8, 4, 6]])
    print("Nuevo tablero\n", t)
    resolver(t, e)

    t = np.array([[4, 1, 5], [7, 0, 2], [8, 3, 6]])
    print("Nuevo tablero\n", t)
    resolver(t, e)

 # Un ejemplo que el libro no tuvo en cuenta
    print("# Un ejemplo que el libro no tuvo en cuenta")
    t = np.array([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    print("Nuevo array:\n", t)
    e.resetearContadores()
    resolver(t, e)
#


if __name__ == "__main__":
    main()
