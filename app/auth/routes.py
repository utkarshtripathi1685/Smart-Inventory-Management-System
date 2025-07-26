from flask import Blueprint, render_template, request, redirect, url_for, session
import json
import os

auth = Blueprint('auth', __name__, template_folder='templates')


USER_FILE = 'data/users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        store_name = request.form['store_name']
        store_type = request.form['store_type']

        users = load_users()
        if any(u['username'] == username for u in users):
            return "Username already exists"

        users.append({
            'username': username,
            'password': password,
            'store_name': store_name,
            'store_type': store_type
        })

        save_users(users)
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            session['user'] = user['username']
            session['store_name'] = user['store_name']
            session['store_type'] = user['store_type']
            return redirect(url_for('dashboard.home'))

        return "Invalid credentials"
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
