class User:
    """
    creates a user model.
    """
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password


class Messages:
    """
    creates a message model.
    """
    def __init__(self, msg, created_at, chat_room_id, user_id):
        self.msg = msg
        self.created_at = created_at
        self.chat_room_id = chat_room_id
        self.user_id = user_id


class ChatRoom:
    """
        creates a chat room model.
    """
    def __init__(self, chat_room_name, chat_room_user_1, chat_room_user_2):
        self.chat_room_name = chat_room_name
        self.chat_room_user_1 = chat_room_user_1
        self.chat_room_user_2 = chat_room_user_2
    


class AddMessages:
    """
    creates a message model.
    """
    def __init__(self, user_name, message):
        self.user_name = user_name
        self.message = message
