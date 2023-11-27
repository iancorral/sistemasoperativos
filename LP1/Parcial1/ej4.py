def leer_materias(materias,calificaciones):
    for i in range (materias):
        mat.append(input(f"Introduce el nombre de la materia {i+1}: "))
        calificaciones.append(int(input("Introduce tu calificacion: ")))

def mostrar_reprobadas(materias,calificaciones):
    for num in calificaciones:
        c=0
        for i in calificaciones:
            if i<6:
                print(f"usted tiene que repetir {materias[num]}")
        c+=1

#main
materias=5
mat=[]
calificaciones=[]
leer_materias(materias,calificaciones)
mostrar_reprobadas(materias,calificaciones)