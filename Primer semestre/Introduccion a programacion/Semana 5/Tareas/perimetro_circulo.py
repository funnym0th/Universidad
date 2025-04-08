i = True
while i == True:
    diametro = float(input("ingrese el diametro del circulo: "))
    if diametro > 0.0:
        perimetro = 3.14 * diametro
        print("el perimetro es: ", perimetro)
    else:
        print("el diametro debe ser positivo")
    i = int(input("quiere seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
