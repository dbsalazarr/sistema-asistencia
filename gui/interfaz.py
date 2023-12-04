import tkinter as tk
from os.path import abspath, dirname, join

icon_path = join(join(dirname(dirname(abspath(__file__))), "media"), "principal.ico")


class Interfaz :    
    def __init__(self, title, window_size, icon_path) :
        self.title = title
        self.window_size = window_size
        self.icon_path = icon_path