from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from models import db, Cart

cart_bp = Blueprint('cart', __name__)

# Add to cart
@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()

    item = Cart(
        product_id=data['product_id'],
        quantity=data['quantity']
    )

    db.session.add(item)
    db.session.commit()

    return {"message": "Added to cart"}


# Get cart
@cart_bp.route('/cart')
def get_cart():
    from models import Product

    items = Cart.query.all()

    result = []
    for i in items:
        product = Product.query.get(i.product_id)

        result.append({
            "product_name": product.name,
            "price": product.price,
            "quantity": i.quantity
        })

    return jsonify(result)
    items = Cart.query.all()

    result = []
    for i in items:
        result.append({
            "id": i.id,
            "product_id": i.product_id,
            "quantity": i.quantity
        })

    return jsonify(result)