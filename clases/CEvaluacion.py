class Evaluacion:
    def __init__(self, id_evaluacion='', fecha_evaluacion=''):
        self._id_evaluacion = id_evaluacion
        self._fecha_evaluacion = fecha_evaluacion

    @property
    def id_evaluacion(self):
        return self._id_evaluacion

    @id_evaluacion.setter
    def id_evaluacion(self, nuevo_id_evaluacion):
        self._id_evaluacion = nuevo_id_evaluacion

    @property
    def fecha_evaluacion(self):
        return self._fecha_evaluacion

    @fecha_evaluacion.setter
    def fecha_evaluacion(self, nueva_fecha_evaluacion):
        self._fecha_evaluacion = nueva_fecha_evaluacion
