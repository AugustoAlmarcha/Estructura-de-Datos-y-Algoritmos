from Colasecuencial import cola
import random

class Cliente: 
    __tiempollegada:int
    __id:int

    def __init__(self,tiempo,id):
        self.__tiempollegada = tiempo
        self.__id=id

    def gettiempollegada(self):
        return self.__tiempollegada
    
    def getid(self):
        return self.__id
    
    def __str__(self):
        return (f"Cliente {self.__id}")
    

def llegadacliente(tiempo):
    if tiempo % 10 == 0:
        return True
    
def Simulacion(ColaIPV):
    tiempo=0
    tiempomaximo=300
    tiempoatencionactual=random.randint(10,20)
    aux=0
    #tiempomaximodeespera= tiempomaximo - tiempo
    atencionvacia=True
    id=0
    while tiempo <= tiempomaximo:
        if llegadacliente(tiempo) is True:
            id+=1
            clientex=Cliente(tiempo,id)
            print(f"Llega {clientex}")
            ColaIPV.insertar(clientex)
        if atencionvacia is True and not ColaIPV.vacia():
            cliente=ColaIPV.suprimir()
            print(f"{cliente} Siendo atendido")
            atencionvacia = False
        else:
            tiempoatencionactual -= 1 #Cuando recien entra el tiempo es random por eso no se disminuye apenas entra, luego del primer minuto disminuye un minuto su atencion.
            aux+=1
            if tiempoatencionactual == 0:
                print(f"Tiempo de atencion maximo alcanzado, fue de {aux} minutos")
                atencionvacia=True
                aux=0
                tiempoatencionactual=random.randint(10,20)
        tiempo +=1
    max=0
    clientessinatender=ColaIPV.suprimir()
    while clientessinatender is not None:
        tiemposinatender = tiempomaximo - clientessinatender.gettiempollegada()
        if max < tiemposinatender:
            max=tiemposinatender
        clientessinatender=ColaIPV.suprimir()
    print(f"El tiempo maximo de espera de un cliente fue de {max} minutos")


if __name__ == "__main__":
    ColaIPV = cola()
    Simulacion(ColaIPV)
