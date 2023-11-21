import mysql.connector as mysql

class Conexion :

    # CONSTRUCTOR
    def __init__(self, host="localhost", database="bdasistencia", user="root", password="gaaaa%123456") :
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    # MÉTODOS DE CLASE
    def conectar_bd(self, host, database, user, password) :
        conexion = mysql.connect(
            host = host,
            database = database,
            user = user, 
            password = password
        )
        return conexion
    
    
    def query_db(self, query) :
        conexion = self.conectar_bd(self.host, self.database, self.user, self.password)
        try :
            cursor = conexion.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        
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

    def crud_bd(self, query) :
        conexion = self.conectar_bd(self.host, self.database, self.user, self.password)
        try :
            cursor = conexion.cursor()
            cursor.execute(query)
            conexion.commit()
            print("Se agrego el registro correctamente")
        
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