# El estado sera la variable que controle el ciclo
estado = 1

# I será usado para controlar el ciclo que dejará al usuario elegir los paquetes a comprar
i = 1

# Valores de los paquetes
paqueteUno = 45000
paqueteDos = 25000
paqueteTres = 50000


while estado == 1:
    # La variable que acumule el total de la compra debe estar inicializada dentro del ciclo, ya que se debe reiniciar a 0 cada vez que el usuario haga una nueva compra
    total = 0
    
    # Aqui se inicia el proceso de compra
    while i != 0:

        # Ahora I se encarga de la eleccion del paquete por el usuario
        i = int(input("Quiere comprar el paquete 1, 2 o 3?\nIngrese un 0 para terminar de añadir al carro\n : "))
        
        # En este caso, si el usuario ingresa 1, se utilizará el paquete N°1
        if i == 1:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            
            # Despues de tomar la cantidad de paquetes, en la variable del total se acumulará el valor del paquete multiplicado por la cantidad que se compren
            total = total + (paqueteUno * cantidad)
            print("Su carro tiene: ", total)

        # Luego se vuelven a repetir los mismos procesos, pero con los otros dos paquetes y la variable del total irá acumulando todo hasta que el usuario ingrese un 0
        elif i == 2:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            total = total + (paqueteDos * cantidad)
            print("Su carro tiene: ", total)
        elif i == 3:
            cantidad = int(input("Cuantos paquetes quiere comprar?: "))
            total = total + (paqueteTres * cantidad)
            print("Su carro tiene: ", total)

    # Si el usuario ingresa un 0, se detiene el ciclo y se le muestra el total de la compra
    print("Su total es de: ", total)

    # Aqui se le pregunta si quiere seguir calculando o no
    estado = int(input("Ingrese 1 para seguir calculando y 0 para salir: "))
