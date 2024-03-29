from clases.CConexion import Conexion

class EscuelaProfesional:
    def __init__(self, id_escuela_profesional='', nombre_escuela='', descripcion='', fk_id_grupo=''):
        self._id_escuela_profesional = id_escuela_profesional
        self._nombre_escuela = nombre_escuela
        self._descripcion = descripcion
        self._fk_id_grupo = fk_id_grupo
        self._conectar = Conexion()

    @property
    def id_escuela_profesional(self):
        return self._id_escuela_profesional

    @id_escuela_profesional.setter
    def id_escuela_profesional(self, nuevo_id_escuela_profesional):
        self._id_escuela_profesional = nuevo_id_escuela_profesional

    @property
    def nombre_escuela(self):
        return self._nombre_escuela

    @nombre_escuela.setter
    def nombre_escuela(self, nuevo_nombre_escuela):
        self._nombre_escuela = nuevo_nombre_escuela

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    @property
    def fk_id_grupo(self):
        return self._fk_id_grupos

    @fk_id_grupo.setter
    def fk_id_grupo(self, nuevo_fk_id_grupo):
        self._fk_id_grupo = nuevo_fk_id_grupo

    # * Métodos de clase
    def listar_escuelas(self, grupo) :
        lista_escuelas = self._conectar.query_db(1, f"call spListarEscuelasGrupo('{grupo}');")
        escuelas_profesionales = []
        for escuela in lista_escuelas :
            escuelas_profesionales.append( escuela[1] )
        return escuelas_profesionales