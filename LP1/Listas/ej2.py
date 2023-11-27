n=int(input("Cuantos elementos tiene la lista? "))
lista= [0]*n
for i in range (len(lista)):
    lista [i]= int(input (f"Escribir número en indice {i}: "))
print(lista)

for elemento in lista:
    print(elemento, end=" ")