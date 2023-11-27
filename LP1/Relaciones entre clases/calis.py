import datetime

class Celular :

    def __init__ (self, marca, aplicacion) :
        self.marca = marca
        self.aplicacion = aplicacion
        self.fecha = datetime.datetime.now ()

    @property
    def marca (self) :
        return self.__marca
    
    @marca.setter
    def marca (self, marca) :
        if not isinstance (marca, str):
            raise ValueError ("Marca debe ser una cadena")
        self.__marca = marca

    @property
    def aplicacion (self) : 
        return self.__aplicacion

    @aplicacion.setter
    def aplicacion (self, aplicacion) :
        if not isinstance (aplicacion, Aplicacion) :
            raise ValueError ("Aplicacion debe ser una instancia de Aplicacion")
        self.__aplicacion = aplicacion

    def encender (self) :
        print (f"Encendiendo el celular {self.marca}")

    def apagar (self) :
        print (f"Apagando el celular {self.marca}")

    def informar (self) :
        print (f"La fecha es: {self.fecha}")

    def _str_ (self) :
        return self.marca
    
class Aplicacion :

    def __init__ (self, nombre) :
        self.nombre = nombre

    @property
    def nombre (self) :
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nombre) :
        if not isinstance (nombre, str) :
            raise ValueError ("Nombre debe ser cadena")
        self.__nombre = nombre

    def obtener_info (self) :
        return f"Usando aplicación: {self.nombre}"

    def _str_ (self) :
        return self.nombre


def main_Agregacion ():
    app = Aplicacion ("WhatsApp")
    celular = Celular ("Samsung", app)
    celular.encender ()
    print (celular.aplicacion.obtener_info()) #AGREGACIÓN
    celular.apagar()

main_Agregacion ()

def main_composicion () :

    app = Aplicacion ("WhatsApp")
    celular = Celular ("Samsung", app)
    celular.informar ()

main_composicion ()