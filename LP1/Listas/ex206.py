import random
def leer_calificaciones(califs,al):
    for i in range(al):
        cal=random.randint(5,10)
        califs.append(cal)
def mostrar_calificaciones(califs):
    print("CALIFICACIONES: ",califs)
def mostrar_estadisticas(califs):
    ap=0;rep=0;suma=0
    for num in califs:
        if num>6:
            ap+=1
        else:
            rep+=1
        suma+=num
    prom=suma/(len(califs))
    print(f"aprobados: {ap}\n Reprobados: {rep}\npromedio general:{prom}")

#Main
al=random.randint(10,30)
califs=[]
leer_calificaciones(califs,al)
mostrar_calificaciones(califs)
mostrar_estadisticas(califs)