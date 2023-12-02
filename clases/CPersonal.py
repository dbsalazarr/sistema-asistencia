from clases.CPersona import Persona

class Personal(Persona):

    def __init__(self, id_personal='', nombre='', apellido_paterno='', apellido_materno='', dni='', fecha_nacimiento='', correo='', telefono='', dir_foto='', codigo_barras='', usuario='', password='', fk_id_empresa='', fk_id_cargo=''):
        super().__init__(nombre, apellido_paterno, apellido_materno, dni, fecha_nacimiento, correo, telefono, dir_foto, codigo_barras)
        self._id_personal = id_personal
        self._usuario = usuario
        self._password = password
        self._fk_id_empresa = fk_id_empresa
        self._fk_id_cargo = fk_id_cargo

    @property
    def id_personal(self):
        return self._id_personal

    @id_personal.setter
    def id_personal(self, nuevo_id_personal):
        self._id_personal = nuevo_id_personal

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nueva_password):
        self._password = nueva_password

    @property
    def fk_id_empresa(self):
        return self._fk_id_empresa

    @fk_id_empresa.setter
    def fk_id_empresa(self, nuevo_fk_id_empresa):
        self._fk_id_empresa = nuevo_fk_id_empresa

    @property
    def fk_id_cargo(self):
        return self._fk_id_cargo

    @fk_id_cargo.setter
    def fk_id_cargo(self, nuevo_fk_id_cargo):
        self._fk_id_cargo = nuevo_fk_id_cargo
    
    # MÉTODOS DE CLASE
    def registrar_personal(self) : 
        self.id_personal = self._conectar.query_db(1, "select fnSiguientePersonal();")
        print(self.id_personal)


personal1 = Personal()
personal1.registrar_personal()