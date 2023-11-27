class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("nombre debe ser cadena")
        self.__nombre = nombre

    def caminar(self):
        pass

    def jugar(self, pelota):
        if not isinstance(pelota, Pelota):
            raise ValueError("Objeto debe ser Pelota")
        
        print("Jugando con la pelota")
        print(f"{self.nombre} está {pelota.botar()}")

    def __str__(self):
        return f"{self.nombre}"


class Pelota:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise ValueError("color debe ser cadena")
        self.__color = color

    def botar(self):
        return f"Botando la pelota {self.color}"

    def __str__(self):
        return f"Pelota {self.color}"

def main():
    pelota = Pelota("verde")
    maria = Persona("María")
    maria.jugar(pelota)
   
if __name__ == "__main__":
    main()