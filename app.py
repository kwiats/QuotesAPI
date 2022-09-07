import os

from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flasgger import Swagger
from flask_jwt_extended import JWTManager

from db import db

from resources.user import User, UserRegister, UserLogin
from resources.quote import Quote, QuoteList
from resources.author import Author, AuthorList
from config.swagger import  template, swagger_config

# Init app
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SWAGGER'] = {
    'title': 'QuoteAPI',
    'uiversion': 3
}

app.secret_key = 'pawel'

jwt = JWTManager(app)
api = Api(app)

@app.before_first_request #zamiennik create_table 
def create_tables():
    db.create_all()


api.add_resource(Quote, '/quote/<int:id_quote>')
api.add_resource(QuoteList, '/quotes')
api.add_resource(Author, '/author/<string:author>')
api.add_resource(AuthorList, '/authors')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

swagger = Swagger(app, config = swagger_config, template=template, parse=True)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
