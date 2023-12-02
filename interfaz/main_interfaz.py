import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class Interfaz():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Control de asistencia")
        self.ventana.iconbitmap("D:\DESARROLLO DE APLICACIONES\sistema_registro_asistencia\media\principal.ico")
        self.ventana.resizable()

        # Obtén las dimensiones de la pantalla
        #ancho_pantalla = ctypes.windll.user32.GetSystemMetrics(0)
        #alto_pantalla = ctypes.windll.user32.GetSystemMetrics(1)

        # Configura la imagen de fondo
        ruta_fondo = "D:\DESARROLLO DE APLICACIONES\sistema_registro_asistencia\media\\fondo.jpg"
        imagen_fondo = Image.open(ruta_fondo)
        imagen_fondo = ImageOps.fit(imagen_fondo, (653, 133))
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

        # Crea un Label con la imagen de fondo y colócalo en la ventana
        etiqueta_fondo = tk.Label(self.ventana, image=imagen_fondo)
        etiqueta_fondo.place(relwidth=1, relheight=1)  # Establece el tamaño del Label para cubrir toda la ventana

        # Añade una foto en la parte superior izquierda
        ruta_imagen = "D:\DESARROLLO DE APLICACIONES\sistema_registro_asistencia\media\\74472.png"
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

class VentanaMatricula:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Matricular alumno")
        ventana_alumno.iconbitmap("D:\DESARROLLO DE APLICACIONES\sistema_registro_asistencia\media\secundario.ico")
        color = "#D3D3D3"

    # Agrega los elementos y la lógica para la ventana de añadir alumno aquí
        etiqueta_nuevo_alumno = tk.Label(ventana_alumno, text="Ingrese los datos del alumno:", bg="gray")
        etiqueta_nuevo_alumno.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Formulario para rellenar nombres y apellidos del alumno
        etiqueta_nombre = tk.Label(ventana_alumno, text="Nombres:", bg=color)
        etiqueta_nombre.grid(row=1, column=0, sticky=tk.E, padx=5)
        entry_nombre = tk.Entry(ventana_alumno)
        entry_nombre.config(width=25)
        entry_nombre.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosPaternos = tk.Label(ventana_alumno, text="Apel. Paternos:", bg=color)
        etiqueta_apellidosPaternos.grid(row=2, column=0, sticky=tk.E, padx=5)
        entry_apellidosPaternos = tk.Entry(ventana_alumno)
        entry_apellidosPaternos.config(width=25)
        entry_apellidosPaternos.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosMaternos = tk.Label(ventana_alumno, text="Apel. Materno:", bg=color)
        etiqueta_apellidosMaternos.grid(row=2, column=2, sticky=tk.E, padx=5)
        entry_apellidosMaternos = tk.Entry(ventana_alumno)
        entry_apellidosMaternos.config(width=25)
        entry_apellidosMaternos.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)

        # Formulario para rellenar D.N.I
        etiqueta_DNI = tk.Label(ventana_alumno, text="D.N.I:", bg=color)
        etiqueta_DNI.grid(row=3, column=0, sticky=tk.E, padx=5)
        entry_DNI = tk.Entry(ventana_alumno)
        entry_DNI.config(width=25)
        entry_DNI.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

        # Formulario para rellenar Fecha de nacimiento
        etiqueta_FechaNacimiento = tk.Label(ventana_alumno, text="Fecha de nacimiento:", bg=color)
        etiqueta_FechaNacimiento.grid(row=3, column=2, sticky=tk.E, padx=5)
        entry_FechaNacimiento = DateEntry(ventana_alumno, date_pattern="dd/mm/yyyy")
        entry_FechaNacimiento.grid(row=3, column=3, pady=5, padx=5, sticky=tk.W)

        # Menú desplegable Grupo
        etiqueta_Grupo = tk.Label(ventana_alumno, text="Grupo:", bg=color)
        etiqueta_Grupo.grid(row=4, column=0, sticky=tk.E, padx=5)
        opciones_Grupo = ["C", "D"]
        self.variable_Grupo = tk.StringVar(ventana_alumno)
        self.variable_Grupo.set("--Seleccione")
        menu_Grupo = ttk.Combobox(ventana_alumno, textvariable=self.variable_Grupo, values=opciones_Grupo, state="readonly")
        menu_Grupo.grid(row=4, column=1, pady=5, padx=5, sticky=tk.W)
        menu_Grupo.bind("<<ComboboxSelected>>", lambda event, menu=menu_Grupo: self.actualizar_opciones_carrera(event, menu))

        # Menú desplegable carreras profesionales
        etiqueta_carrera = tk.Label(ventana_alumno, text="Carrera profesional:", bg=color)
        etiqueta_carrera.grid(row=4, column=2, sticky=tk.E, padx=5)
        opciones_carrera = []
        self.variable_carrera = tk.StringVar(ventana_alumno)
        self.variable_carrera.set("--Seleccione")
        self.menu_carrera = ttk.Combobox(ventana_alumno, textvariable=self.variable_carrera, values=opciones_carrera, style="TCombobox", state="readonly")
        self.menu_carrera.grid(row=4, column=3, pady=5, padx=5, sticky=tk.W)

        # Menu desplegable modalidad
        etiqueta_Modalidad = tk.Label(ventana_alumno, text="Modalidad:", bg=color)
        etiqueta_Modalidad.grid(row=5, column=0, sticky=tk.E, padx=5)
        opciones_modalidad = ["Primera opción", "Ordinario"]
        self.variable_modalidad = tk.StringVar(ventana_alumno)
        self.variable_modalidad.set("--Seleccione")
        menu_modalidad = ttk.Combobox(ventana_alumno, textvariable=self.variable_modalidad, values=opciones_modalidad, state="readonly")
        menu_modalidad.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)

        # Menu desplegable Turno
        etiqueta_Turno = tk.Label(ventana_alumno, text="Turno:", bg=color)
        etiqueta_Turno.grid(row=5, column=2, sticky=tk.E, padx=5)
        opciones_Turno = ["Mañana", "Tarde"]
        self.variable_Turno = tk.StringVar(ventana_alumno)
        self.variable_Turno.set("--Seleccione")
        self.menu_Turno = ttk.Combobox(ventana_alumno, textvariable=self.variable_Turno, values=opciones_Turno, style="TCombobox", state="readonly")
        self.menu_Turno.grid(row=5, column=3, pady=5, padx=5, sticky=tk.W)

        # Datos de los padres o apoderados
        etiqueta_padres_apoderados = tk.Label(ventana_alumno, text="Ingrese los datos de los padres o apoderados:", bg="gray")
        etiqueta_padres_apoderados.grid(row=6, column=0, columnspan=4, pady=10, sticky="ew")

        # Formulario para rellenar datos del Padre o madre
        etiqueta_NombresPadres = tk.Label(ventana_alumno, text="Nombres:", bg=color)
        etiqueta_NombresPadres.grid(row=7, column=0, sticky=tk.E, padx=5)
        entry_NombresPadres = tk.Entry(ventana_alumno)
        entry_NombresPadres.config(width=25)
        entry_NombresPadres.grid(row=7, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosPaternosPadres = tk.Label(ventana_alumno, text="Apel. Paternos:", bg=color)
        etiqueta_apellidosPaternosPadres.grid(row=8, column=0, sticky=tk.E, padx=5)
        entry_apellidosPaternosPadres = tk.Entry(ventana_alumno)
        entry_apellidosPaternosPadres.config(width=25)
        entry_apellidosPaternosPadres.grid(row=8, column=1, pady=5, padx=5, sticky=tk.W)

        etiqueta_apellidosMaternosPadres = tk.Label(ventana_alumno, text="Apel. Materno:", bg=color)
        etiqueta_apellidosMaternosPadres.grid(row=8, column=2, sticky=tk.E, padx=5)
        entry_apellidosMaternosPadres = tk.Entry(ventana_alumno)
        entry_apellidosMaternosPadres.config(width=25)
        entry_apellidosMaternosPadres.grid(row=8, column=3, pady=5, padx=5, sticky=tk.W)

        # Formulario para telefono de padre o madre
        etiqueta_TelPadre = tk.Label(ventana_alumno, text="Celular:", bg=color)
        etiqueta_TelPadre.grid(row=9, column=0, sticky=tk.E, padx=5)
        entry_TelPadre = tk.Entry(ventana_alumno)
        entry_TelPadre.config(width=25)
        entry_TelPadre.grid(row=9, column=1, pady=5, padx=5, sticky=tk.W)

        # Menu desplegable Deuda
        etiqueta_Deuda = tk.Label(ventana_alumno, text="Deuda:", bg=color)
        etiqueta_Deuda.grid(row=9, column=2, sticky=tk.E, padx=5)
        # Validación para asegurar que solo se ingresen valores numéricos
        validation = ventana_alumno.register(self.validate_deuda)
        entry_Deuda = tk.Entry(ventana_alumno, validate="key", validatecommand=(validation, "%P"))
        entry_Deuda.config(width=25)
        entry_Deuda.grid(row=9, column=3, pady=5, padx=5, sticky=tk.W)
        entry_Deuda.insert(0, "S/.")

        #Descripcion adicional
        etiqueta_Descripcion = tk.Label(ventana_alumno, text="Descripcion:", bg=color)
        etiqueta_Descripcion.grid(row=10, column=0, sticky=tk.E, padx=5)
        entry_Descripcion = tk.Entry(ventana_alumno)
        entry_Descripcion.config(width=74)
        entry_Descripcion.grid(row=10, column=1, columnspan=3, pady=5, padx=5, sticky=tk.W)


        # Cambia el estilo según tus preferencias
        estilo = ttk.Style()
        estilo.configure("TCombobox", padding=5, relief="flat", background="#d9d9d9")

        # Asociar la función habilitar_desabilitar_turno al evento de selección del ComboBox de modalidad
        menu_modalidad.bind("<<ComboboxSelected>>", lambda event: self.habilitar_desabilitar_turno())

        # Boton Guardar Alumno
        boton_guardar = tk.Button(ventana_alumno, text="Guardar", font=("Calibri 15"), width=15, height=2,
                                command=lambda: self.guardar_alumno(entry_nombre.get(),
                                                                    entry_DNI.get(),
                                                                    entry_FechaNacimiento.get()))
        boton_guardar.grid(row=11, column=0, columnspan=2, pady=3)

        #Boton Cancelar
        boton_cancelar = tk.Button(ventana_alumno, text="Cancelar", font=("Calibri 15"), width=15, height=2, command=ventana_alumno.destroy)
        boton_cancelar.grid(row=11, column=2, columnspan=2, pady=3)

    def guardar_alumno(self, nombre, edad, curso):
        # Aquí puedes agregar la lógica para guardar los datos del alumno
        print(f"Nombre: {nombre}, Edad: {edad}, Curso: {curso} guardados")

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

class VentanaVerMatricula:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        self.ventana_alumno.title("Ver matricula")
        self.ventana_alumno.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")

        # Crear tabla
        self.tabla = ttk.Treeview(self.ventana_alumno, columns=("Modalidad", "Grupo", "Turno", ))
        self.configurar_tabla_lista()
        self.insertar_fila_ejemplo()
        self.tabla.grid(row=0, rowspan=4, column=0, pady=10)

        # Botones
        boton_crear_lista = tk.Button(self.ventana_alumno, text="Editar datos", command=self.crear_lista)
        boton_crear_lista.grid(row=0, column=4, pady=5, padx=10, sticky="ew")

        boton_modificar_lista = tk.Button(self.ventana_alumno, text="Estadisticas", command=self.modificar_lista)
        boton_modificar_lista.grid(row=1, column=4, pady=5, padx=10, sticky="ew")

        boton_eliminar_lista = tk.Button(self.ventana_alumno, text="Eliminar\nEstudiante", command=self.eliminar_lista)
        boton_eliminar_lista.grid(row=2, column=4, pady=5, padx=10, sticky="ew")

        boton_salir = tk.Button(self.ventana_alumno, text="Salir", command=self.ventana_alumno.destroy, bg="red")
        boton_salir.grid(row=3, column=4, pady=5, padx=10, sticky="ew")

    def crear_lista(self):
        print("Crear lista")

    def modificar_lista(self):
        print("Modificar lista")

    def eliminar_lista(self):
        print("Eliminar lista")

    def configurar_tabla_lista(self):
        # Definir encabezados de columna
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("Modalidad", text="Modalidad")
        self.tabla.heading("Grupo", text="Grupo")
        self.tabla.heading("Turno", text="Turno")

        # Ajustar las columnas para que se expandan con el contenido
        for col in ("Modalidad", "Grupo", "Turno"):
            self.tabla.column(col, anchor="center", width=100)
            self.tabla.heading(col, text=col, anchor="center")

    def insertar_fila_ejemplo(self):
        self.tabla.insert(parent="", index="end", iid=1, text="1", values=("Primera opcion", "C", "Mañana"))

class VentanaAsistencia:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_asistencia = tk.Toplevel(self.ventana_principal.ventana)
        self.ventana_asistencia.title("Asistencia")
        self.ventana_asistencia.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")

        # Etiqueta
        etiqueta_codigo = tk.Label(self.ventana_asistencia, text="Código:")
        etiqueta_codigo.grid(row=0, column=0, pady=5, padx=10, sticky="e")
        entry_codigo = tk.Entry(self.ventana_asistencia)
        entry_codigo.config(width=25)
        entry_codigo.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

        # Botones
        boton_registrar_asistencia = tk.Button(self.ventana_asistencia, text="Registrar Asistencia", command=self.registrar_asistencia, width=20)
        boton_registrar_asistencia.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_modificar_asistencia = tk.Button(self.ventana_asistencia, text="Modificar Asistencia", command=self.modificar_asistencia, width=20)
        boton_modificar_asistencia.grid(row=2, column=0, columnspan=2,pady=5, padx=10)

        boton_eliminar_asistencia = tk.Button(self.ventana_asistencia, text="Eliminar Asistencia", command=self.confirmar_eliminar_asistencia, width=20)
        boton_eliminar_asistencia.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        #Boton buscar estudiante
        boton_buscar_estudiante = tk.Button(self.ventana_asistencia, text="Buscar", width=10)
        boton_buscar_estudiante.grid(row=0, column=5, pady=5)
        entry_buscar = tk.Entry(self.ventana_asistencia, width=30)
        entry_buscar.grid(row=0, column=4, columnspan=2, pady=5, padx=1, sticky=tk.W)

        # Botón para salir
        boton_salir = tk.Button(self.ventana_asistencia, text="Salir", command=self.ventana_asistencia.destroy, bg="red", width=20)
        boton_salir.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        # Tabla
        self.tabla_asistencia = ttk.Treeview(self.ventana_asistencia, columns=("Nombre", "Código", "Hora", "Estado", "Turno"))
        self.configurar_tabla_asistencia()
        self.insertar_fila_asistencia()
        self.tabla_asistencia.grid(row=1, column=2, columnspan=4, rowspan=5, pady=10, padx=10)

    def configurar_tabla_asistencia(self):
        # Definir encabezados de columna
        self.tabla_asistencia.heading("#0", text="ID")
        self.tabla_asistencia.heading("Nombre", text="Nombre")
        self.tabla_asistencia.heading("Código", text="Código")
        self.tabla_asistencia.heading("Hora", text="Hora")
        self.tabla_asistencia.heading("Estado", text="Estado")
        self.tabla_asistencia.heading("Turno", text="Turno")

        # Ajustar las columnas para que se expandan con el contenido
        for col in ("Nombre", "Código", "Hora", "Estado", "Turno"):
            self.tabla_asistencia.column(col, anchor="center", width=100)
            self.tabla_asistencia.heading(col, text=col, anchor="center")

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

class VentanaNotasEstudiante:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Notas de estudiante")
        ventana_alumno.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")

        # Botones
        boton_subir_notas = tk.Button(ventana_alumno, text="Subir notas",  width=20)
        boton_subir_notas.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_modificar_notas = tk.Button(ventana_alumno, text="Modificar nota", width=20)
        boton_modificar_notas.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

        texto_boton = "Promedios\ny\nCalificaciones"
        boton_promedios_calificaciones = tk.Button(ventana_alumno, text=texto_boton, width=20)
        boton_promedios_calificaciones.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        # Botón para salir
        boton_salir = tk.Button(ventana_alumno, text="Salir", command=ventana_alumno.destroy, bg="red", width=20)
        boton_salir.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

class VentanaListaEstudiantes:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Lista de estudiantes")
        ventana_alumno.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")

        # Botones
        boton_detalles_estudiante = tk.Button(ventana_alumno, text="Detalles de estudiante",  width=20)
        boton_detalles_estudiante.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

        boton_editar_informacion = tk.Button(ventana_alumno, text="Editar Informacion",  width=20)
        boton_editar_informacion.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

        boton_estadisticas_estudiante = tk.Button(ventana_alumno, text="Estadisticas de Estudiante",  width=20)
        boton_estadisticas_estudiante.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

        boton_eliminar_estudiante = tk.Button(ventana_alumno, text="Eliminar Estudiante", width=20)
        boton_eliminar_estudiante.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        boton_buscar_estudiante = tk.Button(ventana_alumno, text="Buscar", command=self.buscar_alumno , width=10)
        boton_buscar_estudiante.grid(row=0, column=6, pady=5)
        entry_buscar = tk.Entry(ventana_alumno, width=30)
        entry_buscar.grid(row=0, column=5, columnspan=2, pady=5, padx=1, sticky=tk.W)

        # Botón para salir
        boton_salir = tk.Button(ventana_alumno, text="Salir", command=ventana_alumno.destroy, bg="red", width=20)
        boton_salir.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        # Tabla
        tabla = ttk.Treeview(ventana_alumno, columns=("Nombre", "Código", "Promedio", "Deuda"))
        self.configurar_tabla_lista_estudiantes(tabla)
        self.insertar_fila_lista_estudiantes(tabla)
        tabla.grid(row=1, column=3, columnspan=4, rowspan=5, pady=10, padx=10)

    def configurar_tabla_lista_estudiantes(self, tabla):
        # Definir encabezados de columna
        tabla.heading("#0", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Código", text="Código")
        tabla.heading("Promedio", text="Promedio")
        tabla.heading("Deuda", text="Deuda")

        # Ajustar las columnas para que se expandan con el contenido
        for col in ("Nombre", "Código", "Promedio", "Deuda"):
            tabla.column(col, anchor="center", width=100)
            tabla.heading(col, text=col, anchor="center")

    def insertar_fila_lista_estudiantes(self, tabla):
        tabla.insert(parent="", index="end", iid=1, text="1", values=("Juan Jesus Ramirez Pimpinela", "ABC123", "10.39","Completa"))

    def buscar_alumno(self):
        print("Buscar alumno")

class VentanaConfiguracion:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Configuracion")
        ventana_alumno.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")
        color = "#D3D3D3"

        #Etiqueta de Inicio y fin de PO
        etiqueta_Inicio_y_FinPO = tk.Label(ventana_alumno, text="Ingrese Inicio y Fin de ciclo de PO:", bg="gray")
        etiqueta_Inicio_y_FinPO.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Agregar el Checkbutton para habilitar/deshabilitar las fechas
        self.estado_PO = tk.BooleanVar()
        self.estado_PO.set(False)
        toggle_buttonPO = ttk.Checkbutton(ventana_alumno, text="Habilitar Ciclo PO", variable=self.estado_PO, command=self.Ciclo_PO)
        toggle_buttonPO.grid(row=1, column=0, pady=10)

        # Agregar la etiqueta de Estado
        self.etiqueta_estadoPO = tk.Label(ventana_alumno, text="Estado:")
        self.etiqueta_estadoPO.grid(row=1, column=2, pady=10)
        self.etiqueta_estadoPO_accion = tk.Label(ventana_alumno, text="Terminado", fg="red")
        self.etiqueta_estadoPO_accion.grid(row=1, column=2, columnspan=2, pady=10)

        #Establecer fecha de inicio y fin de ciclo Primera Opcion
        etiqueta_InicioPO = tk.Label(ventana_alumno, text="Fecha de Inicio:", bg=color)
        etiqueta_InicioPO.grid(row=2, column=0, sticky=tk.E, padx=5)
        self.entry_InicioPO = DateEntry(ventana_alumno, date_pattern="dd/mm/yyyy")
        self.entry_InicioPO.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        self.entry_InicioPO.config(state="disabled")

        etiqueta_FinPO = tk.Label(ventana_alumno, text="Fecha de Finalizacion:", bg=color)
        etiqueta_FinPO.grid(row=2, column=2, sticky=tk.E, padx=5)
        self.entry_FinPO = DateEntry(ventana_alumno, date_pattern="dd/mm/yyyy")
        self.entry_FinPO.grid(row=2, column=3, pady=5, padx=5, sticky=tk.W)
        self.entry_FinPO.config(state="disabled")

        #Etiqueta de Inicio y fin de PO
        etiqueta_Inicio_y_FinORD = tk.Label(ventana_alumno, text="Ingrese Inicio y Fin de ciclo de ORD:", bg="gray")
        etiqueta_Inicio_y_FinORD.grid(row=3, column=0, columnspan=4, pady=10, sticky="ew")

        # Agregar el Checkbutton para habilitar/deshabilitar las fechas
        self.estado_ORD = tk.BooleanVar()
        self.estado_ORD.set(False)
        toggle_buttonORD = ttk.Checkbutton(ventana_alumno, text="Habilitar Ciclo ORD",  variable=self.estado_ORD, command=self.Ciclo_ORD)
        toggle_buttonORD.grid(row=4, column=0, pady=10)

        # Agregar la etiqueta de Estado
        self.etiqueta_estadoORD = tk.Label(ventana_alumno, text="Estado:")
        self.etiqueta_estadoORD.grid(row=4, column=2, pady=10)
        self.etiqueta_estadoORD_accion = tk.Label(ventana_alumno, text="Terminado", fg="red")
        self.etiqueta_estadoORD_accion.grid(row=4, column=2, columnspan=2, pady=10)

        #Establecer fecha de inicio y fin de ciclo Ordinario
        etiqueta_InicioORD = tk.Label(ventana_alumno, text="Fecha de Inicio:", bg=color)
        etiqueta_InicioORD.grid(row=5, column=0, sticky=tk.E, padx=5)
        self.entry_InicioORD = DateEntry(ventana_alumno, date_pattern="dd/mm/yyyy")
        self.entry_InicioORD.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)
        self.entry_InicioORD.config(state="disabled")

        etiqueta_FinORD = tk.Label(ventana_alumno, text="Fecha de Finalizacion:", bg=color)
        etiqueta_FinORD.grid(row=5, column=2, sticky=tk.E, padx=5)
        self.entry_FinORD = DateEntry(ventana_alumno, date_pattern="dd/mm/yyyy")
        self.entry_FinORD.grid(row=5, column=3, pady=5, padx=5, sticky=tk.W)
        self.entry_FinORD.config(state="disabled")

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


        #fechas de ciclo
        #horarios

interfaz = Interfaz()
