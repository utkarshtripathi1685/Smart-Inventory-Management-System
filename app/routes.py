from flask import Blueprint, render_template
from modules.inventory import Inventory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    inv = Inventory()
    items = inv.view_inventory()
    return render_template('index.html', inventory=items)
