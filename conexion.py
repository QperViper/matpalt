import mysql.connector

class Registro_de_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='matpalt',
                                                user='root',
                                                password='1234')
            # tipo prod 
    def agregar_tipo(self,tipo,nombre):
        cur = self.conexion.cursor()
        sql = "INSERT INTO tipo_prod (tipo_producto, nombre_producto) VALUES (%s, %s)"
        data = (tipo,nombre)
        cur.execute(sql,data)
        self.conexion.commit()
        cur.close()

    def mostrar_tipo_prod(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tipo_prod"
        cur.execute(sql)
        dato = cur.fetchall()
        cur.close()
        return dato

    def id_nombre_tipo(self):
        cur = self.conexion.cursor()
        sql = "SELECT id,nombre_producto FROM tipo_prod"
        cur.execute(sql)
        nomx = cur.fetchall()
        cur.close()
        return nomx
    
    def nombre_tipo(self,id):
        cur = self.conexion.cursor()
        sql = "SELECT nombre_producto FROM tipo_prod WHERE id = {}".format(id)
        cur.execute(sql)
        id_traer = cur.fetchall()
        cur.close()
        return id_traer
    

    # producto
    def id_producto(self, f_compra):
        cur = self.conexion.cursor()
        sql = "SELECT count(id) FROM producto WHERE f_compra = %s"
        cur.execute(sql, (f_compra,))
        id_traer = cur.fetchall()
        cur.close()
        return id_traer
    
    

    # gamela
    def agregar_gamela_de_compra(self,kilos,fecha,precio,nombre_prod):
        cur = self.conexion.cursor()
        sql = "INSERT INTO producto (kilos,f_compra,precio_compra,id_prod) VALUES (%s, %s, %s, %s)"
        data = (kilos,fecha,precio,nombre_prod)
        cur.execute(sql,data)
        self.conexion.commit()
        cur.close()

    def mostrar_gamela(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM producto"
        cur.execute(sql)
        dato = cur.fetchall()
        cur.close()
        return dato
    
    def mostrar_gamela_por_fecha(self, f_compra):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM producto WHERE f_compra = %s"
        cur.execute(sql, (f_compra,))
        filtro_fecha = cur.fetchall()
        cur.close()
        filtro_fecha_formateado = [
            (id, cantidad, fecha.strftime('%Y-%m-%d'), precio, otro) for id, cantidad, fecha, precio, otro in filtro_fecha
        ]
        return filtro_fecha_formateado