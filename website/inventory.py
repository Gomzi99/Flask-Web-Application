# wasnt able to integrate this
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from models import InventoryItem, db

bp = Blueprint('inventory', __name__)

@bp.route('/inventory')
@login_required
def view_inventory():
    inventory_items = InventoryItem.query.all()
    return render_template('view_inventory.html', inventory_items=inventory_items)

@bp.route('/add_item', methods=['POST'])
@login_required
def add_item():
    name = request.form.get('name')
    quantity = request.form.get('quantity')

    new_item = InventoryItem(name=name, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    flash('Item added successfully!', 'success')

    return redirect(url_for('inventory.view_inventory'))
