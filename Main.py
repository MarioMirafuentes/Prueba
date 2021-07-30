from json import encoder
from flask import Flask
import MySQLdb, sys
import json
from flask import request,redirect
from flask.helpers import url_for


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
          print ("Error" + e.args[0], e.args[1])
          sys.exit()


    def Selec_Estados(self):
            sql="SELECT  * FROM Estado"
     
            try:
                self.cursor.execute(sql)
                estados=self.cursor.fetchall()
                return  estados
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 

    def Selec_Municipios(self,cvestado):
            sql="SELECT  * FROM Municipio WHERE cvestado=" + str(cvestado)
            try:
                self.cursor.execute(sql)
                estados=self.cursor.fetchall()
                return  estados
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 

    def Selec_Colonias(self,cvmunipio):
            sql="SELECT  * FROM Colonia where cvmunicipio=" + str(cvmunipio)
            try:
        
                self.cursor.execute(sql)
                estados=self.cursor.fetchall()
                return  estados
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 

    def Selec_CP(self,cp):
            sql="SELECT  Colonia.CvColonia,Colonia.NombreColonia,Colonia.CodigoPostal,Municipio.CvMunicipio,Municipio.NombreMunicipio,Estado.CvEstado,Estado.NombreEstado FROM Colonia,Estado,Municipio where Colonia.CodigoPostal='"+cp+"' AND Colonia.CvMunicipio=Municipio.CvMunicipio and Municipio.CvEstado=Estado.CvEstado"
            print(sql)
            try:
                self.cursor.execute(sql)
                consulta=self.cursor.fetchall()
                return consulta
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 
    def InsertNew(self,Calle,Ne,Ni,Cvcolonia):
            sql="INSERT INTO Direccion(Calle,NumInt,NumExt,Cvcolonia) VALUES ('"+Calle+"','"+Ne+"','"+Ni+"',"+Cvcolonia+");"
            try:
                self.cursor.execute(sql)
                consulta=self.cursor.fetchall()
                return consulta
            except Exception as e:
                print ((e.args[0], e.args[1]))
                raise 

    def Table(self):
        sql="SELECT Direccion.CvDireccion,Direccion.Calle,Colonia.CodigoPostal,Colonia.NombreColonia,Municipio.NombreMunicipio,Estado.NombreEstado from Direccion,Colonia,Municipio,Estado where Direccion.CvColonia=Colonia.CvColonia and Colonia.CvMunicipio=Municipio.CvMunicipio and Municipio.CvEstado=Estado.CvEstado"            
        try:
            self.cursor.execute(sql)
            consulta=self.cursor.fetchall()
            return consulta
        except Exception as e:
            print ((e.args[0], e.args[1]))
            raise 



db=Database()


from flask import render_template
app = Flask(__name__)
@app.route('/')
def index():
   
    estados=db.Selec_Estados()
    table=db.Table() 
    return render_template('index.html',esta=estados,tab=table)


@app.route('/Municipio/<cvestado>',methods=["GET","POST"])
def municipio(cvestado):
    
    municipios=db.Selec_Municipios(cvestado)

    return json.dumps(municipios)


@app.route('/Colonias/<cvmunicipio>',methods=["GET","POST"])
def colonias(cvmunicipio):
    
    colonias=db.Selec_Colonias(cvmunicipio)

    return json.dumps(colonias)

@app.route('/Cp/<cp>',methods=["GET"])
def codigoP(cp):
    consulta=db.Selec_CP(cp)
    return json.dumps(consulta)


@app.route('/Insert',methods=["POST"])
def insert():
    print(request.form)
    


    calle = request.form["calle"]
    nume = request.form["numeroe"]
    numi = request.form["numeroi"]
    cvcolonia=request.form["colonias"]
    consulta=db.InsertNew(calle,nume,numi,cvcolonia)
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)