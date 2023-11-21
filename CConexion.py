import mysql.connector as mysql

class Conexion :

    # CONSTRUCTOR
    def __init__(self, host="localhost", database="bdasistencia", user="root", password="Admin%123456") :
        self._host = host
        self._database = database
        self._user = user
        self._password = password
    
    # MÉTODOS DE CLASE
    def conectar_bd(self, host, database, user, password) :
        conexion = mysql.connect(
            host = host,
            database = database,
            user = user, 
            password = password
        )
        return conexion
    
    def query_db(self, type_query, query) :
        """
            Funcion para realizar una consulta a la base de datos que retorne un tipo de
            Args :
                type_query (int) : Opcion que permite escoger entre recuperar informacion o modificarla base de datos.
                (1) recuperar información,
                (2) consulta para modificar la base de datos

                query (str) : Consulta a ejecutar en la base de datos
            Returns :
        """
        conexion = self.conectar_bd(self._host, self._database, self._user, self._password)
        try :
            if type_query == 1 :
                cursor = conexion.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                return results
            elif type_query == 2 :
                cursor = conexion.cursor()
                cursor.execute(query)
                conexion.commit()
                print("El registro se agrego/modifico correctamente :)")
            else :
                print("Escoge una opción válida")
                return False
        
        except mysql.Error as err:
            print(f"Se tuvo problemas en: {err}")
            return False
        finally : 
            if 'conexion' in locals() and conexion.is_connected() :
                cursor.close()
                conexion.close()
                print("conexion cerrada")
            else :
                print("La conexión no se llego a realizar")

# conector = Conexion("localhost", "bdasistencia", "root", "Admin%123456")
# # conector.query_db(conector.conexion, "select * from TPersonal")

# conector1 = Conexion()
# datas = conector1.query_db("Select * from TCargo")
# for data in datas :
#     print(data)