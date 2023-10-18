from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_cpu):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_cpu = tiempo_cpu

def round_robin(procesos, quantum):
    cola = deque(procesos)
    tiempo_actual = 0

    while cola:
        proceso = cola.popleft()
        tiempo_ejecucion = min(quantum, proceso.tiempo_cpu)
        
        print(f"Proceso {proceso.nombre} en ejecución durante {tiempo_ejecucion} unidades de tiempo")

        proceso.tiempo_cpu -= tiempo_ejecucion
        tiempo_actual += tiempo_ejecucion

        if proceso.tiempo_cpu > 0:
            cola.append(proceso)
        else:
            print(f"Proceso {proceso.nombre} terminado en tiempo {tiempo_actual}")

if __name__ == "__main__":
    proceso1 = Proceso("P1", 0, 10)
    proceso2 = Proceso("P2", 1, 5)
    proceso3 = Proceso("P3", 3, 8)
    
    procesos = [proceso1, proceso2, proceso3]
    quantum = 2
    
    print("Planificación Round Robin:")
    round_robin(procesos, quantum)
