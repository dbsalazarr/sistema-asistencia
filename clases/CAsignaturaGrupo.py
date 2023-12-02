class AsignaturaGrupo:
    def __init__(self, id_asignatura_grupo='', fk_id_grupo='', fk_id_asignatura=''):
        self._id_asignatura_grupo = id_asignatura_grupo
        self._fk_id_grupo = fk_id_grupo
        self._fk_id_asignatura = fk_id_asignatura

    @property
    def id_asignatura_grupo(self):
        return self._id_asignatura_grupo

    @id_asignatura_grupo.setter
    def id_asignatura_grupo(self, nuevo_id_asignatura_grupo):
        self._id_asignatura_grupo = nuevo_id_asignatura_grupo

    @property
    def fk_id_grupo(self):
        return self._fk_id_grupo

    @fk_id_grupo.setter
    def fk_id_grupo(self, nuevo_fk_id_grupo):
        self._fk_id_grupo = nuevo_fk_id_grupo

    @property
    def fk_id_asignatura(self):
        return self._fk_id_asignatura

    @fk_id_asignatura.setter
    def fk_id_asignatura(self, nuevo_fk_id_asignatura):
        self._fk_id_asignatura = nuevo_fk_id_asignatura
