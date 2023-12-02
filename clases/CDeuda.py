class Deuda:
    def __init__(self, id_deuda='', saldo_pendiente='', fecha_pago='', fk_id_matricula=''):
        self._id_deuda = id_deuda
        self._saldo_pendiente = saldo_pendiente
        self._fecha_pago = fecha_pago
        self._fk_id_matricula = fk_id_matricula

    @property
    def id_deuda(self):
        return self._id_deuda

    @id_deuda.setter
    def id_deuda(self, nuevo_id_deuda):
        self._id_deuda = nuevo_id_deuda

    @property
    def saldo_pendiente(self):
        return self._saldo_pendiente

    @saldo_pendiente.setter
    def saldo_pendiente(self, nuevo_saldo_pendiente):
        self._saldo_pendiente = nuevo_saldo_pendiente

    @property
    def fecha_pago(self):
        return self._fecha_pago

    @fecha_pago.setter
    def fecha_pago(self, nueva_fecha_pago):
        self._fecha_pago = nueva_fecha_pago

    @property
    def fk_id_matricula(self):
        return self._fk_id_matricula

    @fk_id_matricula.setter
    def fk_id_matricula(self, nuevo_fk_id_matricula):
        self._fk_id_matricula = nuevo_fk_id_matricula
