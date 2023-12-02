class AsistenciaPersonal:
    def __init__(self, id_asistencia_personal='', fecha_hora_salida=''):
        self._id_asistencia_personal = id_asistencia_personal
        self._fecha_hora_salida = fecha_hora_salida

    @property
    def id_asistencia_personal(self):
        return self._id_asistencia_personal

    @id_asistencia_personal.setter
    def id_asistencia_personal(self, nuevo_id_asistencia_personal):
        self._id_asistencia_personal = nuevo_id_asistencia_personal

    @property
    def fecha_hora_salida(self):
        return self._fecha_hora_salida

    @fecha_hora_salida.setter
    def fecha_hora_salida(self, nueva_fecha_hora_salida):
        self._fecha_hora_salida = nueva_fecha_hora_salida
