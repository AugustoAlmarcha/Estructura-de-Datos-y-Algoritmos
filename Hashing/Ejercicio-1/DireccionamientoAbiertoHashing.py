#Direccionamiento Abierto Hashing
#Solo Objeto de Datos
import numpy as np

class TablaHash:
    __tabla:np.ndarray
    __tamanio:int

    def __init__(self, tamanio:int):
        self.__tamanio = tamanio
        self.__tabla = np.empty(tamanio, dtype=object)



    