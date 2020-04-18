from typing import Any, Union

import homework.multitoolprog.Celsius
import homework.multitoolprog.Fahrenheit
import homework.multitoolprog.pieniadze
import homework.multitoolprog.piramida
import homework.multitoolprog.wiekpsa
import homework.multitoolprog.kwadrat
import homework.multitoolprog.exitor
import homework.hangman.wisielec
import homework.hangman.lista_slow
import random
import csv

# wybor kolejnego prog, 8 wyjscie, litery i liczby + licznik uruchomien

iterations = 0
prog_run = {}

while True:
    choice = input("""Witaj w Multitool Python Program by iSA
       Wybierz program który cię interesuje:
       1) Rysowanie kwadratu o zadanych parametrach
       2) Rysowanie piramidy o określonej wysokości
       3) Rozmienianie pieniędzy
       4) Przeliczanie Fahrenheita na Celsiusa
       5) Przeliczanie Celsiusa na Fahrenheita 
       6) Obliczanie wieku psa
       7) Wisielec gra
       R) Wybierz program losowo bo nie wiem czego szukam:)
       X) Wyjście z programu
       Twój wybór: _""")

    while choice not in ['1', '2', '3', '4', '5', '6', '7', "R", "X"]:
        choice = input("Podaj liczbę od 1 do 7 lub R albo X: ")

    iterations = iterations + 1

    functions = {"1": homework.multitoolprog.kwadrat.draw_square, "2": homework.multitoolprog.piramida.piramida,
                 "3": homework.multitoolprog.pieniadze.pieniadze, "4": homework.multitoolprog.Celsius.Ceslius,
                 "5": homework.multitoolprog.Fahrenheit.Fahrenheit, "6": homework.multitoolprog.wiekpsa.wiekpsa,
                 "7": homework.hangman.wisielec.wisielec, "X": homework.multitoolprog.exitor.exitor}

    if choice == "R":
        choice = random.choice(list(functions.keys()))

    try:
        num_run = prog_run[choice]
        prog_run[choice] = num_run + 1
    except:
        prog_run[choice] = 1

    fn = functions[choice]
    fn()

    if choice == "X":
        break

print(iterations)
print(prog_run)

with open ("statystki.csv", 'w+') as stats:
    csv_columns = ['Funkcja', 'Liczba uruchomien']
    writer = csv.writer(stats)

    value = prog_run[choice]
    writer.writerow(csv_columns)

    for key in prog_run:
        name = key
        writer.writerow([name, prog_run[key]])


    # for line in prog_run:
    #     writer.writerow("funkcja" + row)
    # for row in iterations:
    #     writer.writerow (row)
    # num_run = prog_run[choice]
    # prog_run[choice] = num_run + 1
    # stats_writer = stats.writerow(prog_run, num_run)









