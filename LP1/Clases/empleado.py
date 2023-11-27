
class Empleado:
    def __init__(self,nombre="omar",horast=1,sueldo=100):
        self.nombre=nombre
        self.horast=horast
        self.sueldo=sueldo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self,nombre):
        if not isinstance(nombre,(str)):
            raise ValueError("Nombre debe ser un texto")
        self.__nombre=nombre

    @property
    def horast(self):
        return self.__horast
    
    @horast.setter
    def horast (self,horast):
        if not isinstance(horast,(int,float)):
            raise ValueError("Horas debe ser un numero")
        if horast<0:
            raise ValueError("Horas debe ser mayor a 0")
        self.__horast=horast

    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo (self,sueldo):
        if not isinstance(sueldo,(int,float)):
            raise ValueError("Sueldo debe ser un numero")
        if sueldo<0:
            raise ValueError("Sueldo debe ser mayor a 0")
        self.__sueldo=sueldo

    def __str__(self):
        return f"Empleado: [Nombre: {self.nombre} | Horas trabajadas:{self.horast} | Sueldo: {self.sueldo}]"
    
    def get_sueldo(self):
        return (self.horast*self.sueldo)