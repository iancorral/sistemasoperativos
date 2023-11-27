from item import Item

def main():
    n=int(input("Ingresa tu cantidad de objetos: "))
    items=[]

    for i in range (n):
        id=int(input(f"Introduce el id de tu objeto {i+1}: "))
        des=input(f"Descripción de tu objeto {i+1}: ")
        uni=int(input(f"Unidades que hay del objeto {i+1}: "))
        pr=int(input(f"Precio del objeto {i+1}: "))
        i1=Item(id,des,uni,pr)
        items.append(i1)
    for n in items:
        print (n, end="\n")
    
main()