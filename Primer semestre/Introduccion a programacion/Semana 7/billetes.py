# Se toma el valor inicial para iniciar el ciclo
i = 1
while i == 1:
    # Se pide el monto inicial
    montoIngreso = int(input("Ingrese un monto: "))
    
    # Se verifica si el monto ingresado es mayor que todos los billetes que hay
    if montoIngreso > 20000:
        # Se hace la division entera para saber cuantas veces cabe el valor del billete (en este caso $20.000) en el monto de ingreso, y con division entera para evitar los decimales
        billetesVeinte = montoIngreso // 20000
        # Despues de esa operacion, convertimos el monto de ingreso al resto de la division que hemos hecho antes
        montoIngreso = montoIngreso % 20000
    
    # Luego repetimos el mismo proceso para todos los otros montos de billetes
    elif montoIngreso > 10000:
        billetesDiez = montoIngreso // 10000
        montoIngreso = montoIngreso % 10000

    elif montoIngreso > 5000:
        billetesCinco = montoIngreso // 5000
        montoIngreso = montoIngreso % 5000

    elif montoIngreso > 2000:
        billetesDos = montoIngreso // 2000
        montoIngreso = montoIngreso % 2000

    elif montoIngreso > 1000:
        billetesMil = montoIngreso // 1000
        montoIngreso = montoIngreso % 1000

    # Se toma el dato del usuario para seguir o cerrar el ciclo
    i = int(input("Ingrese un 1 para seguir o un 0 para salir\n : "))
