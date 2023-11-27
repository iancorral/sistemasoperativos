#Listas con funciones
def introducir_numeros(ln,n):
    for i in range (n):
        num=int(input("Escribir número: "))
        ln.append(num)
def mostrar_numeros(ln):
    print("Lista de números")
    for elemento in (ln):
        print(elemento)
#Main
numeros=[]
introducir_numeros(numeros, 5)
mostrar_numeros(numeros)