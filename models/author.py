from db import db


class AuthorModel(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    authorId = db.Column(db.Integer, unique=True)

    def __init__(self, name, authorId):
        self.name = name
        self.auhtorId = authorId

    @classmethod
    def find_by_id(cls, authorId):
        return cls.query.filter_by(authorId=authorId).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'author': self.name,
                'authorId': self.authorId}
