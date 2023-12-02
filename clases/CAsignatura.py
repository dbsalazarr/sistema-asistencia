class Asignatura:
    def __init__(self, id_asignatura='', nombre_asignatura=''):
        self._id_asignatura = id_asignatura
        self._nombre_asignatura = nombre_asignatura

    @property
    def id_asignatura(self):
        return self._id_asignatura

    @id_asignatura.setter
    def id_asignatura(self, nuevo_id_asignatura):
        self._id_asignatura = nuevo_id_asignatura

    @property
    def nombre_asignatura(self):
        return self._nombre_asignatura

    @nombre_asignatura.setter
    def nombre_asignatura(self, nuevo_nombre_asignatura):
        self._nombre_asignatura = nuevo_nombre_asignatura
