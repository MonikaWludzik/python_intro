licznik = 0
while licznik < 10:
    licznik += 1
    if licznik == 5:
        continue

    print(licznik)

#if licznik in [5,8]
#conitnue skips an iteration in a loop

licznik = 0
while licznik < 10:
    licznik += 1
    if licznik == 5:
        break

    print(licznik)

#break wyjscie z petli
#break also possible for embedded loops

#for element in zbior/zakres/krotka continue i break
#zakres tylko w loopie, poza loopem tylko ostatnia wartosc

zdanie = 'Ala ma kota'
for litera in zdanie:
    print(litera)
print(litera)

#calkowity rozmiar, list, range

for i in range (0,10,3):
    print(i)

#enumerate(lista) >> indeks + wartosc
#iteracja na kilku listach na raz



