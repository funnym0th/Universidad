x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero: "))

resta = (x - y)

print("la resta de los numeros es: ", resta)

if (resta > 0):
    print("el resultado es positivo")

elif (resta < 0):
    print("el resultado es negativo")

else:
    print("el resultado es 0")