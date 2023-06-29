from database.models import Post, PostPhoto, PostComment, db


def get_all_post_db():
    posts = Post.query.all()
    return posts

def get_all_photo_db():
    photos = PostPhoto.query.all()
    return photos

def get_exact_post_db(post_id):
    exact_post = Post.query.filter_by(post_id=post_id).first()
    return exact_post

def delete_exact_post_db(post_id):
    delete_post = Post.query.filter_by(post_id=post_id).first()
    if delete_post:
        db.session.delete(delete_post)
        db.session.commit()
    else:
        return False

def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        post.post_text = new_text
        db.session.commit()

def add_new_post_db(user_id, photo_id, post_text):
    new_post = Post(user_id= user_id, photo=photo_id, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()

    return new_post.post_id
def add_comment_post(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()

def post_new_photo_db(user_id, photo_path):
    new_post_photo = PostPhoto(user_id, photo_path = photo_path)

    db.session.add(new_post_photo)
    db.session.commit()

def get_exact_hashtag_db(user_id, photo_path):
    get_exact_hashtag = HashTag.query.filter(hashtag_name).all()
    if get_exact_hashtag:
        return get_exact_hashtag
    return False

def create_post_for_hashtag(post_id, hashtags):
    created_hashtags=[]
    for hashtag_name in hashtags:
        new_hashtag_post = HashTag(post_id=post_id, hashtag_name=hashtag_name)
        created_hashtags.append(new_hashtag_post)

    db.session.add_all(created_hashtags)
    db.session.commit()

    return True