from flask_restful import Resource, reqparse
from flasgger import swag_from
from models.author import AuthorModel


class Author(Resource):
    #@swag_from('./docs/authorget.yaml')
    def get(self, author):
        author = AuthorModel.find_by_author(author)
        if author:
            return author.json()
        return {'message': 'Author not found.'}, 404

    def post(self, author):
        if AuthorModel.find_by_author(author):
            return {'message': "An author with name '{}' already exists.".format(author)}, 400

        author = AuthorModel(author)
        try:
            author.save_to_db()
        except:
            return {'message': 'An error occurred inserting the author'}, 500

        return author.json(), 201

    def delete(self, author):
        author = AuthorModel.find_by_author(author)
        if author:
            author.delete_from_db()
        
        return {'message': 'Author has been deleted.'}, 404

class AuthorList(Resource):
    def get(self):
        return {'Authors': list(map(lambda author: author.json(), AuthorModel.query.all()))}
