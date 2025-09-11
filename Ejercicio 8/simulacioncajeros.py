from colaencadenada import *
import random

class Cajero:
    __tiempoatencion : int
    __disponible : bool
    __cola: object

    def __init__(self, tiempoatencion, cola):
        self.__tiempoatencion = tiempoatencion
        self.__disponible = True
        self.__cola = cola

    def getTiempoAtencion(self):
        return self.__tiempoatencion
    
    def getDisponible(self):
        return self.__disponible
    
    def setDisponible(self, disponible):
        self.__disponible = disponible
    
    def getcola(self):
        return self.__cola
    
    def atender(self, minuto_actual):
        # Si hay alguien en la cola y el cajero está libre, empieza a atender
        if self.__disponible and not self.__cola.vacia():
            cliente = self.__cola.suprimir()  # ahora recibimos el cliente atendido
            cliente.settiempoqueloatienden(minuto_actual)
            espera = cliente.calculartiempoespera()
            self.__tiempo_restante = self.__tiempoatencion
            self.__disponible = False
            print(f"👉 Cajero empieza a atender a {cliente}, esperó {espera} minutos")
            return espera
        return -1  # Indica que no se atendió a nadie

    
    def tick(self):
        # Simula el paso de 1 minuto en el cajero
        if not self.__disponible:
            self.__tiempo_restante -= 1
            if self.__tiempo_restante == 0:
                self.__disponible = True
                print("✅ Cajero quedó libre")
        

    def __str__(self):
        return (f"Tiempo de Atencion: {self.__tiempoatencion}, Disponible: {self.__disponible}, Cola: {self.__cola.recorrer()}")

    
class Cliente:
    __tiempollegada:int
    __tiempoqueloatienden:int

    def __init__(self, tiempollegada, tiempoqueloatienden=0):
        self.__tiempollegada = tiempollegada
        self.__tiempoqueloatienden = tiempoqueloatienden

    def gettiempollegada(self):
        return self.__tiempollegada

    def gettiempoqueloatienden(self):
        return self.__tiempoqueloatienden
    
    def calculartiempoespera(self):
        return self.__tiempoqueloatienden - self.__tiempollegada
    
    def settiempoqueloatienden(self, tiempoqueloatienden):
        self.__tiempoqueloatienden = tiempoqueloatienden
    
    def crearcliente(self, tiempollegada, tiempoqueloatienden):
        cliente = Cliente(tiempollegada, tiempoqueloatienden)
        return cliente
    
    def __str__(self):
        return (f"Cliente {self.__tiempollegada}")


def SimulaciondeCajeros():
    cajeros = [Cajero(5,cola=ColaEncadenada()), Cajero(3,cola=ColaEncadenada()), Cajero(4,cola=ColaEncadenada())]
    max=0
    promedio=0
    promedioclientessinatender=0
    clientesatendidos=0
    clientessinatender=0
    minutos = 0 #La simulacion se realiza durante 120 minutos
    i=0
    while minutos < 120:
        print(f"Minuto {minutos}")
        if minutos % 2 == 0:  #Cada 2 minutos llega una nueva persona
            cliente = Cliente(minutos)
            colasvacias = []
            while i < len(cajeros):
                colax= cajeros[i].getcola()
                if colax.vacia():
                    print(f"La cola {i+1} esta vacia")
                    colasvacias.append(i)
                i+=1
            if colasvacias:
                elemento = random.choice(colasvacias)
                cajeros[elemento].getcola().insertar(cliente)
                print(f"Se ha insertado a {cliente} en la cola {elemento+1}")
            else:
                min=99999
                colascortas=[]
                j=0
                while j < len(cajeros):
                    cola=cajeros[j].getcola()
                    if min > cola.getcantidad():
                        min = cola.getcantidad()
                        colascortas.clear()
                        colascortas.append(j)
                    elif min == cola.getcantidad():
                        colascortas.append(j)
                    j+=1
                if colascortas:
                    elemento = random.choice(colascortas)
                    cajeros[elemento].getcola().insertar(cliente)
                    print(f"Se ha insertado un cliente en la cola {elemento+1}")
            i=0
        for cajero in cajeros:
            espera = cajero.atender(minutos)
            cajero.tick()
            if espera >= 0: 
                clientesatendidos += 1
                promedio += espera
            if espera > max:
                max = espera
        minutos +=1

    print("Estado de las colas:")
    for cajero in cajeros:
        cola=cajero.getcola()
        print(f"-------------Cola {cajeros.index(cajero)+1}--------------")
        cola.recorrer()
        cliente = cola.suprimir()
        while cliente is not None:
            clientessinatender += 1
            promedioclientessinatender += minutos - cliente.gettiempollegada()
            cliente = cola.suprimir()

    if clientessinatender > 0:
        print(f"El tiempo promedio de espera de los clientes sin atender fue de {promedioclientessinatender/clientessinatender:.2f} minutos")
    else:
        pass
    print(f"Total de clientes sin atender: {clientessinatender}")
    print(f"El tiempo maximo de espera fue de {max} minutos")
    print(f"Total de clientes atendidos: {clientesatendidos}")
    print(f"El tiempo promedio de espera fue de {promedio/clientesatendidos:.2f} minutos")


if __name__=="__main__":
    SimulaciondeCajeros()





        

        

            




