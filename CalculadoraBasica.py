import math
class Calculadora_Basica:
    def __init__(self,num1,num2,result):
        self.num1=num1
        self.num2=num2
        self.result=result
    def suma (self):
        self.result=self.num1+self.num2
        return self.result
    def restar (self):
        self.result=self.num1-self.num2
        return self.result
    def multiplicar (self):
        self.result=self.num1*self.num2
        return self.result
    def division (self):
        if self.num2==0:
            raise ValueError("No se puede dividir entre cero.")
        self.result=self.num1/self.num2
        return self.result
def main():
    micalcb=Calculadora_Basica(0,0,0)
    Ans=0
    while True:
        print("---Operaciones basicas---")
        print(" 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Divion ")
        opcion=int(input("Seleccione una opcion: "))

        if opcion==1:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=Ans
                micalcb.num2=int(input("ingrese el numero: "))
                print("La suma es ", micalcb.suma())
                Ans=micalcb.result
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                print("La suma es ", micalcb.suma())
                Ans=micalcb.result

        elif opcion==2:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=Ans
                micalcb.num2=int(input("ingrese el numero: "))
                print("La resta es ", micalcb.restar())
                Ans=micalcb.result
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                print("La resta es ", micalcb.restar())
                Ans=micalcb.result
        elif opcion==3:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=Ans
                micalcb.num2=int(input("ingrese el numero: "))
                print("La mutiplicacion es ", micalcb.multiplicar())
                Ans=micalcb.result
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                print("La mutiplicacion es ", micalcb.multiplicar())
                Ans=micalcb.result
        elif opcion==4:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=Ans
                micalcb.num2=int(input("ingrese el numero: "))
                print("La division es ", micalcb.division())
                Ans=micalcb.result
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                print("La division es ", micalcb.division())
                Ans=micalcb.result

if __name__ == "__main__":
    main()