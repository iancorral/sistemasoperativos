def fcfs(processes):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # Ordenar los procesos por tiempo de llegada
    processes.sort(key=lambda x: x[1])

    total_time = 0

    for i in range(n):
        # Establecer el tiempo de finalización del proceso actual
        completion_time[i] = max(total_time, processes[i][1]) + processes[i][2]

        # Calcular el tiempo de espera y el tiempo de giro para el proceso actual
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

        # Actualizar el tiempo total
        total_time = completion_time[i]

    print("\nProceso\tTiempo de Llegada\tBurst Time\tTiempo de Espera\tTiempo de Turnaround")
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calcular promedios
    promedio_waiting_time = total_waiting_time / n
    promedio_turnaround_time = total_turnaround_time / n

    print(f"\nPromedio Tiempo de Espera: {promedio_waiting_time}")
    print(f"Promedio Tiempo de Turnaround: {promedio_turnaround_time}")

if __name__ == "__main__":
    # Definir la lista de procesos en el formato (ID, arrivalTime, BurstTime)
    processes = [(1, 4, 5,), (2, 6, 4), (3, 0, 3), (4, 6, 2), (5, 5, 4)]
    
    fcfs(processes)
