class Robot:
    contador=0 #variable de clase, pues esta fuera de la funcion
    def __init__(self,nombre):
        self.nombre=nombre
        Robot.contador +=1
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        if not(isinstance(nombre,str)):
            raise ValueError("Nombre debe ser texto")
        self.__nombre=nombre

    def __str__(self):
        return f"Robot: [{self.nombre}]"