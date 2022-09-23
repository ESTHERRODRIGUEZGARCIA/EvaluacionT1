class Ejer1():
    matriz = [
    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]
    ]
    def sum(matriz):

        for i in matriz():
            matriz[1][3] = sum(matriz[1][:-1])
            matriz[3][3] = sum( matriz[3][:-1])

        matriz()

class Ejer2():
    #dirá si tiene una longitud mayor o igual que 3 y a su vez es menor que 10

    def cadena_texto():
        cadena = str(input("Escriba una cadena de texto: "))
        num = len(cadena.split())
        if num >= 3 and num < 10:
            print("Su texto es mayor o igual que 3 y a su vez es menor que 10 \nTrue.")
        else:
            print("La longitud de su texto no es mayor o igual que 3 ni menor que 10\nFalse.")


class Ejer3():
    def numeros():
        print(list(range(0,11)))
        print(list(range(-10,0)))
        print(list(range(0, 21, 2)))
        print(list(range(-19, 0, 2)))
        print(list(range(0, 51, 5)))

class tabla():
    

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

