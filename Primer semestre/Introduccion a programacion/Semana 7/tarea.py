estado = 1
i = 1
paqueteUno = 45000
paqueteDos = 25000
paqueteTres = 50000
while estado == 1:
    total = 0
    while i != 0:
        i = int(input("Quiere comprar el paquete 1, 2 o 3?\nIngrese un 0 para terminar de añadir al carro\n : "))
        if i == 1:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            total = total + (paqueteUno * cantidad)
            print("Su carro tiene: ", total)
        elif i == 2:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            total = total + (paqueteDos * cantidad)
            print("Su carro tiene: ", total)
        elif i == 3:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            total = total + (paqueteTres * cantidad)
            print("Su carro tiene: ", total)
    print("Su total es de: ", total)
    estado = int(input("Ingrese 1 para seguir calculando y 0 para salir: "))
