import math
class Calculadora_Basica:
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
                micalcb.num1=int(input("ingrese el numero: "))
                micalcb.resul=Ans+micalcb.num1
                print("La suma es ", micalcb.resul)
                Ans=micalcb.resul
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                micalcb.suma()
                print("La suma es ", micalcb.resul)
                Ans=micalcb.resul

        elif opcion==2:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=int(input("ingrese el numero: "))
                micalcb.resul=Ans-micalcb.num1
                print("= ", micalcb.resul)
                Ans=micalcb.resul
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                micalcb.restar()
                print("= ", micalcb.resul)
                Ans=micalcb.resul
        elif opcion==3:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=int(input("ingrese el numero: "))
                micalcb.resul=Ans*micalcb.num1
                print("= ", micalcb.resul)
                Ans=micalcb.resul
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                micalcb.multiplicar()
                print("= ", micalcb.resul)
                Ans=micalcb.resul
        elif opcion==4:
            print(" 1. Ans \n 2. sin.ans")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                micalcb.num1=int(input("ingrese el numero: "))
                micalcb.resul=Ans/micalcb.num1
                print("= ", micalcb.resul)
                Ans=micalcb.resul
            else:
                micalcb.num1=int(input("ingrese el numero 1: "))
                micalcb.num2=int(input("ingrese el numero 2: "))
                micalcb.division()
                print("= ", micalcb.resul)
                Ans=micalcb.resul

if __name__ == "__main__":
    main()