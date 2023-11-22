class Requisitos:
    def __init__(self, id_requisitos="", descripcion="", fecha_falta="", esta_regularizado="", fk_id_personal=""):
        self._id_requisitos = id_requisitos
        self.descripcion = descripcion
        self.fecha_falta = fecha_falta
        self.esta_regularizado = esta_regularizado
        self.fk_id_personal = fk_id_personal

    # Getter y Setter para id_requisitos (privado)
    @property
    def id_requisitos(self):
        return self._id_requisitos

    @id_requisitos.setter
    def id_requisitos(self, nuevo_id):
        self._id_requisitos = nuevo_id

    # Getter y Setter para descripcion (público)
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    # Getter y Setter para fecha_falta (público)
    @property
    def fecha_falta(self):
        return self._fecha_falta

    @fecha_falta.setter
    def fecha_falta(self, nueva_fecha):
        self._fecha_falta = nueva_fecha

    # Getter y Setter para esta_regularizado (público)
    @property
    def esta_regularizado(self):
        return self._esta_regularizado

    @esta_regularizado.setter
    def esta_regularizado(self, nuevo_estado):
        self._esta_regularizado = nuevo_estado

    # Getter y Setter para fk_id_personal (público)
    @property
    def fk_id_personal(self):
        return self._fk_id_personal

    @fk_id_personal.setter
    def fk_id_personal(self, nuevo_id_personal):
        self._fk_id_personal = nuevo_id_personal
