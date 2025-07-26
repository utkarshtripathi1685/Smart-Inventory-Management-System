from flask import Blueprint, render_template, request, redirect, url_for
from modules.product import Product
from modules.inventory import Inventory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    inv = Inventory()
    items = inv.view_inventory()
    return render_template('index.html', inventory=items)

@main.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        quantity = int(request.form['quantity'])
        category = request.form['category']

        product = Product(name, price, quantity, category)
        inv = Inventory()
        inv.add_product(product)

        return redirect(url_for('main.index'))
    
    return render_template('add.html')

@main.route('/delete/<string:name>', methods=['POST'])
def delete_product(name):
    inv = Inventory()
    success = inv.remove_product(name)
    return redirect(url_for('main.index'))
