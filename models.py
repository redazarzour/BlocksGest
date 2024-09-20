from main import db
from datetime import datetime

class RawMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)

class FinishedGood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class WorkInProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class ProductionSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)

class SalesTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deliveries = db.relationship('Delivery', backref='sales_transaction', lazy=True)
    payments = db.relationship('Payment', backref='sales_transaction', lazy=True)

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales_transaction_id = db.Column(db.Integer, db.ForeignKey('sales_transaction.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Pending')

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales_transaction_id = db.Column(db.Integer, db.ForeignKey('sales_transaction.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Pending')

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    shifts = db.relationship('Shift', backref='worker', lazy=True)

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
