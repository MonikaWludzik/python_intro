from homework.ksiegarnia.ksiegarnia_master import Inventory
from homework.ksiegarnia.model.Inventory import Basket, Book, Ebook, Item
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

inventory = Inventory()
cart = Basket()

@app.route('/')
def show_bookstore():
    products = inventory.stock()
    in_cart = len(cart.show())
    return render_template('index.html', products=products, in_cart=in_cart)

@app.route('/product/<id>')
def show_product(id):
    product = inventory.get(id)
    return render_template('product.html', product=product)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    id = int(request.form['id'])
    item = inventory.pull(id)
    cart.add_to_basket(item)
    return redirect(url_for('show_bookstore'))

@app.route('/cart/update', methods=['POST'])
def update_cart():
    id = request.form['id']
    qty = int(request.form['qty'])
    cart.change_amount(id, qty)
    return redirect(url_for('show_cart'))

@app.route('/cart', methods=['GET'])
def show_cart():
    cost = cart.total_cost()
    items = cart.show()
    return render_template('cart.html', cost=cost, items=items)


app.run()