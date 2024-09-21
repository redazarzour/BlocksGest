from flask import render_template, request, jsonify, redirect, url_for, session, send_file
from flask_babel import _
from main import app, db, babel
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction, Delivery, Payment, Worker, Shift, Supplier, PurchaseOrder, PurchaseOrderItem
from utils import update_inventory, create_production_schedule, process_sale
from datetime import datetime, timedelta
from sqlalchemy import func
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import io
import csv

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
    schedules = ProductionSchedule.query.order_by(ProductionSchedule.scheduled_date).all()
    return jsonify([{'product_name': s.product_name, 'quantity': s.quantity, 'scheduled_date': s.scheduled_date.isoformat()} for s in schedules])

@app.route('/api/reports/sales', methods=['GET'])
def sales_report():
    days = request.args.get('days', default=30, type=int)
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    transactions = SalesTransaction.query.filter(
        SalesTransaction.transaction_date >= start_date,
        SalesTransaction.transaction_date <= end_date
    ).order_by(SalesTransaction.transaction_date).all()
    
    return jsonify([{
        'product_name': t.product_name,
        'quantity': t.quantity,
        'total_amount': t.total_amount,
        'transaction_date': t.transaction_date.isoformat()
    } for t in transactions])

@app.route('/labor')
def labor():
    workers = Worker.query.all()
    return render_template('labor.html', workers=workers)

@app.route('/api/worker/add', methods=['POST'])
def add_worker():
    data = request.json
    new_worker = Worker(
        name=data['name'],
        position=data['position'],
        hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d').date(),
        hourly_rate=float(data['hourly_rate'])
    )
    db.session.add(new_worker)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Worker added successfully'})

@app.route('/api/worker/update', methods=['POST'])
def update_worker():
    data = request.json
    worker = Worker.query.get_or_404(data['worker_id'])
    worker.name = data['name']
    worker.position = data['position']
    worker.hire_date = datetime.strptime(data['hire_date'], '%Y-%m-%d').date()
    worker.hourly_rate = float(data['hourly_rate'])
    db.session.commit()
    return jsonify({'success': True, 'message': 'Worker updated successfully'})

@app.route('/api/worker/delete', methods=['POST'])
def delete_worker():
    data = request.json
    worker = Worker.query.get_or_404(data['worker_id'])
    db.session.delete(worker)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Worker deleted successfully'})

@app.route('/api/shift/add', methods=['POST'])
def add_shift():
    data = request.json
    new_shift = Shift(
        worker_id=data['worker_id'],
        start_time=datetime.fromisoformat(data['start_time']),
        end_time=datetime.fromisoformat(data['end_time']),
        hours_worked=float(data['hours_worked'])
    )
    db.session.add(new_shift)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Shift added successfully'})

@app.route('/api/reports/labor', methods=['GET'])
def labor_report():
    workers = Worker.query.all()
    worker_data = []
    for worker in workers:
        total_hours = db.session.query(func.sum(Shift.hours_worked)).filter(Shift.worker_id == worker.id).scalar() or 0
        worker_data.append({
            'name': worker.name,
            'position': worker.position,
            'hire_date': worker.hire_date.isoformat(),
            'hourly_rate': worker.hourly_rate,
            'total_hours': float(total_hours)
        })
    return jsonify(worker_data)

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['ar', 'fr', 'en']:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/api/reports/kpi', methods=['GET'])
def kpi_report():
    try:
        total_sales = db.session.query(func.sum(SalesTransaction.total_amount)).scalar() or 0
        total_production = db.session.query(func.sum(ProductionSchedule.quantity)).scalar() or 0
        
        # Calculate inventory value with error handling
        inventory_value = 0
        raw_materials = RawMaterial.query.all()
        for rm in raw_materials:
            if hasattr(rm, 'unit_price'):
                inventory_value += rm.quantity * rm.unit_price
            else:
                app.logger.warning(f"RawMaterial {rm.id} does not have 'unit_price' attribute")
        
        labor_cost = db.session.query(func.sum(Worker.hourly_rate * Shift.hours_worked)).join(Shift).scalar() or 0

        return jsonify({
            'total_sales': float(total_sales),
            'total_production': int(total_production),
            'inventory_value': float(inventory_value),
            'labor_cost': float(labor_cost),
            'gross_profit': float(total_sales - inventory_value - labor_cost)
        })
    except Exception as e:
        app.logger.error(f"Error in KPI report: {str(e)}")
        return jsonify({'error': 'An error occurred while generating the KPI report'}), 500

