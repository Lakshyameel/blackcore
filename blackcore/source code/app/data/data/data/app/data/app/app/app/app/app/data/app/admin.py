@admin.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        return "Access Denied", 403

    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.role = request.form.get('role')
        db.session.commit()
        return redirect(url_for('admin.admin_panel'))
    return render_template('edit_user.html', user=user)

@admin.route('/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return "Access Denied", 403

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.admin_panel'))

@admin.route('/delete_commodity/<int:commodity_id>')
@login_required
def delete_commodity(commodity_id):
    if current_user.role != 'admin':
        return "Access Denied", 403

    commodity = Commodity.query.get_or_404(commodity_id)
    db.session.delete(commodity)
    db.session.commit()
    return redirect(url_for('admin.admin_panel'))

