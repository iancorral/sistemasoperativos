def num():
    r=0
    for i in range(n,num1+1):
        print(n+r,end=" ")
        r+=1
#main
n=int(input("Ingresa tu primer número: "))
num1=int(input("Ingresa tu segundo número: "))
print(f"{n},{num1} = ")
num()