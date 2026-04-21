from flask import Blueprint

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist')
def get_wishlist():
    return {"message": "wishlist route working"}
