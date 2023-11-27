def tabla(num):
    for i in range (1,11):
        if num>10:
            print("El valor debe ser entre 1 y 10")
            break
        else:
            print(f"{num} x {i} = {num*i}")
num=int(input("Ingresa tu número a multiplicar: "))
tabla(num)