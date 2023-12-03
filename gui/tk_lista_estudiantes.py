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