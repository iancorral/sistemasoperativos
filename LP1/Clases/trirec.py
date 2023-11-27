import math

class Triangulo:

    def __init__(self,altura=1,base=1):
        self.altura=altura
        self.base=base

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
    def base(self):
        return self.__base
    
    @base.setter
    def base (self,base):
        if not isinstance(base,(int,float)):
            raise ValueError("Base debe ser un numero")
        if base<0:
            raise ValueError("Base debe ser mayor a 0")
        self.__base=base

    def get_area(self):
        return((self.base*self.altura))/2
    def get_hipotenusa(self):
        return (math.tan(self.base**2 + self.altura**2))
    def __str__(self):
        return f"Triangulo rectangulo: [Altura: {self.altura} | Base:{self.base}]"