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