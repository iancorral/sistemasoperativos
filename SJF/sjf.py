def sjf(processes, n, burst_time):
    # Ordena los procesos en función del tiempo de ejecución
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if burst_time[j] > burst_time[j + 1]:
                burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
                processes[j], processes[j + 1] = processes[j + 1], processes[j]

    # Calcula el tiempo de espera y el tiempo de retorno
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calcula el tiempo promedio de espera y el tiempo promedio de retorno
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print("Proceso\tTiempo de Ejecución\tTiempo de Espera\tTiempo de Retorno")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}")

    print(f"Tiempo promedio de Espera = {average_waiting_time}")
    print(f"Tiempo promedio de Retorno = {average_turnaround_time}")


# Ejemplo de uso
if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    n = len(processes)
    burst_time = [6, 8, 7, 3]

    sjf(processes, n, burst_time)
