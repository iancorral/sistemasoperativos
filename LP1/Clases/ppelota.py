class Persona:

    def __init__(self,nombre):
        self.nombre=nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self,nombre):
        if not isinstance(nombre,(str)):
            raise ValueError("Nombre debe ser un texto")
        self.__nombre=nombre    
    
    def caminar(self):
        print(self.nombre, "esta caminando")
    
    def jugar(self,pelota):
        if not isinstance(pelota,Pelota):
            raise ValueError("No es una Pelota")
        print("Esta jugando con la pelota")
        print(f"{self.nombre} esta {pelota.botar()}")
    
    def __str__(self):
        return {f"{self.nombre}"}
    
class Pelota:
    def __init__(self,color):
        self.color=color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        if not isinstance (color,str):
            raise ValueError("Color debe ser un texto")
    
    def botar(self):
        print("Botando la pelota")

    def __str__(self):
        return f"Color de pelota {self.color}"

def main():
    persona=Persona("Ian")
    print(persona)
    

