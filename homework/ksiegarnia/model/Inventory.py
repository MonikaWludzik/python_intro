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
        self.items = []

    def add_to_basket(self, item):
        self.items.append(item)
        print (f'You chose {item}')

    def remove_from_basket(self, item):
        self.items.remove(item)
        pass

    def check_basket(self):
        print(self.items)
        total_cost = self.total_cost()
        total_items = len(self.items)
        print(f'Total price: {total_cost}, total items: {total_items}')
        pass

    def total_cost(self):
        costs = [item.price for item in self.items]
        total_cost = sum(costs)
        return total_cost

#print(item) # python's beahviour is to call __str__
#print([item, item, item]) # python's behaiour is to call __repr__ on each thing in the list