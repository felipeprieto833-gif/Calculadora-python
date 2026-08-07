import math
a=0.0
b=0.0
c=0.0
print (f'''seleccione una opcion
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Calcular Seno
[6] Calcular Coseno
[7] Factorial
[8] Fibonacci
[9] Minimo comun divisor
[10] Maximo comun divisor
[11] Null
''')
opcion = int(input('Digite la opcion a calcular: '))

match opcion :
    case 1: 
        a = float(input("digite el numero entero:"))
        b = float(input("digite el numero entero:"))
        c=a+b
        print("la suma es:",c,)

    case 2: 
        a = float(input("digite el numero entero:"))
        b = float(input("digite el numero entero:"))
        c=a-b
        print("la resta es:",c,)

    case 3: 
        a = float(input("digite el numero entero:"))
        b = float(input("digite el numero entero:"))
        c=a*b
        print("la multiplicacion es:",c,)

    case 4: 
        a = float(input("digite el numero entero:"))
        b = float(input("digite el numero entero:"))
        c=a/b
        print("la division es:",c,)

    case 5: 
        a = float(input("digite el numero en radianes:"))
        c=math.sin(a)
        print("el seno es es:",c,)

    case 6: 
            a = float(input("digite el numero en radianes:"))
            c=math.cos(a)
            print("el coseno es es:",c,)


#me lo pela