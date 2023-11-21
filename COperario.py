from CConexion import Conexion # Importar la clase Conexion

class Operario :
    # CONSTRUCTOR
    def __init__(self, idOperario, nombre, apellido_paterno, apellido_materno, DNI, usuario, password) :
        self.idOperario = idOperario
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.DNI = DNI
        self.usuario = usuario
        self.password = password
    
    # SETTERS AND GETTERS

    # MÉTODOS
    def registrar_operario(self):
        conectar = Conexion()
        self.idOperario = 123
        data = conectar.query_db(conectar.conexion, "select fnSiguienteOperario()")
        print(data[0][0])


admin = Operario("", "", "", "", "", "", "")
admin.registrar_operario()