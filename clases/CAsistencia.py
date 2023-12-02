class Asistencia:
    def __init__(self, fecha_hora_llegada='', estado='', turno='', fk_id_personal=''):
        self._fecha_hora_llegada = fecha_hora_llegada
        self._estado = estado
        self._turno = turno
        self._fk_id_personal = fk_id_personal

    @property
    def fecha_hora_llegada(self):
        return self._fecha_hora_llegada

    @fecha_hora_llegada.setter
    def fecha_hora_llegada(self, nueva_fecha_hora_llegada):
        self._fecha_hora_llegada = nueva_fecha_hora_llegada

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, nuevo_turno):
        self._turno = nuevo_turno

    @property
    def fk_id_personal(self):
        return self._fk_id_personal

    @fk_id_personal.setter
    def fk_id_personal(self, nuevo_fk_id_personal):
        self._fk_id_personal = nuevo_fk_id_personal
