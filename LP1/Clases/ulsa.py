#ulsa.py
import random

class Auto:
    def __init__(self,marca="seat", color="Blanco",gasolina=20):
        self.marca=marca
        self.color= color
        self.gasolina= gasolina


    def get_marca(self):
        return self.__marca
    def set_marca(self,marca):
        if not isinstance (marca,(str)):
            raise ValueError("Marca debe ser un texto")
        self.__marca=marca

    def get_color(self):    
        return self.__color
    def set_marca(self,color):
        if not isinstance (color,(str)):
            raise ValueError("Marca debe ser un texto")
        self.__color=color

    @property
    def gasolina(self):
        return self.__gasolina
    @gasolina.setter
    def gasolina(self,gasolina):
        if not isinstance (gasolina,(int)):
            raise ValueError("Gasolina debe ser un número entero")
        if gasolina<0 or gasolina>40:
            raise ValueError("Gasolina debe estar entre 0 y 40")
        self.__gasolina=gasolina

        
    def arrancar(self):
        print("Arrancando auto...")
    def frenar(self):
        print("Frenando auto...")
    def musica(self,cancion):
        print("Play: ",cancion)
    def get_pasajeros(self):
        return random.randint(1,6)
    def dibujar(self):
        print("-----[]----")
        print("0         0")
    
class Cuadrado:
    def __init__(self,color="Negro",lado=1):
        self.color=color
        self.lado=lado
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        if not isinstance(color,(str)):
            raise ValueError("color debe ser un str")
        self.__color=color
    @property
    def lado(self):
        return self.__lado
    @lado.setter
    def lado (self,lado):
        if not isinstance(lado,(int,float)):
            raise ValueError("Lado debe ser un numero")
        if lado<0:
            raise ValueError("Lado debe ser mayor a 0")
        self.__lado=lado

    def get_area(self):
        return self.lado**2
    def get_perimetro(self):
        return self.lado*4
    def __str__(self):
        return f"Cuadrado: [{self.color},{self.lado}]"





IVA= 0.16
meses= ["Enero","Febrero","Marzo"]

def suma(a,b):
    return a + b

class Pelota:
    pass