class Ciclo:
    def __init__(self, id_ciclo='', nombre_ciclo='', fecha_inicio='', fecha_fin=''):
        self._id_ciclo = id_ciclo
        self._nombre_ciclo = nombre_ciclo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin

    @property
    def id_ciclo(self):
        return self._id_ciclo

    @id_ciclo.setter
    def id_ciclo(self, nuevo_id_ciclo):
        self._id_ciclo = nuevo_id_ciclo

    @property
    def nombre_ciclo(self):
        return self._nombre_ciclo

    @nombre_ciclo.setter
    def nombre_ciclo(self, nuevo_nombre_ciclo):
        self._nombre_ciclo = nuevo_nombre_ciclo

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self._fecha_inicio = nueva_fecha_inicio

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, nueva_fecha_fin):
        self._fecha_fin = nueva_fecha_fin
