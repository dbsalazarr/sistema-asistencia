class Empresa:
    def __init__(self, id_empresa='', razon_social='', RUC='', direccion='', telefono='', ciudad=''):
        self._id_empresa = id_empresa
        self._razon_social = razon_social
        self._RUC = RUC
        self._direccion = direccion
        self._telefono = telefono
        self._ciudad = ciudad

    @property
    def id_empresa(self):
        return self._id_empresa

    @id_empresa.setter
    def id_empresa(self, nuevo_id_empresa):
        self._id_empresa = nuevo_id_empresa

    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, nueva_razon_social):
        self._razon_social = nueva_razon_social

    @property
    def RUC(self):
        return self._RUC

    @RUC.setter
    def RUC(self, nuevo_RUC):
        self._RUC = nuevo_RUC

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, nueva_ciudad):
        self._ciudad = nueva_ciudad
