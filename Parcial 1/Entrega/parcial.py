# Joan Jaramillo, 2159930-3743

import random

# Dados
d1 = 0 # Dado 1
d2 = 0 # Dado 2
ds1 = 0 # Dado 1 empieza
ds2 = 0 # Dado 2 empieza

p1 = 1 # Jugador 1 en la casilla 1
p2 = 1 # Jugador 2 en la casilla 1

p1_turn = False

started1 = False
started2 = False

# Función que inicia el juego
def start_game():
    global ds1, ds2
    ds1 = random.randint(1,6)
    ds2 = random.randint(1,6)

    if(ds1 == ds2):
        return True
    
    return False

# Función que simula el lanzamiento de los dados
def dice_roll():
    global d1, d2
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

# Función que simula el juego de carreras
def carreras_simulate():
    global p1, p2, started1, started2
    #i = 0
    while (True):
        #i += 1
        # Si ya empezó el jugador 1 tira los dados
        if (started1):
            dice_roll()
            p1 += d1 + d2
            print('El jugador 1 tira los dados:', p1, d1, d2)

        # Empieza jugador 1
        if(start_game() and (started1 == False)):
            p1 += ds1 + ds2
            started1 = True
            print('El jugador 1 empieza el juego:', ds1, ds2, p1)

        # Verifica si cayó en casilla premio
        if (p1 == 2 or p1 == 17 or p1 == 30 or p1 == 42):
            dice_roll()
            p1 += d1 + d2
            print('El jugador 1 cayó en casilla premio vuelve a lanzar:', p1, d1, d2)

        # Verifica que no se haya pasado
        if (p1 > 50):
            p1 -= (d1 + d2)
            print('El jugador 1 sacó más de 50, pierde turno')
            #print('i:',i)

        # Verifica si ganó
        if (p1 == 50):
            won = True
            print('El jugador 1 ganó')
            break

        # Si ya empezó el jugador 1 tira los dados
        if (started2):
            dice_roll()
            p2 += d1 + d2
            print('El jugador 2 tira los dados:', p2, d1, d2)
        
        # Empieza jugador 2
        if(start_game() and (started2 == False)):
            p2 += ds1 + ds2
            started2 = True
            print('El jugador 2 empieza el juego:', ds1, ds2, p2)

        # Verifica si cayó en casilla premio
        if (p2 == 2 or p2 == 17 or p2 == 30 or p2 == 42):
            dice_roll()
            p2 += d1 + d2
            print('El jugador 2 cayó en casilla premio vuelve a lanzar:', p2, d1, d2)

        # Verifica que no se haya pasado
        if (p2 > 50):
            p2 -= (d1 + d2)
            print('El jugador 2 sacó más de 50, pierde turno')
            #print('i:',i)

        # Verifica si ganó
        if (p2 == 50):
            won = True
            print('El jugador 2 ganó')
            break

        # Verifica empate
        if (p1 == 49 and p2 == 49):
            print('Empate')
            break
        

carreras_simulate()