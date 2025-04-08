a = True
while a == True:
    numero = int(input("ingrese un numero: "))
    if numero % 2 == 0:
        print("el numero es par")
    else:
        print("el numero es impar")
    a = int(input("quiere continuar?\n 1 = seguir\n 0 = salir\n : "))

