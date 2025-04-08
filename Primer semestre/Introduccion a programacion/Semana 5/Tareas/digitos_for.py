estado = 1
for a in range(0, 2, estado):
    contador = 0
    num = int(input("inserte el numero para contar los digitos: "))
    num = str(num)
    for i in num:
        contador = contador + 1
    print("la cantidad de digitos del numero son: ", contador)
    estado = int(input("quiere seguir calculando?\n 1 = continuar\n 0 = salir\n : "))
    if (estado == 1):
        a = a - 1
