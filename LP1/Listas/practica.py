nom=[]
hrs=[]
ho=150
for i in range (2):
    n=str(input(f"Introduce tu nombre {i+1}: "))
    h=int(input("Introduce las horas que trabajaste: "))
    nom.append(n)
    hrs.append(h)
for i in range(len(nom)):
    s=ho*h
    print(f"{n} ha trabajado {h} horas, por lo que gano {s}")
print(nom)
print(hrs)