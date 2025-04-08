i = True
while i == True:
    area = float(input("ingrese la longitud de un lado del cubo: "))
    if area > 0.0:
        areaCubo = 5 * area ** 2
        perimetroCubo = 12 * area
        print("* el area del cubo es: ", areaCubo, "\n* el perimetro del cubo es: ", perimetroCubo)
    else:
        print("el area de un lado del cubo debe ser positiva")
    i = int(input("desea seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
