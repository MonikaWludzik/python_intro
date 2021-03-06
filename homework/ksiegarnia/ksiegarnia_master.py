import openpyxl
import datetime
import os
import homework.homework_17_mar_2020_p4
import homework.ksiegarnia.model.Inventory
import homework.multitoolprog.Celsius

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

print("witaj w naszej ksiegarni! przejdz do listy produktow.")

class Inventory:
    def __init__(self):
        self.inventory = {}
        with open(os.path.join(script_dir, 'ksiegarnia_db.csv'), 'r+') as file:
            headers = file.readline()
            headers = headers.rstrip().split(',')
            rows = []
            for line in file.readlines():
                row = line.rstrip().split(",")
                id = int(row[0])
                rows.append(row)
                # todo: turn the array of values in to a class, based on its "type"
                item = homework.ksiegarnia.model.Inventory.Item()
                item.id = row[0]
                item.title = row[1]
                item.author = row[6]
                item.typ = row[5]
                try:
                    item.amount = int(row[4])
                except:
                    item.amount = -1
                item.price = float(row[9])
                self.inventory[id] = item

    def stock(self):
        return self.inventory.values()

    def get(self, id):
        return self.inventory[int(id)]

    def pull(self, id):
        item_id = int(id)
        if item_id not in self.inventory.keys():
            print('No such item in the inventory.')
        else:
            item_to_get = self.inventory[item_id]
            # todo: use a class instead of an array of values
            amount = int(item_to_get.amount)
            item_to_get.amount = str(amount - 1)
            return item_to_get

    def reclaim(self, id):
        item_id = int(id)
        if item_id not in self.inventory.keys():
            print("We don't sell that... stop it. This is harrassment!")
        else:
            item_to_reclaim = self.inventory[item_id]
            item_to_reclaim.amount += 1

inventory = Inventory()
cart = homework.ksiegarnia.model.Inventory.Basket()

def pokaz_produkty():
    homework.homework_17_mar_2020_p4.drawing_frames(headers, rows)


def buy_something():
    user_wants = homework.multitoolprog.Celsius.interger_check('what item do you want? enter its id: ')
    item = inventory.pull(user_wants)
    cart.add_to_basket(item)


def pokaz_koszyk():
    print('here is what you want to buy!')
    cart.check_basket()

def confirm_purchase():
    cost = cart.total_cost() #instance of class Basket is cart
    print('this basket will cost you ' + str(cost))


def start_shopping():
    while True:
        user_wants = input('what do you want to do? choose from the following [s]how our wares, [b]uy a thing, pokaz [k]oszyk, [c]heckout, [e]xit. your answer: ')
        if user_wants not in ['s', 'b', 'k', 'c', 'e']:
            print('I do not understand. Try again!')
        if user_wants == 's':
            pokaz_produkty()
        if user_wants == 'b':
            buy_something()
        if user_wants == 'k':
            pokaz_koszyk()
        if user_wants == 'c':
            confirm_purchase()
        if user_wants == 'e':
            break
    print('thanks for shopping with us!')


start_shopping()