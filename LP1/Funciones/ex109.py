import math
def dis(x1,y1,x2,y2):
    d= math.sqrt((x1-x2)**2+(y1-y2)**2)
    print(f"Distancia: {d:.1f}")

#main
x1= int(input("Ingresa tu primer punto x: "))
y1= int(input("Ingresa tu primer punto y: "))
x2= int(input("Ingresa tu segundo punto x: "))
y2= int(input("Ingresa tu segundo punto y: "))
dis(x1,x1,y2,y2)