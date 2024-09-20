from main import app, db
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)
    columns = inspector.get_columns('raw_material')
    print("Columns in raw_material table:")
    for column in columns:
        print(f"- {column['name']}: {column['type']}")
