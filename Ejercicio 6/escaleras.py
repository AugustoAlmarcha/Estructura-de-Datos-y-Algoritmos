from Colasecuencial import *

def subir_escaleras(n):
    colax = cola()
    colax.insertar((0, []))  # peldaño actual, lista de pasos

    while not colax.vacia():
        actual, pasos = colax.suprimir()
        if actual == n:
            print(pasos)
        elif actual < n:
            colax.insertar((actual + 1, pasos + [1]))
            colax.insertar((actual + 2, pasos + [2]))

if __name__ == "__main__":
    escalera = int(input("Ingrese la cantidad de escalones: "))
    subir_escaleras(escalera)