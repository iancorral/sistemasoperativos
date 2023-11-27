import random
def leer_numeros(numeros,n):
    for i in range(n):
        numeros.append(random.randint(0,101))
def mostrar_numeros(numeros,i1,i2):
    for i in numeros:
        if (i>=i1)and(i<=i2):
            print(i,end=" ")
    else:
        print("Error la lista esta fuera del rango")

#main
numeros=[]
n=int(input("Introduce cuantos números quieres en tu lista: "))
i1=int(input("Introduce tu primer parametro en el que quieres que se muestre la lista: "))
i2=int(input("Introduce tu segundo parametro en el que quieres que se muestre la lista: "))
leer_numeros(numeros,n)
mostrar_numeros(numeros,i1,i2)