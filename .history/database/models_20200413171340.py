from .db import db

class User_Info(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    phoneNumber = db.IntegerField(required=True, unique=True)
    userPassword = db.StringField(required=True, unique=True)
    address = db.StringField(required=True, unique=True)