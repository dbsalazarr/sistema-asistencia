from clases.CConexion import Conexion
from clases.CPersona import Persona


class Alumno (Persona) :
    def __init__(self, id_alumno='', nombre='', apellido_paterno='', apellido_materno='', dni='', fecha_nacimiento='', telefono='', dir_foto='', codigo_barras='', nombre_apoderado='', apellido_apoderado='', modalidad='', turno_matricula='', fk_id_escuela_profesional=''):
        super().__init__(nombre, apellido_paterno, apellido_materno, dni, fecha_nacimiento, telefono, dir_foto, codigo_barras)
        self._id_alumno = id_alumno
        self._nombre_apoderado = nombre_apoderado
        self._apellido_apoderado = apellido_apoderado
        self._modalidad = modalidad
        self._turno_matricula = turno_matricula
        self._fk_id_escuela_profesional = fk_id_escuela_profesional
        self._conectar = Conexion()

    @property
    def id_alumno(self):
        return self._id_alumno

    @id_alumno.setter
    def id_alumno(self, nuevo_id_alumno):
        self._id_alumno = nuevo_id_alumno

    @property
    def nombre_apoderado(self):
        return self._nombre_apoderado

    @nombre_apoderado.setter
    def nombre_apoderado(self, nuevo_nombre_apoderado):
        self._nombre_apoderado = nuevo_nombre_apoderado

    @property
    def apellido_apoderado(self):
        return self._apellido_apoderado

    @apellido_apoderado.setter
    def apellido_apoderado(self, nuevo_apellido_apoderado):
        self._apellido_apoderado = nuevo_apellido_apoderado

    @property
    def modalidad(self):
        return self._modalidad

    @modalidad.setter
    def modalidad(self, nueva_modalidad):
        self._modalidad = nueva_modalidad

    @property
    def turno_matricula(self):
        return self._turno_matricula

    @turno_matricula.setter
    def turno_matricula(self, nuevo_turno_matricula):
        self._turno_matricula = nuevo_turno_matricula

    @property
    def fk_id_escuela_profesional(self):
        return self._fk_id_escuela_profesional

    @fk_id_escuela_profesional.setter
    def fk_id_escuela_profesional(self, nuevo_fk_id_escuela_profesional):
        self._fk_id_escuela_profesional = nuevo_fk_id_escuela_profesional
    

    def registrar_alumno(self) :
        """
            Funcion para registrar un nuevo alumno en la base de datos
            Parámetros a considerar: 
            pIdAlumno, pNombre, pApellidoPaterno, pApellidoMaterno, pDNI, pFechaNacimiento, pTelefonoApoderado, pCodigoBarras, pDirFoto, pNombreApoderado, pApellidoApoderado, pModalidad, pTurnoMatricula, pFkIdEscuelaProfesional
        """
        id_alumno = self._conectar.query_db(1, "select fnSiguienteAlumno();")[0][0]
        self._conectar.query_db(2, f"call spInsertarAlumno('{id_alumno}','{self.nombre}', '{self.apellido_paterno}', '{self.apellido_materno}', '{self.DNI}', '{self.fecha_nacimiento}', '{self.telefono_apoderado}', '{self.codigo_barras}', '{self.dir_foto}', '{self.nombre_apoderado}', '{self.apellido_apoderado}', '{self.modalidad}', '{self.turno_matricula}', '{self.fk_id_escuela_profesional}');")
        
        

        

        
