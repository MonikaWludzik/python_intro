#import the file
#sort contents by length
#choose word
#use word in the game

import random

def wybierz_slowo(min_slowo):
    with open('lista_slow_1.txt', 'r') as plik:
        for slowo in plik:
            if len(slowo) > min_slowo:
                print(slowo)
                return slowo

