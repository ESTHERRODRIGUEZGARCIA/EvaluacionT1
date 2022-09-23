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