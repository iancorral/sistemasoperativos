import math
#Hipotenusa

def hipotenusa(co,ca):
    resultado= (math.sqrt((co**2+ca**2)))
    return resultado
#main
co=int(input("Cateto opuesto: "))
ca=int(input("Cateto adyacente: "))

hip=hipotenusa(co,ca)
print(f"Su hipotenusa es {hip:.2f}")