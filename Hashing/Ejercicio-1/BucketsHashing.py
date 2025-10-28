#Buckets Hashing
#Solo Objeto de Datos
import numpy as np
class Bucket:
    """Representa un único cubo o entrada de la tabla, con capacidad fija 'b'."""
    __elementos: np.ndarray     # Arreglo para almacenar los 'b' registros
    __contador: int              # Contador o puntero al último elemento insertado
    __enlace_overflow: int       # Enlace/Índice al Área de Overflow. Si es -1, el cubo no tiene desborde; si es >= 0, apunta al primer cubo de overflow asociado.

    def __init__(self, capacidad_b: int):
        self.__elementos = np.empty(capacidad_b, dtype=object)
        self.__contador = 0
        self.__enlace_overflow = -1

class TablaBuckets:
    """Representa la tabla hash completa con Área Primaria y Área de Overflow."""
    __M: int # Tamaño del Área Primaria (M)
    __tabla_primaria: np.ndarray # Arreglo que contiene M objetos de tipo Bucket (Área Primaria)
    __area_overflow: np.ndarray # Arreglo que contiene los Buckets del Área de Overflow

    def __init__(self, M: int, b: int):
        self.__M = M
        self.__tabla_primaria = np.empty(M, dtype=object)
        for i in range(M):
            self.__tabla_primaria[i] = Bucket(b)
        M_overflow = int(M * 0.20) + 1
        self.__area_overflow = np.empty(M_overflow, dtype=object)
        for i in range(M_overflow):  # El área de overflow también se inicializa con Buckets
            self.__area_overflow[i] = Bucket(b)
