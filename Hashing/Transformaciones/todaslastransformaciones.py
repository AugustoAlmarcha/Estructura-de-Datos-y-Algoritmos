class TransformacionesHashing:

    @staticmethod
    def metodo_division(clave, M):
        return clave % M #M es el tamaño del área primaria

    @staticmethod
    def metodo_extraccion(clave, M, inicio=0, longitud=None):
        """
        Método de Extracción: se extraen dígitos específicos de la clave.
        - inicio: posición inicial de los dígitos a extraer
        - longitud: cantidad de dígitos a extraer (por defecto hasta el final)
        """
        clave_str = str(clave)
        if longitud is None:
            longitud = len(str(M))  # número de dígitos suficiente para cubrir M
        subclave = clave_str[inicio:inicio+longitud]
        return int(subclave) % M

    @staticmethod
    def metodo_plegado(clave, M, tam_bloque=2):
        """
        Método de Plegado: dividir la clave en bloques de tam_bloque dígitos, sumarlos y
        aplicar módulo M.
        """
        clave_str = str(clave)
        suma = 0
        for i in range(0, len(clave_str), tam_bloque):
            bloque = clave_str[i:i+tam_bloque]
            suma += int(bloque)
        return suma % M

    @staticmethod
    def metodo_cuadrado_medio(clave, M):
        """
        Método del Cuadrado Medio: eleva la clave al cuadrado y extrae los dígitos
        centrales según el tamaño de M.
        """
        clave_cuad = str(clave ** 2)
        n = len(str(M))
        inicio = len(clave_cuad)//2 - n//2
        subclave = clave_cuad[inicio:inicio+n]
        return int(subclave) % M

    @staticmethod
    def metodo_alfanumerico(cadena, M, base=256):
        """
        Función para claves alfanuméricas.
        - base: base del sistema de codificación (ASCII = 256)
        """
        valor = 0
        i=0
        for c in cadena:
            valor += ord(c) * (base ** i)  # cada carácter ponderado por su posición
            i += 1
        return valor % M
