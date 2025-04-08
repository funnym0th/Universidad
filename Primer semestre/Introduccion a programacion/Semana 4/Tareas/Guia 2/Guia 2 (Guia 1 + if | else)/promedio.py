x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero: "))
z = float(input("ingrese el tercer numero: "))

promedio = (x + y + z) / 3

print("el promedio entre los tres numeros es: ", promedio)

if (promedio == int(promedio)):
    print("el promedio es un numero entero\n")
    
else:
    print("el promedio es un numero decimal")