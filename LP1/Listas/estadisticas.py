import math

def get_promedio(numeros):
    return sum(numeros)/len(numeros)

def get_desviacion(numeros):
    promedio=get_promedio(numeros)
    suma=0

    for numero in numeros:
        suma+=(numero-promedio)**2
    return math.sqrt(suma/(len(numeros)-1))