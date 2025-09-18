import numpy as np
from clasenodo import Nodo

class ListaconCursor:
    __arreglo: np.ndarray
    __cabeza: int
    __disponible: int
    __cantidad: int
    __tamanio: int

    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__arreglo = np.empty(tamanio, dtype=Nodo)
        self.__cabeza = -1
        self.__cantidad = 0
        self.__disponible = 0
        
        # Inicializa el arreglo y enlaza los nodos para la lista de espacios libres
        for i in range(tamanio - 1):
            self.__arreglo[i] = Nodo()
            self.__arreglo[i].setSiguiente(i + 1)
        self.__arreglo[tamanio - 1] = Nodo()
        self.__arreglo[tamanio - 1].setSiguiente(-1)

    # --- Métodos de gestión de la lista de espacios libres ---
    
    def obtener_nodo_disponible(self):
        if self.__disponible == -1:
            return -1 # No hay espacio disponible
        
        indice = self.__disponible
        self.__disponible = self.__arreglo[indice].getSiguiente()
        self.__arreglo[indice].setSiguiente(-1) # Opcional: desconectar para evitar confusiones
        return indice

    def devolver_nodo_disponible(self, indice):
        self.__arreglo[indice].setSiguiente(self.__disponible)
        self.__disponible = indice

    # --- Métodos para la lista principal ---

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.__cantidad:
            print("Error: Posición de inserción fuera de rango.")
            return

        nuevo_nodo_indice = self.obtener_nodo_disponible()
        if nuevo_nodo_indice == -1:
            print("Error: No hay espacio para insertar.")
            return

        self.__arreglo[nuevo_nodo_indice].setDato(dato)
        self.__cantidad += 1

        if posicion == 0:
            # Insertar al inicio
            self.__arreglo[nuevo_nodo_indice].setSiguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo_indice
        else:
            # Insertar en una posición intermedia
            puntero_anterior = self.__cabeza
            for _ in range(posicion - 1):
                puntero_anterior = self.__arreglo[puntero_anterior].getSiguiente()
            
            self.__arreglo[nuevo_nodo_indice].setSiguiente(self.__arreglo[puntero_anterior].getSiguiente())
            self.__arreglo[puntero_anterior].setSiguiente(nuevo_nodo_indice)
    
    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.__cantidad:
            print("Error: Posición de eliminación fuera de rango.")
            return -1

        dato_eliminado = None
        if posicion == 0:
            # Eliminar al inicio
            indice_eliminado = self.__cabeza
            dato_eliminado = self.__arreglo[indice_eliminado].getDato()
            self.__cabeza = self.__arreglo[indice_eliminado].getSiguiente()
        else:
            # Eliminar en una posición intermedia
            puntero_anterior = self.__cabeza
            for _ in range(posicion - 1):
                puntero_anterior = self.__arreglo[puntero_anterior].getSiguiente()
            
            indice_eliminado = self.__arreglo[puntero_anterior].getSiguiente()
            dato_eliminado = self.__arreglo[indice_eliminado].getDato()
            self.__arreglo[puntero_anterior].setSiguiente(self.__arreglo[indice_eliminado].getSiguiente())

        self.devolver_nodo_disponible(indice_eliminado)
        self.__cantidad -= 1
        return dato_eliminado

    def recorrer(self):
        print("Contenido de la lista:")
        puntero = self.__cabeza
        while puntero != -1:
            print(f"[{puntero}] -> {self.__arreglo[puntero].getDato()}")
            puntero = self.__arreglo[puntero].getSiguiente()
        print("Fin de la lista.")

    def __str__(self):
        s = "--- Estado de la Lista con Cursor ---\n"
        s += f"Cantidad de elementos: {self.__cantidad}\n"
        s += f"Cursor de la Cabeza: {self.__cabeza}\n"
        s += f"Cursor de Disponible: {self.__disponible}\n"
        s += "Arreglo de Nodos:\n"
        for i in range(self.__tamanio):
            dato_str = str(self.__arreglo[i].getDato())
            sig_str = str(self.__arreglo[i].getSiguiente())
            s += f"  [{i}]: Dato={dato_str:<5}, Siguiente={sig_str:<3}\n"
        s += "--------------------------------------\n"
        return s

# --- Ejemplo de uso ---
if __name__ == '__main__':
    lista = ListaconCursor(10)
    print("Estado inicial de la lista:")
    print(lista)
    
    print("Llenando la lista con 10 elementos...")
    for i in range(10):
        lista.insertar(f"Dato {i}", 0)
    
    print("Estado de la lista después de llenar:")
    print(lista)
    
    lista.recorrer()
    
    print("Intentando insertar un elemento más en una lista llena...")
    lista.insertar("Extra", 0)

