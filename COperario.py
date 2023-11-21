from CConexion import Conexion
from CPersona import Persona

class Operario( Persona ) :
    # CONSTRUCTOR
    def __init__(self, idOperario="", nombre="", apellido_paterno="", apellido_materno="", DNI="", usuario="", password="") :
        self.idOperario = idOperario
        super().__init__(nombre, apellido_paterno, apellido_materno, DNI)
        self._usuario = usuario
        self._password = password
        self._conectar = Conexion()
    
    # SETTERS AND GETTERS

    # MÉTODOS
    def registrar_operario(self):

        # CONSULTAS
        data = self._conectar.query_db(1, "select fnSiguienteOperario();")
    
        # self.idOperario = data[0][0]
        # self.nombre = input("¿Cual es el nombre del operario? ")
        # self.apellido_paterno = input("¿Cúal es su apellido paterno? ")
        # self.apellido_materno = input("¿Cúal es su apellido materno? ")
        # self.DNI = input("¿Cúal es el DNI? ")
        # self._usuario = input("Define un usuario para el sistema: ")
        # self._password = input("Define una contraseña para el sistema: ")

        self.idOperario = data[0][0]
        self.nombre = "Operator 2"
        self.apellido_paterno = "Tob"
        self.apellido_materno = "Otci"
        self._DNI = "00001001"
        self._usuario = "superAdmin2"
        self._password = "root2"
        
        # self._conectar.query_db(2, f"call spInsertarOperario('{self.idOperario}', '{self.nombre}', '{self.apellido_paterno}', '{self.apellido_materno}', '{self.DNI}', '{self._usuario}', '{self._password}');")
        print(f"call spInsertarOperario('{self.idOperario}', '{self.nombre}', '{self.apellido_paterno}', '{self.apellido_materno}', '{self._DNI}', '{self._usuario}', '{self._password}');")

    def actualizar_operario(self, idOperario) :

        self.idOperario = idOperario
        self.nombre = "Operator 3"
        self.apellido_paterno = "Obt"
        self.apellido_materno = "ToCi"
        self.DNI = "00001001"
        self._usuario = "superAdmin2"
        self._password = "root2"
        # Modificar Operario mediante su ID
        self._conectar.query_db(2, f"call spInsertarOperario('{self.idOperario}', '{self.nombre}', '{self.apellido_paterno}', '{self.apellido_materno}', '{self.DNI}', '{self._usuario}', '{self._password}');")
        


    def listar_operario(self) :
        resultados = self._conectar.query_db(1, "select * from TOperario")
        for data in resultados :
            print(data)
    

oper1 = Operario()
oper1.registrar_operario()
# oper1.actualizar_operario()
# oper1.listar_operario()