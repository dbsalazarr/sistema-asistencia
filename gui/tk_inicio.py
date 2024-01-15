from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from gui.tk_asistencia import VentanaAsistencia
from gui.tk_configuracion import VentanaConfiguracion
from gui.tk_lista_estudiantes import VentanaListaEstudiantes
from gui.tk_matricula import VentanaMatricula
from gui.tk_notas_estudiante import VentanaNotasEstudiante
from gui.tk_ver_matricula import VentanaVerMatricula

class Interfaz():
    def __init__(self):
        super().__init__()
        
        self.ventana = tk.Tk()
        self.ventana.title("Control de asistencia")
        self.ventana.iconbitmap(self.get_icon_path("principal.ico"))
        self.ventana.resizable(0,0)

        # Añade una foto en la parte superior izquierda
        ruta_imagen = self.get_icon_path("74472.png")
        imagen_original = Image.open(ruta_imagen)
        imagen_original = ImageOps.expand(imagen_original, border=10, fill='black')  # Agrega un borde negro
        imagen_redimensionada = imagen_original.resize((150, 160))
        imagen = ImageTk.PhotoImage(imagen_redimensionada)

        #etiqueta_imagen = tk.Label(self.ventana, image=imagen, bd=0)  # bd=0 para eliminar el borde predeterminado
        #etiqueta_imagen.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

        #etiqueta_usuario = tk.Label(self.ventana, text="Usuario:")
        #etiqueta_usuario.grid(row=0, column=0, sticky=tk.E, padx=5)


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

        # frame para los datos del usuario
        fr_usuario = tk.Frame(self.ventana, bd=0, height=50, relief=tk.SOLID, bg="black")
        fr_usuario.pack(side="top", fill=tk.X)

        # sub frame para la foto
        sub_fr_foto = tk.Frame(fr_usuario, bd=0, width=180, height=200, relief=tk.SOLID, padx=10, pady=10, bg="green")
        sub_fr_foto.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label_foto = tk.Label(sub_fr_foto, bg="green", image=imagen)
        label_foto.place(x=0, y=0, relwidth=1, relheight=1)

        # sub frame para lso datos
        sub_fr_datos = tk.Frame(fr_usuario, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        sub_fr_datos.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        #datos de usuario
        lb_usuario = tk.Label(sub_fr_datos, text="Usuario:")
        lb_usuario.grid(row=0, column=0,  padx=10, pady=10)
        


        # frame para los botones
        fr_botones = tk.Frame(self.ventana, bd=0, height=50, width=300, relief=tk.SOLID, bg="red")
        fr_botones.pack(side="bottom", fill=tk.X)
        
        # Botón 1: Matricular alumno
        boton_matricular = tk.Button(fr_botones, text="Matricular alumno", command=lambda: self.click_boton("Matricular alumno"),
                                    bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_matricular.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Botón 2: Ver matrícula
        boton_ver_matricula = tk.Button(fr_botones, text="Ver matrículas", command=lambda: self.click_boton("Ver matricula"),
                                        bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_ver_matricula.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        # Botón 3: Asistencia
        boton_asistencia = tk.Button(fr_botones, text="Asistencia", command=lambda: self.click_boton("Asistencia"),
                                    bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_asistencia.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # Botón 4: Notas de estudiante
        boton_notas_estudiante = tk.Button(fr_botones, text="Notas de estudiante", command=lambda: self.click_boton("Notas de estudiante"),
                                        bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_notas_estudiante.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Botón 5: Lista de estudiantes
        boton_lista_estudiantes = tk.Button(fr_botones, text="Lista de estudiantes", command=lambda: self.click_boton("Lista de estudiantes"),
                                            bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_lista_estudiantes.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        # Botón 6: Configuración
        boton_configuracion = tk.Button(fr_botones, text="Configuración", command=lambda: self.click_boton("Configuración"),
                                        bg="#4CAF50", fg="white", **self.estilo_boton)
        boton_configuracion.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

        # Botón 7: Cerrar programa
        boton_cerrar_programa = tk.Button(fr_botones, text="Cerrar programa", command=lambda: self.click_boton("Cerrar programa"),
                                        bg="#F44336", fg="white", **self.estilo_boton)
        boton_cerrar_programa.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

        # Configurar el redimensionamiento del marco principal
        self.ventana.columnconfigure(list(range(3)), weight=1)
        self.ventana.rowconfigure(0, weight=1)


        # Asigna la imagen a una propiedad de clase para evitar que sea eliminada por el recolector de basura
        self.imagen_tk = imagen

        # Asigna la imagen de fondo a una propiedad de clase para evitar que sea eliminada por el recolector de basura
        #self.imagen_fondo_tk = self.imagen_fondo

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

        #fechas de ciclo
        #horarios

#interfaz = Interfaz()
#interfaz.mainloop()
