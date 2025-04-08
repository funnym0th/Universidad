i = True
while (i == True):
    lado = float(input("inserte la medida de un lado del cuadrado: "))
    if (lado < 0):
        print("la medida del lado del cuadrado debe ser positiva")
    else:
        print("el perimetro del cuadrado es: ", lado * 4, "\nel area del cuadrado es: ", lado ** 2)
    i = int(input("\ndesea seguir usando la calculadora?\n1 = continuar\n0 = salir\n : "))
