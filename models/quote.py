from db import db


class QuoteModel(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    id_quote = db.Column(db.Integer, unique=True)

    quote = db.Column(db.String(1000), unique=True)
    origin = db.Column(db.String(500))

    authorId = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('AuthorModel', back_populates='quotes')

    def __init__(self, id_quote, quote, origin, authorId):
        self.id_quote = id_quote
        self.quote = quote
        self.authorId = authorId
        self.origin = origin

    @classmethod
    def find_by_id(cls, id_quote):
        return cls.query.filter_by(id_quote=id_quote).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'id_quote': self.id_quote,
                'quote': self.quote,
                'origin': self.origin,
                'authorId': self.authorId}
