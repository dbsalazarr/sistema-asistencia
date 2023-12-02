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