

def tabla():
    
    fila = int(input("Introduzca un número de filas "))
    columna = int(input("Introduzca un número de columnas "))

    if fila < 1 or fila > 9 or columna < 1 or columna > 9:
        print("Error.")

    else:
        for i in range(fila):
            print(" ")
            for j in range(columna):
                print(" * ", end='')

