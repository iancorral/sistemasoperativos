import random
def get_lista(n):
    for i in range(n):
        lista1.append(random.randint(0,100))
        lista2.append(random.randint(0,100))
    return lista1,lista2
def suma_lista(lista1,lista2):
    for i in range (len(lista1)):
        suma=lista1[i]+lista2[i]
        lista3.append(suma)
    return lista3
#main
n=5
lista1=[]
lista2=[]
lista3=[]
print("Las listas son: ",get_lista(n))
print("La suma de las dos listas es de: ",suma_lista(lista1,lista2))