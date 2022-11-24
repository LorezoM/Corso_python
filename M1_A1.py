import random
from random import randrange
NUM_DIGITS = 3
MAX_GUESSES = 10

class numero_grande():
    """Accade quando il numero introdotto è troppo grande"""
    pass


class numero_piccolo():
    """Accade quando il numero introdotto è troppo piccolo"""
    pass

def get_magic_number(NUM_DIGITS):
    MAGIC_NUMBER = []
    for i in range(NUM_DIGITS):
        MAGIC_NUMBER.append(random.randint(0, 9))
    return(MAGIC_NUMBER)

def get_guess(NUM_DIGITS):
    GUESS=[]
    while True:
        try:
            GUESS=[int(i) for i in str(input(f'inset your guess'))]
            if len(GUESS) < NUM_DIGITS:
                raise numero_piccolo
            elif len(GUESS) > NUM_DIGITS:
                raise numero_grande
                print(f'numero inserito troppo grande! \n  {len(GUESS) - NUM_DIGITS } cifre in più sono state inserite')
            else:
                break
        except numero_piccolo:
            print(f'numero inserito troppo piccolo! \n mancano {NUM_DIGITS - len(GUESS)} cifre')
        except numero_grande:
            print(f'numero inserito troppo grande! \n  {len(GUESS) - NUM_DIGITS} cifre in più sono state inserite')
        except:
            print(f'error in input digit n° {i+1} !')
    return (GUESS)

def game(NUM_DIGITS,GUESS,MAGIC_NUMBER):
    a = b = 0
    for i in range(NUM_DIGITS):
        if GUESS[i] == MAGIC_NUMBER[i]:
            a += 1
        else:
            if MAGIC_NUMBER.count(GUESS[i]) > 0:
                b += 1
    if a >= 1:
        print('numero corretto in posizione corretta !')
    if b >= 1:
        print('un numero è presente ma in una posizione errata !')
    if (a == 0) & (b == 0):
        print('nessuna cifra del numero dato è contenuta nel numero magico !')
    return (a)

if __name__ == '__main__':
    MAGIC_NUMBER = get_magic_number(NUM_DIGITS)
    print('Benvenuto al gioco! \n indovina il numero magico per vincere')
    j = 0
    while j < MAX_GUESSES:
        print(f'Hai {MAX_GUESSES-j} tentativi per vincere!')
        GUESS = get_guess(NUM_DIGITS)
        a = game(NUM_DIGITS, GUESS, MAGIC_NUMBER)
        if a == NUM_DIGITS:
            print('complimenti hai vinto il gioco!')
            break
        j += 1
    if a < 3:
        print('Mi dispiace hai perso')

