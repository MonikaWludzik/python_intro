import homework.multitoolprog.Celsius
import homework.multitoolprog.Fahrenheit
import homework.multitoolprog.pieniadze
import homework.multitoolprog.piramida
import homework.multitoolprog.wiekpsa
import homework.multitoolprog.kwadrat
import random


choice = homework.multitoolprog.Celsius.interger_check("""Witaj w Multitool Python Program by iSA
   Wybierz program który cię interesuje:
   1) Rysowanie kwadratu o zadanych parametrach
   2) Rysowanie piramidy o określonej wysokości
   3) Rozmienianie pieniędzy
   4) Przeliczanie Fahrenheita na Celsiusa
   5) Przeliczanie Celsiusa na Fahrenheita 
   6) Obliczanie wieku psa
   7) Wybierz program losowo bo nie wiem czego szukam:)
   8) Wyjście z programu
   Twój wybór: _""")

while choice not in [1,2,3,4,5,6,7, 8]:
    choice = homework.multitoolprog.Celsius.interger_check("Podaj liczbę od 1 do 8: ")


def choicelist(choice):
    if choice == 1:
        homework.multitoolprog.kwadrat.draw_square()

    if choice == 2:
        homework.multitoolprog.piramida.piramida()

    if choice == 3:
        homework.multitoolprog.pieniadze.pieniadze()

    if choice == 4:
        homework.multitoolprog.Celsius.Ceslius()

    if choice == 5:
        homework.multitoolprog.Fahrenheit.Fahrenheit()

    if choice == 6:
        homework.multitoolprog.wiekpsa.wiekpsa()

    if choice == 7:
        list = [1,2,3,4,5,6,7,8]
        rando = random.choice(list)
        print(rando)
        choicelist(rando)

    if choice == 8:
        print("exit")

choicelist(choice)