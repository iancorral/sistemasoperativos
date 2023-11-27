import random
def leer_calificaciones(califs,n):
    for i in range(n):
        cal=random.randint(5,10)
        califs.append(cal)
def get_reprobados(califs):
    rep=0
    for cal in califs:
        if cal <=5:
            rep=rep+1
    return rep
def get_aprobados(califs):
    ap=0
    for cal in califs:
        if cal > 6:
            ap=ap+1
    return ap
def get_promedio(califs):
        prom=sum(califs)/n
        return prom
#main
calificaciones=[]
n=20
leer_calificaciones(calificaciones,n)
print(calificaciones)
print("El número de reprobados es= ",get_reprobados(calificaciones),"El de aprobados es= ", get_aprobados(calificaciones),"y su promedio es= ",get_promedio(calificaciones))

