

def tabla():
    
    fila = int(input("Introduzca un argumento "))
    columna = int(input("Introduzca un argumento "))

    if fila < 1 or fila > 9 or columna < 1 or columna > 9:
        print("Error.")

    else:
        for i in range(fila):
            for i in range(columna):
                print(" * ", end='')

