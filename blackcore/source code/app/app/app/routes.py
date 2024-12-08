from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Commodity
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    data = Commodity.query.all()
    return render_template('dashboard.html', commodities=data)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        pass
    return render_template('login.html')
