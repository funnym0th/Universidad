i = True
potencia = 1
while (i == True):
    num = int(input("ingrese el numero a potenciar: "))
    conteo = int(input("ingrese el exponente: "))
    while (conteo > 0):
        potencia = potencia * num
        conteo = conteo - 1
    print("la potencia es: ", potencia)
    i = int(input("quiere seguir calculando?\n1 = continuar\n0 = salir\n : "))
