from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from api.views import chat_blueprint
from api.models.models_1 import User
from api.models.validators import is_valid_user_name, is_valid_email, is_valid_password
from api.models.database import db_connection
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Fuck the police'
jwt = JWTManager(app)

@chat_blueprint.route('/signup', methods=['POST'])
def add_user():
    user_input = request.json
    if is_valid_user_name(user_input):
        return is_valid_user_name(user_input), 400

    if is_valid_email(user_input):
        return is_valid_email(user_input), 400

    if is_valid_password(user_input):
        return is_valid_password(user_input), 400
    user_name = request.json.get('user_name')
    email = request.json.get('email')
    password = request.json.get('password')

    user_1 = User(user_name, email, password)

    if db_connection.fetch_user(user_1):
        return jsonify({"message": "user already exists"}), 201

    db_connection.add_user(user_1)
    return jsonify({"message": "you have created an account"})

@chat_blueprint.route('/login', methods=['POST'])
def login():
    user_input = request.json

    user_name = request.json.get('user_name')
    password = request.json.get('password')
    login_user = User(user_name, '', password)
    current_user = db_connection.fetch_user(login_user)

    if not current_user:
        return jsonify({"message": "user does not exist"})

    if current_user['password'] != password:
        return jsonify({"message": "wrong password"})
    user = {"user_id":current_user["user_id"], "user_name":current_user["user_name"]}

    access_token = create_access_token(identity=user)
    return jsonify({'access_token':access_token, 'message':'user logged in Successfully', 'user_name':current_user["user_name"]}), 200


@chat_blueprint.route('/users', methods=['GET'])
def fetch_all_users():
    users = db_connection.fetch_all_users()
    newlist =[]
    for user in users:
        newlist.append(user)  
    return jsonify({"Users":newlist}),200