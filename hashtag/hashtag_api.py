from flask import Blueprint

hashtag_bp = Blueprint('hashtag', __name__, url_prefix = '/hashtag')

@hashtag_bp.route('/', methods=['GET'])
def get_hashtags(size:int):
    pass

@hashtag_bp.route('/<string:hashtag_name>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    pass