@app.route('/api/reports/forecast', methods=['GET'])
def forecast_report():
    sales_data = SalesTransaction.query.with_entities(
        SalesTransaction.transaction_date, 
        func.sum(SalesTransaction.total_amount)
    ).group_by(SalesTransaction.transaction_date).order_by(SalesTransaction.transaction_date).all()

    df = pd.DataFrame(sales_data, columns=['date', 'sales'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    if len(df) < 3:
        return jsonify({
            'dates': [],
            'forecast': [],
            'error': 'Not enough data for forecasting'
        })

    try:
        model = ARIMA(df['sales'].astype(float), order=(1, 1, 1))
        results = model.fit()

        last_date = df.index[-1]
        future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30)

        forecast = results.forecast(steps=30)

        return jsonify({
            'dates': [date.strftime('%Y-%m-%d') for date in future_dates],
            'forecast': forecast.tolist()
        })
    except Exception as e:
        return jsonify({
            'dates': [],
            'forecast': [],
            'error': str(e)
        })

@app.route('/api/reports/kpi/export', methods=['GET'])
def export_kpi_report():
    kpi_data = kpi_report().json

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Metric', 'Value'])
    for key, value in kpi_data.items():
        writer.writerow([key.replace('_', ' ').title(), value])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='kpi_report.csv'
    )

@app.route('/api/reports/inventory/export', methods=['GET'])
def export_inventory_report():
    raw_materials = RawMaterial.query.all()
    finished_goods = FinishedGood.query.all()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Type', 'Name', 'Quantity', 'Unit'])
    for rm in raw_materials:
        writer.writerow(['Raw Material', rm.name, rm.quantity, rm.unit])
    for fg in finished_goods:
        writer.writerow(['Finished Good', fg.name, fg.quantity, 'units'])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='inventory_report.csv'
    )

@app.route('/api/reports/production/export', methods=['GET'])
def export_production_report():
    schedules = ProductionSchedule.query.order_by(ProductionSchedule.scheduled_date).all()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Product Name', 'Quantity', 'Scheduled Date'])
    for schedule in schedules:
        writer.writerow([schedule.product_name, schedule.quantity, schedule.scheduled_date])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='production_report.csv'
    )

@app.route('/api/reports/sales/export', methods=['GET'])
def export_sales_report():
    days = request.args.get('days', default=30, type=int)
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    transactions = SalesTransaction.query.filter(
        SalesTransaction.transaction_date >= start_date,
        SalesTransaction.transaction_date <= end_date
    ).order_by(SalesTransaction.transaction_date).all()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Product Name', 'Quantity', 'Total Amount', 'Transaction Date'])
    for transaction in transactions:
        writer.writerow([
            transaction.product_name,
            transaction.quantity,
            transaction.total_amount,
            transaction.transaction_date
        ])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='sales_report.csv'
    )

@app.route('/api/reports/labor/export', methods=['GET'])
def export_labor_report():
    workers = Worker.query.all()
    
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Name', 'Position', 'Hire Date', 'Hourly Rate', 'Total Hours'])
    for worker in workers:
        total_hours = db.session.query(func.sum(Shift.hours_worked)).filter(Shift.worker_id == worker.id).scalar() or 0
        writer.writerow([
            worker.name,
            worker.position,
            worker.hire_date,
            worker.hourly_rate,
            float(total_hours)
        ])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='labor_report.csv'
    )

@app.route('/suppliers')
def suppliers():
    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/api/supplier/add', methods=['POST'])
