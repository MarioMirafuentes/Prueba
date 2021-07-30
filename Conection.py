
import MySQLdb, sys

class Database:
    def __init__(self):
        try:
            self.connection = MySQLdb.connect(
            host='SG-Prueba-4721-mysql-master.servers.mongodirector.com',
                user='Prueba123.',
                password='Prueba123.',
                db='Prueba'
             )
            print("CONEXION ESTABLECIDA")
            self.cursor = self.connection.cursor()
        except MySQLdb.Error as e:
          print ("Error %d: %s" % (e.args[0], e.args[1]))
          sys.exit()


    def Selec_Estados(self):
            sql="SELECT json_object * FROM Estado"
            try:
                self.cursor.execute(sql)
                estados=self.cursor.fetchall()
                return  estados
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 


db=Database()
db.Selec_Estados()
    


