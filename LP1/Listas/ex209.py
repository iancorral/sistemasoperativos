def leer(nombres, horas, sueldo_hora, n):
    for i in range (n):
        nombres.append(input(f"Introduce el nombre de empleado {i+1}: "))
        horas.append(int(input("Introduce tus horas trabajadas: ")))

def mostrar(nombre, horas, sueldo_hora):
    print(f"Nombres \t Horas \t Sueldo total")
    for i in range(len(nombres)):
        print(f"{nombres[i]} \t\t {horas[i]} \t {(horas[i]*(sueldo_hora))} pesos")

#main
n=2
sueldo_hora=int(input("Introduce el sueldo por hora de los empleados: "))
nombres=[]
horas=[]
leer(nombres,horas,sueldo_hora,n)
mostrar(nombres,horas,sueldo_hora)