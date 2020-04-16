#from words import get_random_word
import homework.hangman.lista_slow
import homework.multitoolprog.Celsius

def choose_between(prompt, min, max):
    liczba_prob = min - 2
    while (min <= liczba_prob <= max) is False:
        liczba_prob = homework.multitoolprog.Celsius.interger_check(prompt)
    return liczba_prob


def wyswietl_liczbe_prob():
    return choose_between("Okresl ilosc prob zgadniecia slowa (1-20): ", 1, 20)

def wyswietl_dlugosc_slowa():
    return choose_between("Ile liter ma miec slowo? (4-12): ", 4, 12)


class GameState:
    def __init__(self):
        self.proby = wyswietl_liczbe_prob()
        self.dlugosc = wyswietl_dlugosc_slowa()
        self.slowo = homework.hangman.lista_slow.wybierz_slowo(self.dlugosc)
        self.slowo_lista = list(self.slowo)
        self.won = False
        self.chosen = 0

    def record_choice(self, litera):
        self.chosen = self.chosen + 1
        self.slowo_lista.remove(litera)

    def all_chosen(self):
        return self.dlugosc == self.chosen

    def is_over(self):
        return self.proby == 0 or self.won

    def litera_w_slowie(cls):
        litera = input('Jaka litera jest w slowie? ')

        if litera in cls.slowo_lista:
            print(f'{litera} jest w slowie!')
            # record the correct letter
            cls.record_choice(litera)
            # if all correct letters are chosen
            if cls.all_chosen():
                # set win
                cls.won = True
                # end the game
        else:
            cls.proby = cls.proby - 1
            print(f'Zgaduj dalej! Masz jeszcze {cls.proby}!')

while True:
    game = GameState()
    while not game.is_over():
        game.litera_w_slowie()

    print('Koniec gry!')
    if game.won:
        print('Wygrales!')
    game1 = input('Czy chcesz zagrac jeszcze raz? T/N ')
    if game1 == 'N':
        print('Dzieki!')
        break
