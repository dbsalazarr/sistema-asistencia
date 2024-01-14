from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class VentanaVerMatricula:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        self.ventana_alumno.title("Ver matriculas")
        self.ventana_alumno.iconbitmap(self.get_icon_path("secundario.ico"))
        # Estilo general para los botones
        self.estilo_boton = {
            "font": ("Calibri", 12),
            "width": 25,
            "height": 2,
            "border": 5,
            "relief": "ridge",
            "highlightbackground": "#d9d9d9",
            "highlightthickness": 2,
            "cursor": "hand2"
        }

        #Frame para la tabla
        fr_tabla_lista = tk.Frame(self.ventana_alumno, bd=0, width=300, relief=tk.SOLID, bg="black")
        fr_tabla_lista.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        
        # Crear tabla
        self.tabla_matricula = ttk.Treeview(fr_tabla_lista, columns=("Codigo", "Nombre", "Modalidad", "Grupo", "Turno", "Deuda"))
        self.tabla_matricula.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        # Configuración de expansión de filas y columnas
        fr_tabla_lista.columnconfigure(0, weight=1)  # Configura la columna 0 para expandirse
        fr_tabla_lista.rowconfigure(0, weight=1)     # Configura la fila 0 para expandirse
         #columnas de la tabla
        self.tabla_matricula.column("#0", width=0, stretch="no")
        self.tabla_matricula.column("Codigo", anchor="center", width=100)
        self.tabla_matricula.column("Nombre", anchor="center", width=360)
        self.tabla_matricula.column("Modalidad", anchor="center", width=90)
        self.tabla_matricula.column("Grupo", anchor="center", width=90)
        self.tabla_matricula.column("Turno", anchor="center", width=90)
        self.tabla_matricula.column("Deuda", anchor="center", width=90)
        
        #Encabezado de las columnas
        self.tabla_matricula.heading("#0")
        self.tabla_matricula.heading("Codigo", text="Codigo")
        self.tabla_matricula.heading("Nombre", text="Nombre")
        self.tabla_matricula.heading("Modalidad", text="Modalidad")
        self.tabla_matricula.heading("Grupo", text="Grupo")
        self.tabla_matricula.heading("Turno", text="Turno")
        self.tabla_matricula.heading("Deuda", text="Deuda")

        #Frame para los botones
        fr_botones = tk.Frame(self.ventana_alumno, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#9b9b9b")
        fr_botones.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        #Botones
        boton_crear_lista = tk.Button(fr_botones, text="Editar datos", command=self.crear_lista, **self.estilo_boton)
        boton_crear_lista.grid(row=0, column=0, pady=5, padx=5, sticky="ew")

        boton_modificar_lista = tk.Button(fr_botones, text="Estadisticas", command=self.modificar_lista, **self.estilo_boton)
        boton_modificar_lista.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

        boton_eliminar_lista = tk.Button(fr_botones, text="Eliminar\nEstudiante", command=self.eliminar_lista, **self.estilo_boton)
        boton_eliminar_lista.grid(row=2, column=0, pady=5, padx=5, sticky="ew")

        boton_salir = tk.Button(fr_botones, text="Salir", command=self.ventana_alumno.destroy, bg="red", **self.estilo_boton)
        boton_salir.grid(row=3, column=0, pady=5, padx=5, sticky="ew")

    def crear_lista(self):
        print("Crear lista")

    def modificar_lista(self):
        print("Modificar lista")

    def eliminar_lista(self):
        print("Eliminar lista")

    def insertar_fila_ejemplo(self):
        self.tabla.insert(parent="", index="end", iid=1, text="1", values=("Primera opcion", "C", "Mañana"))

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