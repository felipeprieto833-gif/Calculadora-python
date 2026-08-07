import math
class Calculadora:
    def __init__(self,num1,num2,resul):
        self.num1=num1
        self.num2=num2
        self.resul=resul
    def suma (self):
        self.resul=self.num1+self.num2
        return self.resul
    def restar (self):
        self.resul=self.num1-self.num2
        return self.resul
    def multiplicar (self):
        self.resul=self.num1*self.num2
        return self.resul
    def division (self):
        self.resul=self.num1/self.num2
        return self.resul
    def seno(self,angulo):
        return math.sin(angulo)
    def coseno(self,angulo):
        return math.cos(angulo)
    def tangente(self,angulo):
        return math.tan(angulo)
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    def factorial(self, a):
        self.resul = 1
        for i in range(1, a+1):
            self.resul*=i
        return self.resul
micalc=Calculadora(0,0,0)
Ans=0
print("---Binvenido a la calculadora---")
print(" 1. Operaciones Basicas \n 2. Razones Tringonometricas \n 3. Funciones Especiales ")
o=int(input("Seleccione una opcion: "))


if o==1:
    while True:
        print("---Operaciones basicas---")
        print(" 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Divion \n 5. Seno \n 6. Coseno \n 7. Tangente")
        opcion=int(input("Seleccione una opcion: "))

        if opcion==1:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalc.num1=int(input("ingrese el numero: "))
                micalc.resul=Ans+micalc.num1
                print("La suma es ", micalc.resul)
                Ans=micalc.resul
            else:
                micalc.num1=int(input("ingrese el numero 1: "))
                micalc.num2=int(input("ingrese el numero 2: "))
                micalc.suma()
                print("La suma es ", micalc.resul)
                Ans=micalc.resul

        elif opcion==2:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalc.num1=int(input("ingrese el numero: "))
                micalc.resul=Ans-micalc.num1
                print("= ", micalc.resul)
                Ans=micalc.resul
            else:
                micalc.num1=int(input("ingrese el numero 1: "))
                micalc.num2=int(input("ingrese el numero 2: "))
                micalc.restar()
                print("= ", micalc.resul)
                Ans=micalc.resul
        elif opcion==3:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalc.num1=int(input("ingrese el numero: "))
                micalc.resul=Ans*micalc.num1
                print("= ", micalc.resul)
                Ans=micalc.resul
            else:
                micalc.num1=int(input("ingrese el numero 1: "))
                micalc.num2=int(input("ingrese el numero 2: "))
                micalc.multiplicar()
                print("= ", micalc.resul)
                Ans=micalc.resul
        elif opcion==4:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalc.num1=int(input("ingrese el numero: "))
                micalc.resul=Ans/micalc.num1
                print("= ", micalc.resul)
                Ans=micalc.resul
            else:
                micalc.num1=int(input("ingrese el numero 1: "))
                micalc.num2=int(input("ingrese el numero 2: "))
                micalc.division()
                print("= ", micalc.resul)
                Ans=micalc.resul
elif o==2:
    while True:
        print("---Operaciones basicas---")
        print(" 1. Seno \n 2. Coseno \n 3. Tangente")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            a=float(input ("Ingrese el valor del angulo: "))
            micalc.seno(a)
            print("sen(",a,")= ", micalc.resul)
        elif opcion==2:
            a=float(input ("Ingrese el valor del angulo: "))
            micalc.coseno(a)
            print("cos(",a,")= ", micalc.resul)
        elif opcion==3:
            a=float(input ("Ingrese el valor del angulo: "))
            micalc.tangente(a)
            print("tan(",a,")= ", micalc.resul)
elif o==3:
    while True:
        print("---Funciones especiales---")
        print(" 1. raiz \n 2. pot \n 3. factorial \n 4. MCM \n 5. MCD")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                b=float(input("Ingrese el exponente de la raiz: "))
                micalc.resul=Ans**(1/b)
                print("La raiz es ", micalc.resul)
                Ans=micalc.resul
            else:
                a=float(input("Ingrese el valor a calcular: "))
                b=float(input("Ingrese el exponente de la raiz: "))
                micalc.resul=a**(1/b)
                print("La raiz es ", micalc.resul)
                Ans=micalc.resul
        elif opcion==2:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                a=float(input("Ingrese el valor del exponente: "))
                micalc.resul=Ans**a
                print("= ", micalc.resul)
                Ans=micalc.resul
            else:
                a=float(input("Ingrese el valor de la base: "))
                b=float(input("Ingrese el valor del exponente: "))
                micalc.resul=a**b
                print("= ", micalc.resul)
                Ans=micalc.resul
        elif opcion==3:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalc.resul=1
                micalc.resul = micalc.factorial(micalc, Ans)
                print("El factorial es ", micalc.resul)

                Ans=micalc.resul
            else:
                a=int(input("Ingrese el valor a calcular: "))
                micalc.resul=1
                micalc.resul = micalc.factorial(micalc, a)
                print("El factorial es ", micalc.resul)

                Ans=micalc.resul
        elif opcion==4:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                a=int(input("Ingrese el segundo numero: "))
                micalc.resul = micalc.mcm(Ans, a)
                print("El MCM es ", micalc.resul)
                Ans=micalc.resul
            else:
                a=int(input("Ingrese el primer numero: "))
                b=int(input("Ingrese el segundo numero: "))
                micalc.resul = micalc.mcm(a, b)
                print("El MCM es ", micalc.resul)
                Ans=micalc.resul
        elif opcion==5:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                a=int(input("Ingrese el segundo numero: "))
                micalc.resul = micalc.mcd(Ans, a)
                print("El MCD es ", micalc.resul)
                Ans=micalc.resul
            else:
                a=int(input("Ingrese el primer numero: "))
                b=int(input("Ingrese el segundo numero: "))
                micalc.resul = micalc.mcd(a, b)
                print("El MCD es ", micalc.resul)
                Ans=micalc.resul
