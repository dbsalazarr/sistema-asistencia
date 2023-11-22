class Persona : 
    def __init__(self, nombre, apellido_paterno, apellido_materno, DNI) :
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self._DNI = DNI    
    
    # SETTERS AND GETTERS
    @property
    def nombre (self) : 
        return self.nombre
    
    @nombre.setter
    def set_base(self, new_nombre) :
        self.nombre = new_nombre
    
