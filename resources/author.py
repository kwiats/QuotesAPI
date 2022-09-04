from tkinter.tix import INTEGER
from flask_restful import Resource, reqparse

from models.author import AuthorModel


class Author(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help='This filed cannot be left blank.')

    def get(self, authorId):
        author = AuthorModel.find_by_id(authorId)
        if author:
            return author.json()
        return {'message': 'Author not found.'}, 404

    def post(self, authorId):
        if AuthorModel.find_by_id(authorId):
            return {'message': "An author with id '{}' already exists.".format(authorId)}, 400

        data = Author.parser.parse_args()

        author = AuthorModel(authorId, data['name'])
        try:
            author.save_to_db()
        except:
            return {'message': 'An error occurred inserting the author'}, 500

        return author.json(), 201


class AuthorList(Resource):
    def get(self):
        return {'Authors': list(map(lambda author: author.json(), AuthorModel.query.all()))}
