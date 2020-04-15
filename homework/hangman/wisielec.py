#from words import get_random_word
import homework.hangman.lista_slow




def wyswietl_liczbe_prob():
    liczba_prob = ""
    while liczba_prob.isnumeric() is False:
        liczba_prob = input("Okresl ilosc prob zgadniecia slowa (1-20): ")
        if 1 <= int(liczba_prob) <= 20:
            return int(liczba_prob)

def wyswietl_dlugosc_slowa():
    dlugosc_slowa = ""
    while dlugosc_slowa.isnumeric() is False:
        dlugosc_slowa = input("Ile liter ma miec slowo? (4-12): ")
        if 4 <= int(dlugosc_slowa) <= 12:
            return int(dlugosc_slowa)




class GameState:
    def __init__(self):
        self.proby = wyswietl_liczbe_prob()
        self.dlugosc = wyswietl_dlugosc_slowa()
        self.slowo = homework.hangman.lista_slow.wybierz_slowo(self.dlugosc)
        self.won = False
        self.chosen = 0

    def all_chosen(self):
        return self.dlugosc == self.chosen

    def is_over(self):
        return self.proby == 0 or self.won

    def litera_w_slowie(cls):
        litera = input('Jaka litera jest w slowie? ')
        if litera in cls.slowo:
            print(f'{litera} jest w slowie!')
            # record the correct letter
            cls.chosen = cls.chosen + 1
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

    print('game is done')
    if game.won:
        print('yu win!')
    game1 = input('Do you want to play again? Y/N ')
    if game1 == 'N':
        print('Thank you!')
        break
