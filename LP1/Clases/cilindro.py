#cilindro.py
import math

class Cilindro:
    def __init__(self,altura=4,radio=2):
        self.altura=altura
        self.radio=radio

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura (self,altura):
        if not isinstance(altura,(int,float)):
            raise ValueError("Altura debe ser un numero")
        if altura<0:
            raise ValueError("Altura debe ser mayor a 0")
        self.__altura=altura

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio (self,radio):
        if not isinstance(radio,(int,float)):
            raise ValueError("Radio debe ser un numero")
        if radio<0:
            raise ValueError("Radio debe ser mayor a 0")
        self.__radio=radio

    def get_area_base(self):
        return (((self.radio)**2)*(math.pi))
    def get_area_lateral(self):
        return (((2*math.pi)*(self.radio))*(self.altura))
    def get_area_total(self):
        return (((2*math.pi)*(self.radio))*(self.altura+self.radio))
    def get_volumen(self):
        return ((((self.radio)**2)*(math.pi))*(self.altura))
    def __str__(self):
        return f"Cilindro: [{self.altura},{self.radio}]"