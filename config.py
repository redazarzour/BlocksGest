import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
