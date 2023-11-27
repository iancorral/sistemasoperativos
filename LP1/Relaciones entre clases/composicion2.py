import datetime
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x debe ser un número")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y debe ser un número")
        self.__y = y

    def __str__(self):
        return f"Point2D [{self.x},{self.y}]"
    
class Circulo:
    def __init__(self, radio=1, x = 0, y = 0):
        self.radio = radio
        self.__centro = Point2D(x, y)
        self.__create = datetime.datetime.now()

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        if not (isinstance(radio, (int, float)) and radio > 0):
            raise ValueError(f"radio debe ser número positivo -> {radio}")
        self.__radio = radio

    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Radio[radio={self.radio}, create={self.__create} centro={self.__centro}]"

def main():
    c1 = Circulo(3, 5,5)
    print("Radio = ", c1.radio)
    print("Area = ", c1.get_area())
    print("str = ",c1)

main()