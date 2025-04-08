x = float(input("ingrese la temperatura en grados fahrenheit: "))

celsius = (x - 32) * 5 / 9 

print("\nla temperatura en celsius es: ", celsius, "\n")

if (celsius >= 30):
    print("* la temperatura es igual o mayor a 30° celsius")

elif (celsius >= 15):
    print("* la temperatura es igual o mayor a 15° y menor a 30° celsius")

elif (celsius >= 0):
    print("* la temperatura es igual o mayor a 0° y menor que 15° celsius")

elif (celsius < 0 and celsius >= -5):
    print("* la temperatura es menor a 0° y mayor o igual a -5° celsius")

else:
    print("* la temperatura es menor a -5° celsius")