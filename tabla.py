def tabla():
    fila = input("Introduzca un argumento ")
    print(fila)
    columna = input("Introduzca un argumento ")
    print(columna)
    if fila in range (0,9):
        print()
    else:
        print("Error.")

    if columna in range (0,9):
        print()
    else:
        print("Error.")


    for i in range(fila):
            for i in range(columna):
                print(" * ", end='')
