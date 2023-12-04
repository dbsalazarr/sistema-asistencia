import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from tk_asistencia import VentanaAsistencia
from tk_configuracion import VentanaConfiguracion
from tk_lista_estudiantes import VentanaListaEstudiantes
from tk_matricula import VentanaMatricula
from tk_notas_estudiante import VentanaNotasEstudiante
from tk_ver_matricula import VentanaVerMatricula

class Interfaz():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Control de asistencia")
        self.ventana.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\principal.ico")
        self.ventana.resizable()

        # Obtén las dimensiones de la pantalla
        #ancho_pantalla = ctypes.windll.user32.GetSystemMetrics(0)
        #alto_pantalla = ctypes.windll.user32.GetSystemMetrics(1)

        # Configura la imagen de fondo
        ruta_fondo = "D:\\Personal\\TRABAJOS\\Python trabajos\\fondo.jpg"
        imagen_fondo = Image.open(ruta_fondo)
        imagen_fondo = ImageOps.fit(imagen_fondo, (653, 133))
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crea un Label con la imagen de fondo y colócalo en la ventana
        etiqueta_fondo = tk.Label(self.ventana, image=imagen_fondo)
        etiqueta_fondo.place(relwidth=1, relheight=1)  # Establece el tamaño del Label para cubrir toda la ventana

        # Añade una foto en la parte superior izquierda
        ruta_imagen = "D:\\Personal\\TRABAJOS\\Python trabajos\\74472.png"
        imagen_original = Image.open(ruta_imagen)
        imagen_original = ImageOps.expand(imagen_original, border=10, fill='black')  # Agrega un borde negro
        imagen_redimensionada = imagen_original.resize((150, 140))
        imagen = ImageTk.PhotoImage(imagen_redimensionada)

        etiqueta_imagen = tk.Label(self.ventana, image=imagen, bd=0)  # bd=0 para eliminar el borde predeterminado
        #etiqueta_imagen.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

        etiqueta_usuario = tk.Label(self.ventana, text="Usuario:")
        #etiqueta_usuario.grid(row=0, column=0, sticky=tk.E, padx=5)


        # Estilo general para los botones
        estilo_boton = {
            "font": ("Calibri", 12),
            "width": 20,
            "height": 2,
            "border": 5,
            "relief": "ridge",
            "highlightbackground": "#d9d9d9",
            "highlightthickness": 2,
            "cursor": "hand2"
        }

        # Botón 1: Matricular alumno
        boton_matricular = tk.Button(self.ventana, text="Matricular alumno", command=lambda: self.click_boton("Matricular alumno"),
                                    bg="#4CAF50", fg="white", **estilo_boton)
        boton_matricular.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Botón 2: Ver matrícula
        boton_ver_matricula = tk.Button(self.ventana, text="Ver matrícula", command=lambda: self.click_boton("Ver matricula"),
                                        bg="#4CAF50", fg="white", **estilo_boton)
        boton_ver_matricula.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        # Botón 3: Asistencia
        boton_asistencia = tk.Button(self.ventana, text="Asistencia", command=lambda: self.click_boton("Asistencia"),
                                    bg="#4CAF50", fg="white", **estilo_boton)
        boton_asistencia.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # Botón 4: Notas de estudiante
        boton_notas_estudiante = tk.Button(self.ventana, text="Notas de estudiante", command=lambda: self.click_boton("Notas de estudiante"),
                                        bg="#4CAF50", fg="white", **estilo_boton)
        boton_notas_estudiante.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Botón 5: Lista de estudiantes
        boton_lista_estudiantes = tk.Button(self.ventana, text="Lista de estudiantes", command=lambda: self.click_boton("Lista de estudiantes"),
                                            bg="#4CAF50", fg="white", **estilo_boton)
        boton_lista_estudiantes.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        # Botón 6: Configuración
        boton_configuracion = tk.Button(self.ventana, text="Configuración", command=lambda: self.click_boton("Configuración"),
                                        bg="#4CAF50", fg="white", **estilo_boton)
        boton_configuracion.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

        # Botón 7: Cerrar programa
        boton_cerrar_programa = tk.Button(self.ventana, text="Cerrar programa", command=lambda: self.click_boton("Cerrar programa"),
                                        bg="#F44336", fg="white", **estilo_boton)
        boton_cerrar_programa.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

        # Configurar el redimensionamiento del marco principal
        self.ventana.columnconfigure(list(range(3)), weight=1)
        self.ventana.rowconfigure(0, weight=1)


        # Asigna la imagen a una propiedad de clase para evitar que sea eliminada por el recolector de basura
        self.imagen_tk = imagen

        # Asigna la imagen de fondo a una propiedad de clase para evitar que sea eliminada por el recolector de basura
        self.imagen_fondo_tk = imagen_fondo

        # Inicia el bucle principal para abrir la ventana
        self.ventana.mainloop()

    def click_boton(self, valor):
        if valor == "Ver matricula":
            VentanaVerMatricula(self)
        elif valor == "Matricular alumno":
            VentanaMatricula(self)
        elif valor == "Asistencia":
            VentanaAsistencia(self)
        elif valor == "Notas de estudiante":
            VentanaNotasEstudiante(self)
        elif valor == "Lista de estudiantes":
            VentanaListaEstudiantes(self)
        elif valor == "Configuración":
            VentanaConfiguracion(self)
        elif valor == "Cerrar programa":
            self.ventana.destroy()  # Cierra la ventana principal


        #fechas de ciclo
        #horarios

interfaz = Interfaz()
