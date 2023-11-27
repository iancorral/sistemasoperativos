import random

v=random.randint(5,10)
votos=[1]*(v)

c1=0;c2=0;c3=0
for i in range(v):
    votos[i]=random.randint(1,3)
    if votos[i]==1:
        c1+=1
    elif votos[i]==2:
        c2+=1
    else:
        c3+=1
print(f"Votos\nAlumnos que votaron: {votos}\nJuan {c1} votos \nmaria {c2} votos \npepe {c3} votos")