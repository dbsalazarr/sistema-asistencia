class VentanaMatricula:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_alumno = tk.Toplevel(self.ventana_principal.ventana)
        ventana_alumno.title("Matricular alumno")
        ventana_alumno.iconbitmap("D:\\Personal\\TRABAJOS\\Python trabajos\\secundario.ico")
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