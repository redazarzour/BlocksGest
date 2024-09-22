from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction, Delivery, Payment, Worker, Shift

if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            logger.info("تم إنشاء جداول قاعدة البيانات بنجاح")
        except Exception as e:
            logger.error(f"خطأ في إنشاء جداول قاعدة البيانات: {str(e)}")
    
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        logger.error(f"خطأ في بدء التطبيق: {str(e)}")
