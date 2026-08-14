print("---Binvenido a la calculadora---")
print(" 1. Operaciones Basicas \n 2. Razones Tringonometricas \n 3. Funciones Especiales ")
o=int(input("Seleccione una opcion: "))

if o==1:
    from CalculadoraBasica import basicMain
    if __name__ == "__main__":
        basicMain()
        
elif o==2:
    from CalculadoraTrigonomitrica import trigoMain
    if __name__ == "__main__":
        trigoMain()

elif o==3:
    from CalculadoraEspecial import especialMain
    if __name__ == "__main__":
        especialMain()
