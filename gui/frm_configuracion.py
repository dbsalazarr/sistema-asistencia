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