from db import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password



