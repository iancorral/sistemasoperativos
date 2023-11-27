import cilindro

def main():
    altura=float(input("Altura del cuadrado: "))
    radio=float(input("Radio del cuadrado: "))

    c=cilindro.Cilindro(altura,radio)

    print(c)
    print("El area total es: ",round(c.get_area_total(),2))
    print("El volumen es: ",round (c.get_volumen(),2))

    altura=float(input("Nuevo valor del altura: "))
    c.altura=altura

    print(c)
    print("El area total es: ",round(c.get_area_total(),2))
    print("El volumen es: ",round (c.get_volumen(),2))

main()
