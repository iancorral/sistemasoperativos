def mayor():
    return m
#main
n=[]
for i in range(4):
    nums=int(input(f"Introduce tu número {i+1}: "))
    n.append(nums)
print(n)
m=max(n)
print(f"Tu número mayor de la lista es: {mayor()}")
mayor()