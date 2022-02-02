from flask import request
from http import HTTPStatus
from models.user import User
from flask_restful import Resource
from schemas.user import UserSchema
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required

user_schema = UserSchema()
user_public_schema = UserSchema(exclude=('email',))
#para obter detalhes do usuáro
class MeResource(Resource):
    @jwt_required
    def get(self):
        user = User.get_by_id(id = get_jwt_identity())
        return user_schema.dump(user), HTTPStatus.OK

#consultar usuario
class UserResouce(Resource):
    @jwt_optional
    def get(self, username):

        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user == user.id:
              data = user_schema.dump(user)
        else:
            data = user_public_schema.dump(user)
        return data, HTTPStatus.OK

#criar usuario
class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        data = user_schema.load(json_data)

        if User.get_by_username(data.get('email')):
            return {'message': 'username already in use'}, HTTPStatus.BAD_REQUEST
        if User.get_by_email(data.get('username')):
            return {'message': 'email already in use'}, HTTPStatus.BAD_REQUEST

        user = User(**data)
        user.save()

        return user_schema.dump(user), HTTPStatus.CREATED