i = True
while (i == True):
    longLadoCubo = float(input("inserte la longitud de un lado del cubo: "))
    if (longLadoCubo < 0):
        print("el numero es negativo, tiene que ingresar un valor positivo")
    else:
        perimCubo = longLadoCubo * 12
        areaCubo = 6 * (longLadoCubo ** 2)
        print("el perimetro del cubo es: ", perimCubo, "\nel area del cubo es: ", areaCubo)
    i = int(input("\ndesea seguir calculando?\n1 = continuar\n0 = salir\n : "))
        
