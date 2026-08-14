import math
class CalculadoraTrigonometrica:
    def __init__(self,a,r):
        self.angulo=a
        self.resultado=r
    def seno(self):
        self.resultado=math.sin(self.angulo)
    def coseno(self):
        self.resultado=math.cos(self.angulo)
    def tangente(self):
        self.resultado=math.tan(self.angulo)
def trigomain():
    micalct=CalculadoraTrigonometrica(0,0)
    while True:
        print("---Operaciones Trigonométricas---")
        print(" 1. Seno \n 2. Coseno \n 3. Tangente")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            a=float(input ("Ingrese el valor del angulo: "))
            micalct.angulo=a
            micalct.seno()
            print("sen(",a,")= ", micalct.resultado)
        elif opcion==2:
            a=float(input ("Ingrese el valor del angulo: "))
            micalct.angulo=a
            micalct.coseno()
            print("cos(",a,")= ", micalct.resultado)
        elif opcion==3:
            a=float(input ("Ingrese el valor del angulo: "))
            micalct.angulo=a
            micalct.tangente()
            print("tan(",a,")= ", micalct.resultado)
if __name__ == "__main__":
    trigomain()
