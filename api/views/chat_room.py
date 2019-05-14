from flask import jsonify, request, json
from api.views import chat_blueprint
from api.models.database import db_connection
from api.models.models_1 import ChatRoom
from flask_jwt_extended import jwt_required,get_jwt_identity
import datetime

@chat_blueprint.route('/chat_room', methods=['POST'])
@jwt_required
def create_chat_room():
    user_identiy = get_jwt_identity()
    chat_room_input = request.json
    # chat_room_user_1 = request.json.get('chat_room_user_1')
    chat_room_user_2 = request.json.get('chat_room_user_2')
    new_chat_room = ChatRoom('peer-to-peer', user_identiy['user_name'], chat_room_user_2)
    db_connection.add_chatroom(new_chat_room)
    chat_room = db_connection.query_last_item()
    return jsonify({"message":"chat room added successfully"}),201

# know more about jwt parameters 
# how to set them and how to use them
# click on name and create chat room but what if 
# u already have a chatroom and u just need to load it.