import tkinter as tk
from tkinter import messagebox
from os.path import abspath, dirname, join


from CCargo import Cargo

# global variables
icon_path = join(dirname(dirname(abspath(__file__))), "media" ) + "\principal.ico"

# Funciones para los botones
def show_message():
    pass

def registrar_cargo():
    cargo1 = Cargo()
    nombre_cargo = txt_cargo.get()
    nivel_acceso = txt_nivel_acceso.get()
    cargo1.registrar_cargo(nombre_cargo, nivel_acceso)
    messagebox.showinfo("Mensaje", "Registro agregado correctamente")

def eliminar_cargo() :
    cargo1 = Cargo()
    cargo1.eliminar_cargo()
    lbl_last_id.config(text=f"Ahora el ultimo id es: {cargo1.ultimo_id() }")

ventana = tk.Tk()
ventana.geometry("768x480")
ventana.title("Registrar Cargo")
ventana.iconbitmap(icon_path)

# Crear una etiqueta
lbl_cargo = tk.Label(ventana, text="Ingrese el nombre del Cargo")
lbl_cargo.pack()

# Agregando un campo de texto
txt_cargo = tk.Entry(ventana)
txt_cargo.pack()

# Campos para el nivel de acceso

lbl_nivel_acceso = tk.Label(ventana, text="Defina el nivel de Acceso")
lbl_nivel_acceso.pack()

# Agregando un campo de texto
txt_nivel_acceso = tk.Entry(ventana)
txt_nivel_acceso.pack()
# Crear el botón de registro
lbl_last_id = tk.Label(ventana, text="")
lbl_last_id.pack()

btn_registrar_cargo = tk.Button(ventana, text="Registrar Cargo", command=registrar_cargo)
btn_registrar_cargo.pack()

btn_eliminar_cargo = tk.Button(ventana, text="Eliminar Cargo", command=eliminar_cargo)
btn_eliminar_cargo.pack()

ventana.mainloop()