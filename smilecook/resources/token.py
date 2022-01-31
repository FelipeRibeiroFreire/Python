from http import HTTPStatus
from flask import request
from flask_restful import Resource
from models.user import User
from resources.utils import check_password
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
)

class TokenResource(Resource):

    def post(self):
        json_data = request.get_json()
        email = json_data.get('email')
        password = json_data.get('password')
        user = User.get_by_email(email=email)

        if not user or not check_password(password, user.password):
            return {'message': 'email or password is incorrect'}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id, fresh=True) # cria um token de acesso
        refhesh_token = create_refresh_token(identity=user.id)

        return {'access_token': access_token,'refhesh_token': refhesh_token}, HTTPStatus.OK

class RefreshResource(Resource):
    # expecifica ao endpoint o refhesh_token
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        acess_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': acess_token},HTTPStatus.OK
