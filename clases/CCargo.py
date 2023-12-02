class Cargo:
    def __init__(self, id_cargo='', nombre_cargo='', nivel_acceso=''):
        self._id_cargo = id_cargo
        self._nombre_cargo = nombre_cargo
        self._nivel_acceso = nivel_acceso

    @property
    def id_cargo(self):
        return self._id_cargo

    @id_cargo.setter
    def id_cargo(self, nuevo_id_cargo):
        self._id_cargo = nuevo_id_cargo

    @property
    def nombre_cargo(self):
        return self._nombre_cargo

    @nombre_cargo.setter
    def nombre_cargo(self, nuevo_nombre_cargo):
        self._nombre_cargo = nuevo_nombre_cargo

    @property
    def nivel_acceso(self):
        return self._nivel_acceso

    @nivel_acceso.setter
    def nivel_acceso(self, nuevo_nivel_acceso):
        self._nivel_acceso = nuevo_nivel_acceso
