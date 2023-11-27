import random
def leer_sueldos(sueldos):
    for i in range(em):
        sueldo=random.randint(1200,2200)
        sueldos.append(sueldo)
def mostrar_resultados(sueldos):
        print(sueldos)
        ma=max(sueldos); me=min(sueldos)
        prom=sum(sueldos)/em
        print(f"El sueldo maximo de la lista es ${ma}, y el minimo es ${me}, mientras que el promedio de todos los sueldos es: ${prom}")


#main
em=10
sueldos=[]
leer_sueldos(sueldos)
mostrar_resultados(sueldos)