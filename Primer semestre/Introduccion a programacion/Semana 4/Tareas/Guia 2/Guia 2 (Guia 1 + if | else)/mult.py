x = float(input("ingrese un numero: "))
y = float(input("ingrese otro numero: "))

mult = (x * y)

print("la multiplicacion es: ", mult)

if (mult > 0):
    print("el resultado de la multiplicacion es positivo")

elif (mult < 0):
    print("el resultado de la multiplicacion es negativo")

else:
    print("el resultado de la multiplicacion es 0")