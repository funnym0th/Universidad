i = True
while (i == True):
    radio = float(input("ingrese el radio del circulo: "))
    if (radio < 0):
        print("el numero que insertó es negativo, tiene que ser positvo")
    else:
        permCirculo = 2 * 3.14 * radio
        print("el perimetro del circulo es: ", permCirculo)
    i = int(input("quiere seguir usando la calculadora?\n1 = continuar\n0 = salir\n : "))
