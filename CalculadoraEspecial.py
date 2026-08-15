import math
class CalculadoraEspeciales:
    def __init__(self,num1,num2,result):
        self.num1=num1
        self.num2=num2
        self.result=result

    def raiz(self):
        if self.num1 <= 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        self.result = self.num1**(1/2)
        return self.result

    def potencia(self):
        self.result = 1
        for i in range(1, self.num2):
            self.result *= self.num1
        return self.result

    def abs(self, num):
        if num < 0:
            return -num
        return num

    def factorial(self):
        if self.num1 < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo.")
        self.result = 1
        for i in range(1, self.num1+1):
            self.result*=i
        return self.result

    def fibonacci(self):
        if self.num1 < 0:
            raise ValueError("No se puede calcular el número de Fibonacci de un número negativo.")
        a, b = 0, 1
        for _ in range(self.num1):
            a, b = b, a + b
        self.result = a
        return self.result

    def mcd(self):
        while self.num2 != 0:
            self.num1, self.num2 = self.num2, self.num1 % self.num2
        self.result = self.abs(self.num1)
        return self.result

    def mcm(self):
        self.result = self.abs(self.num1*self.num2)//self.mcd()
        return self.result

def especialMain():
    micalc=CalculadoraEspeciales(0,0,0)
    while True:
        print("---Funciones especiales---")
        print(" 1. raiz \n 2. pot \n 3. factorial \n 4. fibonacci \n 5. MCM \n 6. MCD")
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            micalc.num1 = float(input("Ingrese el valor a calcular: "))
            print("La raiz es ", micalc.raiz())
        elif opcion==2:
            micalc.num1 = float(input("Ingrese el valor de la base: "))
            micalc.num2 = float(input("Ingrese el valor del exponente: "))
            print("La potencia es igual a: ", micalc.potencia())
        elif opcion==3:
            micalc.num1=int(input("Ingrese el valor a calcular: "))
            print("El factorial es ", micalc.factorial())
        elif opcion==4:
            micalc.num1 = int(input("Ingrese el primer numero: "))
            print("El numero de fibonacci es ", micalc.fibonacci())
        elif opcion==5:
            micalc.num1 = int(input("Ingrese el primer numero: "))
            micalc.num2 = int(input("Ingrese el segundo numero: "))
            print("El MCM es ", micalc.mcm())
        elif opcion==6:
            micalc.num1 = int(input("Ingrese el primer numero: "))
            micalc.num2 = int(input("Ingrese el segundo numero: "))
            print("El MCD es ", micalc.mcd())

if __name__ == "__main__":
    especialMain()