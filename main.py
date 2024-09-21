from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, get_locale
from flask_migrate import Migrate
from config import Config
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
babel = Babel(app)
migrate = Migrate(app, db)

def get_locale():
    logger.debug(f"Request headers: {request.headers}")
    logger.debug(f"Accept languages: {request.accept_languages}")
    selected_lang = request.accept_languages.best_match(['en', 'fr', 'ar']) or 'en'
    logger.debug(f"Selected language: {selected_lang}")
    return selected_lang

babel.init_app(app, locale_selector=get_locale)
app.jinja_env.globals.update(get_locale=get_locale)

from routes import *
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction, Delivery, Payment, Worker, Shift

if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")
    
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        logger.error(f"Error starting the application: {str(e)}")
