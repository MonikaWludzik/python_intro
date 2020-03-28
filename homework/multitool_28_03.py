import homework.multitoolprog.Celsius
import homework.multitoolprog.Fahrenheit
import homework.multitoolprog.pieniadze
import homework.multitoolprog.piramida
import homework.multitoolprog.wiekpsa
import homework.multitoolprog.kwadrat
import homework.multitoolprog.exitor
import random

# wybor kolejnego prog, 8 wyjscie, litery i liczby + licznik uruchomien

iterations = 0

while True:
    choice = input("""Witaj w Multitool Python Program by iSA
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

    while choice not in ['1', '2', '3', '4', '5', '6', "R", "X"]:
        choice = input("Podaj liczbę od 1 do 6 lub R albo X: ")

    iterations = iterations + 1

    functions = {"1": homework.multitoolprog.kwadrat.draw_square, "2": homework.multitoolprog.piramida.piramida,
                 "3": homework.multitoolprog.pieniadze.pieniadze, "4": homework.multitoolprog.Celsius.Ceslius,
                 "5": homework.multitoolprog.Fahrenheit.Fahrenheit, "6": homework.multitoolprog.wiekpsa.wiekpsa,
                 "X": homework.multitoolprog.exitor.exitor}

    if choice == "R":
        choice = random.choice(list(functions.keys()))

    fn = functions[choice]
    fn()

    if choice == "X":
        break

print(iterations)






