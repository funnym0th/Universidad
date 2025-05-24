# Elegir cabaña y mostrar ocupacion
# Reservar espacios o dias en la cabaña
# Mostrar valor a pagar * dias 
cabanas = [[1, 2, 3], [10000, 20000, 30000], [0, 0, 0], [["días disponibles cabaña 1"], ["días disponibles cabaña 2"], ["días disponibles cabaña 3"]]]
print("Lista de cabañas: ")
for i in cabanas[0]:
    print(f"Cabaña {i}: Para {cabanas[0][i - 1]} persona(s), valor ${cabanas[1][i - 1]}")
eleccion = int(input("Que cabaña desea reservar?\n : "))
while eleccion in cabanas[0] and cabanas[2][eleccion - 1] < cabanas[0][eleccion - 1]:
    print(f"La ocupacion de la cabaña {eleccion} es de {cabanas[2][eleccion - 1]} persona(s)")
    