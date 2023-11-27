import ulsa

def main():
    a1= ulsa.Auto(color="negro")
    print("Gasolina ",a1.gasolina)
    a1.gasolina=30
    print(a1.gasolina)
    

main()