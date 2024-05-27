import mysql.connector

class Registro_de_datos():
    def __init__(self):
        # self.conexion = mysql.connector.connect(host='cs.ilab.cl',
        #                                         database='2_BD_69',
        #                                         user='2_BD_69',
        #                                         password='nicolas.matamalal23')
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='matpalt',
                                                user='root',
                                                password='1234')
        
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
    
    def nombre_tipo(self):
        cur = self.conexion.cursor()
        sql = "SELECT nombre_producto FROM tipo_prod"
        cur.execute(sql)
        nomx = cur.fetchall()
        cur.close()
        return nomx


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

        #login
    # def buscar_user(self, nombres):
    #     cur = self.conexion.cursor()
    #     sql = "SELECT * FROM cajero WHERE rut = {}".format(nombres)
    #     cur.execute(sql)
    #     nomx = cur.fetchall()
        # cur.close()
        # return nomx
    
    # def busca_password(self, contrasena):
    #     cur = self.conexion.cursor()
    #     sql = "SELECT * FROM cajero WHERE password = {}".format(contrasena)
    #     cur.execute(sql)
    #     conx = cur.fetchall()
    #     cur.close()
    #     return conx

    #productos
    def ingresar_producto_por_kg_gamelas(self, id, preciounitario,comentario, fecha_venta, hora_venta):
        cur = self.conexion.cursor()
        sql = "INSERT INTO historial (id, preciounitario,comentario, fecha_venta, hora_venta) VALUES ( %s, %s, %s, %s, %s)"
        data = (id, preciounitario,comentario, fecha_venta, hora_venta)
        cur.execute(sql, data)
        self.conexion.commit()
        cur.close()

    def ingresar_producto_a_pagina_web(self, id, id_categoria, nombre, descripcion, imagen, precio):
        cur = self.conexion.cursor()
        sql = "INSERT INTO producto (id, id_categoria, nombre, descripcion, imagen, precio) VALUES ( %s, %s, %s, %s, %s,%s)"
        data = (id, id_categoria, nombre, descripcion, imagen, precio)
        cur.execute(sql, data)
        self.conexion.commit()
        cur.close()

    def ingresar_producto_a_boleta(self, id, id_producto,id_venta, fecha_venta, precio):
        cur = self.conexion.cursor()
        sql = "INSERT INTO boleta (id, id_producto,id_venta, fechaventa, precio) VALUES ( %s, %s, %s, %s,%s)"
        data = (id, id_producto,id_venta, fecha_venta, precio)
        cur.execute(sql, data)
        self.conexion.commit()
        cur.close()

    def obtener_todos_los_productos(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT * FROM hitorial")
        productos = cur.fetchall()  # Obtener todas las filas de la tabla
        cur.close()
        return productos
    
    def eliminar_producto_por_contador(self, contador):
        cur = self.conexion.cursor()
        sql = "DELETE FROM hitorial WHERE id = %s"
        data = (contador)
        cur.execute(sql, data)
        self.conexion.commit()
        cur.close()

    def traer_ultimo_id_producto(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT MAX(id) FROM producto")
        
        traer_id = cur.fetchall()  # Obtener todas las filas de la tabla
        cur.close()
        return traer_id

    def busca_id_categoria(self, id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM producto WHERE  id_categoria = {}".format(id)
        cur.execute(sql)
        i = cur.fetchall()
        cur.close()
        return i
    
    def obtener_todos_los_productos_de_historial_por_id(self, id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial WHERE id = %s"
        data = (id)
        cur.execute(sql, data)
        id = cur.fetchall()  
        cur.close()
        return id
    
    #filtros
    def HISTORIAL_flitrar_por_fecha_completa(self,f):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial WHERE fecha_venta = %s"
        data = (f)
        cur.execute(sql,data)
        f = cur.fetchall()
        cur.close()
        return f
    def HISTORIAL_flitrar_por_dia(self,f):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial WHERE DAY(fecha_venta) = %s"
        data = (f)
        cur.execute(sql,data)
        f = cur.fetchall()
        cur.close()
        return f
    def HISTORIAL_flitrar_por_mes(self,f):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial WHERE MONTH(fecha_venta) = %s"
        data = (f)
        cur.execute(sql,data)
        f = cur.fetchall()
        cur.close()
        return f
    def HISTORIAL_flitrar_por_año(self,f):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial WHERE YEAR(fecha_venta) = %s"
        data = (f)
        cur.execute(sql,data)
        f = cur.fetchall()
        cur.close()
        return f
    
    def HISTORIAL_flitrar_orden_de_fecha(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM hitorial ORDER BY fecha_venta DESC"
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
