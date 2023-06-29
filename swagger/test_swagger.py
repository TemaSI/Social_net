from flask import Blueprint,request
# from main import api
from flask_restx import Resource, Api, fields
from database.userservice import delete_user_db, get_exact_user_db, get_all_users_db,register_user_db

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api = Api(swagger_bp)


model_user = api.model('registration', {'user_name': fields.String,
                                        'first_name':fields.String,
                                        'last_name': fields.String,
                                        'email': fields.String,
                                        'birthday':fields.Date})

user_id_field = api.model('user_id', {'user_id': fields.Integer})
@api.route('/test-user')
class TestSwagger(Resource):
    def get(self):
        all_users = get_all_users_db()
        return {'message':all_users}

@api.route('/<int:user_id>')
class UserService(Resource):
    @api.expect(user_id_field)
    def get(self):
        responce = request.json
        user_id = responce.get('user_id')
        exact_user = get_exact_user_db(user_id)

        return {'message': exact_user}

# Удалить определённого пользователя
    def delete(self):
        responce = request.json
        user_id = responce.get('user_id')
        deleted_user = delete_user_db(user_id)

        return {'message': deleted_user}

# Регистрация пользователя
    @api.expect(model_user)
    def post(self):
        responce = request.json
        new_user = register_user_db(**responce)
        return {'status': 'Registered'}
