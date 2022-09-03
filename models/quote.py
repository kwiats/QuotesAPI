from db import db


class QuoteModel(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    id_quote = db.Column(db.Integer)
    quote = db.Column(db.String(1000), unique=True)
    author = db.Column(db.String(300))
    origin = db.Column(db.String(500))

    def __init__(self, id_quote,  quote, author, origin):
        self.id_quote = id_quote
        self.quote = quote
        self.author = author
        self.origin = origin

    @classmethod
    def find_by_id(cls, id_quote):
        return cls.query.filter_by(id_quote=id_quote).first()

    @classmethod
    def find_by_author(cls, author):
        return cls.query.filter_by(author=author).first()

    @classmethod
    def find_by_quote(cls, quote):
        return cls.query.filter_by(quote=quote).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'id': self.id,
                'quote': self.quote,
                'author': self.author,
                'origin': self.origin}
