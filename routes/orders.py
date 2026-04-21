from flask import Blueprint, jsonify
from models import db, Cart, Product, Order

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/order', methods=['POST'])
def place_order():
    cart_items = Cart.query.all()

    if not cart_items:
        return {"message": "Cart is empty"}

    for item in cart_items:
        product = Product.query.get(item.product_id)

        order = Order(
            product_name=product.name,
            price=product.price,
            quantity=item.quantity
        )

        db.session.add(order)

    # clear cart
    Cart.query.delete()

    db.session.commit()

    return {"message": "Order placed successfully"}


@orders_bp.route('/order')
def get_orders():
    orders = Order.query.all()

    result = []
    for o in orders:
        result.append({
            "product_name": o.product_name,
            "price": o.price,
            "quantity": o.quantity
        })

    return jsonify(result)