import os

from flask import Flask, request
from flask_restful import Resource, Api
from db import db

from resources.quote import Quote, QuoteList
from resources.author import Author, AuthorList

# Init app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATEBASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "123456"

api = Api(app)

api.add_resource(Quote, '/quote/<int:id_quote>')
api.add_resource(QuoteList, '/quotes')
api.add_resource(Author, '/author/<string:name>')
api.add_resource(AuthorList, '/authors')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
