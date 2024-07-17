import customtkinter as ctk
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.ventana = ctk.CTkFrame(self.root)
        self.ventana.pack(pady=20, padx=20, fill="both", expand=True)

        # Vincular la función de cerrado
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Aquí puedes poner el código que quieras ejecutar cuando se cierra la ventana
        print("La ventana se está cerrando.")
        self.root.destroy()  # Esto cierra la ventana

root = ctk.CTk()
app = App(root)
root.mainloop()
