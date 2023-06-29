from flask import Blueprint

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('/<int:post_id>', methods = ['GET'])
def get_exact_post_comments(post_id: int):
    pass

@comment_bp.route('/<int:post_id>/<int:comment_id>', methods=['POST'])
def change_comment(post_id: int, comment_id: int ):
    pass

# @comment_bp.route('/<int:')
