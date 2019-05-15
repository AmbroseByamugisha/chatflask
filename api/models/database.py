from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as ambrosebyamu
from api import app
from api.models.models_1 import User
import json


class Database_1:
    """
    creates a schema for the databases
    """
    def __init__(self):
        # database_url = app.config['DATABASE_URL']
        database_url = postgres://bsjsghxjvfheeo:68720d88d9d0dc239389fb26d699d4357abc7941835046a7882bc0978876067b@ec2-50-19-114-27.compute-1.amazonaws.com:5432/d9tt1lsndqhn2n
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=host,
        port=port
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=ambrosebyamu.RealDictCursor)
        print("Successfully connected to "+database_url)
        self.create_tables()
        admin = User('ambrose', 'ambrose@gmail.com', 'password123')
        if not self.fetch_user(admin):
            self.add_user(admin)

    def create_tables(self):
        """
        method creates tables
        """
        commands = (
        """
        CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY,\
          user_name varchar(50), email varchar(100), password varchar(20))""",

        """
        CREATE TABLE IF NOT EXISTS chatroom(chat_room_id serial PRIMARY KEY,\
        chat_room_name varchar(50), user_1 INT, user_2 INT)""",


        """CREATE TABLE IF NOT EXISTS messages(message_id serial PRIMARY KEY,\
          msg varchar(100), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
          chat_room_id INTEGER REFERENCES chatroom(chat_room_id),\
          user_id INTEGER REFERENCES users(user_id))""",

          """
          CREATE TABLE IF NOT EXISTS addmessages(user_name varchar(50) PRIMARY KEY,\
          message varchar(100))"""
          )
          #FOREIGN KEY (user_id) REFERENCES users(user_id) )""",

        for command in commands:
             self.cursor.execute(command)

    def drop_tables(self):
        """
        method drops tables
        """
        drop_user_table = "DROP TABLE users cascade"
        drop_chatroom_table = "DROP TABLE chatroom cascade"
        drop_messages_table = "DROP TABLE messages cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_chatroom_table)
        self.cursor.execute(drop_messages_table)

    def fetch_all_entries(self,table_name):
        """ Fetches all entries from the database"""
        query = ("SELECT * FROM %s;") %(table_name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def add_user(self, user_1):
        self.cursor.execute("INSERT INTO users(user_name,email,password) VALUES\
        (%s, %s, %s);",(user_1.user_name, user_1.email, user_1.password))

    def fetch_user(self,user):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM users WHERE user_name=%s"
        self.cursor.execute(query, (user.user_name,))
        user = self.cursor.fetchone()
        return user

    def fetch_all_users(self):
        return self.fetch_all_entries('users')

    def fetch_all_messages(self):
        return self.fetch_all_entries('messages')

    #added chatroom logic
    def add_chatroom(self,chatroom):
        self.cursor.execute("INSERT INTO chatroom(chat_room_name, chat_room_user_1, chat_room_user_2) VALUES\
        (%s, %s, %s);",(chatroom.chat_room_name, chatroom.chat_room_user_1, chatroom.chat_room_user_2))

    def add_message(self,message):
        self.cursor.execute("INSERT INTO messages(msg, chat_room_id,\
        user_id) VALUES(%s, %s, %s);",(message.msg, message.chat_room_id,\
        message.user_id))

    def send_message(self,addmessages):
        self.cursor.execute("INSERT INTO addmessages(user_name,\
        message) VALUES(%s, %s);",(addmessages.user_name, addmessages.message))

    def fetch_all_messages(self):
        return self.fetch_all_entries('messages')

    def fetch_message(self,column,did):
        """Returns a user in form of a dict or None if user not found"""
        query = """SELECT * FROM messages WHERE {0}={1}""".format(column,did,)
        self.cursor.execute(query,)
        message = self.cursor.fetchall()
        return message

    def query_last_item(self):
        query = """SELECT * FROM messages ORDER BY message_id DESC LIMIT 1"""
        self.cursor.execute(query,)
        message = self.cursor.fetchone()
        return message

    def get_user_name_from_message(self):
        query = """SELECT users.user_name, messages.msg FROM users INNER JOIN messages 
        ON users.user_id = messages.user_id WHERE users.user_id = messages.user_id 
        ORDER BY messages.created_at DESC 
        """
        self.cursor.execute(query,)
        userName = self.cursor.fetchall()
        return userName


db_connection = Database_1()
# the choose username from user_id in messages
# SELECT user_name FROM users INNER JOIN messages 
# ON users.user_id = messages.user_id WHERE users.user_id = messages.user_id;
# a way to do sql queries in python or php or js
# validate not create mulitple chat rooms like in fetch user 
# but check both user_1 an user_2 in sql condition