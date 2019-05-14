from flask import jsonify, request, json
from api.views import chat_blueprint
from api.models.database import db_connection
from api.models.models_1 import Messages, AddMessages
from flask_jwt_extended import jwt_required,get_jwt_identity
from config import create_app
import datetime

@chat_blueprint.route('/messages', methods=['POST'])
@jwt_required
def create_message():
    user_identiy = get_jwt_identity()
    message_input = request.json
    msg = request.json.get('msg')
    # chat_room_id = request.json.get('chat_room_id')
    # fetch specific chat room logic
    new_msg = Messages(msg, ' ', 2, user_identiy['user_id'])
    db_connection.add_message(new_msg)
    message = db_connection.query_last_item()
    return jsonify({"message":"msg sent successfully","message":message}),201


@chat_blueprint.route('/messages', methods=['GET'])
# @jwt_required
def fetch_all_messages():
    # user_identiy = get_jwt_identity()
    messages = db_connection.fetch_all_messages()
    users = db_connection.get_user_name_from_message()
    newlist =[]
    user_list = []
    for message in messages:
        newlist.append(message)
    for user in users:
        user_list.append(user) 
    return jsonify({"userName": user_list}),200