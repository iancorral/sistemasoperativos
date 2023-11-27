from empleado import Empleado

def main():
        nombre=(input(f"Nombre del empleado: "))
        horast=float(input(f"Ingresa tus horas trabajadas: "))
        sueldo=float(input(f"Ingresa tu sueldo: "))
        e1=Empleado(nombre,horast,sueldo)
        print(e1)
        print("El sueldo total es: $",round(e1.get_sueldo(),2))
        
main()