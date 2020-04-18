class Item():
    def __init__(self):
        self.id
        self.title
        self.date_entry
        purchase_date = self.date_purchase
        item_amount = self.amount
        self.typ
        self.author
        self.pages
        self.format
        item_price = self.price
        self.currency

class Book(Item):
    def __init__(self):
        self.id
        self.title
        self.date_entry
        purchase_date = self.date_purchase
        item_amount = self.amount
        self.typ
        self.author
        self.pages
        self.format
        item_price = self.price
        self.currency

class Ebook(Book):
    def __init__(self):
        self.id
        self.title
        self.date_entry
        purchase_date = self.date_purchase
        item_amount = self.amount
        self.typ
        self.author
        self.pages
        self.format
        item_price = self.price
        self.currency

class Basket():
    def __init__(self):
        self.items = []

    def add_to_basket(self, item):
        self.items.append(item)
        pass

    def remove_from_basket(self, item):
        self.items.remove(item)
        pass

    def check_basket(self):
        print(self.items)
        pass
