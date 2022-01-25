from http import HTTPStatus
from flask import request
from flask_restful import Resource
from models.user import User
from flask_jwt_extended import create_access_token
from utils import check_password

class TokenResource(Resource):

    def post(self):
        data_request = request.get_json()

