import barcode
import hashlib
from CPersona import Persona
from CConexion import Conexion
from barcode.writer import ImageWriter

class Personal (Persona) :
    def __init__(self, id_personal="", nombre="", apellido_paterno="", apellido_materno="", DNI="", fecha_nacimiento="", correo="", telefono="", dir_foto="", codigo_barras="", fk_id_empresa="", fk_id_cargo="") :

        self.id_personal = id_personal
        super().__init__(nombre, apellido_paterno, apellido_materno, DNI)
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.telefono = telefono
        self.dir_foto = dir_foto
        self._codigo_barras = codigo_barras
        self._fk_id_empresa = fk_id_empresa
        self._fk_id_cargo = fk_id_cargo
        self._conectar = Conexion()
    
    def generar_carnet(self) :
        if self._DNI and self.nombre and self.apellido_paterno and self.apellido_materno :
            data_bar_code = self.nombre + self.apellido_paterno + self.apellido_materno + self._DNI
            self._codigo_barras = barcode.Code39(data_bar_code, writer=ImageWriter(), add_checksum=False)
            print("Se tiene: ",self._codigo_barras)
            self._codigo_barras.save(f'./media/code_bars/carnet_{self._DNI}.png')
            print(f"Carnet generado para {self.nombre} {self.apellido_materno} {self.apellido_materno} con DNI: {self._DNI}")
        else:
            print("No se pueden generar carnet sin DNI, nombre y apellidos")

    def encriptar_codigo_barras(self, data) :
        sha256 = hashlib.sha256()
        sha256.update(data.encode('utf-8'))
        hashed_data = sha256.hexdigest()
        
        return int(hashed_data, 16)
    
    def registrar_personal(self) :
        pass

persona_1 = Personal("PE000001", "Washintong", "Caceres", "Huaman", "78129301", "2023-11-15", "washash@gmail.com", "967124581", "HOME", "1234567890")
print(persona_1._codigo_barras)
print(persona_1._DNI)
# persona_1.generar_carnet()
print( persona_1.encriptar_codigo_barras("WashintongCaceresHuaman78129301") )