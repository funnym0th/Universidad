suma = 0
contador = 0
for i in range(30):
    print("* numero: ", contador + 1)
    numero = float(input("ingrese el numero: "))
    suma = suma + numero
    contador = contador + 1
promedio = suma / 30
print("el promedio es: ", promedio)
