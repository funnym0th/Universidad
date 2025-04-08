i = True
while (i == True):
    radio = float(input("inserte el radio de la esfera: "))
    if (radio < 0):
        print("el radio no puede ser negativo")
    else:
        print("el volumen de la esfera es: ", (4/3) * 3.14 * (radio ** 3))
    i = int(input("quiere seguir calculando?\n1 = continuar\n0 = salir\n : "))
