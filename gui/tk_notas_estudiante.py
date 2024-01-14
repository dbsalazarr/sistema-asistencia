from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class VentanaNotasEstudiante:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Notas de estudiante")
        ventana_alumno.iconbitmap(self.get_icon_path("secundario.ico"))
         # Estilo general para los botones
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

#----------------------------------------------------------------------------------------------------------------------------
        #Frame para los botones
        fr_bot_notas = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_bot_notas.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        # Botones
        boton_subir_notas = tk.Button(fr_bot_notas, text="Subir notas", **self.estilo_boton, command=self.subir_nota)
        boton_subir_notas.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_modificar_notas = tk.Button(fr_bot_notas, text="Modificar nota", **self.estilo_boton)
        boton_modificar_notas.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

        texto_boton = "Promedios\ny\nCalificaciones"
        boton_promedios_calificaciones = tk.Button(fr_bot_notas, text=texto_boton, **self.estilo_boton)
        boton_promedios_calificaciones.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        # Botón para salir
        boton_salir = tk.Button(fr_bot_notas, text="Salir", command=ventana_alumno.destroy, bg="red", **self.estilo_boton)
        boton_salir.grid(row=5, column=0, columnspan=2, pady=5, padx=10)
#----------------------------------------------------------------------------------------------------------------------------
        #Frame de la tabla para visualizar promedio de notas
        fr_bot_notas = tk.Frame(ventana_alumno, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_bot_notas.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #Frame para el boton buscar
        fr_buscar_notas = tk.Frame(fr_bot_notas, bd=0, height=50, relief=tk.SOLID, bg="#fcfcfc")
        fr_buscar_notas.pack(side="top", expand=tk.NO, fill=tk.BOTH)

        #Boton buscar estudiante
        boton_buscar_nota_estudiante = tk.Button(fr_buscar_notas, text="Buscar", width=10)
        boton_buscar_nota_estudiante.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)
        entry_buscar = tk.Entry(fr_buscar_notas, width=50)
        entry_buscar.pack(side="left", padx=5, pady=5, expand=tk.NO, fill=tk.BOTH)

        #Frame para la tabla de las notas
        fr_tab_notas = tk.Frame(fr_bot_notas, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_tab_notas.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        # Tabla
        self.tab_notas = ttk.Treeview(fr_tab_notas, columns=("Codigo", "Nombre", 
                                                             "Algebra", "Aritmetica", 
                                                             "Linguistica", "Civica", 
                                                             "Historia", "Geografia", 
                                                             "Filosofia", "Economia", 
                                                             "Promedio"))
        self.tab_notas.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        # Configuración de expansión de filas y columnas
        fr_tab_notas.columnconfigure(0, weight=1)  # Configura la columna 0 para expandirse
        fr_tab_notas.rowconfigure(0, weight=1)     # Configura la fila 0 para expandirse

        #columnas de la tabla
        self.tab_notas.column("#0", width=0, stretch="no")
        self.tab_notas.column("Codigo", anchor="center", width=80, stretch=tk.NO)
        self.tab_notas.column("Nombre", anchor="center", width=320, stretch=tk.NO)
        self.tab_notas.column("Algebra", anchor="center", width=80)
        self.tab_notas.column("Aritmetica", anchor="center", width=80)
        self.tab_notas.column("Linguistica", anchor="center", width=120)
        self.tab_notas.column("Civica", anchor="center", width=80)
        self.tab_notas.column("Historia", anchor="center", width=80)
        self.tab_notas.column("Geografia", anchor="center", width=80)
        self.tab_notas.column("Filosofia", anchor="center", width=80)
        self.tab_notas.column("Economia", anchor="center", width=80)
        self.tab_notas.column("Promedio", anchor="center", width=80)
        #Encabezado de las columnas
        self.tab_notas.heading("#0")
        self.tab_notas.heading("Codigo", text="Codigo")
        self.tab_notas.heading("Nombre", text="Nombre")
        self.tab_notas.heading("Algebra", text="Algebra")
        self.tab_notas.heading("Aritmetica", text="Aritmetica")
        self.tab_notas.heading("Linguistica", text="Comp. Linguistica")
        self.tab_notas.heading("Civica", text="Civica")
        self.tab_notas.heading("Historia", text="Historia")
        self.tab_notas.heading("Geografia", text="Geografia")
        self.tab_notas.heading("Filosofia", text="Filosofia")
        self.tab_notas.heading("Economia", text="Economia")
        self.tab_notas.heading("Promedio", text="Promedio")

    def subir_nota(self):
        VentanaSubirNotas(self.ventana_principal.ventana)

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


class VentanaSubirNotas:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.vent_subir_notas = tk.Toplevel(self.ventana_principal)
        self.vent_subir_notas.title("Subir notas de estudiante")
        self.vent_subir_notas.iconbitmap(self.get_icon_path("secundario.ico"))

        #Frame para los nombres de los alumnos
        fr_nombres_alumnos = tk.Frame(self.vent_subir_notas, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_nombres_alumnos.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #Tabla de nombres
        # Tabla
        self.tabla_notas_estudiantes = ttk.Treeview(fr_nombres_alumnos, columns=("Codigo", "Nombre", "Modalidad", "Grupo"))
        self.tabla_notas_estudiantes.grid(row=1, column=3, columnspan=4, rowspan=5, pady=5, padx=5)

        #columnas de la tabla
        self.tabla_notas_estudiantes.column("#0", width=0, stretch="no")
        self.tabla_notas_estudiantes.column("Codigo", anchor="center", width=100)
        self.tabla_notas_estudiantes.column("Nombre", anchor="center", width=360)
        self.tabla_notas_estudiantes.column("Modalidad", anchor="center", width=90)
        self.tabla_notas_estudiantes.column("Grupo", anchor="center", width=90)
        
        #Encabezado de las columnas
        self.tabla_notas_estudiantes.heading("#0")
        self.tabla_notas_estudiantes.heading("Codigo", text="Codigo")
        self.tabla_notas_estudiantes.heading("Nombre", text="Nombre")
        self.tabla_notas_estudiantes.heading("Modalidad", text="Modalidad")
        self.tabla_notas_estudiantes.heading("Grupo", text="Grupo")
        
        #Frame para la fecha y subir las notas
        fr_fecha_y_notas = tk.Frame(self.vent_subir_notas, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_fecha_y_notas.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        
        #Frame para fecha de examen
        fr_fecha = tk.Frame(fr_fecha_y_notas, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_fecha.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        # titulo para la fecha de examen
        etiqueta_fecha = tk.Label(fr_fecha, text="Ingrese fecha de examen:", bg="gray")
        etiqueta_fecha.grid(row=0, columnspan=2, pady=10, sticky="ew")

        #Fecha de examen programado
        etiqueta_Fecha_examen = tk.Label(fr_fecha, text="Fecha de examen:", bg="#D3D3D3")
        etiqueta_Fecha_examen.grid(row=1, column=0, sticky=tk.E, padx=5)
        etiqueta_Fecha_examen = DateEntry(fr_fecha, date_pattern="dd/mm/yyyy")
        etiqueta_Fecha_examen.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
        etiqueta_Fecha_examen.config(width=21)

        #Frame para las notas
        fr_notas = tk.Frame(fr_fecha_y_notas, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        fr_notas.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        #Titulo para ingreso de notas
        etiqueta_subirnota = tk.Label(fr_notas, text="Ingrese codigo y notas de estudiante:", bg="gray")
        etiqueta_subirnota.grid(row=0, columnspan=4, pady=10, sticky="ew")

        #Ingreso de codigo de alumno
        etiq_codigo = tk.Label(fr_notas, text="Codigo:", bg="#D3D3D3")
        etiq_codigo.grid(row=1, column=0, columnspan=2, sticky=tk.E, padx=5)
        entry_codigo = tk.Entry(fr_notas, width=18)
        entry_codigo.grid(row=1, column=2, columnspan=2, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de linguistica
        etiq_linguistica = tk.Label(fr_notas, text="Comp. Lingusitica:", bg="#D3D3D3")
        etiq_linguistica.grid(row=2, column=0, sticky=tk.E, padx=5)
        entry_linguistica = tk.Entry(fr_notas, width=12)
        entry_linguistica.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de Aritmetica
        etiq_aritmetica = tk.Label(fr_notas, text="Aritmetica:", bg="#D3D3D3")
        etiq_aritmetica.grid(row=3, column=0, sticky=tk.E, padx=5)
        entry_aritmetica = tk.Entry(fr_notas, width=12)
        entry_aritmetica.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de Algebra
        etiq_algebra = tk.Label(fr_notas, text="Algebra:", bg="#D3D3D3")
        etiq_algebra.grid(row=4, column=0, sticky=tk.E, padx=5)
        entry_algebra = tk.Entry(fr_notas, width=12)
        entry_algebra.grid(row=4, column=1, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de Historia
        etiq_historia = tk.Label(fr_notas, text="Historia:", bg="#D3D3D3")
        etiq_historia.grid(row=5, column=0, sticky=tk.E, padx=5)
        entry_historia = tk.Entry(fr_notas, width=12)
        entry_historia.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de Geografia
        etiq_geografia = tk.Label(fr_notas, text="Geografia:", bg="#D3D3D3")
        etiq_geografia.grid(row=2, column=2, sticky=tk.E, padx=5)
        entry_geografia = tk.Entry(fr_notas, width=12)
        entry_geografia.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)
        
        #Ingreso del curso de Civica
        etiq_civica = tk.Label(fr_notas, text="Civica:", bg="#D3D3D3")
        etiq_civica.grid(row=3, column=2, sticky=tk.E, padx=5)
        entry_civica = tk.Entry(fr_notas, width=12)
        entry_civica.grid(row=3, column=3, pady=5, padx=5, sticky=tk.W)
        
        #Ingreso del curso de Economia
        etiq_economia = tk.Label(fr_notas, text="Economia:", bg="#D3D3D3")
        etiq_economia.grid(row=4, column=2, sticky=tk.E, padx=5)
        entry_economia = tk.Entry(fr_notas, width=12)
        entry_economia.grid(row=4, column=3, pady=5, padx=5, sticky=tk.W)

        #Ingreso del curso de Economia
        etiq_filosofia = tk.Label(fr_notas, text="Filosofia:", bg="#D3D3D3")
        etiq_filosofia.grid(row=5, column=2, sticky=tk.E, padx=5)
        entry_filosofia = tk.Entry(fr_notas, width=12)
        entry_filosofia.grid(row=5, column=3, pady=5, padx=5, sticky=tk.W)


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
