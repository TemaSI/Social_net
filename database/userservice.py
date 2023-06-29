from database.models import User, db, Password

def register_user_db(**user_data):
    new_user = User(**user_data)

    db.session.add(new_user)
    db.session.commit()

def check_user_db(email):
    checker_email = User.query.filter_by(email=email).first()
    if checker_email:
        return True
    return False

def check_user_password_db(email,password):
    cheker_email = User.query.filter_by(email=email).first()
    cheker_pass = Password.query.filter_by(password=password).first()
    if cheker_email and cheker_pass:
        return True
    return False

def get_all_users_db():
    users = User.query.all()
    return users

def get_exact_user_db(user_id):
    exact_user = User.query.filter_by(user_id=user_id).first()
    return exact_user

def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user_id)
        db.commit()
        return True
    else:
        return False