#Unica Impresora
#Los trabajos a imprimir tienen como maximo 100 paginas, cantidad aleatoria de paginas.
#Los trabajos llegan en promedio cada 5 minutos 
#La impresora imprime 10 paginas por minuto
#La impresora tiene un tiempo maximo de 3 minutos para imprimir
#El trabajo que no se termina de imprimir vuelve a la cola
#Tiempo de simulacion 60 minutos

from Colasecuencial import cola
import random as rd

class Trabajo:
    __paginas:int
    __llegada:int

    def __init__(self , minutoactual):
        self.__paginas = rd.randint(1, 100)
        self.__llegada = minutoactual

    def getpaginas(self):
        return self.__paginas

    def getllegada(self):
        return self.__llegada

    def imprimir(self, cant=10):
        if self.__paginas >= cant:
            self.__paginas -= cant
            return cant
        else:
            aux = self.__paginas
            self.__paginas = 0
            return aux
    
    def terminado(self):
        return self.__paginas == 0
    
    def __str__(self):
        return f"Trabajo con {self.__paginas} páginas restantes"

def simular_impresora():
    coladeimpresion = cola()
    minutos = 0
    tiempodesimulacion = 60
    tiempotrabajo = 0  # tiempo dedicado al trabajo actual
    trabajo_actual = None
    contarpaginasimpresas = 0
    contartrabajos = 0
    tiempopromedio = 0

    while minutos < tiempodesimulacion:
        print(f"\n[minuto {minutos}]")
        if minutos % 5 == 0: # Nuevo trabajo cada 5 minutos, 0 % 5 == 0 y agrega el primer trabajo
            nuevo = Trabajo(minutos)
            coladeimpresion.insertar(nuevo)
            print(f"Llegó {nuevo}")
            contartrabajos += 1

        if trabajo_actual is None and coladeimpresion.vacia() is False: # Si no hay trabajo, toma uno de la cola
            trabajo_actual = coladeimpresion.suprimir()
            tiempotrabajo = 0
            print(f"Comienza a imprimirse {trabajo_actual}")

        if trabajo_actual:
            paginas_impresas = trabajo_actual.imprimir(10)
            contarpaginasimpresas += paginas_impresas
            tiempotrabajo += 1
            print(f"Se imprimieron {paginas_impresas} páginas -> {trabajo_actual}")

            if trabajo_actual.terminado():
                print("Trabajo finalizado")
                tiempopromedio += (minutos - trabajo_actual.getllegada())
                print("Tiempo en cola:", minutos - trabajo_actual.getllegada(), "minutos")
                trabajo_actual = None
                tiempotrabajo = 0

            elif tiempotrabajo == 3: # Tiempo maximo de impresion alcanzado, 3 minutos
                print("Tiempo agotado, el trabajo vuelve a la cola")
                coladeimpresion.insertar(trabajo_actual)
                trabajo_actual = None
                tiempotrabajo = 0
        minutos += 1
    print(f"\nSimulación finalizada. Total de páginas impresas: {contarpaginasimpresas}")
    
    cantidadsinatender = 0 
    while coladeimpresion.vacia() == False:
        coladeimpresion.suprimir()
        cantidadsinatender += 1
    print(f"Cantidad de trabajos sin atender: {cantidadsinatender}")

    if contartrabajos > 0:
        print(f"Tiempo promedio en cola: {tiempopromedio / contartrabajos:.2f} minutos")
    else:
        print("No se procesaron trabajos.")

if __name__ == "__main__":
    simular_impresora()





