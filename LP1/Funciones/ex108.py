def num():
    n1=[]
    for i in range (3):
        n=int(input(f"Introduce tu número {i+1}: "))
        n1.append(n)
    print(n1)
    p=sum(n1)/3
    print(f"El número mayor es {max(n1)} y el menor es {min(n1)}, y su promedio es {p}")
num()