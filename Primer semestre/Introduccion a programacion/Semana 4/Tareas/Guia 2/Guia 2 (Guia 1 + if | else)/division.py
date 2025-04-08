x = float(input("ingrese un numero: "))
y = float(input("ingrese otro numero: "))

division = x / y

print("la division de los numeros es: ", division)

if (division == int(division)):
    print("el resultado de la division es entero")
    
else:
    print("el resultado de la division es decimal")