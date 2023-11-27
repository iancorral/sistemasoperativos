def leer(lista,n):
    for i in range (n):
        num=(input(f"Escribe tu nombre {i+1}: "))
        lista.append(num)
        lista.sort()    
def mostrar(lista):
    print("La lista de nombres es: ")
    for j in lista:
        print(j)

#main
lista= []
n=int(input("Cuantos nombres quieres en tu lista: "))
leer (lista,n)
mostrar(lista)