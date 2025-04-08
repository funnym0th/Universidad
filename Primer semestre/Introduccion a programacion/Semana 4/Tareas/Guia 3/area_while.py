i = True
print("Calculadora de area del circulo")
while (i == True):
    radio = int(input("\nIngrese el radio del circulo: "))
    area = 3.14 * (radio**2)
    if (radio < 0):
        print("Error, el numero no puede ser negativo")
    else:
        print("El area del circulo es: ", area)
    i = bool(input("\nDesea hacer otra operacion?\n * 1 = Continuar\n * 0 = Terminar\n: "))
    if (i == False):
        break