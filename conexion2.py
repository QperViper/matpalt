import mysql.connector

class Registro_de_datos():
    def __init__(self):
        self.conexion2 = mysql.connector.connect(host='localhost',
                                                database='matpalt3',
                                                user='root',
                                                password='Logmatri10')
            # tipo prod 

    def producto(self):# en Qué caso ocupo esto? debo poner un limite
        cur = self.conexion2.cursor()
        sql = "SELECT * FROM producto"
        cur.execute(sql)
        dato = cur.fetchall()
        cur.close()
        return dato
    def compra_fruta(self,id_producto,kg,precio_total,fecha_compra):
        id_compra = 0
        cur = self.conexion2.cursor()
        sql = "INSERT INTO compra_fruta (id_compra,id_producto,kg,precio_total,fecha_compra) VALUES (%s, %s, %s, %s, %s)"
        data = (id_compra,id_producto,kg,precio_total,fecha_compra)
        cur.execute(sql,data)
        self.conexion2.commit()
        cur.close()

    def ingresar_producto(self,nom):
        id= 0
        cur = self.conexion2.cursor()
        sql = "INSERT INTO producto (id_producto, nombre) VALUES (%s,%s)"
        data = (id, nom)
        cur.execute(sql,data)
        self.conexion2.commit()
        cur.close()











    # def agregar_tipo(self,tipo,nombre):
    #     cur = self.conexion.cursor()
    #     sql = "INSERT INTO tipo_prod (tipo_producto, nombre_producto) VALUES (%s, %s)"
    #     data = (tipo,nombre)
    #     cur.execute(sql,data)
    #     self.conexion.commit()
    #     cur.close()

    # def mostrar_tipo_prod(self):# en Qué caso ocupo esto? debo poner un limite
    #     cur = self.conexion.cursor()
    #     sql = "SELECT * FROM tipo_prod"
    #     cur.execute(sql)
    #     dato = cur.fetchall()
    #     cur.close()
    #     return dato

