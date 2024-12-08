# app/admin.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Commodity
from . import db

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_panel():
    if current_user.role != 'admin':
        return "Access Denied", 403

    users = User.query.all()
    commodities = Commodity.query.all()
    return render_template('admin_panel.html', users=users, commodities=commodities)
