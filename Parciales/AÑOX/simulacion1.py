from Colasecuencial import cola
import random

class Cajero:
    __cantidad:int
    __disponible:bool
    __cola:object
    __tiempoatencion:object
    __tiemporestante:int

    def __init__(self,tiempoatencion, cola):
        self.__cantidad = 0 
        self.__disponible = True
        self.__cola = cola
        self.__tiempoatencion = tiempoatencion
        self.__tiemporestante = 0

    def getCantidad(self):
        return self.__cantidad
    
    def getdisponible(self):
        return self.__disponible
    
    def getcola(self):
        return self.__cola
    
    def gettiempoatencion(self):
        return self.__tiempoatencion
    
    def gettiemporestante(self):
        return self.__tiemporestante
    
    def atendercliente(self,i):
        if self.__disponible is True and not self.__cola.vacia():
            cliente=self.__cola.suprimir()
            self.__disponible = False
            print(f"{cliente} siendo atendido en el cajero numero {i+1}")
            self.__cantidad +=1
            self.__tiemporestante = self.__tiempoatencion()
        
    def pasaeltiempo(self,i):
        if self.__disponible == False:
            print(f"El cajero {i+1} esta ocupado se demorara {self.__tiemporestante} minutos")
            self.__tiemporestante -=1
            if self.__tiemporestante < 0:
                print("Se acabo el tiempo de atencion, se libera el cajero")
                self.__disponible = True

class Cliente:
    __id:int
    
    def __init__(self,id):
        self.__id = id

    def getid(self):
        return self.__id
    
    def __str__(self):
        return (f"Cliente {self.__id}")
    
def Simulacion():
    id=0
    tiemposimulacion=50
    Cajeros = [Cajero(lambda: random.randint(3,9), cola=cola()), Cajero(lambda:random.randint(2,6),cola=cola())]
    tiempoactual = 0
    while tiempoactual < tiemposimulacion:
        print(f"-----------Minuto {tiempoactual}-----------------")
        if tiempoactual % 3 == 0:
            id +=1
            clientex=Cliente(id)
            print(f"Llego {clientex}")
            
            colaslibres = []
            i=0
            while i < len(Cajeros):
                if Cajeros[i].getcola().vacia():
                    colaslibres.append(i)
                i+=1
            if colaslibres:
                print("Hay colas libres")
                elemento = random.choice(colaslibres)
                colax= Cajeros[elemento].getcola()
            else:
                elemento=random.randint(0,1)
                colax=Cajeros[elemento].getcola()
            colax.insertar(clientex)
            print(f"Se inserto el cliente en la cola {elemento+1}")
        
        i=0
        while i< len(Cajeros):
            Cajeros[i].atendercliente(i)
            Cajeros[i].pasaeltiempo(i)
            i+=1

        
        tiempoactual+=1
        
    
    j=0
    while j < len(Cajeros):
        print(f"La cantidad de personas que atendio el cajero {j+1} fue de {Cajeros[j].getCantidad()}")
        j+=1

if __name__ == "__main__":
    Simulacion()






