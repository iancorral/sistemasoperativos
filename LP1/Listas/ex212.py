def leer(lista, n):
    for i in range(n):
        lista.append(int(input(f"Introduce el numero {i+1} de tu lista: ")))
def mostrar_numeros(lista, orden):
    if orden=="A" or "a":
        print(lista)
    else:
        lista.reverse()
        print(lista)

#main
lista=[]
n=int(input("Introduce cuantos numeros quieres en tu lista: "))
orden=(input("En que parametro quieres que se imprima tu lista, (A) Orden original o (B) Orden inverso: "))
leer(lista,n)
mostrar_numeros(lista,orden)