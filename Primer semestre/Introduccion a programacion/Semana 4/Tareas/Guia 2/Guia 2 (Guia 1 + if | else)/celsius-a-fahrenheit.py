x = float(input("ingrese la temperatura en grados celsius: "))

fahrenheit = x * (9 / 5) + 32

print("la temperatura en fahrenheit es: ", fahrenheit)

if (fahrenheit >= 86):
    print("* la temperatura es igual o mayor a 86° fahrenheit")

elif (fahrenheit >= 59):
    print("* la temperatura es igual o mayor a 59° y menor a 86° fahrenheit")

elif (fahrenheit >= 32):
    print("* la temperatura es igual o mayor a 32° y menor que 59° fahrenheit")

elif (fahrenheit < 32 and fahrenheit >= 23):
    print("* la temperatura es menor a 32° y mayor o igual a 23° fahrenheit")

else:
    print("* la temperatura es menor a 23° fahrenheit")