from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class VentanaConfiguracion:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Configuracion")
        ventana_alumno.iconbitmap(self.get_icon_path("secundario.ico"))
        color = "#D3D3D3"
        self.estilo_boton = {
            "font": ("Calibri", 12),
            "width": 20,
            "height": 2,
            "border": 5,
            "relief": "ridge",
            "highlightbackground": "#d9d9d9",
            "highlightthickness": 2,
            "cursor": "hand2"
        }

        #Frame para ingrreso de inicio de PO
        fr_inicioPO = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_inicioPO.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        #Etiqueta de Inicio y fin de PO
        etiqueta_Inicio_y_FinPO = tk.Label(fr_inicioPO, text="Ingrese Inicio y Fin de ciclo de PO:", bg="gray")
        etiqueta_Inicio_y_FinPO.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Agregar el Checkbutton para habilitar/deshabilitar las fechas
        self.estado_PO = tk.BooleanVar()
        self.estado_PO.set(False)
        toggle_buttonPO = ttk.Checkbutton(fr_inicioPO, text="Habilitar Ciclo PO", variable=self.estado_PO, command=self.Ciclo_PO)
        toggle_buttonPO.grid(row=1, column=0, pady=10)

        # Agregar la etiqueta de Estado
        self.etiqueta_estadoPO = tk.Label(fr_inicioPO, text="Estado:")
        self.etiqueta_estadoPO.grid(row=1, column=2, pady=10)
        self.etiqueta_estadoPO_accion = tk.Label(fr_inicioPO, text="Terminado", fg="red")
        self.etiqueta_estadoPO_accion.grid(row=1, column=2, columnspan=2, pady=10)

        #Establecer fecha de inicio y fin de ciclo Primera Opcion
        etiqueta_InicioPO = tk.Label(fr_inicioPO, text="Fecha de Inicio:", bg=color)
        etiqueta_InicioPO.grid(row=2, column=0, sticky=tk.E, padx=5)
        self.entry_InicioPO = DateEntry(fr_inicioPO, date_pattern="dd/mm/yyyy")
        self.entry_InicioPO.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        self.entry_InicioPO.config(state="disabled")

        etiqueta_FinPO = tk.Label(fr_inicioPO, text="Fecha de Finalizacion:", bg=color)
        etiqueta_FinPO.grid(row=2, column=2, sticky=tk.E, padx=5)
        self.entry_FinPO = DateEntry(fr_inicioPO, date_pattern="dd/mm/yyyy")
        self.entry_FinPO.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)
        self.entry_FinPO.config(state="disabled")

        #Frame para inicio y fin de ORD
        fr_inicioORD = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_inicioORD.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        #Etiqueta de Inicio y fin de ORD
        etiqueta_Inicio_y_FinORD = tk.Label(fr_inicioORD, text="Ingrese Inicio y Fin de ciclo de ORD:", bg="gray")
        etiqueta_Inicio_y_FinORD.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Agregar el Checkbutton para habilitar/deshabilitar las fechas
        self.estado_ORD = tk.BooleanVar()
        self.estado_ORD.set(False)
        toggle_buttonORD = ttk.Checkbutton(fr_inicioORD, text="Habilitar Ciclo ORD",  variable=self.estado_ORD, command=self.Ciclo_ORD)
        toggle_buttonORD.grid(row=1, column=0, pady=10)

        # Agregar la etiqueta de Estado
        self.etiqueta_estadoORD = tk.Label(fr_inicioORD, text="Estado:")
        self.etiqueta_estadoORD.grid(row=1, column=2, pady=10)
        self.etiqueta_estadoORD_accion = tk.Label(fr_inicioORD, text="Terminado", fg="red")
        self.etiqueta_estadoORD_accion.grid(row=1, column=2, columnspan=2, pady=10)

        #Establecer fecha de inicio y fin de ciclo Ordinario
        etiqueta_InicioORD = tk.Label(fr_inicioORD, text="Fecha de Inicio:", bg=color)
        etiqueta_InicioORD.grid(row=2, column=0, sticky=tk.E, padx=5)
        self.entry_InicioORD = DateEntry(fr_inicioORD, date_pattern="dd/mm/yyyy")
        self.entry_InicioORD.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        self.entry_InicioORD.config(state="disabled")

        etiqueta_FinORD = tk.Label(fr_inicioORD, text="Fecha de Finalizacion:", bg=color)
        etiqueta_FinORD.grid(row=2, column=2, sticky=tk.E, padx=5)
        self.entry_FinORD = DateEntry(fr_inicioORD, date_pattern="dd/mm/yyyy")
        self.entry_FinORD.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)
        self.entry_FinORD.config(state="disabled")

        #Frame para definir horarios de entrada
        fr_hora_entrada = tk.Frame(ventana_alumno)
        fr_hora_entrada.pack(side="top", fill=tk.X)

        #Hora de entrada turno mañana
        etiq_hora_entrada = tk.Label(fr_hora_entrada, text="Horario de entrada", bg="gray")
        etiq_hora_entrada.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        #Hora de entrada turno tarde 


        #Frame para botones 
        fr_botones_config = tk.Frame(ventana_alumno)
        fr_botones_config.pack(side="bottom", fill=tk.X)

        # Boton Guardar Alumno
        boton_guardar = tk.Button(fr_botones_config, text="Guardar", **self.estilo_boton, )
        boton_guardar.pack( padx=10, pady=10, side="left")

        #Boton Cancelar
        boton_cancelar = tk.Button(fr_botones_config, text="Cancelar", bg="red", fg="white", **self.estilo_boton, command=ventana_alumno.destroy)
        boton_cancelar.pack(padx=10, pady=10, side="right")

    def Ciclo_PO(self):
        if self.estado_PO.get():
            # Habilitar las fechas si el Checkbutton está activado
            self.entry_InicioPO.config(state="normal")
            self.entry_FinPO.config(state="normal")
            self.etiqueta_estadoPO_accion.config(text="Activo", fg="green")

        elif self.estado_ORD.get():
            self.entry_InicioORD.config(state="normal")
            self.entry_FinORD.config(state="normal")
            self.etiqueta_estadoORD_accion.config(text="Activo", fg="green")

        else:
            # Deshabilitar las fechas si el Checkbutton está desactivado en PO
            self.entry_InicioPO.config(state="disabled")
            self.entry_FinPO.config(state="disabled")
            #Colores de texto
            self.etiqueta_estadoPO_accion.config(text="Terminado", fg="red")

    def Ciclo_ORD(self):
        if self.estado_ORD.get():
            # Habilitar las fechas si el Checkbutton está activado
            self.entry_InicioORD.config(state="normal")
            self.entry_FinORD.config(state="normal")
            self.etiqueta_estadoORD_accion.config(text="Activo", fg="green")

        else:
            # Deshabilitar las fechas si el Checkbutton está desactivado en ORD
            self.entry_InicioORD.config(state="disabled")
            self.entry_FinORD.config(state="disabled")
            #Colores de texto
            self.etiqueta_estadoORD_accion.config(text="Terminado", fg="red")
        
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