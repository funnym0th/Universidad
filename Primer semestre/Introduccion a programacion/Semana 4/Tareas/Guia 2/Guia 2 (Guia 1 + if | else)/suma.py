firstNum = float(input("ingrese el primer valor: "))
secondNum = float(input("ingrese el segundo valor: "))

suma = (firstNum + secondNum)

print("la suma de ambos numeros es: ", suma)

if (suma > 0):
    print("el resultado de la suma es positivo")

elif (suma < 0):
    print("el resultado de la suma es negativo")

else:
    print("el resultado de la suma es 0")