class AsistenciaAlumno:
    def __init__(self, id_asistencia_alumno='', fk_id_alumno=''):
        self._id_asistencia_alumno = id_asistencia_alumno
        self._fk_id_alumno = fk_id_alumno

    @property
    def id_asistencia_alumno(self):
        return self._id_asistencia_alumno

    @id_asistencia_alumno.setter
    def id_asistencia_alumno(self, nuevo_id_asistencia_alumno):
        self._id_asistencia_alumno = nuevo_id_asistencia_alumno

    @property
    def fk_id_alumno(self):
        return self._fk_id_alumno

    @fk_id_alumno.setter
    def fk_id_alumno(self, nuevo_fk_id_alumno):
        self._fk_id_alumno = nuevo_fk_id_alumno
