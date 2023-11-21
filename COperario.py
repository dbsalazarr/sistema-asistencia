from CConexion import Conexion # Importar la clase Conexion

class Operario :
    # CONSTRUCTOR
    def __init__(self, idOperario="", nombre="", apellido_paterno="", apellido_materno="", DNI="", usuario="", password="") :
        self.idOperario = idOperario
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.DNI = DNI
        self.usuario = usuario
        self.password = password
        self.conectar = Conexion()
    
    # SETTERS AND GETTERS

    # MÉTODOS
    def registrar_operario(self):

        # CONSULTAS
        data = self.conectar.query_db("select fnSiguienteOperario()")
    
        self.idOperario = data[0][0]
        self.nombre = input("¿Cual es el nombre del operario? ")
        self.apellido_paterno = input("¿Cúal es su apellido paterno? ")
        self.apellido_materno = input("¿Cúal es su apellido materno? ")
        self.DNI = input("¿Cúal es el DNI? ")
        self.usuario = input("Define un usuario para el sistema: ")
        self.password = input("Define una contraseña para el sistema: ")

        # self.idOperario = data[0][0]
        # self.nombre = "Operator 2"
        # self.apellido_paterno = "Tob"
        # self.apellido_materno = "Otci"
        # self.DNI = "00001001"
        # self.usuario = "superAdmin2"
        # self.password = "root2"
        
        self.conectar.crud_bd(f"call spInsertarOperario('{self.idOperario}', '{self.nombre}', '{self.apellido_paterno}', '{self.apellido_materno}', '{self.DNI}', '{self.usuario}', '{self.password}');")

    def listar_operario(self) :
        resultados = self.conectar.query_db("select * from TOperario")
        for data in resultados :
            print(data)
    


admin = Operario()
admin.registrar_operario()
admin.listar_operario()