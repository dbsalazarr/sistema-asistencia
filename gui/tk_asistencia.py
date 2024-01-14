from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class VentanaAsistencia:
    def __init__(self, ventana_principal):
        
        self.ventana_principal = ventana_principal
        self.ventana_asistencia = tk.Toplevel(self.ventana_principal.ventana)
        self.ventana_asistencia.title("Asistencia")
        self.ventana_asistencia.iconbitmap(self.get_icon_path("secundario.ico"))
        # Estilo general para los botones
        self.estilo_boton = {
            "font": ("Calibri", 11),
            "width": 25,
            "height": 1,
            "border": 5,
            "relief": "ridge",
            "highlightbackground": "#d9d9d9",
            "highlightthickness": 2,
            "cursor": "hand2"
        }
#-------------------------------------------------------------------------------------------------------------------------------------------
        #Frame para los botones
        fr_botones_y_busqueda = tk.Frame(self.ventana_asistencia, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_botones_y_busqueda.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        # Etiqueta
        etiqueta_codigo = tk.Label(fr_botones_y_busqueda, text="Código:", font= ("Calibri", 11))
        etiqueta_codigo.grid(row=0, column=0, pady=5, padx=10, sticky="e")
        entry_codigo = tk.Entry(fr_botones_y_busqueda)
        entry_codigo.config(width=18, font= ("Calibri", 11))
        entry_codigo.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

        # Botones
        boton_registrar_asistencia = tk.Button(fr_botones_y_busqueda, text="Registrar Asistencia", **self.estilo_boton, command=self.registrar_asistencia)
        boton_registrar_asistencia.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_modificar_asistencia = tk.Button(fr_botones_y_busqueda, text="Modificar Asistencia", **self.estilo_boton, command=self.modificar_asistencia)
        boton_modificar_asistencia.grid(row=2, column=0, columnspan=2,pady=5, padx=10)

        boton_eliminar_asistencia = tk.Button(fr_botones_y_busqueda, text="Eliminar Asistencia", **self.estilo_boton, command=self.confirmar_eliminar_asistencia)
        boton_eliminar_asistencia.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        # Botón para salir
        boton_salir = tk.Button(fr_botones_y_busqueda, text="Salir", **self.estilo_boton, command=self.ventana_asistencia.destroy)
        boton_salir.grid(row=4, column=0, columnspan=2, pady=5, padx=10)
#-------------------------------------------------------------------------------------------------------------------------------------------
        #Frame para boton buscar y tabla
        fr_bot_tab = tk.Frame(self.ventana_asistencia, bd=0, relief=tk.SOLID, bg="black")
        fr_bot_tab.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #Frame para boton buscar 
        fr_bot_buscar = tk.Frame(fr_bot_tab, bd=0, relief=tk.SOLID, bg="black")
        fr_bot_buscar.pack(side="top", expand=tk.NO, fill=tk.X)

        #Boton buscar estudiante
        boton_buscar_estudiante = tk.Button(fr_bot_buscar, text="Buscar", width=10)
        boton_buscar_estudiante.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)
        entry_buscar = tk.Entry(fr_bot_buscar, width=50)
        entry_buscar.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)

        #Frame para la tabla
        fr_tab_asistencia = tk.Frame(fr_bot_tab, bd=0, relief=tk.SOLID, bg="black")
        fr_tab_asistencia.pack(side="top", expand=tk.YES, fill=tk.BOTH)
        
        # Tabla
        self.tabla_asistencia = ttk.Treeview(fr_tab_asistencia, columns=("Codigo", "Nombre", "Estado", "Turno", "Hora"))
        self.tabla_asistencia.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        # Configuración de expansión de filas y columnas
        fr_tab_asistencia.columnconfigure(0, weight=1)  # Configura la columna 0 para expandirse
        fr_tab_asistencia.rowconfigure(0, weight=1)     # Configura la fila 0 para expandirse

        #columnas de la tabla
        self.tabla_asistencia.column("#0", width=0, stretch="no")
        self.tabla_asistencia.column("Codigo", anchor="center", width=100)
        self.tabla_asistencia.column("Nombre", anchor="center", width=360)
        self.tabla_asistencia.column("Estado", anchor="center", width=90)
        self.tabla_asistencia.column("Turno", anchor="center", width=90)
        self.tabla_asistencia.column("Hora", anchor="center", width=120)
        #Encabezado de las columnas
        self.tabla_asistencia.heading("#0")
        self.tabla_asistencia.heading("Codigo", text="Codigo")
        self.tabla_asistencia.heading("Nombre", text="Nombre")
        self.tabla_asistencia.heading("Estado", text="Estado")
        self.tabla_asistencia.heading("Turno", text="Turno")
        self.tabla_asistencia.heading("Hora", text="Hora")

    def insertar_fila_asistencia(self):
        self.tabla_asistencia.insert(parent="", index="end", iid=1, text="1", values=("Juan Jesus Ramirez Pimpinela", "ABC123", "10:00 AM"))

    def registrar_asistencia(self):
        print("Registrar Asistencia")

    def modificar_asistencia(self):
        print("Modificar Asistencia")

    def confirmar_eliminar_asistencia(self):
        respuesta = messagebox.askquestion("Confirmación", "¿Estás seguro que quieres eliminar la asistencia?")
        if respuesta == 'yes':
            self.eliminar_asistencia()
        else:
            print("Eliminación cancelada")

    def eliminar_asistencia(self):
        print("Eliminar Asistencia")

    
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