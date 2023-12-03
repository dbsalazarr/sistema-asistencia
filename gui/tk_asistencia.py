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