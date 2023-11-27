import datetime

class Celular:
    def __init__(self, marca="Samsung", aplicacion="Instagram"):
        self.marca = marca
        self.aplicacion = aplicacion
        self.__hf=datetime.datetime.now()

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        if not isinstance(marca, str):
            raise ValueError("marca debe ser cadena")
        self.__marca = marca

    @property
    def aplicacion(self):
        return self.__aplicacion

    @aplicacion.setter
    def aplicacion(self, aplicacion):
        if not isinstance(aplicacion, Aplicacion):
            raise ValueError("Objeto debe ser aplicacion")
        self.__aplicacion = aplicacion
    
    def on(self):
        print("Prendiendo el celular...")
        
    def off(self):
        print("Apagando el celular...")
        
    def __str__(self):
        return f"Usted esta utilizando la aplicación de: {self.aplicacion.nombre}, con su celular marca: {self.marca}, el día y hora: {self.__hf}"
        
class Aplicacion:
    def __init__(self, nombre="Instagram"):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("nombre debe ser cadena")
        self.__nombre = nombre
        
    def estado(self,texto):
        print (f"Subiendo un estado: {texto}")
    
    def __str__ (self) :
        return self.nombre

def main():
    app=Aplicacion("Facebook")
    cel= Celular("Iphone",app)
    cel.on()
    print(cel)
    cel.aplicacion.estado("Aquí de vacaciones :)")
    cel.off()
    
main()