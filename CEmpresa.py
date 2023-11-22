class Empresa:
    def __init__(self, id_empresa, razon_social, RUC, direccion):
        self._id_empresa = id_empresa
        self.razon_social = razon_social
        self.RUC = RUC
        self.direccion = direccion

    # Getter y Setter para id_empresa (privado)
    @property
    def id_empresa(self):
        return self._id_empresa

    @id_empresa.setter
    def id_empresa(self, nuevo_id):
        self._id_empresa = nuevo_id

    # Getter y Setter para razon_social (público)
    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, nueva_razon_social):
        self._razon_social = nueva_razon_social

    # Getter y Setter para RUC (público)
    @property
    def RUC(self):
        return self._RUC

    @RUC.setter
    def RUC(self, nuevo_RUC):
        self._RUC = nuevo_RUC

    # Getter y Setter para direccion (público)
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion
    
    # MÉTODOS DE CLASE
    