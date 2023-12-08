import tkinter as tk
import ctypes
from os.path import abspath, dirname, join


class Interfaz :
   

    def __init__(self, title='', w_width='768', w_height='480', w_x='', w_y='', icon_path='', config='', resizable=True):
        self._title = title
        self._w_width = w_width
        self._w_height = w_height
        
        self._icon_path = self.get_icon_path(icon_path)
        self._config = config # Diccionario
        self._resizable = resizable # Tupla True, True
        
        # Recuperar las dimensiones del monitor utilizado
        self._d_width, self._d_height = self.get_display_size()
        # 
        self._w_x =  w_x or self.center_window(self._d_width, self._w_width)
        self._w_y = w_y or self.center_window(self._d_height, self._w_height)
        
    def center_window(self, display_size, window_size) :
        return (int(display_size)-int(window_size))//2

    def get_icon_path(self, icon_name) :
        path = join(join(dirname(dirname(abspath(__file__))), "media"), icon_name)
        return path
    
    def start(self) :
        ventana = tk.Tk()
        dd = self.get_display_size()

        ventana.geometry(f"{self._w_width}x{self._w_height}+{self._w_x}+{self._w_y}")
        # ventana.geometry(f"{self._w_width}x{self._w_height}")


        ventana.iconbitmap(self._icon_path)
        ventana.config(self._config)
        ventana.resizable(self._resizable, self._resizable)
        
        ventana.mainloop()

    def get_display_size(self) :
        root = tk.Tk()
        root.withdraw()
        root.iconbitmap(self._icon_path)
        display_width = root.winfo_screenwidth()
        display_height = root.winfo_screenheight()
        root.destroy()
        return display_width, display_height
    

    # Métodos de clase
    # TODO : Generar una función que retorne la ruta de un archivo (media) a utilizar, debe recibir como parámetro el nombre del archivo a traer (Se puede crear en el método get de la propiedad icon_path)

inter1 = Interfaz(icon_path="principal.ico", config={})
inter1.start()
print( inter1._d_width)
print( inter1._d_height)