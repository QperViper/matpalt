from sys import exception
from tkinter import messagebox
import tkinter as tk
from turtle import title
from CTkMessagebox import CTkMessagebox
from PIL.Image import preinit
from customtkinter import *
from CTkListbox import *
from customtkinter import  CTkButton, CTkEntry, CTkLabel
import customtkinter as ctk
from datetime import datetime
from datetime import date

from tkcalendar import Calendar
import conexion2

# hacer que se haga un historial de lo que se gasta, gana y se pierde de las frutas
# hacerlo con sql obviamente con matematicas, quizas implemetar una funcion. 


class Interfaz(object):

    def __init__(self) -> None:
        self.ventana=ctk.CTk()
        self.datos = conexion2.Registro_de_datos()

        w = 1240 # mucho texto no es necesario todo esto, que se habra en 1240 y listo
        h = 740
        ws = self.ventana.winfo_screenwidth() 
        hs = self.ventana.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
       
        self.ventana.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # self.ventana.iconbitmap("C:\\img_MP\\p2.ico")
        # self.ventana.title("MATPALT")
        # self.ventana.config(bg="green")
        # border= ctk.CTkFrame(self.ventana, background_corner_colors=["black", "red"])
        # self.ventana.config(bd=5, relief="ridge")    
        # self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_principal)
        self.ventana.title("MATPALT")

# Frame principal simulando borde negro
        border = ctk.CTkFrame(self.ventana, corner_radius=0, fg_color="black", width=1240, height=740)
        border.place(x=0, y=0)

