print("---Binvenido a la calculadora---")
print(" 1. Operaciones Basicas \n 2. Razones Tringonometricas \n 3. Funciones Especiales ")
o=int(input("Seleccione una opcion: "))

if o==1:
    from CalculadoraBasica import main
    if __name__ == "__main__":
        main()
        
elif o==2:
    from CalculadoraTrigonomitrica import trigomain
    if __name__ == "__main__":
        trigomain()

elif o==3:
    from CalculadoraEspecial import espmain
    if __name__ == "__main__":
        espmain()
