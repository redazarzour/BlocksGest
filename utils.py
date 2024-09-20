from main import db
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction
from datetime import datetime

def update_inventory(item_type, item_id, quantity):
    if item_type == 'raw_material':
        item = RawMaterial.query.get(item_id)
    elif item_type == 'finished_good':
        item = FinishedGood.query.get(item_id)
    elif item_type == 'work_in_progress':
        item = WorkInProgress.query.get(item_id)
    else:
        return {'success': False, 'message': 'Invalid item type'}

    if item:
        item.quantity = quantity
        db.session.commit()
        return {'success': True, 'message': 'Inventory updated successfully'}
    else:
        return {'success': False, 'message': 'Item not found'}

def create_production_schedule(product_name, quantity, scheduled_date):
    schedule = ProductionSchedule(product_name=product_name, quantity=quantity, scheduled_date=datetime.fromisoformat(scheduled_date))
    db.session.add(schedule)
    db.session.commit()
    return {'success': True, 'message': 'Production schedule created successfully'}

def process_sale(product_name, quantity, total_amount):
    finished_good = FinishedGood.query.filter_by(name=product_name).first()
    if finished_good and finished_good.quantity >= quantity:
        finished_good.quantity -= quantity
        transaction = SalesTransaction(product_name=product_name, quantity=quantity, total_amount=total_amount)
        db.session.add(transaction)
        db.session.commit()
        return {'success': True, 'message': 'Sale processed successfully'}
    else:
        return {'success': False, 'message': 'Insufficient inventory'}
