i = True
while (i == True):
    num = int(input("inserte un numero: "))
    if (num % 2 == 0):
        print("el numero es par")
    else:
        print("el numero es impar")
    i = int(input("quiere insertar otro numero?\n1 = continuar\n0 = cerrar\n : "))