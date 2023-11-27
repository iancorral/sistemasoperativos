import random
def get_lista(n):
    for i in range(n):
        lista.append(random.randint(-10,11))
    return lista
def resultados(lista):
    ne=0;p=0;c=0
    for elemento in lista:
        if (elemento>0):
            p+=1
        elif (elemento<0):
            ne+=1
        else:
            c+=1
    print(f"Sus numeros positivos: {p}")
    print(f"Sus numeros negativos: {ne}")
    print(f"Sus numeros 0: {c} ")
    mp=p/len(lista)
    mn=ne/len(lista)
    print("La media números positivos es de: ",mp,"y la media de números negativos es de: ",mn  )
#main
n=10
lista=[]
print("La lista es: ",get_lista(n))
resultados(lista)