import math
class CalculadoraEspeciales:
    def __init__(self,num1,num2,resul):
        self.num1=num1
        self.num2=num2
        self.resul=resul

    def raiz(self):
        if self.num1 < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.num1)

    def potencia(self):
        return math.pow(self.num1, self.num2)

    def factorial(self):
        self.resul = 1
        for i in range(1, self.num1+1):
            self.resul*=i
        return self.resul
    def mcd(self):
        while self.num2 != 0:
            self.num1, self.num2 = self.num2, self.num1 % self.num2
        return abs(self.num1)
    def mcm(self):
        return abs(self.num1*self.num2)//self.mcd()
def espmain():
    micalc=CalculadoraEspeciales(0,0,0)
    while True:
        print("---Funciones especiales---")
        print(" 1. raiz \n 2. pot \n 3. factorial \n 4. MCM \n 5. MCD")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            a=float(input("Ingrese el valor a calcular: "))
            b=float(input("Ingrese el exponente de la raiz: "))
            micalc.resul=a**(1/b)
            print("La raiz es ", micalc.resul)
        elif opcion==2:
            a=float(input("Ingrese el valor de la base: "))
            b=float(input("Ingrese el valor del exponente: "))
            micalc.resul=a**b
            print("= ", micalc.resul)
        elif opcion==3:
            a=int(input("Ingrese el valor a calcular: "))
            micalc.resul=1
            micalc.num1=a
            micalc.resul = micalc.factorial()
            print("El factorial es ", micalc.resul)
        elif opcion==4:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            micalc.resul = micalc.mcm(a, b)
            print("El MCM es ", micalc.resul)
        elif opcion==5:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            micalc.resul = micalc.mcd(a, b)
            print("El MCD es ", micalc.resul)
if __name__ == "__main__":
    espmain()