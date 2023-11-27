import ulsa

def main():
    color=input("color del cuadrado: ")
    lado=float(input("lado del cuadrado: "))

    c=ulsa.Cuadrado(color,lado)

    print(c)
    print("El area es: ",c.get_area())
    print("El perimetro es: ",c.get_perimetro())

    lado=float(input("Nuevo valor del lado: "))
    c.lado=lado

    print(c)
    print("El area es: ",c.get_area())
    print("El perimetro es: ",c.get_perimetro())

main()