#import the file
#sort contents by length
#choose word
#use word in the game

import os
import random

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def wybierz_slowo(min_slowo):
    with open(os.path.join(__location__,'lista_slow_1.txt'), 'r') as plik:
        for slowo in plik:
            if len(slowo) > min_slowo:
                return slowo