def add_supplier():
    data = request.json
    new_supplier = Supplier(
        name=data['name'],
        contact_person=data['contact_person'],
        email=data['email'],
        phone=data['phone'],
        address=data['address']
    )
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Supplier added successfully'})

@app.route('/api/supplier/update', methods=['POST'])
def update_supplier():
    data = request.json
    supplier = Supplier.query.get_or_404(data['supplier_id'])
    supplier.name = data['name']
    supplier.contact_person = data['contact_person']
    supplier.email = data['email']
    supplier.phone = data['phone']
    supplier.address = data['address']
    db.session.commit()
    return jsonify({'success': True, 'message': 'Supplier updated successfully'})

@app.route('/api/supplier/delete', methods=['POST'])
def delete_supplier():
    data = request.json
    supplier = Supplier.query.get_or_404(data['supplier_id'])
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Supplier deleted successfully'})

@app.route('/purchase_orders')
def purchase_orders():
    purchase_orders = PurchaseOrder.query.all()
    return render_template('purchase_orders.html', purchase_orders=purchase_orders)

@app.route('/api/purchase_order/add', methods=['POST'])
def add_purchase_order():
    data = request.json
    new_purchase_order = PurchaseOrder(
        supplier_id=data['supplier_id'],
        delivery_date=datetime.fromisoformat(data['delivery_date']),
        total_amount=data['total_amount']
    )
    db.session.add(new_purchase_order)
    db.session.commit()

    for item in data['items']:
        new_item = PurchaseOrderItem(
            purchase_order_id=new_purchase_order.id,
            raw_material_id=item['raw_material_id'],
            quantity=item['quantity'],
            unit_price=item['unit_price']
        )
        db.session.add(new_item)
    
    db.session.commit()
    return jsonify({'success': True, 'message': 'Purchase order added successfully'})

@app.route('/api/purchase_order/update', methods=['POST'])
def update_purchase_order():
    data = request.json
    purchase_order = PurchaseOrder.query.get_or_404(data['purchase_order_id'])
    purchase_order.supplier_id = data['supplier_id']
    purchase_order.delivery_date = datetime.fromisoformat(data['delivery_date'])
    purchase_order.status = data['status']
    purchase_order.total_amount = data['total_amount']

    # Remove existing items
    for item in purchase_order.items:
        db.session.delete(item)

    # Add updated items
    for item in data['items']:
        new_item = PurchaseOrderItem(
            purchase_order_id=purchase_order.id,
            raw_material_id=item['raw_material_id'],
            quantity=item['quantity'],
            unit_price=item['unit_price']
        )
        db.session.add(new_item)

    db.session.commit()
    return jsonify({'success': True, 'message': 'Purchase order updated successfully'})

@app.route('/api/purchase_order/delete', methods=['POST'])
def delete_purchase_order():
    data = request.json
    purchase_order = PurchaseOrder.query.get_or_404(data['purchase_order_id'])
    db.session.delete(purchase_order)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Purchase order deleted successfully'})

@app.route('/api/reports/suppliers', methods=['GET'])
def suppliers_report():
    suppliers = Supplier.query.all()
    supplier_data = []
    for supplier in suppliers:
        total_orders = PurchaseOrder.query.filter_by(supplier_id=supplier.id).count()
        total_amount = db.session.query(func.sum(PurchaseOrder.total_amount)).filter_by(supplier_id=supplier.id).scalar() or 0
        supplier_data.append({
            'name': supplier.name,
            'contact_person': supplier.contact_person,
            'email': supplier.email,
            'phone': supplier.phone,
            'total_orders': total_orders,
            'total_amount': float(total_amount)
        })
    return jsonify(supplier_data)

@app.route('/api/reports/purchase_orders', methods=['GET'])
def purchase_orders_report():
    purchase_orders = PurchaseOrder.query.all()
    po_data = []
    for po in purchase_orders:
        po_data.append({
            'id': po.id,
            'supplier_name': po.supplier.name,
            'order_date': po.order_date.isoformat(),
            'delivery_date': po.delivery_date.isoformat(),
            'status': po.status,
            'total_amount': float(po.total_amount)
        })
    return jsonify(po_data)