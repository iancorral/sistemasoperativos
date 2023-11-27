def suma(n):
    if n>=0:
        s=0
        for i in range (1,n+1):
            s+=i
        return s
    else:
        return -1

#Main
n=int(input("Escribe tu número: "))
print(f"Tu suma de 1 a {n} es: {suma(n)}")