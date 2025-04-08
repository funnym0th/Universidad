i = True
while (i == True):
    ladoRectanguloA = float(input("ingrese la medida de un lado: ")) 
    ladoRectanguloB = float(input("ingrese la medida del otro lado: "))
    if (ladoRectanguloA > 0.0) and (ladoRectanguloB > 0.0):
        areaRectangulo = ladoRectanguloA * ladoRectanguloB
        print("el area del rectangulo es: ", areaRectangulo)
    else:
        print("ambas medidas deben ser positivas")
    i = int(input("quiere seguir calculando?\n 1 = seguir\n 0 = salir\n : "))
