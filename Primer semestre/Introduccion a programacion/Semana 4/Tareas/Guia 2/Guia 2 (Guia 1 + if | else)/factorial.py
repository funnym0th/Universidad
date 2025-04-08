from math import factorial
x = int(input("ingrese un numero: "))
print("el factorial del numero ingresado es: ", factorial(x))

if (factorial(x) % 2 == 0):
    print("el resultado del factorial es par")
    
else:
    print("el resultado del factorial es impar")