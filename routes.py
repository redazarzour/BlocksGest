from flask import render_template, request, jsonify, redirect, url_for
from main import app, db
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction, Delivery, Payment
from utils import update_inventory, create_production_schedule, process_sale
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    raw_materials = RawMaterial.query.all()
    finished_goods = FinishedGood.query.all()
    work_in_progress = WorkInProgress.query.all()
    return render_template('inventory.html', raw_materials=raw_materials, finished_goods=finished_goods, work_in_progress=work_in_progress)

@app.route('/api/inventory/update', methods=['POST'])
def update_inventory_api():
    data = request.json
    result = update_inventory(data['item_type'], data['item_id'], data['quantity'])
    return jsonify(result)

@app.route('/production')
def production():
    schedules = ProductionSchedule.query.all()
    return render_template('production.html', schedules=schedules)

@app.route('/api/production/schedule', methods=['POST'])
def create_production_schedule_api():
    data = request.json
    result = create_production_schedule(data['product_name'], data['quantity'], data['scheduled_date'])
    return jsonify(result)

@app.route('/sales')
def sales():
    transactions = SalesTransaction.query.all()
    return render_template('sales.html', transactions=transactions)

@app.route('/api/sales/process', methods=['POST'])
def process_sale_api():
    data = request.json
    result = process_sale(data['product_name'], data['quantity'], data['total_amount'])
    if result['success']:
        # Create initial delivery and payment records
        new_transaction = SalesTransaction.query.order_by(SalesTransaction.id.desc()).first()
        delivery = Delivery(sales_transaction_id=new_transaction.id, quantity=data['quantity'])
        payment = Payment(sales_transaction_id=new_transaction.id, amount=data['total_amount'])
        db.session.add(delivery)
        db.session.add(payment)
        db.session.commit()
    return jsonify(result)

@app.route('/transaction/<int:transaction_id>')
def transaction_details(transaction_id):
    transaction = SalesTransaction.query.get_or_404(transaction_id)
    return render_template('transaction_details.html', transaction=transaction)

@app.route('/api/delivery/update', methods=['POST'])
def update_delivery():
    data = request.json
    delivery = Delivery.query.get_or_404(data['delivery_id'])
    delivery.quantity = data['quantity']
    delivery.delivery_date = datetime.fromisoformat(data['delivery_date'])
    delivery.status = data['status']
    db.session.commit()
    return jsonify({'success': True, 'message': 'Delivery updated successfully'})

@app.route('/api/payment/update', methods=['POST'])
def update_payment():
    data = request.json
    payment = Payment.query.get_or_404(data['payment_id'])
    payment.amount = data['amount']
    payment.payment_date = datetime.fromisoformat(data['payment_date'])
    payment.status = data['status']
    db.session.commit()
    return jsonify({'success': True, 'message': 'Payment updated successfully'})

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/api/reports/inventory', methods=['GET'])
def inventory_report():
    raw_materials = RawMaterial.query.all()
    finished_goods = FinishedGood.query.all()
    return jsonify({
        'raw_materials': [{'name': rm.name, 'quantity': rm.quantity, 'unit': rm.unit} for rm in raw_materials],
        'finished_goods': [{'name': fg.name, 'quantity': fg.quantity} for fg in finished_goods]
    })

@app.route('/api/reports/production', methods=['GET'])
def production_report():
    schedules = ProductionSchedule.query.all()
    return jsonify([{'product_name': s.product_name, 'quantity': s.quantity, 'scheduled_date': s.scheduled_date.isoformat()} for s in schedules])

@app.route('/api/reports/sales', methods=['GET'])
def sales_report():
    transactions = SalesTransaction.query.all()
    return jsonify([{'product_name': t.product_name, 'quantity': t.quantity, 'total_amount': t.total_amount, 'transaction_date': t.transaction_date.isoformat()} for t in transactions])
