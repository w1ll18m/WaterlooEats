import requests
import os
from functools import wraps
from dotenv import load_dotenv
from flask_restful import Resource
from sqlalchemy import or_
from flask import request, jsonify, make_response
from ..database.user import User
from ..utils.auth_client import validate_auth0_token, get_management_api_token
from .. import db

load_dotenv()

class CheckExistingUser(Resource):
    def post(self):
        uuid = request.form.get("uuid")
        if not uuid:
            return make_response("Please provide field 'uuid'", 400)
        existing_user = User.query.filter_by(id=uuid).first()
        if not existing_user:
            return make_response(jsonify({"valid_user": False}), 200)
        return make_response(jsonify({"valid_user": True}), 200)
    
class CreateNewUser(Resource):
    def post(self):
        uuid = request.form.get("uuid")
        if not uuid:
            return make_response("Please provide field 'uuid'", 400)
        email = request.form.get("email")
        if not email:
            return make_response("Please provide field 'email'", 400)
        phone_number = request.form.get("phone_number")
        if not phone_number:
            return make_response("Please provide field 'phone_number'", 400)
        address = request.form.get("address")
        if not address:
            return make_response("Please provide field 'address'", 400)
        
        condition = or_(User.id == uuid, User.email == email, User.phone_number == phone_number)
        existing_user = User.query.filter(condition).first()
        if existing_user:
            return make_response("User with provided user id, email, or phone number already exists", 409)
        
        new_user = User(uuid, email, phone_number, address)
        db.session.add(new_user)
        db.session.commit()

        return make_response(f"User with user id '{uuid}' succesfully created.", 200)

class ValidateAuth0Token(Resource):
    def get(self):
        token = request.headers.get("Authorization")
        if not token:
            return make_response("Access token is missing", 401)
        
        decoded_token = validate_auth0_token(token)
        if not decoded_token:
            return make_response("Access token has expired or is invalid. login required", 401)
        return make_response(jsonify(decoded_token), 200)


def token_required(f):
    @wraps(f)
    def validate(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return make_response("Access token is missing, login required", 401)
        
        decoded_token = validate_auth0_token(token)
        if not decoded_token:
            return make_response("Access token has expired or is invalid. login required", 401)
        return f(*args, **kwargs)
    return validate

def scope_required(scopes):
    def scope_required_decorator(f):
        @wraps(f)
        def validate(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return make_response("Access token is missing, login required", 401)
            
            decoded_token = validate_auth0_token(token)
            if not decoded_token:
                return make_response("Access token has expired or is invalid. login required", 401)
            
            for scope in scopes:
                if not scope in decoded_token["permissions"]:
                    return make_response("Access token does not have correct permissions to access resource", 401)
            
            return f(*args, **kwargs)
        return validate
    return scope_required_decorator

            