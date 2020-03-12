#ksiazka
#tytul = "Ksiazka pod tytutlem \"OKO\"."
#print(tytul)
#same for apostrophes in English
#formatowanie
#liczba = 2.3
#print('Wprowadz liczbe: + str(liczba)')
#print(f'Wprowadz liczbe: + {liczba}')
#it can be inside and it can replicated
#indeksy
#nie ma zera od konca
#[::-1] odwrocenie stringa
#if, elif, elif (inny warunek)
#zmienna po if

#append dodawanie nowego elementu do listy; jednego elementu do listy
#usuwa element z listy funkcja del del(lista_3[0])
#remove lista3.remove("dom")

list_a = [2, 'house', 'street', 32, 1000, 51, 'road']
print(list_a)

if 'house' in list_a:
    list_a.remove("house")
else:
    print('does not exist')
print(list_a)

#indeks - kwadratowy nawias [int]
#lista zagniezdzona - mutable

list_b = [[1,2,3], [4,5,6],[7,8,9]]
print(list_b[1][2])
print(list_b[1][1])
print(list_b[2])

#tuple = krotka - immutable
#read_only, mozna iterowac krotka = (1,2,3) - nawiasy okragle - inne od listy gdzie sa kwadratowe, elementy sa mutable

krotka1 = ("jeden", "dwa", "trzy")
print(type(krotka1))
print(krotka1[2])

#petla
#nieskonczona petla
#uwaga na spacje po input

czy_kontynuac = 'T'
while czy_kontynuac == 'T':
    print('.')
    czy_kontynuac = input('Czy kontynowac [T/N]')

print("Koniec")

licznik = 0
while licznik < 10:
    print('.')
    licznik = licznik + 1 #to samo licznik += 1
print("Koniec")