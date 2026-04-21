from flask import Blueprint

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviews')
def get_reviews():
    return {"message": "reviews route working"}