def leer(lista,n):
  for i in range (n):
    num=int(input(f"Escribe tu número {i+1}: "))
    lista.append(num)

def mostrar(lista):
    print("La lista de números es: ")
    for j in lista:
        print(j)
        lista.sort()

#main
lista= []
n=int(input("Cuantos numeros quieres en tu lista: "))
leer (lista,n)
mostrar(lista)