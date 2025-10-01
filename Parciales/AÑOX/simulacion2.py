from Colasecuencial import cola
import random

class Cajero:
    __disponible:bool
    __contador:int
    __funciontiempoatencion:object
    __tiemporestante:int

    def __init__(self, tiempoatencion):
        self.__disponible = True
        self.__contador = 0
        self.__funciontiempoatencion = tiempoatencion
        self.__tiemporestante = 0

    def getcontador(self):
        return self.__contador
    
    def getdisponible(self):
        return self.__disponible
    
    def getfunciontiempoatencion(self):
        return self.__funciontiempoatencion
    
    def gettiemporestante(self):
        return self.__tiemporestante
    
    def ingresalcajero(self,fila):
        if self.__disponible is True and not fila.vacia():
            print("Cajero empieza a atender")
            self.__disponible = False
            x=fila.suprimir()
            print(f"La {x} esta siendo atendida")
            self.__contador +=1
            self.__tiemporestante = self.__funciontiempoatencion()
        else:
            print("El cajero esta ocupado o no hay clientes que atender")

    def tick(self):
        if self.__disponible is False:
            self.__tiemporestante -=1
            if self.__tiemporestante == 0: 
                print("Se desocupo un cajero")
                self.__disponible = True
        else:
            print("Cajero Disponible")

def Simulacion():
    Doscajeros = [Cajero(lambda: random.randint(2,8)),Cajero(lambda: random.randint(1,5))]
    Fila = cola()
    tiempo=0
    i=0
    tiempototal=50
    while tiempo < tiempototal:
        print(f"-------------Minuto {tiempo}----------------")
        if tiempo % 2 == 0:
            i+=1
            persona = (f"Persona {i}")
            Fila.insertar(persona)
            print("Se inserto una persona en la fila")
        j=0
        while j<len(Doscajeros):
            print(f"Cajero {j+1}")
            Doscajeros[j].tick()
            Doscajeros[j].ingresalcajero(Fila)
            j+=1
        
        tiempo +=1

    k=0
    while k < len(Doscajeros):
        print(f"El cajero {k+1} atendio {Doscajeros[k].getcontador()}")
        k+=1

if __name__ == "__main__":
    Simulacion()