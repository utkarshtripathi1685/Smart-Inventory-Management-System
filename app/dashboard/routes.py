from flask import Blueprint, session, url_for, redirect, render_template
from modules.inventory import Inventory


dashboard = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard.route('/dashboard')
def home():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    inv = Inventory(session['user'])  # ✅ Safe here
    inventory = inv.view_inventory()

    return render_template('dashboard.html', 
                           user=session['user'], 
                           store=session['store_name'],
                           type=session['store_type'],
                           inventory=inventory)

