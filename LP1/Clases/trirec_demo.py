from trirec import Triangulo

def main():
        base=int(input(f"Base del triangulo: "))
        altura=int(input(f"Altura del triangulo: "))
        t1=Triangulo(base,altura)
        print(t1)
        print("El area total es: ",round(t1.get_area(),2))
        print("La hipotenusa es: ",round (t1.get_hipotenusa(),2))
main()