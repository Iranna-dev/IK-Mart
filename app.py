from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from auth import auth_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.wishlist import wishlist_bp
from routes.orders import orders_bp
from routes.reviews import reviews_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(products_bp, url_prefix='/api')
app.register_blueprint(cart_bp, url_prefix='/api')
app.register_blueprint(wishlist_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(reviews_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/api')

from models import Product

with app.app_context():
    db.create_all()

    if Product.query.count() == 0:
        db.session.add(Product(name="Laptop", price=60000, description="Gaming laptop"))
        db.session.add(Product(name="Phone", price=20000, description="Smartphone"))
        db.session.add(Product(name="TV", price=30000, description="Smart TV"))
        db.session.commit()

if __name__ == "__main__":
    app.run()