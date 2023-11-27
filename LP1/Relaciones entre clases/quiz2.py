class Computadora:
    def __init__(self, marca="Sony", teclado="Ingles"):
        self.marca = marca
        self.teclado = teclado

    @property
    def marca(self):
        return self.__marca
        
    @marca.setter
    def marca(self, marca):
        if not isinstance(marca, str):
            raise TypeError("marca debe ser texto")
        self.__marca = marca

    @property
    def teclado(self):
        return self.__teclado
        
    @teclado.setter
    def teclado(self, teclado):
        if not isinstance(teclado, Teclado):
            raise TypeError("Objeto debe ser teclado")
        self.__teclado = teclado
    
    def on(self):
        print("Prendiendo la computadora...")
        
    def off(self):
        print("Apagando la computadora...")
        

    def __str__(self):
        return f"La computadora marca {self.marca}, tiene un teclado configurado con el idioma {self.teclado.idioma}"
        
    
class Teclado:
    def __init__(self, idioma="Español"):
        self.idioma = idioma

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, idioma):
        if not isinstance(idioma, str):
            raise ValueError("idioma debe ser cadena")
        self.__idioma = idioma
        
    def escribir(self,texto):
        print (f"Escribiendo un saludo: {texto}")

def main():
    teclado=Teclado("Español")
    pc = Computadora("MSI",teclado)
    pc.on()
    pc.teclado.escribir("Buenos días")
    print(pc)
    pc.off()
    
main()