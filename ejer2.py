
#dirá si tiene una longitud mayor o igual que 3 y a su vez es menor que 10

def cadena_texto():
    cadena = str(input("Escriba una cadena de texto: "))
    num = len(cadena.split())
    if num >= 3 and num < 10:
        print("Su texto es mayor o igual que 3 y a su vez es menor que 10 \nTrue.")
    else:
        print("La longitud de su texto no es mayor o igual que 3 ni menor que 10\nFalse.")