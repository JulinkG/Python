import mysql.connector

class candidatos:

    def abrir(self):
        conexion=mysql.connector.connect(host="127.0.0.1", 
                                              user="root", 
                                              passwd="JulinkR00t", 
                                              database="cartera1")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Cartera(nombre, contacto, perfil) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select perfil, contacto from Cartera where nombre=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre, perfil, contacto from Cartera"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()