# Frame interior con fondo verde
        inner_frame = ctk.CTkFrame(border, corner_radius=10, fg_color="green", width=1220, height=720)
        inner_frame.place(x=10, y=10)

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_principal)


        self.count =0 #este count es usado para que no se acumule el numero cuando se busca el id en el sql

        
        #HACER COPIA PARA QUE NO SE BORRE. no se que es esto especificar más
        self.fecha_hoy = datetime.today()
        self.f_h = self.fecha_hoy.strftime("%d/%m/%y")
        
        
        self.operaciones()
        self.botones_inicio()
        self.ventana.mainloop()
    
    
    #CIERRE DE VENTANA
    def cerrar_ventana_principal(self):
        self.msg = CTkMessagebox(title="Cerrar", message="Desea salir del programa?",
                        icon="question", option_1="No", option_2="Si")
        response = self.msg.get()
        if response=="Si":
            self.ventana.destroy()     
         

        # Aquí puedes poner el código que quieras ejecutar cuando se cierra la ventana
        #  if messagebox.askokcancel("Salir", "Desea salir?"):
        #      self.ventana.destroy()
    #OPERACIONES Y BOTONES PARA EJECUTAAR TAREAS
    def botones_inicio(self):
        self.btn1 = CTkButton(self.ventana,text='Ingresar Nuevo Producto',width=180,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.ingresar_producto()).place(x=980, y=50)
        self.btn2 = CTkButton(self.ventana,text='Compra de Frutas',width=180,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.comprar_fruta()).place(x=980, y=90)
        self.btn3 = CTkButton(self.ventana,text='Vender Fruta o Frutas',width=180,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.vender_fruta()).place(x=980, y=130)
        self.btn4 = CTkButton(self.ventana,text='Ingresar Nuevo Insumo',width=180,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.ingresar_insumo()).place(x=980, y=170)
        self.btn5 = CTkButton(self.ventana,text='Registro de Cambio',width=180,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.registro_cambio()).place(x=980, y=210)
    def operaciones(self):
        self.lbl_fecha = CTkLabel(self.ventana, bg_color="green", text=f"{self.f_h} versión 0.15", text_color="black").place(x=1080, y=550)

        # self.lista1 = CTkListbox(self.ventana, height=400,width=480, fg_color="black", bg_color="green",font=("Arial", 14))
        # self.lista1.place(x=460,y=50)

    # ========================================================
    # borra los entrys, y botones
    # # ========================================================
    def borrar_widgets(self):
        widgets = [
        'btn_agregar', 'combo', 'kilos_label', 'kilos_entry',
        'precio_label', 'precio_entry', 'tipo_entry',
        'tipo2_label', 'tipo_label', 'nom_entry', 'nom_label','filtro_fecha',
        'btn_filtrar','combo','fecha1','fecha1E','fecha2','fecha2E','btn_buscarCierre',"nombre_entry",
        "nombre_label", "val_ins", "nom_ins","moneda","billete"]
        for widget_name in widgets:
            widget = getattr(self, widget_name, None)  # Get the widget, or None if it doesn't exist
            if widget is not None:  # Only destroy if the widget exists
                widget.destroy()
    def borrar_filtro(self):
        self.lista1.delete(0, tk.END)
    def eliminar(self):
        try:
            self.borrar_widgets()
            
        except:
            print("error dado pero pasado")
        try:
            self.borrar_filtro()
            
        except:
            print("error dado pero pasado")
        

    def ingresar_producto(self):
        self.eliminar()

        self.nombre_entry = CTkEntry(self.ventana,bg_color="green", text_color="white", placeholder_text="nombre producto")
        self.nombre_entry.place(x=10, y=230)
        self.ventana.bind("<Return>", lambda event: self.ingresar_producto2())
        self.btn_agregar = CTkButton(self.ventana,bg_color="green", text='Aceptar', command=self.ingresar_producto2, text_color="white")
        self.btn_agregar.place(x=10,y=270)

        self.nombre_entry.focus()




    def ingresar_producto2(self):
        
        nom=self.nombre_entry.get()
        if nom =="":
            self.msgok =  CTkMessagebox(self.ventana, title="Error", message="ingrese datos")

        else:
            try:
                self.datos.ingresar_producto(nom)
                self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")
            except:
                self.msgok =  CTkMessagebox(self.ventana, title="Error", message="error al ingresar datos")
                


    def comprar_fruta(self):
        self.eliminar()

        consultasql = self.datos.producto()
        self.mapa = {item[1]: item[0] for item in consultasql}

        self.combo = CTkComboBox(self.ventana, bg_color="green", values=list(self.mapa.keys()))
        self.combo.place(x=10, y=250)

        self.kilos_entry = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Kilos")
        self.kilos_entry.place(x=10, y=330)
        self.kilos_entry.focus()  # foco inicial aquí

        self.precio_entry = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Precio")
        self.precio_entry.place(x=10, y=410)

        self.btn_agregar = CTkButton(self.ventana, bg_color="green", text='Aceptar',
                                 command=self.comprar_fruta2, text_color="white")
        self.btn_agregar.place(x=10, y=450)

        self.kilos_entry.bind("<Return>", lambda e: self.precio_entry.focus())
        self.precio_entry.bind("<Return>", lambda e: self.comprar_fruta2())



    def comprar_fruta2(self):
        fecha = date.today().strftime("%Y-%m-%d")
        # self.fech_entry.delete(0, "end")
        # self.fech_entry.insert(0, hoy)
        kilos = self.kilos_entry.get()
        precio = self.precio_entry.get()
        nombre = self.combo.get()
        id_producto = self.mapa.get(nombre)

        
        try:
            self.datos.compra_fruta(id_producto,kilos,precio,fecha)
            print(id_producto,kilos,precio,fecha + "entró")
        except:
            print("error al ingresar compra fruta2")
            pass
        self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")

    def comprar_proteina(self):
        pass

    def comprar_proteina2(self):
        pass


    def vender_fruta(self):
        self.eliminar()
            
  
        consultasql = self.datos.producto()
        self.mapa = {item[1]: item[0] for item in consultasql} 
         # {"fruta":1, "merma":2, "proteina":3}
        self.combo = CTkComboBox(self.ventana, bg_color="green", values=list(self.mapa.keys()))
        self.combo.place(x=10, y=250)

        self.kilos_entry = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Kilos")
        self.kilos_entry.place(x=10, y=330)
        self.kilos_entry.focus()  # foco inicial aquí

        self.precio_entry = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Precio")
        self.precio_entry.place(x=10, y=410)

        self.btn_agregar = CTkButton(self.ventana, bg_color="green", text='Aceptar',
                                 command=self.vender_fruta2, text_color="white")
        self.btn_agregar.place(x=10, y=450)

        self.kilos_entry.bind("<Return>", lambda e: self.precio_entry.focus())
        self.precio_entry.bind("<Return>", lambda e: self.vender_fruta2())
       




    def vender_fruta2(self):
        print("empezando introducción de datos a db")

        fecha = date.today().strftime("%Y-%m-%d")
        # self.fech_entry.delete(0, "end")
        # self.fech_entry.insert(0, hoy)
        kilos = self.kilos_entry.get()
        precio = self.precio_entry.get()
        nombre = self.combo.get()
        id_producto = self.mapa.get(nombre)

        
        try:
            self.datos.vernder_fruta(id_producto,kilos,precio,fecha)
            print(id_producto,kilos,precio,fecha + "entró")
        except:
            print("error al ingresar compra fruta2")
            pass
        self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")
        



    def ingresar_insumo(self):
        self.eliminar()



        self.nom_ins = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Insumo")
        self.nom_ins.place(x=10, y=330)
        self.nom_ins.focus()  # foco inicial aquí

        self.val_ins = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Valor")
        self.val_ins.place(x=10, y=410)

        self.btn_agregar = CTkButton(self.ventana, bg_color="green", text='Aceptar',
                                 command=self.ingresar_insumo2, text_color="white")
        self.btn_agregar.place(x=10, y=450)

        self.nom_ins.bind("<Return>", lambda e: self.val_ins.focus())
        self.val_ins.bind("<Return>", lambda e: self.ingresar_insumo2())
        pass



    def ingresar_insumo2(self):
        print("empezando introducción de datos a db")

        fecha = date.today().strftime("%Y-%m-%d")
        # self.fech_entry.delete(0, "end")
        # self.fech_entry.insert(0, hoy)
        insumo = self.nom_ins.get()
        valor = self.val_ins.get()
        

        
        try:
            self.datos.ingresar_insumo(insumo,valor,fecha)
            print(insumo,valor,fecha + "entró")
            self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")
        except:
            print("error al ingresar insumo")
            self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos no ingresados")
            pass
    
    def registro_cambio(self):
        self.eliminar()



        self.moneda = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Moneda")
        self.moneda.place(x=50, y=130)
        self.moneda.focus()  # foco inicial aquí

        self.billete = CTkEntry(self.ventana, bg_color="green", text_color="white", placeholder_text="Billetes")
        self.billete.place(x=250, y=130)

        self.btn_agregar = CTkButton(self.ventana, bg_color="green", text='Aceptar',
                                 command=self.registro_cambio2, text_color="white")
        self.btn_agregar.place(x=50, y=170)

        self.moneda.bind("<Return>", lambda e: self.billete.focus())
        self.billete.bind("<Return>", lambda e: self.registro_cambio2())
        
        pass
    def registro_cambio2(self):
        print("mostrando información moneda billetes")

    # convertir los valores a enteros y formatear con comas
        valor_moneda = f"{int(self.moneda.get()):,}"
        valor_billete = f"{int(self.billete.get()):,}"

        self.moneda_lbl = CTkLabel(
            self.ventana,
            anchor="center",
            width=50,
            height=50,
            corner_radius=100,
            text=f"MONEDAS\n{valor_moneda}"
        )
        self.moneda_lbl.place(x=70, y=30)

        self.billete_lbl = CTkLabel(
            self.ventana,
            anchor="center",
            width=50,
            height=50,
            corner_radius=100,
            text=f"BILLETES\n{valor_billete}"
        )
        self.billete_lbl.place(x=270, y=30)
Interfaz()