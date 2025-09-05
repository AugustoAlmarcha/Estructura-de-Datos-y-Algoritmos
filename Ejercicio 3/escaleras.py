from pilaencadenada import *

def subir_escaleras(n):
    pila = Pilaencadenada()
    pila.insertar((0, []))  # peldaño actual, lista de pasos

    while not pila.vacia():
        actual, pasos = pila.suprimir()
        if actual == n:
            print(pasos)
        elif actual < n:
            pila.insertar((actual + 1, pasos + [1]))
            pila.insertar((actual + 2, pasos + [2]))

if __name__ == "__main__":
    escalera = int(input("Ingrese la cantidad de escalones: "))
    subir_escaleras(escalera)