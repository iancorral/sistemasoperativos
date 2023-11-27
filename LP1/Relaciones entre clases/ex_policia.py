class Motor:
    def __init__(self, cilindros=2):
        self.cilindros = cilindros

    @property
    def cilindros(self):
        return self.__cilindros

    @cilindros.setter
    def cilindros(self, cilindros):
        if not isinstance(cilindros, int):
            raise TypeError("cilindros debe ser un entero")
        if cilindros<0 or cilindros > 12:
            raise ValueError("cilindros debe ser mayor a cero y menor igual a 12")
        self.__cilindros = cilindros

    def arrancar(self):
        return "run run run"

class Motocicleta:
    def __init__(self, modelo="Yamaha"):
        self.modelo = modelo
        self.__motor = Motor(2)

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        if not isinstance(modelo, str):
            raise TypeError("modelo debe ser una cadena")
        self.__modelo = modelo
    
    def arrancar_motocicleta(self):
        print(self.__motor.arrancar())

    def __str__(self):
        return (f"Modelo Motocicleta: {self.modelo}, Cilindros: {self.__motor.cilindros}")

class Pistola:
    def __init__(self, calibre):
        self.calibre = calibre

    @property
    def calibre(self):
        return self.__calibre

    @calibre.setter
    def calibre(self, calibre):
        if not isinstance(calibre, int):
            raise TypeError("calibre debe ser un entero")
        if calibre<0:
            raise ValueError("calibre debe ser mayor a cero")
        self.__calibre = calibre        

    def cargar(self):
        return "Cargando balas..."
        
    def disparar(self):
        return "Bang, bang, ....."

    def __str__(self):
        return f"Pistola calibre: {self.calibre}"
    
class Policia:
    def __init__(self, nombre, pistola):
        self.nombre = nombre
        self.pistola = pistola
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser un str")
        self.__nombre = nombre

    @property
    def pistola(self):
        return self.__pistola

    @pistola.setter
    def pistola(self, pistola):
        if not isinstance(pistola, Pistola):
            raise TypeError("El objeto debe ser Pistola")
        self.__pistola = pistola

    def manejar(self, moto):
        if not isinstance(moto, Motocicleta):
            raise TypeError("Objeto debe ser Motocicleta")
        print(f"Manejando la motocicleta: {moto}")
        print("Arrancando la Motocicleta")
        moto.arrancar_motocicleta()
        
    def __str__(self):
        return f"Policia: {self.nombre} Pistola: {self.pistola}"
    
def main():
    # Composición
    print("Creando un objeto Motocicleta")
    moto = Motocicleta()
    moto.arrancar_motocicleta()
    print(moto)

    # Agregación
    print("\n\nCreando objetos Policía y Pistola")
    p = Pistola(22)
    poli1 = Policia("Ramirez", p)
    print(poli1.pistola.cargar())
    print(poli1.pistola.disparar())
    print(poli1)

    # Asociación
    print("\n\nAsociación")
    poli1.manejar(moto)

main()
