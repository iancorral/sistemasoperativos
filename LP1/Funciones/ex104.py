def caracter(pal):
    pal= pal.upper()[0]
    if (pal in "AEIOU"):
        return True
    else:
        return False
def caracter2(pal):
    pal= pal.upper()[0]
    if ((len(pal)==1) and (pal in "AEIOU")):
        return True
    else:
        return False
#main
pal= str(input("Introduce tu letra: "))

if caracter2(pal):
    print("Es una vocal")
else:
    print("No es vocal")

#Objeto: es el que se crea apartir de una clase.
#Clase: Define una plantilla para crear objetos.