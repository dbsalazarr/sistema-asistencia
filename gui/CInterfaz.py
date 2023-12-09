import tkinter as tk
from os.path import abspath, dirname, join


class Interfaz :

    def __init__(self, title='', w_width='768', w_height='480', w_x='', w_y='', icon_path='', config={}, resizable=True):

        self._window = tk.Tk()
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

    def get_icon_path(self, image_name) :
        """
            Recupera el directorio hasta la carpeta media y concatena a tal ruta el nombre de la imagen a utilizar en la interfaz
            Args : 
                image_name (str) : Es el nombre de la imagen con sus extensión
            Returns :
                (str) : Retorna la ruta de la imagen indicada (debe encontrarse en la carpeta media del proyecto)
        """
        path = join(join(dirname(dirname(abspath(__file__))), "media"), image_name)
        return path
    
    def start(self) :

        ventana = self._window
        ventana.title(self._title)
        ventana.iconbitmap(self._icon_path)
        ventana.geometry(f"{self._w_width}x{self._w_height}+{self._w_x}+{self._w_y}")
        ventana.config(self._config)
        ventana.resizable(self._resizable, self._resizable)

        return ventana
        
    def show_window(self) :
        self._window.mainloop()

    def get_display_size(self) :
        root = tk.Tk()
        root.withdraw()
        display_width = root.winfo_screenwidth()
        display_height = root.winfo_screenheight()
        root.destroy()
        return display_width, display_height
    
    def entry_text(self, text_input="boton", config_input={}) :
        input_text = tk.Entry(self._window, text=text_input)
        input_text.configure( config_input)
        input_text.pack()
    
