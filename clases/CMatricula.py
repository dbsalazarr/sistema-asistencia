class Matricula:
    def __init__(self, id_matricula='', fecha_matricula='', importe='', descripcion='', estado='', fk_id_alumno='', fk_id_empresa='', fk_id_personal='', fk_id_ciclo=''):
        self._id_matricula = id_matricula
        self._fecha_matricula = fecha_matricula
        self._importe = importe
        self._descripcion = descripcion
        self._estado = estado
        self._fk_id_alumno = fk_id_alumno
        self._fk_id_empresa = fk_id_empresa
        self._fk_id_personal = fk_id_personal
        self._fk_id_ciclo = fk_id_ciclo

    @property
    def id_matricula(self):
        return self._id_matricula

    @id_matricula.setter
    def id_matricula(self, nuevo_id_matricula):
        self._id_matricula = nuevo_id_matricula

    @property
    def fecha_matricula(self):
        return self._fecha_matricula

    @fecha_matricula.setter
    def fecha_matricula(self, nueva_fecha_matricula):
        self._fecha_matricula = nueva_fecha_matricula

    @property
    def importe(self):
        return self._importe

    @importe.setter
    def importe(self, nuevo_importe):
        self._importe = nuevo_importe

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @property
    def fk_id_alumno(self):
        return self._fk_id_alumno

    @fk_id_alumno.setter
    def fk_id_alumno(self, nuevo_fk_id_alumno):
        self._fk_id_alumno = nuevo_fk_id_alumno

    @property
    def fk_id_empresa(self):
        return self._fk_id_empresa

    @fk_id_empresa.setter
    def fk_id_empresa(self, nuevo_fk_id_empresa):
        self._fk_id_empresa = nuevo_fk_id_empresa

    @property
    def fk_id_personal(self):
        return self._fk_id_personal

    @fk_id_personal.setter
    def fk_id_personal(self, nuevo_fk_id_personal):
        self._fk_id_personal = nuevo_fk_id_personal

    @property
    def fk_id_ciclo(self):
        return self._fk_id_ciclo

    @fk_id_ciclo.setter
    def fk_id_ciclo(self, nuevo_fk_id_ciclo):
        self._fk_id_ciclo = nuevo_fk_id_ciclo
