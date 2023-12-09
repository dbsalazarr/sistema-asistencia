from CInterfaz import Interfaz



"""
   La clase debe retorna una objeto ventana, con la cual se pueda trabajar 
"""
interfaz = Interfaz(title="Lista de estudiantes matriculados", w_width="1024", w_height=768, icon_path="principal.ico")

# * VENTANA CREADA ACTUALMENTE
main = interfaz.start()

interfaz.entry_text("Botón agregado")




interfaz.show_window()
