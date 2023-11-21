import mysql.connector as mysql

class Conexion :

    # CONSTRUCTOR
    def __init__(self, host="localhost", database="bdasistencia", user="root", password="daata%123456") :
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexion = self.conectar_bd(host, database, user, password)
    
    # MÉTODOS DE CLASE
    def conectar_bd(self, host, database, user, password) :
        conexion = mysql.connect(
            host = host,
            database = database,
            user = user, 
            password = password
        )
        return conexion
    
    def query_db(self, conexion, query) :
        try :
            cursor = conexion.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        
        except mysql.Error as err:
            print(f"Se tuvo problemas en {err}")
            return False
        finally : 
            if 'conexion' in locals() and conexion.is_connected() :
                cursor.close()
                conexion.close()
                print("conexion cerrada")

# conector = Conexion("localhost", "bdasistencia", "root", "Admin%123456")
# # conector.query_db(conector.conexion, "select * from TPersonal")

# conector1 = Conexion()
# conector1.query_db(conector1.conexion, "Select * from TCargo")