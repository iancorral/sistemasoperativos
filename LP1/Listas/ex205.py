import random
def leer_aleatorio(numeros):
    for i in range(20):
        num=random.randint(0,10)
        numeros.append(num)

def mostrar_pares(numeros):
    for num in numeros:
        if (num%2==0) and (num!=0):
            print(num, end= " ")
        else:
            print("-", end=" ")
#main
numeros=[]
leer_aleatorio(numeros)
mostrar_pares(numeros)