class Cargo:
    def __init__(self, id_cargo, descripcion):
        self._id_cargo = id_cargo
        self.descripcion = descripcion

    # Getter y Setter para id_cargo (privado)
    @property
    def id_cargo(self):
        return self._id_cargo

    @id_cargo.setter
    def id_cargo(self, nuevo_id):
        self._id_cargo = nuevo_id

    # Getter y Setter para descripcion (público)
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

