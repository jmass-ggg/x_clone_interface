from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
file_name = 'login.json'

def load_users():
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_users(users):
    with open(file_name, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        user_password = request.form['password']
        users = load_users()
        user = next((u for u in users if u['username'] == user_name), None)
        if user and user['password'] == user_password:
            return redirect(url_for('home'))  # Redirect to /home after login
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        users = load_users()
        user_exists = any(u['username'] == user_name or u.get('email') == user_email for u in users)
        if user_exists:
            return render_template('resister.html', error="User already exists")
        user_data = {
            'username': user_name,
            'email': user_email,
            'password': user_password
        }
        users.append(user_data)
        save_users(users)
        return redirect(url_for('login'))
    return render_template('resister.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
