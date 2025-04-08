i = True
while i == True:
    radio = float(input("ingrese el radio de la esfera: "))
    if radio > 0.0:
        volumen = (4 / 3) * 3.14159 * (radio ** 3)
        print("el volumen de la esfera es: ", volumen)
    else:
        print("el radio de la esfera debe ser positivo")
    i = int(input("quiere seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
