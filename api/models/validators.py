from flask import jsonify
import re

def is_valid_user_name(json_input):
     x = json_input.get('user_name')
     if len(x) < 6:
         return jsonify({"message": "username should be atleast 6 characters long"})

def is_valid_email(json_input):
    y = json_input.get('email')
    emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if emailRegex.search(y) is None:
        return jsonify({"message": "please use a valid email address"})

def is_valid_password(json_input):
    z = json_input.get('password')
    numRegex = re.compile(r'\d')
    letterRegex = re.compile(r"[a-z]")
    symbolRegex = re.compile(r'\W')
    capsRegex = re.compile(r"[A-Z]")
    if numRegex.search(z) is None:
        return jsonify({"message": "password should have atleast one digit"})
    if letterRegex.search(z) is None:
        return jsonify({"message": "password should have atleast one letter"})
    if symbolRegex.search(z) is None:
        return jsonify({"message": "password should have atleast one symbol"})
    if capsRegex.search(z) is None:
        return jsonify({"message": "password should have atleast one uppercase letter"})

def is_valid_price(json_iput):
    a = json_iput.get('price')
    if (type(a) != int):
        return jsonify({"message": "price should be a digit"})
        
