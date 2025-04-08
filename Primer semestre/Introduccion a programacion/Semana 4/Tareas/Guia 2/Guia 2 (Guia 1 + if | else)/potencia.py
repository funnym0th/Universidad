x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero para exponente: "))

potencia = (x ** y)

print("el resultado de la potencia es: ", potencia)

if (potencia % 2 == 0):
    print("el resultado de la potencia es par")
    
else:
    print("el resultado de la potencia es impar")