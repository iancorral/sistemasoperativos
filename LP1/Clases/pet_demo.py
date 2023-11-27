import pet

def main():
    nombre=input("Nombre de la mascota: ")
    tanimal=input("Introduce tu tipo de animal: ")
    edad=float(input("Edad de la mascota: "))

    m1=pet.Pet(nombre,tanimal,edad)

    print(m1)
    print("El nombre es: ",m1.nombre)
    print("El tipo es: ",m1.tanimal)
    print("Su edad es: ",m1.edad)
    
main()