suma = 0
contador = 0

while contador < 30:
    print("* numero", contador + 1)
    numero = float(input("ingrese el número para el calculo de promedio: "))
    suma = suma + numero
    contador = contador + 1
promedio = suma / 30

print("el promedio de los 30 numeros es:", promedio)

