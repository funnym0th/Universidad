import math
x = float(input("ingrese el numero para la raiz cuadrada: √"))

raiz = math.sqrt(x)

print("la raiz cuadrada del numero es: ", raiz)

if (raiz == int(raiz)):
    print("la raiz es un numero entero")
    
else:
    print("la raiz es un numero decimal")