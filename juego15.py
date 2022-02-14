import random

run = True

juego_inicio = [
    1,2,3,4,
    5,6,7,8,
    9,10,11,12,
    13,14,15,0
    ]

juego_final = [
    0,1,2,3,
    4,5,6,7,
    8,9,10,11,
    12,13,14,15
    ]

def mov_arriba(posicion, matriz):
    if ((posicion - 4) < 0):
        return (posicion, matriz)
    else:
        copia = matriz[posicion - 4]
        matriz[posicion - 4] = 0
        matriz[posicion] = copia
        return (posicion-4, matriz)

def mov_abajo(posicion, matriz):
    if ((posicion + 4) > 15):
        return (posicion, matriz)
    else:
        copia = matriz[posicion + 4]
        matriz[posicion + 4] = 0
        matriz[posicion] = copia
        return (posicion + 4, matriz)

def mov_derecha(posicion, matriz):
    if ((posicion + 1) > 15):
        return (posicion, matriz)
    else:
        copia = matriz[posicion + 1]
        matriz[posicion + 1] = 0
        matriz[posicion] = copia
        return (posicion + 1, matriz)

def mov_izquierda(posicion, matriz):
    if ((posicion - 1) < 0):
        return (posicion, matriz)
    else:
        copia = matriz[posicion - 1]
        matriz[posicion - 1] = 0
        matriz[posicion] = copia
        return (posicion - 1, matriz)

def movimiento(numero, posicion, matriz):
    if (numero == 0):
        return mov_arriba(posicion, matriz)
    elif(numero == 1):
        return mov_abajo(posicion, matriz)
    elif(numero == 2):
        return mov_derecha(posicion, matriz)
    elif(numero == 3):
        return mov_izquierda(posicion, matriz)
    else:
        return (posicion, matriz)

while(run):
    posicion_cero = juego_inicio.index(0)
    posicion_cero_final = juego_final.index(0)
    
    if(posicion_cero != posicion_cero_final):
        r = random.randint(0,4)   
        (posicion_cero, juego_inicio) = movimiento(r, posicion_cero, juego_inicio)
        print(juego_inicio)

    elif (posicion_cero == posicion_cero_final):
        run = False
    