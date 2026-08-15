import math
class CalculadoraTrigonometrica:
    def __init__(self,angle,radians,result):
        self.angle=angle
        self.radian=radians
        self.result=result
    def toRadians(self):
        self.radians = self.angle * math.pi / 180
        return self.radians

    def seno(self):
        self.toRadians()
        self.result=math.sin(self.radians)
        print("sen(",self.angle,")= ", self.result)
        return self.result
    def coseno(self):
        self.toRadians()
        self.result=math.cos(self.radians)
        print("cos(",self.angle,")= ", self.result)
        return self.result
    def tangente(self):
        while self.angle==90 or self.angle==270:
            print("La tangente no está definida para 90 y 270 grados.")
            self.angle= float(input("Ingrese el valor del angulo: "))
        self.toRadians()
        self.result=math.tan(self.radians)
        print("tan(",self.angle,")= ", self.result)

        return self.result
def trigoMain():
    micalct=CalculadoraTrigonometrica(0,0,0)
    while True:
        print("---Operaciones Trigonométricas---")
        print(" 1. Seno \n 2. Coseno \n 3. Tangente")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            micalct.seno()
        elif opcion==2:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            micalct.coseno()
        elif opcion==3:
            micalct.angle=float(input ("Ingrese el valor del angulo: "))
            micalct.tangente()
