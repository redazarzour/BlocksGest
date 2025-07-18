import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=(LocalDB)\\MSSQLLocalDB;DATABASE=C:\\Database\\ConcreteBlocks.mdf;Trusted_Connection=yes;"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
