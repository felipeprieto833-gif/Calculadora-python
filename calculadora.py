print("---Binvenido a la calculadora---")
print(" 1. Operaciones Basicas \n 2. Razones Tringonometricas \n 3. Funciones Especiales ")
o=int(input("Seleccione una opcion: "))

if o==1:
    from CalculadoraBasica import basicMain
    basicMain()
        
elif o==2:
    from CalculadoraTrigonomitrica import trigoMain
    trigoMain()

elif o==3:
    from CalculadoraEspecial import especialMain
    especialMain()
