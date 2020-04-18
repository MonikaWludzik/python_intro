import openpyxl
import datetime
import homework.homework_17_mar_2020_p4
import homework.ksiegarnia.model.Inventory

print("Witaj w naszej ksiegarni! Przejdz do listy produktow.")

inventory = {}
with open('ksiegarnia_db.csv', 'r+') as file:
    headers = file.readline()
    headers = headers.rstrip().split(',')
    rows = []
    for line in file.readlines():
        row = line.rstrip().split(",")
        id = row[0]
        rows.append(row)
        # todo: turn the array of values in to a class, based on its "type"
        inventory[id] = row


cart = homework.ksiegarnia.model.Inventory.Basket()

def pokaz_produkty():
    homework.homework_17_mar_2020_p4.drawing_frames(headers, rows)

def pull_from_inventory(item_id):
    # todo: ensure the item_id exists in the inventory... handle when it is not something we have
    item_to_get = inventory[item_id]
    # todo: use a class instead of an array of values
    amount = int(item_to_get[4])
    item_to_get[4] = str(amount - 1)
    return item_to_get[0]

def buy_something():
    # todo: make sure this is a valid integer
    user_wants = input('what item do you want? enter its ID: ')
    item = pull_from_inventory(user_wants)
    cart.add_to_basket(item)

def pokaz_koszyk():
    print('Here is what you want to buy!')
    print(cart.items)

def confirm_purchase():
    cost = 0
    for item in cart.items:
        # todo: look up the cost of the item, add to total cost
        pass
    #todo: maybe turn this routine in to a method on the basket class ;)
    print('This basket will cost you ' + str(cost))


def start_shopping():
    while True:
        user_wants = input('what do you wanna do? [S]how our wares, [B]uy a thing, Pokaz [K]oszyk, [C]heckout, [E]xit')
        # TODO: check valid values. re-use the function ;)

        if user_wants == 'S':
            pokaz_produkty()
        if user_wants == 'B':
            buy_something()
        if user_wants == 'K':
            pokaz_koszyk()
        if user_wants == 'C':
            confirm_purchase()
        if user_wants == 'E':
            break
    print('Thanks for shopping with us!')


start_shopping()