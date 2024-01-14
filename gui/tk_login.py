from os.path import abspath, dirname, join

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from tk_inicio import Interfaz

class App:
    def validar_datos(self):
        user = self.usuario.get()
        password = self.contraseña.get()
        if (user == "Sergio" and password == "123456"):
            self.ventana.destroy()
            Interfaz()
        else:
            messagebox.showerror(message="Contraseña o usuario no validos", title="Error")
            
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de secion")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        
        #frame de logo
        fr_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="green")
        fr_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label_logo = tk.Label(fr_logo, bg="green")
        label_logo.place(x=0, y=0, relwidth=1, relheight=1)

        #frame derecho
        fr_derecho = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_derecho.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #frame de titulo
        fr_titulo = tk.Frame(fr_derecho, bd=0, height=50, relief=tk.SOLID)
        fr_titulo.pack(side="top", fill=tk.X)
        titulo = tk.Label(fr_titulo, text="Inicio de sesion", font=("Times", 30), fg="black", bg="#fcfcfc", pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)

        #frame de datos
        fr_datos = tk.Frame(fr_derecho, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_datos.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #etiqueta usuario
        etiq_usuario = tk.Label(fr_datos, text="Usuario:", font=("Times", 14), fg="black", bg="#fcfcfc", anchor="w")
        etiq_usuario.pack(fill=tk.X, padx=20, pady=5)
        #entrada de usuario
        self.usuario = ttk.Entry(fr_datos, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        #etiqueta contraseña
        etiq_contraseña = tk.Label(fr_datos, text="Contraseña:", font=("Times", 14), fg="black", bg="#fcfcfc", anchor="w")
        etiq_contraseña.pack(fill=tk.X, padx=20, pady=5)
        #entrada de contraseña
        self.contraseña = ttk.Entry(fr_datos, font=("Times", 14))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="•")

        #boton ingresar
        boton_inicio = tk.Button(fr_datos, text="Iniciar sesion", font=("Times", 15, BOLD), fg="black", bg="#fcfcfc", command=self.validar_datos)
        boton_inicio.pack(fill=tk.X, padx=20, pady=20)


        self.ventana.mainloop()
    

    def get_icon_path(self, image_name) :
        """
            Recupera el directorio hasta la carpeta media y concatena a tal ruta el nombre de la imagen a utilizar en la interfaz
            Args : 
                image_name (str) : Es el nombre de la imagen con sus extensión
            Returns :
                (str) : Retorna la ruta de la imagen indicada (debe encontrarse en la carpeta media del proyecto)
        """
        path = join(join(dirname(dirname(abspath(__file__))), "media"), image_name)
        return path
