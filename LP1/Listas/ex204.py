import random

def leer(nom,ed,cat):
    categorias= ["A","B","C"]
    for i in range(5):
        n=(input("Introduce tu nombre:"))
        e=int(input("Introduce tu edad: "))
        c=random.choice(categorias)
        nom.append(n)
        ed.append(e)
        cat.append(c)
def mostrar(nom,ed,cat):
        for i in range(len(nom)):
                 print(f"Su nombre es: {nom[i]}, tiene {ed[i]} años y su categoria es: {cat[i]}")
#Main
nom=[]
ed=[]
cat=[]
leer(nom,ed,cat)
mostrar(nom,ed,cat)