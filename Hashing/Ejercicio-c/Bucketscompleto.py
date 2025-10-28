#Se ejecuta escribiendo ↓ en la terminal.
#py -m Ejercicio-c.Bucketscompleto
import numpy as np
from Transformaciones.todaslastransformaciones import *

class Bucket:
    """Un cubo con capacidad fija b y posible enlace a overflow"""
    __elementos: np.ndarray
    __contador: int
    __enlace_overflow: int

    def __init__(self, capacidad_b: int):
        self.__elementos = np.empty(capacidad_b, dtype=object)
        self.__contador = 0
        self.__enlace_overflow = -1

    def esta_lleno(self):
        return self.__contador == len(self.__elementos)

    def insertar(self, clave):
        if not self.esta_lleno():
            self.__elementos[self.__contador] = clave
            self.__contador += 1
            return True
        return False

    def buscar(self, clave):
        for i in range(self.__contador):
            if self.__elementos[i] == clave:
                return self.__elementos[i]
        return None

    def mostrar(self):
        return [self.__elementos[i] for i in range(self.__contador)]

class TablaBuckets:
    """Tabla hash con área primaria y overflow"""
    __M: int
    __tabla_primaria: np.ndarray
    __area_overflow: np.ndarray

    def __init__(self, M: int, b: int):
        self.__M = M
        self.__tabla_primaria = np.empty(M, dtype=object)
        for i in range(M):
            self.__tabla_primaria[i] = Bucket(b)
        M_overflow = int(M * 0.20) + 1
        self.__area_overflow = np.empty(M_overflow, dtype=object)
        for i in range(M_overflow):
            self.__area_overflow[i] = Bucket(b)

    def insertar(self, clave):
        pos = TransformacionesHashing.metodo_division(clave, self.__M)
        bucket = self.__tabla_primaria[pos]
        # Intentamos insertar en el bucket principal
        if bucket.insertar(clave):
            return
        # Si está lleno, buscamos un bucket libre en overflow
        overflow_pos = 0
        while overflow_pos < len(self.__area_overflow) and self.__area_overflow[overflow_pos].esta_lleno():
            overflow_pos += 1
        if overflow_pos == len(self.__area_overflow):
            print("Tabla llena, no se puede insertar:", clave)
            return
        # Insertamos en el bucket de overflow
        self.__area_overflow[overflow_pos].insertar(clave)
        # Enlazamos el bucket principal si aún no tiene enlace
        if bucket._Bucket__enlace_overflow == -1:
            bucket._Bucket__enlace_overflow = overflow_pos

    def buscar(self, clave):
        pos = TransformacionesHashing.metodo_division(clave, self.__M)
        bucket = self.__tabla_primaria[pos]

        # Buscamos en el bucket principal
        if bucket.buscar(clave) is not None:
            return f"Clave {clave} encontrada en área primaria, posición {pos}"

        # Si tiene enlace a overflow, seguimos
        enlace = bucket._Bucket__enlace_overflow
        while enlace != -1:
            bucket_over = self.__area_overflow[enlace]
            if bucket_over.buscar(clave) is not None:
                return f"Clave {clave} encontrada en overflow, posición {enlace}"
            enlace = bucket_over._Bucket__enlace_overflow

        return f"Clave {clave} no encontrada"

    def mostrar(self):
        print("Área primaria:")
        for i in range(self.__M):
            print(f"Posición {i}: {self.__tabla_primaria[i].mostrar()}, enlace overflow:", self.__tabla_primaria[i]._Bucket__enlace_overflow)
        print("Área de overflow:")
        for i in range(len(self.__area_overflow)):
            print(f"Overflow {i}: {self.__area_overflow[i].mostrar()}, enlace overflow:", self.__area_overflow[i]._Bucket__enlace_overflow)


if __name__ == "__main__":
    hash = TablaBuckets(5, 2)  # 5 buckets principales, 2 elementos cada bucket
    claves = [10, 15, 20, 25, 30, 35, 40, 45]

    for c in claves:
        hash.insertar(c)

    hash.mostrar()
    print("\nBuscando claves:")
    print("Buscar 20:", hash.buscar(20))
    print("Buscar 45:", hash.buscar(45))
    print("Buscar 99:", hash.buscar(99))
