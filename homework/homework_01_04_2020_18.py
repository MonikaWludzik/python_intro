import openpyxl
import homework.homework_17_mar_2020_p4

#zadanie 18
#
# 1) odczyt danych
# 2) przygotowanie danych
# 3) rysowanie tabeli

with open ('lista_osob.csv', 'r+') as plik:
    # print(plik.read())

    dictionary_osoby = {}
    headers = plik.readline()
    headers = headers.rstrip().split(',')
    # option 1 - create an array, then loop through all lines.
    rows = []
    for line in plik.readlines():
        row = line.rstrip().split(",")
        rows.append(row)
        # lengths = [len(cell) for cell in row] #transforming values in a list; comprehension!!! in other langs, called "mapping"
        # the_longest = max(lengths)
        # print({headers[0]: row[0], headers[1]: row[1], headers[2]: row[2]})

    # option 2 - using comprehensions turns the previous 4 lines in to a single line!
    # rows = [line.rstrip().split(",") for line in plik.readlines()]


    homework.homework_17_mar_2020_p4.drawing_frames(headers, rows)
#loop througn headers

#modify the data



