#!/usr/bin/python
i = True
while (i == True):
    num = int(input("ingrese el numero para calcular el factorial: "))
    fact = 1
    conteo = num
    while conteo > 0:
        fact = fact * conteo
        conteo = conteo - 1
    print("El factorial de", num, "es: ", fact)
    i = input("desea calcular otro factorial?\n : ")
