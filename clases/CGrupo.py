class Grupo:
    def __init__(self, id_grupo='', nombre_grupo=''):
        self._id_grupo = id_grupo
        self._nombre_grupo = nombre_grupo

    @property
    def id_grupo(self):
        return self._id_grupo

    @id_grupo.setter
    def id_grupo(self, nuevo_id_grupo):
        self._id_grupo = nuevo_id_grupo

    @property
    def nombre_grupo(self):
        return self._nombre_grupo

    @nombre_grupo.setter
    def nombre_grupo(self, nuevo_nombre_grupo):
        self._nombre_grupo = nuevo_nombre_grupo
