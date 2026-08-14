import math
class CalculadoraTrigonometrica:
    def __init__(self,angle,result):
        self.angle=angle
        self.result=result
    def seno(self):
        self.result=math.sin(self.angle)
        return self.result
    def coseno(self):
        self.result=math.cos(self.angle)
        return self.result
    def tangente(self):
        if self.angle==90 or self.angle==270:
            raise ValueError("La tangente no está definida para 90 y 270 grados.")
        self.result=math.tan(self.angle)
        return self.result
def trigomain():
    micalct=CalculadoraTrigonometrica(0,0)
    while True:
        print("---Operaciones Trigonométricas---")
        print(" 1. Seno \n 2. Coseno \n 3. Tangente")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            print("sen(",micalct.angle,")= ", micalct.seno())
        elif opcion==2:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            micalct.coseno()
            print("cos(",micalct.angle,")= ", micalct.result)
        elif opcion==3:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            micalct.tangente()
            print("tan(",micalct.angle,")= ", micalct.result)
if __name__ == "__main__":
    trigomain()
