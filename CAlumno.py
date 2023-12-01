from CPersona import Persona
class Alumno(Persona):
    def __init__(self,nombre=' ',apellido_paterno=' ',apellido_materno=' ',DNI=' ',fecha_nacimiento=' ',correo='',telefono=' ',dir_foto=' ',codigo_barras=' ',id_alumno=' ',nombre_apoderado=' ',apellido_apoderado=' ',modalidad=' ',turno_matricula=' ',fk_id_grupo=' '):
        super().__init__(nombre,apellido_paterno,apellido_materno,DNI,fecha_nacimiento,correo,telefono,dir_foto,codigo_barras)
        self._id_alumno = id_alumno
        self._nombre_apoderado = nombre_apoderado
        self._apellido_apoderado = apellido_apoderado
        self._modalidad = modalidad
        self._turno_matricula = turno_matricula
        self._fk_id_grupo = fk_id_grupo

  #Getters
    @property
    def leer_id_alumno(self):
        return self._id_alumno
    @property
    def leer_nombre_apoderado(self):
        return self._id_nombre_apoderado
    @property
    def leer_apellido_apoderado(self):
        return self._apellido_apoderado
    @property
    def leer_modalidad(self):
        return self._modalidad
    @property
    def leer_turno_matricula(self):
        return self._turno_matricula
    @property
    def leer_fk_id_grupo(self):
        return self._fk_id_grupo
  
    #Setters
    def set_id_alumno(self, nuevo_id_alumno):
        self._id_alumno = nuevo_id_alumno
    def set_nombre_apoderado(self, nuevo_nombre_apoderado):
        self._nombre_apoderado = nuevo_nombre_apoderado
    def set_apellido_apoderado(self, nuevo_apellido_apoderado):
        self._apellido_apoderado = nuevo_apellido_apoderado
    def set_modalidad(self, nueva_modalidad):
        self._modalidad = nueva_modalidad
    def set_turno_matricula(self, nuevo_turno_matricula):
        self._nuevo_turno_matricula = nuevo_turno_matricula
    def set_fk_id_grupo(self, nuevo_fk_id_grupo):
        self._fk_id_grupo = nuevo_fk_id_grupo