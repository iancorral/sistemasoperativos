import random
def leer_aleatorio(numeros, n):
    for i in range(n):
        num=random.randrange(-1,2)
        numeros.append(num)

def mostrar(numeros):
    print(numeros)
    p=0;n=0;c=0
    for num in numeros:
        if (num>0):
            p+=1
            
        elif (num<0):
            n+=1
        
        else:
            c+=1

    print(f"Sus numeros positivos: {p}")
    print(f"Sus numeros negativos: {n}")
    print(f"Sus numeros 0: {c} ")

        
#main
n=5
numeros=[]
leer_aleatorio(numeros,n)
mostrar(numeros)
