from db import db


class AuthorModel(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80))

    quotes = db.relationship('QuoteModel', back_populates='author', lazy='dynamic')

    def __init__(self, author):
        self.author = author

    @classmethod
    def find_by_author(cls, author):
        return cls.query.filter_by(author=author).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'id':self.id,
            'author':self.author,
            'quotes': [quote.json() for quote in self.quotes.all()]
        }
