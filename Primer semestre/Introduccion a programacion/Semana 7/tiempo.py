# Se toma la variable para que el ciclo inicie mientras el usuario quiera continuar
i = 1
while i == 1:
    
    # Se toma el tiempo en segundos a partir de lo que ingrese el usuario
    tiempo = int(input("Inserte el tiempo en segundos: "))
    
    # Esta es la operacion para las horas, se hace la division entera para obtener las horas ya que dentro de una hora hay 3600 segundos, y tambien se excluyen los decimales
    horas = tiempo // 3600
    
    # Luego se realiza otra division entera, se divide entre 60 el resto de las horas ya que dentro de una hora hay 60 minutos, y seguimos excluyendo los decimales
    minutos = (tiempo % 3600) // 60
    
    # Los segundos restantes se obtienen a traves del resto de todos los segundos entre 60 (un minuto), ya que esa operacion nos da todos los segundos que NO conforman un minuto
    segundos = tiempo % 60
    
    print(horas, "horas", minutos, "minutos y", segundos, "segundos")

    # Se toma el valor del ciclo por el usuario para saber si seguir calculando o no
    i = int(input("Ingrese 1 para seguir calculando o 0 para salir"))
