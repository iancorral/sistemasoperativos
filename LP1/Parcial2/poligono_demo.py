from poligono import PoligonoRegular

def main () :
    p1 =PoligonoRegular ()
    print (p1)
    print (p1.get_area ())
    print (p1.get_perimetro ())

    p2 = PoligonoRegular(6,4)
    print (p2)
    print (p2.get_area ())
    print (p2.get_perimetro())

    p3 = PoligonoRegular(10,4,5.6,7.8)
    print (p3)
    print (p3.get_area ())
    print (p3.get_perimetro ())
main()