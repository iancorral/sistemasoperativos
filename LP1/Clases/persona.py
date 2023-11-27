class Persona:
    def caminar(self):
        print("La persona esta caminando")

    def pagar(self,tarjeta):
        if not isinstance(tarjeta,TarjetaCredito):
            raise ValueError("No es una tarjeta de credito")
        print("Shopping")
        tarjeta.validar_tarjeta()
        tarjeta.hacer_pago(90)


class TarjetaCredito:
    def hacer_pago(self,num_tarjeta):
        print("Pagar las compras",num_tarjeta)

    def validar_tarjeta(self):
        print("Validando tarjeta")
    
def main():
    p=Persona()
    tc=TarjetaCredito()
    p.caminar()
    p.pagar(tc)
main()
