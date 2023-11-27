class Pet:
    def __init__(self,nombre="tom",tanimal="PERRO",edad=5):
        self.nombre=nombre
        self.edad=edad
        self.tanimal=tanimal

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        if not isinstance(nombre,(str)):
            raise ValueError("nombre debe ser un texto")
        self.__nombre=nombre

    @property
    def tanimal(self):
        return self.__tanimal
    
    @tanimal.setter
    def tanimal(self,tanimal):
        tipo=["PAJARO","PERRO","GATO"]
        if not isinstance(tanimal,(str)):
            raise ValueError("el tipo de animal debe ser un texto")
        if tanimal.upper() not in tipo:
            raise ValueError("Tu tipo de animal no esta dentro de la lista: [Pajaro,Gato,Perro] ")
        self.__tanimal=tanimal

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad (self,edad):
        if not isinstance(edad,(int,float)):
            raise ValueError("Edad debe ser un numero")
        if edad<0:
            raise ValueError("Edad debe ser mayor a 0")
        self.__edad=edad

    def __str__(self):
        return f"PET: [{self.nombre},{self.tanimal},{self.edad}]"