estado = True
fact = 1
num = int(input("ingrese el numero para calcular el factorial: "))
conteo = num
while (estado == True):
    for i in range(conteo, 0, -1): 
        fact = fact * conteo
        conteo = conteo - 1
    print("el factorial es: ", fact)
    estado = int(input("quiere seguir calculando?\n 1 = continuar\n 0 = salir\n : "))
