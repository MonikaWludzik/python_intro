class Item():
    def __init__(self):
        self.id = 0
        self.title = ''
        # self.date_entry
        # self.date_purchase
        self.amount = 0
        # self.typ
        # self.author
        # self.pages
        # self.format
        self.price = 0
        # self.currency

    def __str__(self):
        return f'Item "{self.title}" RRP {self.price}'


    def __repr__(self):
        return self.__str__()

class Book(Item):
    def __init__(self):
        super().__init__()

class Ebook(Book):
    def __init__(self):
        super().__init__()

class Basket():
    def __init__(self):
        # self.items = []
        self.inside = {}

    def add_to_basket(self, item):
        if item.id in self.inside:
            existing = self.inside[item.id]
            existing['quantity'] += 1
        else:
            newthing = {}
            newthing['id'] = item.id
            newthing['title'] = item.title
            newthing['price'] = item.price
            newthing['quantity'] = 1
            self.inside[item.id] = newthing

        # self.items.append(item)
        print (f'You chose {item}')
        print ('current basket', self.inside)

    def remove_from_basket(self, item):
        if item.id in self.inside:
            existing = self.inside[item.id]
            existing['quantity'] -= 1
            # let's not pay the customer money for them NOT taking our stuff.
            if existing['quantity'] <= 0:
                del self.inside[item.id]
        # self.items.remove(item)
        pass

    def change_amount(self, id, qty):
        if id in self.inside:
            if qty <= 0:
                del self.inside[id]
            else:
                existing = self.inside[id]
                existing['quantity'] = qty

    def check_basket(self):
        print(self.inside)
        total_cost = self.total_cost()
        total_items = sum([thing['quantity'] for thing in self.inside.values()])
        print(f'Total price: {total_cost}, total items: {total_items}')
        pass

    def show(self):
        return self.inside.values()

    def total_cost(self):
        costs = [thing['price'] * thing['quantity'] for thing in self.inside.values()]
        total_cost = sum(costs)
        return total_cost

#print(item) # python's beahviour is to call __str__
#print([item, item, item]) # python's behaiour is to call __repr__ on each thing in the list