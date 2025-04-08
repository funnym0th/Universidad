print("piensa en un numero desde el 1 al 4")
print("contesta S (sí) o N (no) a las preguntas: ")
uno = input("el número pensado es mayor que 2? ")

if uno == "S":
    dos = input("el número pensado es mayor que 3? ")
    if dos == "S":
        print("el valor que pensó es 4")
    elif (dos == "N"):
        print("el valor que pensó es 3")
elif uno == "N":
    dos = input("el número pensado es mayor que 1? ")
    if dos == "S":
        print("el valor que pensó es 3")
    elif (dos == "N"):
        print("el valor que pensó es el 1")

print("nos vemos...")
