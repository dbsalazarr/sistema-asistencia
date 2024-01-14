from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class VentanaListaEstudiantes:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Lista de estudiantes")
        ventana_alumno.iconbitmap(self.get_icon_path("secundario.ico"))
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

        #frame para los botones
        fr_bot_detalles_estudiantes = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_bot_detalles_estudiantes.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        # Botones
        boton_detalles_estudiante = tk.Button(fr_bot_detalles_estudiantes, text="Detalles de estudiante", **self.estilo_boton)
        boton_detalles_estudiante.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_editar_informacion = tk.Button(fr_bot_detalles_estudiantes, text="Editar Informacion",**self.estilo_boton)
        boton_editar_informacion.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

        boton_estadisticas_estudiante = tk.Button(fr_bot_detalles_estudiantes, text="Estadisticas de Estudiante",**self.estilo_boton)
        boton_estadisticas_estudiante.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        boton_eliminar_estudiante = tk.Button(fr_bot_detalles_estudiantes, text="Eliminar Estudiante", **self.estilo_boton)
        boton_eliminar_estudiante.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        # Botón para salir
        boton_salir = tk.Button(fr_bot_detalles_estudiantes, text="Salir", command=ventana_alumno.destroy, bg="red", **self.estilo_boton)
        boton_salir.grid(row=5, column=0, columnspan=2, pady=5, padx=10)
#-------------------------------------------------------------------------------------------------------------------------------
        #Frame para tabla y boton buscar
        fr_tab_bot_estudiantes = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_tab_bot_estudiantes.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #Frame para boton buscar 
        fr_bot_buscar_estudiante = tk.Frame(fr_tab_bot_estudiantes, bd=0, relief=tk.SOLID, bg="black")
        fr_bot_buscar_estudiante.pack(side="top", expand=tk.NO, fill=tk.X)

        #Boton buscar estudiante
        boton_buscar_estudiante = tk.Button(fr_bot_buscar_estudiante, text="Buscar", command=self.buscar_alumno , width=10)
        boton_buscar_estudiante.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)
        entry_buscar = tk.Entry(fr_bot_buscar_estudiante, width=30)
        entry_buscar.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)

        #Frame para boton buscar 
        fr_tab_estudiante = tk.Frame(fr_tab_bot_estudiantes, bd=0, relief=tk.SOLID, bg="black")
        fr_tab_estudiante.pack(side="top", expand=tk.NO, fill=tk.X)

        # Tabla
        self.tabla_estudiantes = ttk.Treeview(fr_tab_estudiante, columns=("Codigo", "Nombre", "Modalidad", "Turno", "Grupo"))
        self.tabla_estudiantes.grid(row=1, column=3, columnspan=4, rowspan=5, pady=5, padx=5)

        #columnas de la tabla
        self.tabla_estudiantes.column("#0", width=0, stretch="no")
        self.tabla_estudiantes.column("Codigo", anchor="center", width=100)
        self.tabla_estudiantes.column("Nombre", anchor="center", width=360)
        self.tabla_estudiantes.column("Modalidad", anchor="center", width=90)
        self.tabla_estudiantes.column("Turno", anchor="center", width=90)
        self.tabla_estudiantes.column("Grupo", anchor="center", width=90)
        
        #Encabezado de las columnas
        self.tabla_estudiantes.heading("#0")
        self.tabla_estudiantes.heading("Codigo", text="Codigo")
        self.tabla_estudiantes.heading("Nombre", text="Nombre")
        self.tabla_estudiantes.heading("Modalidad", text="Modalidad")
        self.tabla_estudiantes.heading("Turno", text="Turno")
        self.tabla_estudiantes.heading("Grupo", text="Grupo")
        
    def configurar_tabla_lista_estudiantes(self, tabla):
        pass

    def insertar_fila_lista_estudiantes(self, tabla):
        tabla.insert(parent="", index="end", iid=1, text="1", values=("Juan Jesus Ramirez Pimpinela", "ABC123", "10.39","Completa"))

    def buscar_alumno(self):
        print("Buscar alumno")

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