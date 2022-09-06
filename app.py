import os

from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flasgger import Swagger
from db import db

from resources.quote import Quote, QuoteList
from resources.author import Author, AuthorList
from config.swagger import  template, swagger_config

# Init app
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATEBASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title': 'QuoteAPI',
    'uiversion': 3
}
app.secret_key = "123456"

api = Api(app)


api.add_resource(Quote, '/quote/<int:id_quote>')
api.add_resource(QuoteList, '/quotes')
api.add_resource(Author, '/author/<string:author>')
api.add_resource(AuthorList, '/authors')

swagger = Swagger(app, config = swagger_config, template=template, parse=True)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
