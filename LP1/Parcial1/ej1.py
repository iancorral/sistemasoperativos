def leer_nombres(n):
    for i in range(n):
        nombres.append(input(f"Introduce el nombre {i+1} de tu lista: "))
    return nombres
def mostrar_nombres(nombres):
        nombres.reverse()
        print(nombres)

#main
nombres=[]
n=int(input("Introduce cuantos nombres quieres en tu lista: "))
print(leer_nombres(n))
mostrar_nombres(nombres)