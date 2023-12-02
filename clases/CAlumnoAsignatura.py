class AlumnoAsignatura:
    def __init__(self, id_alumno_asignatura='', nota='', fk_id_alumno='', fk_id_asignatura='', fk_id_evaluacion=''):
        self._id_alumno_asignatura = id_alumno_asignatura
        self._nota = nota
        self._fk_id_alumno = fk_id_alumno
        self._fk_id_asignatura = fk_id_asignatura
        self._fk_id_evaluacion = fk_id_evaluacion

    @property
    def id_alumno_asignatura(self):
        return self._id_alumno_asignatura

    @id_alumno_asignatura.setter
    def id_alumno_asignatura(self, nuevo_id_alumno_asignatura):
        self._id_alumno_asignatura = nuevo_id_alumno_asignatura

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nueva_nota):
        self._nota = nueva_nota

    @property
    def fk_id_alumno(self):
        return self._fk_id_alumno

    @fk_id_alumno.setter
    def fk_id_alumno(self, nuevo_fk_id_alumno):
        self._fk_id_alumno = nuevo_fk_id_alumno

    @property
    def fk_id_asignatura(self):
        return self._fk_id_asignatura

    @fk_id_asignatura.setter
    def fk_id_asignatura(self, nuevo_fk_id_asignatura):
        self._fk_id_asignatura = nuevo_fk_id_asignatura

    @property
    def fk_id_evaluacion(self):
        return self._fk_id_evaluacion

    @fk_id_evaluacion.setter
    def fk_id_evaluacion(self, nuevo_fk_id_evaluacion):
        self._fk_id_evaluacion = nuevo_fk_id_evaluacion
