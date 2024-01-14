from os.path import abspath, dirname, join

import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class VentanaMatricula():
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Matricular alumno")
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
        #Validación para asegurar que solo se ingresen valores numéricos
        validation = ventana_alumno.register(self.validate_deuda)

#----------------------------------------------------------------------------------------------------------------------
        #Frame para los datos del alumno
        fr_datos_alumno = tk.Frame(ventana_alumno)
        fr_datos_alumno.pack(side="top", fill=tk.X)

        # Agrega los elementos y la lógica para la ventana de añadir alumno aquí
        etiqueta_nuevo_alumno = tk.Label(fr_datos_alumno, text="Ingrese los datos del alumno:", bg="gray")
        etiqueta_nuevo_alumno.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Formulario para rellenar nombres y apellidos del alumno
        etiqueta_nombre = tk.Label(fr_datos_alumno, text="Nombres:", bg=color)
        etiqueta_nombre.grid(row=1, column=0, sticky=tk.E, padx=5)
        entry_nombre = tk.Entry(fr_datos_alumno)
        entry_nombre.config(width=25)
        entry_nombre.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosPaternos = tk.Label(fr_datos_alumno, text="Apel. Paternos:", bg=color)
        etiqueta_apellidosPaternos.grid(row=2, column=0, sticky=tk.E, padx=5)
        entry_apellidosPaternos = tk.Entry(fr_datos_alumno)
        entry_apellidosPaternos.config(width=25)
        entry_apellidosPaternos.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosMaternos = tk.Label(fr_datos_alumno, text="Apel. Materno:", bg=color)
        etiqueta_apellidosMaternos.grid(row=2, column=2, sticky=tk.E, padx=5)
        entry_apellidosMaternos = tk.Entry(fr_datos_alumno)
        entry_apellidosMaternos.config(width=25)
        entry_apellidosMaternos.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)

        # Formulario para rellenar D.N.I
        etiqueta_DNI = tk.Label(fr_datos_alumno, text="D.N.I:", bg=color)
        etiqueta_DNI.grid(row=3, column=0, sticky=tk.E, padx=5)
        entry_DNI = tk.Entry(fr_datos_alumno, validate="key", validatecommand=(validation, "%P"),)
        entry_DNI.config(width=25)
        entry_DNI.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        # Formulario para rellenar Fecha de nacimiento
        etiqueta_FechaNacimiento = tk.Label(fr_datos_alumno, text="Fecha de nacimiento:", bg=color)
        etiqueta_FechaNacimiento.grid(row=3, column=2, sticky=tk.E, padx=5)
        entry_FechaNacimiento = DateEntry(fr_datos_alumno, date_pattern="dd/mm/yyyy")
        entry_FechaNacimiento.grid(row=3, column=3, pady=5, padx=5, sticky=tk.W)
        entry_FechaNacimiento.config(width=21)

        # Menú desplegable Grupo
        etiqueta_Grupo = tk.Label(fr_datos_alumno, text="Grupo:", bg=color)
        etiqueta_Grupo.grid(row=4, column=0, sticky=tk.E, padx=5)
        opciones_Grupo = ["C", "D"]
        self.variable_Grupo = tk.StringVar(fr_datos_alumno)
        self.variable_Grupo.set("--Seleccione")
        menu_Grupo = ttk.Combobox(fr_datos_alumno, textvariable=self.variable_Grupo, values=opciones_Grupo, state="readonly")
        menu_Grupo.grid(row=4, column=1, pady=5, padx=5, sticky=tk.W)
        menu_Grupo.config(width=21)
        menu_Grupo.bind("<<ComboboxSelected>>", lambda event, menu=menu_Grupo: self.actualizar_opciones_carrera(event, menu))

        # Menú desplegable carreras profesionales
        etiqueta_carrera = tk.Label(fr_datos_alumno, text="Carrera profesional:", bg=color)
        etiqueta_carrera.grid(row=4, column=2, sticky=tk.E, padx=5)
        opciones_carrera = []
        self.variable_carrera = tk.StringVar(fr_datos_alumno)
        self.variable_carrera.set("--Seleccione")
        self.menu_carrera = ttk.Combobox(fr_datos_alumno, textvariable=self.variable_carrera, values=opciones_carrera, style="TCombobox", state="readonly")
        self.menu_carrera.grid(row=4, column=3, pady=5, padx=5, sticky=tk.W)
        self.menu_carrera.config(width=21)

        # Menu desplegable modalidad
        etiqueta_Modalidad = tk.Label(fr_datos_alumno, text="Modalidad:", bg=color)
        etiqueta_Modalidad.grid(row=5, column=0, sticky=tk.E, padx=5)
        opciones_modalidad = ["Primera opción", "Ordinario"]
        self.variable_modalidad = tk.StringVar(fr_datos_alumno)
        self.variable_modalidad.set("--Seleccione")
        menu_modalidad = ttk.Combobox(fr_datos_alumno, textvariable=self.variable_modalidad, values=opciones_modalidad, state="readonly")
        menu_modalidad.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)
        menu_modalidad.config(width=21)

        # Menu desplegable Turno
        etiqueta_Turno = tk.Label(fr_datos_alumno, text="Turno:", bg=color)
        etiqueta_Turno.grid(row=5, column=2, sticky=tk.E, padx=5)
        opciones_Turno = ["Mañana", "Tarde"]
        self.variable_Turno = tk.StringVar(fr_datos_alumno)
        self.variable_Turno.set("--Seleccione")
        self.menu_Turno = ttk.Combobox(fr_datos_alumno, textvariable=self.variable_Turno, values=opciones_Turno, style="TCombobox", state="readonly")
        self.menu_Turno.grid(row=5, column=3, pady=5, padx=5, sticky=tk.W)
        self.menu_Turno.config(width=21)
