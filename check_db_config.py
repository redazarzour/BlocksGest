import os

db_host = os.getenv('PGHOST')
db_name = os.getenv('PGDATABASE')
db_user = os.getenv('PGUSER')

print(f"Database connection info:")
print(f"Host: {db_host}")
print(f"Database: {db_name}")
print(f"User: {db_user}")
print("Password: [HIDDEN]")
print(f"Port: {os.getenv('PGPORT')}")
