potencia = 1
num = int(input("ingrese un numero positivo para la base: "))
exp = int(input("ingrese un numero positivo para el exponente: "))
if (num > 0 and exp > 0):
    for i in range(exp, 0, -1):
        potencia = potencia * num
    print("el resultado de la potencia es: ", potencia)
else:
    print("error, uno de los valores no es positivo")
