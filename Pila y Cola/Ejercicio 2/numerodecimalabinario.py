from pilasecuencial import *

def decimal_a_binario(numero_decimal):
    pila=PilaSecuencial(100)
    while numero_decimal > 0:
        resto = (numero_decimal % 2)
        numero_decimal = (numero_decimal // 2)
        pila.insertar(int(resto))

    return pila

def mostrarordenado(pila):
    numero=""
    while not pila.vacia():
        numero += str(pila.suprimir())
    print(f"El numero en binario es {numero}")
        

if __name__ == "__main__":
    numerodecimal=int(input("Ingrese el numero decimal que quiere convertir en binario"))
    pilax=decimal_a_binario(numerodecimal)
    mostrarordenado(pilax)

