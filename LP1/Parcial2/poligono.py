import math

class PoligonoRegular:

    def __init__(self,n=3,lado=1, cx=0, cy=0):
        self.n=n
        self.lado=lado
        self.cx=cx
        self.cy=cy
        
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self,n):
        if not isinstance(n,(int,float)):
            raise ValueError("El número de lados debe ser un numero")
        if n<0:
            raise ValueError("El número de lados debe ser mayor a 0")
        self.__n=n

    @property
    def lado(self):
        return self.__lado
    
    @lado.setter
    def lado(self,lado):
        if not isinstance(lado,(int,float)):
            raise ValueError("La medida de el lado debe ser un numero")
        if lado<0:
            raise ValueError("La medida del lado debe ser mayor a 0")
        self.__lado=lado
    
    @property
    def cx(self):
        return self.__cx
    
    @cx.setter
    def cx(self,cx):
        if not isinstance(cx,(int,float)):
            raise ValueError("La coordenada en x debe ser un numero")
        if cx<0:
            raise ValueError("La coordenada en x debe ser mayor a 0")
        self.__cx=cx
    
    @property
    def cy(self):
        return self.__cy
    
    @cy.setter
    def cy(self,cy):
        if not isinstance(cy,(int,float)):
            raise ValueError("La coordenada en y debe ser un numero")
        if cy<0:
            raise ValueError("La coordenada en y debe ser mayor a 0")
        self.__cy=cy

    def get_perimetro(self):
        return (self.n)*(self.lado)
    
    def get_area(self):
        return ((self.n)*(self.lado**2))/(4)*(math.tan(math.pi/self.n))

    def __str__(self):
        return f"Poligono: [Número de lados: {self.n} | Medida de lado: {self.lado} | Coordenada en x: {self.cx} | Coordenada en y: {self.cy}]"
    