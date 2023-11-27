class Policia:
    def __init__(self,nombre,pistola):
        self.nombre=nombre
        self.pistola=pistola #_______AGREGACION DE PISTOLA

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un str")
        self.__nombre=nombre
    
    @property
    def pistola(self):
        return self.__pistola
    @pistola.setter
    def pistola(self,pistola):
        if not isinstance(pistola, Pistola): #__________AGREGACIÓN DE PISTOLA
            raise ValueError("Objeto debe de ser Pistola")
        self.__pistola=pistola 
    
    def manejar(self,motocicleta):
        if not isinstance (motocicleta,Motocicleta):
            raise ValueError("El objeto debe de ser Motocicleta ")
        print(f"{self.nombre} esta: ")     #_________ASOSIACIÓN DE MOTO
        motocicleta.arrancar()
        
    def __str__(self): #_____AGREGACION
        return f"El policía {self.nombre}, usa la pistola {self.pistola}"

class Pistola:
    def __init__(self,modelo):
        self.modelo=modelo

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,modelo):
        if not isinstance(modelo,str):
            raise ValueError("La pistola debe ser un str")
        self.__modelo=modelo

    def __str__(self):
        return f"{self.modelo}"

class Motocicleta: 
    def __init__(self,gasolina,modelo,modelo_motor="FT200"):
        self.gasolina=gasolina
        self.modelo=modelo
        self.__motor=Motor(modelo_motor) #_________COMPOSICIÓN DE MOTOR

    @property
    def gasolina(self):
        return self.__gasolina
    
    @gasolina.setter
    def gasolina(self,gasolina):
        if not isinstance(gasolina,int):
            raise ValueError ("La gasolina debe ser un número")
        if gasolina<0:
            raise ValueError("La gasolina debe de ser mayor de 0")
        self.__gasolina=gasolina
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,modelo):
        if not isinstance(modelo,str):
            raise ValueError("El modelo debe de ser str")
        self.__modelo=modelo

    def arrancar(self) : #_________ASOCIACION
        print (f"Arrancando...{self.modelo} ")
        
    def __str__(self):
        return (f"La moto {self.modelo} tiene {self.gasolina} litros de gas y un motor {self.__motor}")

class Motor: 
    def __init__(self,modelo_motor):
        self.modelo_motor=modelo_motor

    @property
    def modelo_motor(self):
        return self.__modelo_motor
    
    @modelo_motor.setter
    def modelo_motor(self,modelo_motor):
        if not isinstance (modelo_motor, (str)) :
            raise ValueError ("El modelo del motor debe ser un str")
        self.__modelo_motor = modelo_motor
    
    def __str__ (self) :
        return (f"{self.modelo_motor}")

def main():
    
    pistola=Pistola("Colt Python")
    policia=Policia("Hernandez",pistola) #___AGREGACION
    
    print(policia)

    moto=Motocicleta(35,"ITALIKA") #_____ASOCIACION
    policia.manejar(moto)

    print(moto)
    print("Modelo de pistola:",pistola)
    
main()


















#COMPOSICIÓN va dentro del init y no se ocupa property ni setter
#AGREGACIÓN va dentro del setter como un parámetro para una propiedad de init
#ASOSIACIÓN va dentro de una función y no se incluye en el init 