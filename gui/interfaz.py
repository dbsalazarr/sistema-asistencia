import tkinter as tk
from os.path import abspath, dirname, join


class Interfaz:
    def __init__(self, title='', window_size='768x480', icon_path='', config='', resizable=True):
        self._title = title
        self._window_size = window_size
        self._icon_path = self.get_icon_path(icon_path)
        self._config = config # Diccionario
        self._resizable = resizable # Tupla True, True
        

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, nuevo_title):
        self._title = nuevo_title

    @property
    def window_size(self):
        return self._window_size

    @window_size.setter
    def window_size(self, nuevo_window_size):
        self._window_size = nuevo_window_size

    @property
    def icon_path(self):
        return self._icon_path

    @icon_path.setter
    def icon_path(self, nuevo_icon_path):
        self._icon_path = self.get_icon_path(nuevo_icon_path)

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, nueva_config):
        self._config = nueva_config

    @property
    def resizable(self):
        return self._resizable

    @resizable.setter
    def resizable(self, nuevo_resizable):
        self._resizable = nuevo_resizable

    def get_icon_path(self, icon_name) :
        path = join(join(dirname(dirname(abspath(__file__))), "media"), icon_name)
        return path
    
    def start(self) :
        ventana = tk.Tk()
        dd = self.get_display_size()
        print(dd['width'])
        print(dd['height'])
        ventana.geometry(self._window_size+F"+{dd['width']//2 - 384}+{dd['height']//2 - 240}")
        ventana.iconbitmap(self._icon_path)
        ventana.config(self._config)
        ventana.resizable(self._resizable, self._resizable)
        
        ventana.mainloop()
    
    def get_display_size(self) :
        root = tk.Tk()
        display_width = root.winfo_screenwidth()
        display_height = root.winfo_screenheight()
        root.destroy()
        return {
            'width' : display_width,
            'height' : display_height
        }
        

    # Métodos de clase
    # TODO : Generar una función que retorne la ruta de un archivo (media) a utilizar, debe recibir como parámetro el nombre del archivo a traer (Se puede crear en el método get de la propiedad icon_path)

inter1 = Interfaz(icon_path="principal.ico", config={})
print(inter1.window_size)
print(inter1.resizable)
inter1.start()