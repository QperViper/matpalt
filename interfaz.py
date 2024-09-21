from tkinter import messagebox
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from CTkListbox import *
from customtkinter import  CTkButton, CTkEntry, CTkLabel
import customtkinter as ctk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
import conexion

# hacer que se haga un historial de lo que se gasta, gana y se pierde de las frutas
# hacerlo con sql obviamente con matematicas, quizas implemetar una funcion. 


class Interfaz(object):

    def __init__(self) -> None:
        self.ventana=ctk.CTk()
        self.datos = conexion.Registro_de_datos()
    
        w = 1240 
        h = 740
        ws = self.ventana.winfo_screenwidth() 
        hs = self.ventana.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.ventana.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # self.ventana.iconbitmap("C:\\img_MP\\p2.ico")
        self.ventana.title("MATPALT")
        self.ventana.config(bg="green") 
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_principal)
        self.count =0

       
        
        #HACER COPIA PARA QUE NO SE BORRE. no se que es esto especificar más
        
        self.fecha_hoy = datetime.today()
        self.f_h = self.fecha_hoy.strftime("%d/%m/%y")
        self.product_list=[]
        self.btns = {}
        self.datos1 = []
        
        self.operaciones()
        self.botones()
        self.ventana.mainloop()
    

    def cerrar_ventana_principal(self):
        self.msg = CTkMessagebox(title="Cerrar", message="Desea salir del programa?",
                        icon="question", option_1="No", option_2="Si")
        response = self.msg.get()
    
        if response=="Si":
            self.ventana.destroy()     
         

        # Aquí puedes poner el código que quieras ejecutar cuando se cierra la ventana
        #  if messagebox.askokcancel("Salir", "Desea salir?"):
        #      self.ventana.destroy()

    def botones(self):
        self.btnprod = CTkButton(self.ventana,text='Agregar Gamela',width=120,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.agregar_nueva_fruta()).place(x=980, y=50)
        self.btnprod2 = CTkButton(self.ventana,text='Mostrar Gamela',width=120,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.mostrar_gamelas()).place(x=980, y=90)
        self.btntipo = CTkButton(self.ventana,text='Agregar Tipo',width=120,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.agregar_tipo()).place(x=1110, y=50)
        self.btntipo2 = CTkButton(self.ventana,text='Mostrar Tipo',width=120,height=30,border_width=0,corner_radius=20,bg_color='green',command=lambda:self.mostrar_tipos()).place(x=1110, y=90)
        self.cierre = CTkButton(self.ventana,text='Cierre',width=120,height=30,border_width=0,corner_radius=20,fg_color="black",bg_color='green',command=lambda:self.Cierre()).place(x=980, y=130)
    def operaciones(self):
        # self.lbl_fecha = CTkLabel(self.ventana,bg_color="green",text=f"{self.f_h} {"versión 1.10.6"}", text_color="black").place(x=1080,y=700)
        self.lbl_fecha = CTkLabel(self.ventana, bg_color="green", text=f"{self.f_h} versión 1.11.-4", text_color="black").place(x=1080, y=550)

        self.lista1 = CTkListbox(self.ventana, height=400,width=480, fg_color="black", bg_color="green",font=("Arial", 14))
        self.lista1.place(x=460,y=50)

    # ========================================================
    # borra los entrys ARREGLAR ojala hacer otro para borrar el fitro y el btn 
    # ========================================================
    def borrar_widgets(self):
        widgets = [
        'btn_agregar', 'combo', 'kilos_label', 'kilos_entry',
        'precio_label', 'precio_entry', 'tipo_entry',
        'tipo2_label', 'tipo_label', 'nom_entry', 'nom_label','filtro_fecha',
        'btn_filtrar','combo','fecha1','fecha1E','fecha2','fecha2E'

    ]
    
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
        
    # ========================================================
    # agrega tipo Arreglar 
    # ========================================================
    def agregar_tipo(self):

        self.eliminar()
        

        self.tipo_label = CTkLabel(self.ventana,bg_color="green", text="Nombre tipo", text_color="white")
        self.tipo_label.place(x=10, y=10)

        self.tipo_entry = CTkEntry(self.ventana,bg_color="green", text_color="black")
        self.tipo_entry.place(x=10, y=50)

        self.nom_label = CTkLabel(self.ventana,bg_color="green",text="Nombre Fruta", text_color="white")
        self.nom_label.place(x=10, y=90)

        self.nom_entry = CTkEntry(self.ventana,bg_color="green", text_color="black")
        self.nom_entry.place(x=10, y=130)

        self.btn_agregar = CTkButton(self.ventana,bg_color="green",command=self.agregar_nuevo_tipo ,text='Aceptar', text_color="white")
        self.btn_agregar.place(x=10, y=170) 
    # ========================================================
    # ejecuta el agregado tipo Arreglar (debe ingresar a una xlsx tambien)
    # ========================================================
    def agregar_nuevo_tipo(self):


        tipo = self.tipo_entry.get()
        nom = self.nom_entry.get()
        if tipo=="" or nom =="":
            self.msg = CTkMessagebox(self.ventana, title="Error", message="no existen datos para ingresar")
        else:
            try:
                tipo = self.tipo_entry.get()
                nom = self.nom_entry.get()
            except (Exception):

                self.msg2 = CTkMessagebox(self.ventana, title="Error", message="Los Kilos y el Precio deben ser numeros enteros")

        self.datos.agregar_tipo(tipo,nom)
        self.agregar_tipo()
        self.msgok = CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")   
    # ========================================================
    # muestra los tipos de frutas y sus nombres
    # ========================================================
    def mostrar_tipos(self):
        self.eliminar()
      
        consultasql = self.datos.mostrar_tipo_prod()
        result = [item[0] for item in consultasql]
        datos = [item[1] for item in consultasql]
        datos2 = [item[2] for item in consultasql]
        try:
            self.lista1.delete(0, tk.END)
            self.filtro_fecha.destroy()
            self.btn_filtrar.destroy()

        except:
            print("error pasado")
        for i in range(len(result)):
            # datoc= [datos[i],datos2[i]]
            self.lista1.insert(result[i], f"{datos[i]}, ({datos2[i]})")
            
            # self.lista1.insert(result[i],formatted_datoc[i])

    # ========================================================
    # agrega una nueva fruta que compra el dueño a un archivo xlsx
    # ========================================================
    def agregar_nueva_fruta(self):
        self.eliminar()
            
  
        consultasql = self.datos.id_nombre_tipo()

        result = [item[1] for item in consultasql]
        datos=result
        self.tipo2_label = CTkLabel(self.ventana,bg_color="green",text="Tipo Fruta:", text_color="white")
        self.tipo2_label.place(x=10, y=10)
        self.combo = CTkComboBox(self.ventana, bg_color="green",values=datos)
        self.combo.place(x=10, y=50)
        
        self.kilos_label = CTkLabel(self.ventana,bg_color="green",text="Kilos:", text_color="white")
        self.kilos_label.place(x=10, y=90)
        self.kilos_entry = CTkEntry(self.ventana,bg_color="green", text_color="white")
        self.kilos_entry.place(x=10, y=130)

        self.precio_label = CTkLabel(self.ventana,bg_color="green", text="Precio", text_color="white")
        self.precio_label.place(x=10, y=170)
        self.precio_entry = CTkEntry(self.ventana,bg_color="green", text_color="white")
        self.precio_entry.place(x=10, y=210)
        

        self.btn_agregar = CTkButton(self.ventana,bg_color="green", text='Aceptar', command=self.agregar_gamela_frutas, text_color="white")
        self.btn_agregar.place(x=10,y=250)
    # ========================================================
    # hace la ejecucion de agregar_nueva_fruta. Arreglar(debe ingresar estos datos tambien a sql)
    # ========================================================
    def agregar_gamela_frutas(self,):

        kilos = self.kilos_entry.get()
        precio = self.precio_entry.get()
        if kilos=="" or precio =="":
            self.msg = CTkMessagebox(self.ventana, title="Error", message="no existen datos para ingresar")
        else:
            try:
                
                comboint = self.combo.get()
                kilos = self.kilos_entry.get()
                precio = self.precio_entry.get()
                kilosint= int(kilos)
                precioint = int(precio)
                fecha_hoy = date.today()
                now = datetime.now()

            except (Exception):
                self.msg2 = CTkMessagebox(self.ventana, title="Error", message="Los Kilos y el Precio deben ser numeros enteros")
                print(kilosint,precioint)
            consultasql = self.datos.id_nombre_tipo()
            result = [item[1] for item in consultasql]
            print(comboint)
            
            for i in range(len(result[1])):
                for i in result:
                    self.count += 1
                    if self.combo.get() == i:
                        # result2= 
                        break                                                       
                else:
                    continue  
                break 
        self.datos.agregar_gamela_de_compra(kilosint, fecha_hoy, precioint,self.count)
        self.msgok =  CTkMessagebox(self.ventana, title="Exito", message="datos ingresados correctamente")
        self.agregar_nueva_fruta()
        self.count =0
        # self.historial_frutas.agregar_fruta(kilosint, fecha_hoy, precioint,1)
        # self.msg2 = CTkMessagebox(self.ventana, title="ok", message="ingresado")
    # ========================================================
    # ========================================================
    def mostrar_gamelas(self):
        consultasql = self.datos.mostrar_gamela()
        consultasql1 = self.datos.mostrar_tipo_prod()
        d = [item[0] for item in consultasql]
        d1 = [item[1] for item in consultasql]
        d2 = [item[2] for item in consultasql]
        d3 = [item[3] for item in consultasql]
        d4 = [item[4] for item in consultasql]
        try:
            self.filtro_fecha.destroy()
            self.btn_filtrar.destroy()
        except:
            print("error pasado")
            
        self.mostrar_gamelas_por_fecha()

        for i in range(0, 51):
        
            try:
                d5=int(d4[i])
                nom=self.datos.nombre_tipo(d5)
            except (Exception):
                print("error pasado")

            formatted_output = ', '.join(f"{item[0]}" for index, item in enumerate(nom))
            print(formatted_output)

            
            # datoc= [datos[i],datos2[i]]
            self.lista1.insert(d[i], f"gamela:{d[i]}, Kg:{d1[i]}, Fecha:{d2[i]}, Precio:{d3[i]}, {formatted_output}")

    def mostrar_gamelas_por_fecha(self):
        try:
            self.borrar_widgets()
            
        except:
            print("error dado pero pasado")

        self.filtro_fecha = Calendar(self.ventana)
        self.filtro_fecha.place(x=180,y=50)

        self.btn_filtrar = CTkButton(self.ventana,bg_color="green", text='Aceptar', command=self.filtro, text_color="white")
        self.btn_filtrar.place(x=180,y=250)
    
    # ========================================================
    # debe cerrar con todo lo cobrado en el mes
    # ========================================================     
    def Cierre(self):
        self.eliminar()

        self.filtro_fecha = Calendar(self.ventana)
        self.filtro_fecha.place(x=180,y=50)

        self.btn_filtrar = CTkButton(self.ventana,bg_color="green", text='Insertar', command=self.C1, text_color="white")
        self.btn_filtrar.place(x=180,y=250)

        self.btn_buscarCierre = CTkButton(self.ventana,bg_color="green", text='Buscar', command=self.C2, text_color="white")
        self.btn_buscarCierre.place(x=180,y=290)

        self.fecha1 = CTkLabel(self.ventana,bg_color="green",text="DESDE el:", text_color="white")
        self.fecha1.place(x=10, y=90)
        self.fecha1E = CTkEntry(self.ventana,bg_color="green", text_color="white")
        self.fecha1E.place(x=10, y=130)

        self.fecha2 = CTkLabel(self.ventana,bg_color="green", text="HASTA EL:", text_color="white")
        self.fecha2.place(x=10, y=170)
        self.fecha2E = CTkEntry(self.ventana,bg_color="green", text_color="white")
        self.fecha2E.place(x=10, y=210)
        pass
    
    def C1(self):
        print("entra")
        fecha_seleccionada = self.filtro_fecha.get_date()
        # Convertir la fecha a objeto datetime
        fecha_obj = datetime.strptime(fecha_seleccionada, '%m/%d/%y')
        # Formatear la fecha en 'YYYY-MM-DD'
        fecha_formateada = fecha_obj.strftime('%Y-%m-%d')
        if self.fecha1E.get()=="":
            try:
                self.fecha1E.insert(0, fecha_formateada)
                
            except:
                print("error")
        else:
            if self.fecha2E.get()=="":
                try:
                    self.fecha2E.insert(0, fecha_formateada)
                except:
                    print("error")

        consultasql = self.datos.mostrar_tipo_prod()
        result = [item[0] for item in consultasql]
        datos = [item[1] for item in consultasql]
        datos2 = [item[2] for item in consultasql]
        try:
            self.lista1.delete(0, tk.END)

        except:
            print("error pasado")
        for i in range(len(result)):
            # datoc= [datos[i],datos2[i]]
            self.lista1.insert(result[i], f"{datos2[i]}")

    def C2(self):
        seleccion = self.lista1.curselection()

        # PUEDO CAMBIAR Y PONER EL INT DE SQL y deberia por si se borra será siempre el int id 
        print(seleccion + 1)

        # Verificamos si seleccion es una tupla no vacía
        
        print(self.fecha1E.get())
        print(self.fecha2E.get())
        
        
        
        
        
            
        
    def filtro(self):
        fecha_seleccionada = self.filtro_fecha.get_date()
        # Convertir la fecha a objeto datetime
        fecha_obj = datetime.strptime(fecha_seleccionada, '%m/%d/%y')
        # Formatear la fecha en 'YYYY-MM-DD'
        fecha_formateada = fecha_obj.strftime('%Y-%m-%d')
        # print(fecha_formateada)
        consultasql = self.datos.mostrar_gamela_por_fecha(fecha_formateada)
        consultasql1 = self.datos.id_producto(fecha_formateada)
        self.lista1.delete(0, tk.END)
        count = [item[0] for item in consultasql1]
        
        s= count[0]  # toma el valor son parentesis ni corchete

        d = [item[0] for item in consultasql]
        d1 = [item[1] for item in consultasql]
        d2 = [item[2] for item in consultasql]
        d3 = [item[3] for item in consultasql]
        d4 = [item[4] for item in consultasql]
        for i in range(0, s):
            try:
                d5=int(d4[i])
                nom=self.datos.nombre_tipo(d5)
            except (Exception):
                print("error pasado")
            formatted_output = ', '.join(f"{item[0]}" for index, item in enumerate(nom))
            print(formatted_output)
            self.lista1.insert(d[i], f"gamela:{d[i]}, Kg:{d1[i]}, Fecha:{d2[i]}, Precio:{d3[i]}, {formatted_output}")   
        

Interfaz()