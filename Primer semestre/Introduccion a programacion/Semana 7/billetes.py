i = 1
while i == 1:
    montoIngreso = int(input("Ingrese un monto: "))
    
    billetesVeinte = 0
    billetesDiez = 0
    billetesCinco = 0
    billetesDos = 0
    billetesMil = 0

    if montoIngreso > 20000:
        billetesVeinte = montoIngreso // 20000
        montoIngreso = montoIngreso % 20000
    
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

    i = int(input("Ingrese un 1 para seguir o un 0 para salir\n : "))
