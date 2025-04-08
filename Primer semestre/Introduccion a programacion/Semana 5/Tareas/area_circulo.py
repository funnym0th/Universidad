i = True
while i == True:
    radio = float(input("ingrese el radio del circulo: "))
    if radio > 0.0:
        area = 3.14 * (radio ** 2)
        print("el area es: ", area)
    else:
        print("el radio tiene que ser positivo")
    i = int(input("quiere seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
