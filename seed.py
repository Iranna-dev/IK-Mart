from app import app
from models import db, Product

with app.app_context():
    db.create_all()   # IMPORTANT

    p1 = Product(name="Laptop", price=50000, description="Gaming laptop")
    p2 = Product(name="Phone", price=20000, description="Smartphone")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    print("Data inserted")