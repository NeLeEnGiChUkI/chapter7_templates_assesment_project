from app import app
from flask import render_template 


@app.route('/')
@app.route('/shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='shop')


@app.route('/register')
def register():
    """Register URL"""
    return render_template('register.html', title='register')


@app.route('/login')
def login():
    """Login URL"""
    return render_template('login.html', title='login')
