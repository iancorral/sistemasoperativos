import random
def leer_numeros(numeros,n):
    for i in range (n):
        numeros.append(random.randint(1,100))
def mostrar_numeros(numeros,pm,pme):
    print(numeros)
    num=0
    for i in numeros:
        if i>pme and i< pm:
            num+=1
    print(f"Los numeros entre el parametro mayor y menor es de: ",num)

#main
n=10
numeros=[]
pm=int(input("Ingresa tu parametro mayor: "))
pme=int(input("Ingresa tu parametro menor: "))
leer_numeros(numeros,n)
mostrar_numeros(numeros,pm,pme)