from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, get_locale
from flask_migrate import Migrate  # Add this line
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
babel = Babel(app)
migrate = Migrate(app, db)  # Add this line

def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'ar']) or 'en'

babel.init_app(app, locale_selector=get_locale)
app.jinja_env.globals.update(get_locale=get_locale)

from routes import *
from models import RawMaterial, FinishedGood, WorkInProgress, ProductionSchedule, SalesTransaction, Delivery, Payment, Worker, Shift

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5001)  # Changed port to 5001
