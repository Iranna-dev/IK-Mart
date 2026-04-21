from flask import Blueprint, jsonify
from models import db, Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def get_products():
    products = db.session.query(Product).all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description
        })

    return jsonify(result)

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    from flask import request

    data = request.get_json()

    product = Product.query.get(id)

    if not product:
        return {"message": "Product not found"}, 404

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get('description', product.description)

    db.session.commit()

    return {"message": "Product updated successfully"}