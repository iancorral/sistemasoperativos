import random

def leer(lista, n):
    for i in range(n):
        lista.append(random.randint(1,21))
def asteriscos(lista):
    print(lista)
    for n in lista:
        print("*"*n)
    print("\n")


#main
lista=[]
n=3
leer(lista,n)
asteriscos(lista)