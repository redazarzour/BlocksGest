from main import db
from models import RawMaterial

def update_raw_materials():
    raw_materials = RawMaterial.query.all()
    for rm in raw_materials:
        if rm.unit_price is None:
            rm.unit_price = 0.0
    db.session.commit()
    print("Raw materials updated successfully.")

if __name__ == "__main__":
    update_raw_materials()