#----------------------------------------------------------------------------------------------------------------------
        #frame para datos de los padres
        fr_datos_padres = tk.Frame(ventana_alumno)
        fr_datos_padres.pack(side="top", fill=tk.X)

        # Datos de los padres o apoderados
        etiqueta_padres_apoderados = tk.Label(fr_datos_padres, text="Ingrese los datos de los padres o apoderados:", bg="gray")
        etiqueta_padres_apoderados.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Formulario para rellenar datos del Padre o madre
        etiqueta_NombresPadres = tk.Label(fr_datos_padres, text="Nombres:", bg=color)
        etiqueta_NombresPadres.grid(row=1, column=0, sticky=tk.E, padx=5)
        entry_NombresPadres = tk.Entry(fr_datos_padres)
        entry_NombresPadres.config(width=25)
        entry_NombresPadres.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosPaternosPadres = tk.Label(fr_datos_padres, text="Apel. Paternos:", bg=color)
        etiqueta_apellidosPaternosPadres.grid(row=2, column=0, sticky=tk.E, padx=5)
        entry_apellidosPaternosPadres = tk.Entry(fr_datos_padres)
        entry_apellidosPaternosPadres.config(width=25)
        entry_apellidosPaternosPadres.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosMaternosPadres = tk.Label(fr_datos_padres, text="Apel. Materno:", bg=color)
        etiqueta_apellidosMaternosPadres.grid(row=2, column=2, sticky=tk.E, padx=5)
        entry_apellidosMaternosPadres = tk.Entry(fr_datos_padres)
        entry_apellidosMaternosPadres.config(width=31)
        entry_apellidosMaternosPadres.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)

        # Formulario para telefono de padre o madre
        etiqueta_TelPadre = tk.Label(fr_datos_padres, text="Celular:", bg=color)
        etiqueta_TelPadre.grid(row=3, column=0, sticky=tk.E, padx=5)
        entry_TelPadre = tk.Entry(fr_datos_padres, validate="key", validatecommand=(validation, "%P"))
        entry_TelPadre.config(width=25)
        entry_TelPadre.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        #Descripcion adicional
        etiqueta_Descripcion = tk.Label(fr_datos_padres, text="Descripcion:", bg=color)
        etiqueta_Descripcion.grid(row=4, column=0, sticky=tk.E, padx=5)
        entry_Descripcion = tk.Entry(fr_datos_padres)
        entry_Descripcion.config(width=74)
        entry_Descripcion.grid(row=4, column=1, columnspan=3, pady=5, padx=5, sticky=tk.W)
#----------------------------------------------------------------------------------------------------------------------
        #frame para lo datos del importe pagado 
        fr_importe = tk.Frame(ventana_alumno)
        fr_importe.pack(side="top", fill=tk.X)
        
        #Etiqueta monto a pagar
        etiqueta_monto_pagar = tk.Label(fr_importe, text="Ingrese el monto a pagar:", bg="gray")
        etiqueta_monto_pagar.grid(row=0, column=0, columnspan=6, pady=10, sticky="ew")

        #Costo de la matricula
        etiqueta_costo = tk.Label(fr_importe, text="Costo:")
        etiqueta_costo.grid(row=1, column=0,sticky=tk.E, padx=6)
        self.entry_costo = tk.Entry(fr_importe, validate="key", validatecommand=(validation, "%P"))
        self.entry_costo.config(width=19)
        self.entry_costo.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
        self.entry_costo.bind("<KeyRelease>", lambda event: self.calcular_deuda())
        
        #Importe a la matricula
        etiqueta_importe = tk.Label(fr_importe, text="Importe:")
        etiqueta_importe.grid(row=1, column=2, sticky=tk.E, padx=5)
        self.entry_importe = tk.Entry(fr_importe, validate="key", validatecommand=(validation, "%P"))
        self.entry_importe.config(width=19)
        self.entry_importe.grid(row=1, column=3, pady=5, padx=6, sticky=tk.W)
        self.entry_importe.bind("<KeyRelease>", lambda event: self.calcular_deuda())

        #Deuda
        etiqueta_deuda = tk.Label(fr_importe, text="Deuda:", bg=color)
        etiqueta_deuda.grid(row=1, column=4, sticky=tk.E, padx=5)
        self.entry_deuda = tk.Entry(fr_importe)
        self.entry_deuda.config(width=19, state="readonly")
        self.entry_deuda.grid(row=1, column=5, pady=5, padx=6, sticky=tk.W)
        self.entry_deuda.insert(0, "S/.")
