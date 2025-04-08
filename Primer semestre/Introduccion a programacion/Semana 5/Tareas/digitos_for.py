i = True
while i == True:
    contador = 0
    num = int(input("inserte el numero para contar los digitos: "))
    num = str(num)
    for i in num:
        contador = contador + 1
    print("la cantidad de digitos del numero son: ", contador)
    i = int(input("quiere seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
