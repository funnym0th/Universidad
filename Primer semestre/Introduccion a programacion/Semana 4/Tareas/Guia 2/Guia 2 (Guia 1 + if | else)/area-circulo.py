x = float(input("ingrese el radio del circulo: "))
area = (3.14 * (x**2))

print("el area del circulo es: ", area)

if (area > 50):
    print("el area es mayor a 50")

elif (area > 10):
    print("el area es mayor a 10 y menor que 50")

else:
    print("el area es menor a 10")