#----------------------------------------------------------------------------------------------------------------------
        # Cambia el estilo según tus preferencias
        estilo = ttk.Style()
        estilo.configure("TCombobox", padding=5, relief="flat", background="#d9d9d9")

        # Asociar la función habilitar_desabilitar_turno al evento de selección del ComboBox de modalidad
        menu_modalidad.bind("<<ComboboxSelected>>", lambda event: self.habilitar_desabilitar_turno())
#----------------------------------------------------------------------------------------------------------------------
        #Frame para botones 
        fr_botones = tk.Frame(ventana_alumno)
        fr_botones.pack(side="top", fill=tk.X)

        # Boton Guardar Alumno
        boton_guardar = tk.Button(fr_botones, text="Guardar", **self.estilo_boton, command=lambda: self.guardar_alumno(
                                                                                                        entry_nombre.get(),
                                                                                                        entry_apellidosPaternos.get(),
                                                                                                        entry_apellidosMaternos.get(),
                                                                                                        entry_DNI.get(),
                                                                                                        entry_FechaNacimiento.get(),
                                                                                                        self.variable_Grupo.get(), 
                                                                                                        self.variable_carrera.get(), 
                                                                                                        self.variable_modalidad.get(), 
                                                                                                        self.variable_Turno.get()))
        boton_guardar.pack( padx=10, pady=10, side="left")

        #Boton Cancelar
        boton_cancelar = tk.Button(fr_botones, text="Cancelar", **self.estilo_boton, command=ventana_alumno.destroy)
        boton_cancelar.pack(padx=10, pady=10, side="right")
#----------------------------------------------------------------------------------------------------------------------
    #Funcionalidades 
    def guardar_alumno(self, nombre, apellpate, apellmate, DNI, fecha, grupo, carrera, modalidad, turno):
        # Aquí puedes agregar la lógica para guardar los datos del alumno
        print(f"Nombre: {nombre} {apellpate} {apellmate}, DNI: {DNI}, Fecha de nacimiento: {fecha} guardados")
        print(f"Grupo: {grupo}, Carrera: {carrera}, Modalidad: {modalidad} y el el turno {turno}")

    def actualizar_opciones_carrera(self, event, menu_Grupo):
        seleccion_grupo = menu_Grupo.get()
        opciones_carrera = []

        if seleccion_grupo == "C":
            opciones_carrera = ["Administración",
                                "Contabilidad",
                                "Economia",
                                "Turismo"]
        elif seleccion_grupo == "D":
            opciones_carrera = ["Antropologia",
                                "Arqueologia",
                                "Ciencias de la comunicacion",
                                "Derecho",
                                "Educacion",
                                "Filosofia",
                                "Historia",
                                "Psicologia"]

        self.variable_carrera.set("--Seleccione")  # Reinicia el valor predeterminado
        self.menu_carrera["values"] = opciones_carrera

    def habilitar_desabilitar_turno(self):
        seleccion_modalidad = self.variable_modalidad.get()

        if seleccion_modalidad == "Primera opción":
            self.menu_Turno['state'] = 'readonly'  # Habilitar el ComboBox de Turno
        elif seleccion_modalidad == "Ordinario":
            self.menu_Turno.set("--Seleccione")  # Reiniciar la selección
            self.menu_Turno['state'] = 'disabled'  # Deshabilitar el ComboBox de Turno

    def validate_deuda(self, new_value):
        # Función de validación para asegurarse de que solo se ingresen valores numéricos
        try:
            if new_value == "":
                return True  # Permite eliminar el contenido del Entry
            float(new_value)
            return True
        except ValueError:
            return False  # No permite ingresar caracteres no numéricos
        
    def calcular_deuda(self):
        try:
            costo_str = self.entry_costo.get()
            importe_str = self.entry_importe.get()

            # Verificar que las cadenas no estén vacías antes de convertirlas a float
            if costo_str and importe_str:
                costo = float(costo_str)
                importe = float(importe_str)
                deuda = costo - importe
                self.entry_deuda.config(state="normal")
                self.entry_deuda.delete(0, tk.END)
                self.entry_deuda.insert(0, deuda)
            else:
                self.entry_deuda.config(state="normal")
                self.entry_deuda.delete(0, tk.END)
                self.entry_deuda.insert(0, "0")
        except ValueError:
            self.entry_deuda.config(state="normal")
            self.entry_deuda.delete(0, tk.END)
            self.entry_deuda.insert(0, "0")
        finally:
            self.entry_deuda.config(state="readonly")

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