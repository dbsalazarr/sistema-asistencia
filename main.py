from clases.CPersonal import Personal
from interfaz.main_interfaz import Interfaz

def main() :
    trabajador1 = Personal()
    trabajador1.registrar_personal()
    interfaz = Interfaz()

if __name__ == "__main__" :
    main()

