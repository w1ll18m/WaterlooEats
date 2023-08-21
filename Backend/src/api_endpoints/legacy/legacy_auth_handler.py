import bcrypt
import uuid
import jwt
import time
from datetime import datetime
from flask_restful import Resource
from flask import current_app, request, jsonify, make_response
from ....src.database.resteraunt_owner import ResterauntOwner
from ....src.extensions import db

# THE FOLLOWING CLASSES WERE USED FOR OLD JWT TOKEN AUTHENTICATION SYSTEM
# =========================================================================================================================================================================
def validate_unique_username(username):
    existing_user = ResterauntOwner.query.filter_by(username=username).first()
    if existing_user:
        return False
    return True

def validate_unique_email(email):
    existing_user = ResterauntOwner.query.filter_by(email=email).first()
    if existing_user:
        return False
    return True

def validate_jwt_token(token):    
    try:
        app = current_app
        secret_key = app.config["SECRET_KEY"]
        decoded_token = jwt.decode(token, secret_key, "HS256")
        return decoded_token
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

class SignUpUser(Resource):
    def post(self):
        username = request.form.get("username")
        if not username:
            return make_response("Please provide field 'username'", 400)
        if not validate_unique_username(username):
            return make_response(f"Resteraunt owner with username '{username}' already exists", 409)
        
        email = request.form.get("email")
        if not email:
            return make_response("Please provide field 'email'", 400)
        if not validate_unique_email(email):
            return make_response(f"Resteraunt owner with email '{email}' already exists", 409)
        
        password = request.form.get("password")
        if not password:
            return make_response("Please provide field 'password'", 400)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = ResterauntOwner(str(uuid.uuid4()), username, hashed_password, email, datetime.now())
        db.session.add(new_user)
        db.session.commit()

        return make_response(f"User with username '{username}' succesfully created.", 200)

class Login(Resource):
    def post(self):
        EXPIRE_MINUTES = 60

        username = request.form.get("username")
        if not username:
            return make_response("Please provide field 'username'", 400)
        
        existing_user = ResterauntOwner.query.filter_by(username=username).first()
        if not existing_user:
            return make_response(f"User with username '{username}' does not exist", 404)
        
        password = request.form.get("password").encode('utf-8')
        if not password:
            return make_response(f"Please provide field 'password'", 400)
        actual_password = existing_user.password
        is_valid = bcrypt.checkpw(password, actual_password)
        if not is_valid:
            return make_response(f"Incorrect password for user with username '{username}'", 401)
        
        expiration_time = int(time.time()) + (EXPIRE_MINUTES * 60)
        payload = {
            'public_id': existing_user.public_id, 
            'username': existing_user.username, 
            'role': 'resteraunt-owner', 
            'id': existing_user.id, 
            'email': existing_user.email,
            'exp': expiration_time
        }
        app = current_app
        secret_key = app.config["SECRET_KEY"]

        encoded_token = jwt.encode(payload, secret_key, "HS256")
        return make_response(jsonify({"token": encoded_token, "role": "resteraunt-owner", "id": existing_user.id}), 200)
    
class ValidateJWTToken(Resource):
    def get(self):
        token = request.headers.get("Authorization")
        if not token:
            return make_response("JWT token is missing", 401)
        
        decoded_token = validate_jwt_token(token)
        if not decoded_token:
            return make_response("JWT token has expired or is invalid", 401)
        return make_response(jsonify(decoded_token), 200)

class ValidateExistingUser(Resource):
    def post(self):
        identification = request.form.get("identification")
        if not identification:
            return make_response("Please provide field 'identification'", 400)
        
        identification_type = request.form.get("identification_type")
        if not identification_type:
            return make_response("Please provide field 'username'", 400)
        
        if identification_type == "username":
            condition = (ResterauntOwner.username == identification)
        elif identification_type == "email":
            condition = (ResterauntOwner.email == identification)
        else:
            return make_response("'identification_type' must be either 'username' or 'email'", 400)
        existing_user = ResterauntOwner.query.filter(condition).first()

        if not existing_user:
            return make_response(jsonify({"valid_user": False}), 200)
        return make_response(jsonify({"valid_user": True}), 200)
# =========================================================================================================================================================================