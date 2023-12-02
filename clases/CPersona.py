import barcode 
from barcode.writer import ImageWriter
from clases.CConexion import Conexion


class Persona:
    def __init__(self, nombre='', apellido_paterno='', apellido_materno='', dni='', fecha_nacimiento='', correo='', telefono='', dir_foto='', codigo_barras=''):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._correo = correo
        self._telefono = telefono
        self._dir_foto = dir_foto
        self._codigo_barras = codigo_barras
        self._conectar = Conexion()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, nuevo_apellido_paterno):
        self._apellido_paterno = nuevo_apellido_paterno

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self, nuevo_apellido_materno):
        self._apellido_materno = nuevo_apellido_materno

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni):
        self._dni = nuevo_dni

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha_nacimiento):
        self._fecha_nacimiento = nueva_fecha_nacimiento

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    @property
    def dir_foto(self):
        return self._dir_foto

    @dir_foto.setter
    def dir_foto(self, nueva_dir_foto):
        self._dir_foto = nueva_dir_foto

    @property
    def codigo_barras(self):
        return self._codigo_barras

    @codigo_barras.setter
    def codigo_barras(self, nuevo_codigo_barras):
        self._codigo_barras = nuevo_codigo_barras

    # MËTODOS DE CLASE 
    def generar_carnet(self) :
        if self._DNI and self.nombre and self.apellido_paterno and self.apellido_materno :
            self._codigo_barras = barcode.Code39(self._DNI, writer=ImageWriter(), add_checksum=False)
            print("Se tiene: ",self._codigo_barras)
            self._codigo_barras.save(f'./media/code_bars/carnet_{self._DNI}.png')
            print(f"Carnet generado para {self.nombre} {self.apellido_materno} {self.apellido_materno} con DNI: {self._DNI}")
        else:
            print("No se pueden generar carnet sin DNI, nombre y apellidos")
