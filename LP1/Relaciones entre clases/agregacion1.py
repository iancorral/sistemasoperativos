class Persona:
    def __init__(self, nombre, celular):
        self.nombre = nombre
        self.celular = celular

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("nombre debe ser cadena")
        self.__nombre = nombre

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        if not isinstance(celular, Celular):
            raise ValueError("Objeto debe ser celular")
        self.__celular = celular 
        
    def caminar(self):
        pass

    def __str__(self):
        return f"{self.nombre}, tiene un celular {self.celular.modelo}"


class Celular:
    def __init__(self, modelo):
        self.modelo = modelo

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        if not isinstance(modelo, str):
            raise ValueError("modelo debe ser cadena")
        self.__modelo = modelo

    def marcar(self, numero):
        print (f"Marcanco número: {numero}")

    def mensaje(self, mensaje):
        print (f"Enviando mensaje: {mensaje}")

    def __str__(self):
        return f"Celular {self.modelo}"

def main():
    samsung = Celular("Samsung X20")
    maria = Persona("Maria", samsung)

    print("Nombre:", maria.nombre)
    print("Celular:", maria.celular.modelo)
    maria.celular.mensaje("Hola")
    maria.celular = Celular("Nokia 2022")
    print(maria)

if __name__ == "__main__":
    main()