x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero: "))

modulo = (x % y)

print("el resto de la division entera entre los dos numeros es: ", modulo)

if (modulo > 0):
    print("la division si tiene resto")
    
else:
    print("la division no tiene resto")